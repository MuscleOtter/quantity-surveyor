# Privacy and data boundaries

The skill's instructions do not transmit project data. Your chosen AI app and any tools it uses have their own data policies and permissions. Check those before providing confidential drawings, tenders or rates.

Memory is off by default. The optional helper stores records only in a root you explicitly choose, with explicit user/project scope; it has no network code. Keep that root private, outside this repository and the installed skill. It is not encrypted and the scope arguments are not user authentication. Do not share memory stores, backups or input files as examples.

A successful memory write does not prove that the host will retain its directory after the session. Verify durable storage and later-session access before promising persistence; otherwise describe the result as session-only and offer an export to a location the user chooses. Cowork can access authorized local folders, so storage durability must be assessed by location rather than assuming every Cowork file is temporary.

Release checks are off by default. The optional `--online` checker requests public metadata from GitHub, which can see ordinary connection information such as an IP address and a generic user-agent. It sends no project content, memory, tokens or unique installation ID. No telemetry, remote storage or background monitor is included.

User-supplied standards and libraries require appropriate reading, redistribution and AI-use rights where relevant. A freely accessible download does not grant all those rights. The public package contains original guidance and links only.

For bugs, share the smallest synthetic reproduction. Never include real client names, private files, account credentials or project memory in public GitHub issues. See [security reporting](../SECURITY.md).
