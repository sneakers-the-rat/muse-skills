## Completion

Finish only by calling `web_artifacts.exit_build`, your final report, not a plain message. A parent agent message mid-build changes this build, not a separate task; fold it in and deliver the whole artifact.

`success`: the page exists and is shown; a page missing part of the request is still `success`, gap in `summary`; claim there only the automatic behavior you built and checked. `SUCCEEDED`: you verified the page from the evidence you have and, after an audit, did what its `assessment.next` asked, each finding you leave (and why) named in `verification_notes`. `FAILED`: the page did not load or the capture failed, cause in `verification_notes`; a `FAILED` page is still shown with a not-verified warning.

`failure`: the build cannot complete and nothing is shown: wrong runtime or artifact type, incompatible request, audit tool cannot run, or a missing source or capability leaves nothing honest to ship; carries `FAILED`, cause in `verification_notes`.

`needs_user_input`: a create build only; the only exit that ends with a question, and carries no `verification_status`. Any other rule that says to ask or confirm with the user: name it in `verification_notes`.
