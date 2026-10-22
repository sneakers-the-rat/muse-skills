");

/// Gate is fail-closed: unresolved accounts read the not-enabled stub.
pub fn reconcile_workspace_voice_doc(paths: &HatchPaths, enabled: bool) -> Result<()> {
    let docs_dir = paths.workspace_docs_dir();
    std::fs::create_dir_all(&docs_dir).map_err(|e| HatchError::io(&docs_dir, e))?;
    let content = if enabled {
        VOICE_DOC_ENABLED_CONTENT
    } else {
        VOICE_DOC_NOT_ENABLED_CONTENT
    };
    write_workspace_doc_if_changed(&docs_dir.join(VOICE_DOC_RELATIVE_PATH), content)
}

/// Daemon-reconciled per account; not a WORKSPACE_DOC_SEEDS entry. The
/// guide describes the sidebar's Spaces section, so it exists only while
/// the account's Spaces placement gate is on and is removed when it is off.
const SPACES_DOC_RELATIVE_PATH: &str = "