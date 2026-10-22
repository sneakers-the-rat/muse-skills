");
    let docs_dir = paths.workspace_docs_dir();
    let content = if enabled {
        SHARED_DOC
    } else {
        include_str!("