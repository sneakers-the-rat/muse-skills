",
];

const WORKSPACE_DOC_SEEDS: &[WorkspaceDocSeed] = &[
    WorkspaceDocSeed {
        relative_path: PRODUCT_DOC_RELATIVE_PATH,
        content: product_doc::TEMPLATE,
        internal_test_only: false,
    },
    WorkspaceDocSeed {
        relative_path: "