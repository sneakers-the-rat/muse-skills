"),
        internal_test_only: false,
    },
];

/// Reconcile the chat guides.
/// Leave the shared guides and any other files under docs/chat untouched.
pub fn reconcile_user_chat_prompt_docs(paths: &HatchPaths) -> Result<()> {
    let docs_dir = paths.workspace_docs_dir();
    let mut errors = Vec::new();
    for seed in USER_CHAT_PROMPT_DOC_SEEDS {
        if let Err(error) = apply_workspace_doc_seed(&docs_dir, seed, true, false) {
            errors.push(error.to_string());
        }
    }
    if errors.is_empty() {
        Ok(())
    } else {
        Err(HatchError::other(format!(
            "chat prompt docs reconciliation failed: {}",
            errors.join("; ")
        )))
    }
}

/// Reconcile only the canonical channel guides to `allowed_relative_paths`.
/// Other workspace docs and obsolete-path cleanup remain owned by first boot.
pub fn reconcile_workspace_connection_docs(
    paths: &HatchPaths,
    allowed_relative_paths: &[&str],
) -> Result<()> {
    let docs_dir = paths.workspace_docs_dir();
    std::fs::create_dir_all(&docs_dir).map_err(|e| HatchError::io(&docs_dir, e))?;
    let transport_seeds = WORKSPACE_DOC_SEEDS
        .iter()
        .filter(|seed| seed.is_connection_doc())
        .collect::<Vec<_>>();
    let mut errors = Vec::new();

    // Fail closed even when one path is malformed: attempt every denied
    // removal before restoring any allowed guide.
    for seed in transport_seeds
        .iter()
        .copied()
        .filter(|seed| !allowed_relative_paths.contains(&seed.relative_path))
    {
        if let Err(error) = apply_workspace_doc_seed(&docs_dir, seed, false, false) {
            errors.push(error.to_string());
        }
    }
    for seed in transport_seeds
        .iter()
        .copied()
        .filter(|seed| allowed_relative_paths.contains(&seed.relative_path))
    {
        if let Err(error) = apply_workspace_doc_seed(&docs_dir, seed, true, false) {
            errors.push(error.to_string());
        }
    }

    let channels_dir = docs_dir.join("chat-connections");
    match std::fs::remove_dir(&channels_dir) {
        Ok(()) => {}
        Err(error) if error.kind() == std::io::ErrorKind::DirectoryNotEmpty => {}
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => {}
        Err(error) => errors.push(HatchError::io(&channels_dir, error).to_string()),
    }
    if errors.is_empty() {
        Ok(())
    } else {
        Err(HatchError::other(format!(
            "channel docs reconciliation failed: {}",
            errors.join("; ")
        )))
    }
}

/// Daemon-reconciled per account; not a WORKSPACE_DOC_SEEDS
/// entry (like the channel guides).
const VOICE_DOC_ENABLED_CONTENT: &str = include_str!("