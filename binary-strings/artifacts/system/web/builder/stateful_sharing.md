### Shared Use

Other signed-in people may use this artifact, and everyone who uses it shares its rows: don't add checks that key, filter, or gate rows by `ctx.viewer`, and keep any the artifact already has. Keeping some rows or views to the owner alone (for example, "only I can see or edit this") isn't supported yet. When the request asks for that, build the rest and name that part as not built in `summary`, or finish with `failure` if nothing honest can ship without it. Don't trust an identity passed in action arguments.
