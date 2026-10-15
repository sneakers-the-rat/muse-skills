# File Hosting

## Choose where the file goes

- Work out who needs the file, for how long and whether they will edit it. If only the user needs it, the chat file link or the Library download is enough, as `~/docs/files-and-library.md` explains.

- Use the service and account the user named or already approved, and do not suggest alternatives to a firm choice.

- For a quick public link with no service chosen, use Muse's built-in storage. Its link opens for anyone who has it and lasts up to 48 hours. Ask for less with `--ttl-hours` when something will fetch the file once, and remove a link early with `/opt/hatch/bin/remote-storage delete-file --url URL`.

- When the file must last longer, reach only named people or be edited together, or is larger than 1.5 GiB, recommend a storage account the user has, such as Google Drive, Dropbox, Box or OneDrive, and ask before uploading.

- On a confidential VM, Muse cannot make a public link. Explain that, and let the user decide whether a copy may leave the VM.

- To publish a page or app you built, share the artifact instead, as `~/docs/artifacts.md` describes.

## Keep files away from risky hosts

- Never pick an anonymous file host such as catbox.moe, litterbox or transfer.sh yourself, and never try another host after one refuses.

- Choose established services with clear ownership, privacy terms and access controls. A sensitive file needs a destination fit for that data, shared only with the intended people.

## When the user has no account

- Start with Muse's built-in storage. When its limits do not fit, an established transfer service such as SwissTransfer sends a file without registration. Check its current size limit, expiry and verification steps before relying on it.

- Keep the sender's needs apart from the recipient's. Recipients can often open Dropbox, Google Drive or OneDrive links without an account, but the sender still needs one to upload.

- A temporary transfer does not meet a request for lasting storage. Say when a link will stop working.

## Match access to the audience

- Keep a stored copy private unless the user wants it shared. Share with named people directly, give edit rights only when asked, and check what the destination folder already shares.

- Anyone can forward a link that opens for anyone. Say so, and set an expiry or password when the service supports one.

- Clarify the audience before changing access when the choice would expose the file. Never make a file public just to get past an access error.

## Upload, verify and hand over

- Confirm the file, version and destination. Check the size against the service's limits, keep the original, and replace an existing remote file only when that is the request. Put several files in one folder or archive with clear names.

- Wait for the upload to finish, then check the remote name, size and location. Open a preview or a downloaded copy when conversion could have changed the content.

- After a timeout, look for the uploaded file before trying again. When you cannot tell whether it arrived, do not retry.

- Use the link the service returns, never one you built. Check its permissions, and open it as the recipient would when you can, because the owner's view does not prove others can open it.

- Return the link with who can open it and when it expires. If the upload or the check failed, keep the file and say what remains.

## Available connectors

- [Google Drive](/opt/hatch/connectors/google_drive/CONNECTOR.md) for lasting storage and sharing with named people or by link.

- [Dropbox](/opt/hatch/connectors/dropbox/CONNECTOR.md) for shared links, and for file requests that collect files from other people.

- [Box](/opt/hatch/connectors/box/CONNECTOR.md) for shared links and collaborator invitations in a personal or company Box.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Use `browser.spawn_task` for a service without a connector, and grant it only the file being shared. Tell it the audience and expiry the user chose, and have it return the share link and its access setting.

- [OneDrive](https://onedrive.live.com/) for the user's Microsoft storage, or their organization's OneDrive for work files.

- [SwissTransfer](https://www.swisstransfer.com/) for a large one-time transfer without registration, run by Infomaniak in Switzerland.

- [WeTransfer](https://wetransfer.com/) for one-time transfers, subject to its current account and plan rules.

- [Proton Drive](https://drive.proton.me/) for end-to-end encrypted storage when privacy matters most.

- [iCloud Drive](https://www.icloud.com/iclouddrive/) for users who keep their files with Apple.

## Alternatives for better results

- For a small file going to one person, attaching it to the email or message is often simpler than a link.

- For ongoing work, share one folder rather than many separate links, so everyone sees the same latest copy.

- For a sensitive file, prefer access for named people with an expiry over a link that anyone could forward.
