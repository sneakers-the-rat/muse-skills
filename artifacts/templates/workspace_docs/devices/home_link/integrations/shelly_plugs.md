"
        ),
        internal_test_only: false,
    },
];

fn write_workspace_doc_if_changed(path: &std::path::Path, content: &str) -> Result<()> {
    match std::fs::read_to_string(path) {
        Ok(existing) if existing == content => return Ok(()),
        Ok(_) => {}
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => {}
        Err(error) => return Err(HatchError::io(path, error)),
    }
    let parent = path
        .parent()
        .ok_or_else(|| HatchError::other("workspace doc path has no parent"))?;
    let mut staged =
        tempfile::NamedTempFile::new_in(parent).map_err(|error| HatchError::io(path, error))?;
    match std::fs::metadata(path) {
        Ok(metadata) => staged
            .as_file()
            .set_permissions(metadata.permissions())
            .map_err(|error| HatchError::io(path, error))?,
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => {
            #[cfg(unix)]
            {
                use std::os::unix::fs::PermissionsExt;
                staged
                    .as_file()
                    .set_permissions(std::fs::Permissions::from_mode(0o644))
                    .map_err(|error| HatchError::io(path, error))?;
            }
        }
        Err(error) => return Err(HatchError::io(path, error)),
    }
    std::io::Write::write_all(&mut staged, content.as_bytes())
        .map_err(|error| HatchError::io(path, error))?;
    staged
        .persist(path)
        .map_err(|error| HatchError::io(path, error.error))?;
    Ok(())
}

fn apply_workspace_doc_seed(
    docs_dir: &std::path::Path,
    seed: &WorkspaceDocSeed,
    should_seed: bool,
    sharing_enabled: bool,
) -> Result<()> {
    let path = docs_dir.join(seed.relative_path);
    if !should_seed {
        return match std::fs::remove_file(&path) {
            Ok(()) => Ok(()),
            Err(error) if error.kind() == std::io::ErrorKind::NotFound => Ok(()),
            Err(error) => Err(HatchError::io(&path, error)),
        };
    }
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|e| HatchError::io(parent, e))?;
    }
    write_workspace_doc_if_changed(&path, &seed.rendered(sharing_enabled))
}

fn seed_workspace_docs_for_scope(paths: &HatchPaths, is_internal_test: bool) -> Result<()> {
    let docs_dir = paths.workspace_docs_dir();
    std::fs::create_dir_all(&docs_dir).map_err(|e| HatchError::io(&docs_dir, e))?;

    for relative_path in OBSOLETE_WORKSPACE_DOC_PATHS {
        let path = docs_dir.join(relative_path);
        if !path.exists() {
            continue;
        }
        std::fs::remove_file(&path).map_err(|e| HatchError::io(&path, e))?;
    }

    // Channel guides are reconciler-owned: the daemon seeds and removes them
    // per account from the Gatekeeper state (`reconcile_workspace_connection_docs`),
    // so first boot neither writes nor requires them.
    for seed in WORKSPACE_DOC_SEEDS
        .iter()
        .filter(|seed| !seed.is_connection_doc())
    {
        apply_workspace_doc_seed(&docs_dir, seed, seed.should_seed(is_internal_test), false)?;
    }
    Ok(())
}

pub fn seed_workspace_docs(paths: &HatchPaths) -> Result<()> {
    seed_workspace_docs_for_scope(paths, hatch_config::deployment_channel::is_internal_test())
}

/// Reconcile sharing instructions through the canonical seeding path.
/// Disabling the rollout restores the original guides, including after upgrades.
pub fn reconcile_artifact_sharing_doc(paths: &HatchPaths, enabled: bool) -> Result<()> {
    const SHARED_DOC: &str = include_str!("