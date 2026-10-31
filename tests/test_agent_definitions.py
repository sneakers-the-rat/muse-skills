from hatch_extract.mechanisms.agent_definitions import agent_definitions

DOC = (b'id = "%s"\nname = "%s"\nmodel = "m"\nprovider = "p"\n'
       b'tool_loading = "all"\ntools = [\n    "do_thing",\n]\n')


def _registry():
    d1 = DOC % (b"alpha_agent", b"Alpha")
    d2 = DOC % (b"beta_agent", b"Beta")
    # beta's entry name abuts its document, as the binary stores it
    return b"\x00" * 8 + d1 + b"beta_agent" + d2


def test_two_definitions_extracted():
    found, problems = agent_definitions(_registry())
    assert set(found) == {"alpha_agent", "beta_agent"}
    assert problems == []
    off, body = found["alpha_agent"]
    assert body.startswith(b'id = "alpha_agent"')
    assert body.endswith(b"]")


def test_missing_required_field_rejected():
    bad = (b'id = "bad_agent"\nname = "Bad"\nmodel = "m"\n')
    found, problems = agent_definitions(bad)
    assert found == {}
    assert problems and "bad_agent" in problems[0]


def test_non_toml_line_rejected():
    # a garbage line INSIDE the document (not trailing — trailing
    # lines of the last document are trimmed by design)
    doc = DOC % (b"x_agent", b"X")
    bad = doc.replace(b'model = ', b'garbage line here\nmodel = ')
    found, problems = agent_definitions(bad)
    assert "x_agent" not in found
    assert problems


def test_trailing_garbage_trimmed_from_last_document():
    doc = DOC % (b"x_agent", b"X")
    found, problems = agent_definitions(doc + b"\ngarbage line here\n")
    assert found["x_agent"][1] == doc
    assert problems == []
