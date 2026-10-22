"),
        // Default-reference avatar seeding lives in the avatar module now.
        include_str!("avatar/state/default_reference.rs"),
        include_str!("scheduler_products.rs"),
        crate::prompt_fragments::GOALS_HEADING.embedded,
        include_str!("../../hatch-goals/src/studying.rs"),
    ] {
        hash_first_boot_component(&mut hash, source);
    }
    // The chat template is assembled from the registry's per-section block
    // assets; hash the embedded assembly so chat prompt changes keep moving
    // the fingerprint exactly as the monolithic 