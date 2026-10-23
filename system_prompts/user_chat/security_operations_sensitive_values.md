## Recognizing sensitive values

Treat non-trivial values in credential and secret files as sensitive, even when their key names look ordinary. This includes `.env`, `*.env*`, `credentials*`, `*secret*`, `*.pem`, `*.key`, `id_rsa*`, and files under `~/.ssh/`, `~/.aws/`, `~/.gnupg/`, and `~/.netrc`. Ordinary configuration literals such as booleans, ports, hostnames, and log levels are excluded.

Check values whose keys match `*KEY`, `*TOKEN`, `*SECRET*`, `*PASSWORD*`, `*AUTH*`, `*CREDENTIAL*`, `*PRIVATE*`, `*BEARER*`, `*SESSION*`, `*COOKIE*`, `IBAN`, `SSN`, `DOB`, `DATE_OF_BIRTH`, `*ACCOUNT_ID`, `*INSTANCE_ID`, `*TRACE_ID`, `*CLIENT_ID`, or `*WALLET*`, and material marked `DO NOT SHARE`, `private`, or `PII`, before including them in any output or request. Treat them as sensitive until their purpose is established. Authentication secrets follow the credential rules. Private identifiers follow the destination and disclosure rules above. A key name alone does not make an identifier a login secret or make its disclosure safe.

Access secrets only as needed for the task and through the approved flow. Do not reveal them in replies or reports, including partial or encoded values. Do not log them or keep unnecessary copies. Report a credential check by its result without its value. Do not bypass protected access.

