#!/usr/bin/env python3
"""Copy and configure this CLI for one registered, header-authenticated MCP."""

import argparse
import json
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import DynamicCredentialError, add_surrogate_to_request


PROVIDER = ""
ENDPOINT = ""
ALLOWED_TOOLS: set[str] = set()
PROTOCOLS = {"2025-11-25", "2025-06-18", "2025-03-26"}


class McpError(RuntimeError):
    """A transport or protocol failure with no automatic replay."""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise McpError("MCP endpoint redirected; verify the endpoint before continuing")


class Client:
    def __init__(self):
        endpoint = urllib.parse.urlsplit(ENDPOINT)
        if (
            not PROVIDER.startswith("custom.")
            or endpoint.scheme != "https"
            or not endpoint.hostname
            or endpoint.username
            or endpoint.password
            or endpoint.query
            or endpoint.fragment
            or endpoint.port not in (None, 443)
        ):
            raise McpError("Configure a registered provider and its fixed HTTPS endpoint")
        self.host = endpoint.hostname
        self.opener = urllib.request.build_opener(NoRedirect())
        self.session = None
        self.protocol = "2025-11-25"
        self.sequence = 0

    def send(self, method, params, *, notification=False):
        self.sequence += 1
        request_id = None if notification else self.sequence
        body = {"jsonrpc": "2.0", "method": method, "params": params}
        if request_id is not None:
            body["id"] = request_id
        encoded = json.dumps(body).encode()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": self.protocol,
        }
        if self.session:
            headers["Mcp-Session-Id"] = self.session
        request = urllib.request.Request(ENDPOINT, data=encoded, headers=headers, method="POST")
        add_surrogate_to_request(request, PROVIDER, allowed_hosts=[self.host])
        try:
            with self.opener.open(request, timeout=45) as response:
                if session := response.headers.get("Mcp-Session-Id"):
                    if not all(33 <= ord(c) <= 126 for c in session):
                        raise McpError("MCP server returned an invalid session header")
                    self.session = session
                if notification and response.status == 202:
                    return None
                if notification:
                    raise McpError("MCP server did not accept the initialization notification")
                return self.read_result(response, request_id)
        except urllib.error.HTTPError as error:
            raise McpError(f"MCP returned HTTP {error.code}; the operation was not replayed") from None
        except (urllib.error.URLError, TimeoutError, OSError):
            raise McpError("MCP request did not complete; check any write before retrying") from None

    @staticmethod
    def decode(payload, request_id):
        message = json.loads(payload)
        if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
            raise McpError("MCP returned an invalid JSON-RPC message")
        if type(message.get("id")) is not int or message["id"] != request_id:
            return None
        if "error" in message:
            raise McpError("MCP returned a JSON-RPC error; the operation was not replayed")
        if not isinstance(message.get("result"), dict):
            raise McpError("MCP returned no result object")
        return message["result"]

    @classmethod
    def read_result(cls, response, request_id):
        content_type = response.headers.get_content_type()
        if content_type == "application/json":
            result = cls.decode(response.read(), request_id)
            if result is None:
                raise McpError("MCP returned the wrong request ID")
            return result
        if content_type != "text/event-stream":
            raise McpError("MCP returned an unsupported content type")
        data = []
        while True:
            line = response.readline()
            if not line:
                raise McpError("MCP event stream ended before the matching result")
            line = line.rstrip(b"\r\n")
            if line.startswith(b"data:"):
                data.append(line[5:].lstrip(b" "))
            elif not line and data:
                result = cls.decode(b"\n".join(data), request_id)
                data.clear()
                if result is not None:
                    return result

    def initialize(self):
        result = self.send("initialize", {
            "protocolVersion": self.protocol,
            "capabilities": {},
            "clientInfo": {"name": "muse-custom-connector", "version": "1"},
        })
        protocol = result.get("protocolVersion")
        capabilities = result.get("capabilities")
        if (
            not isinstance(protocol, str)
            or protocol not in PROTOCOLS
            or not isinstance(capabilities, dict)
            or not isinstance(capabilities.get("tools"), dict)
        ):
            raise McpError("MCP server did not negotiate a supported tool protocol")
        self.protocol = protocol
        self.send("notifications/initialized", {}, notification=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    listing = subparsers.add_parser("list-tools")
    listing.add_argument("--cursor")
    calling = subparsers.add_parser("call-tool")
    calling.add_argument("--name", required=True)
    calling.add_argument("--arguments-file", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "call-tool":
        if args.name not in ALLOWED_TOOLS:
            parser.error("Inspect this operation's schema and add its exact name to ALLOWED_TOOLS")
        arguments = json.loads(args.arguments_file.read_bytes())
        if not isinstance(arguments, dict):
            parser.error("arguments must be a JSON object")
    client = Client()
    client.initialize()
    if args.command == "list-tools":
        result = client.send("tools/list", {"cursor": args.cursor} if args.cursor else {})
    else:
        result = client.send("tools/call", {"name": args.name, "arguments": arguments})
    print(json.dumps(result, ensure_ascii=False))
    return 1 if result.get("isError") else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (McpError, DynamicCredentialError, ValueError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
