"),
);

/// Gate is fail-closed: unresolved accounts have no Spaces guide.
pub fn reconcile_spaces_doc(
    paths: &HatchPaths,
    enabled: bool,
    stateful_artifact_sharing_enabled: bool,
) -> Result<()> {
    apply_workspace_doc_seed(
        &paths.workspace_docs_dir(),
        &WorkspaceDocSeed {
            relative_path: SPACES_DOC_RELATIVE_PATH,
            content: if stateful_artifact_sharing_enabled {
                SPACES_SAVED_SHARES_DOC_CONTENT
            } else {
                SPACES_DOC_CONTENT
            },
            internal_test_only: false,
        },
        enabled,
        false,
    )
}

pub(crate) fn workspace_onboarding_completed(paths: &HatchPaths) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_onboarding_completed(paths)
        .map_err(Into::into)
}

pub(crate) fn workspace_onboarding_flow_active_override(
    paths: &HatchPaths,
) -> Result<Option<bool>> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_onboarding_flow_active_override(
        paths,
    )
    .map_err(Into::into)
}

pub(crate) fn workspace_onboarding_active(paths: &HatchPaths) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_onboarding_active(paths)
        .map_err(Into::into)
}

pub(crate) fn mark_workspace_onboarding_pages_started(paths: &HatchPaths) -> Result<()> {
    hatch_workspace_identity::onboarding::lifecycle::mark_workspace_onboarding_pages_started(paths)
        .map_err(Into::into)
}

pub(crate) fn claim_workspace_onboarding_initial_message_enqueue(
    paths: &HatchPaths,
) -> Result<(String, bool)> {
    hatch_workspace_identity::onboarding::lifecycle::claim_workspace_onboarding_initial_message_enqueue(paths).map_err(Into::into)
}

pub(crate) fn workspace_deferred_entry_context_delivered(
    paths: &HatchPaths,
    submission_id: &str,
) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_deferred_entry_context_delivered(
        paths,
        submission_id,
    )
    .map_err(Into::into)
}

pub(crate) fn mark_workspace_deferred_entry_context_delivered(
    paths: &HatchPaths,
    submission_id: &str,
) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::mark_workspace_deferred_entry_context_delivered(paths, submission_id).map_err(Into::into)
}

pub(crate) fn workspace_growth_onboarding_context(
    paths: &HatchPaths,
) -> Result<Option<GrowthOnboardingContext>> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_growth_onboarding_context(paths)
        .map_err(Into::into)
}

pub(crate) fn prepare_workspace_growth_onboarding_context(
    paths: &HatchPaths,
    context: GrowthOnboardingContext,
) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::prepare_workspace_growth_onboarding_context(
        paths, context,
    )
    .map_err(Into::into)
}

pub(crate) fn workspace_growth_onboarding_continuation_delivered(
    paths: &HatchPaths,
) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_growth_onboarding_continuation_delivered(paths).map_err(Into::into)
}

pub(crate) fn mark_workspace_growth_onboarding_continuation_delivered(
    paths: &HatchPaths,
) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::mark_workspace_growth_onboarding_continuation_delivered(paths).map_err(Into::into)
}

pub(crate) fn claim_workspace_onboarding_ideas_tab_highlight(
    paths: &HatchPaths,
) -> Result<(String, bool)> {
    hatch_workspace_identity::onboarding::lifecycle::claim_workspace_onboarding_ideas_tab_highlight(
        paths,
    )
    .map_err(Into::into)
}

pub(crate) fn has_completed_onboarding_chat(paths: &HatchPaths) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::has_completed_onboarding_chat(paths)
        .map_err(Into::into)
}

pub(crate) fn mark_workspace_onboarding_completed(
    paths: &HatchPaths,
    presentation_locale: hatch_i18n::SupportedLocale,
    client_timezone: Option<&str>,
) -> Result<crate::onboarding::OnboardingCompletionClaim> {
    hatch_workspace_identity::onboarding::lifecycle::mark_workspace_onboarding_completed(
        paths,
        presentation_locale,
        client_timezone,
        None,
    )
    .map_err(Into::into)
}

pub(crate) fn workspace_onboarding_questionnaire_completed(paths: &HatchPaths) -> Result<bool> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_onboarding_questionnaire_completed(
        paths,
    )
    .map_err(Into::into)
}

pub(crate) fn mark_workspace_onboarding_questionnaire_completed(paths: &HatchPaths) -> Result<()> {
    hatch_workspace_identity::onboarding::lifecycle::mark_workspace_onboarding_questionnaire_completed(paths).map_err(Into::into)
}

pub(crate) fn clear_workspace_onboarding_questionnaire_completed(paths: &HatchPaths) -> Result<()> {
    hatch_workspace_identity::onboarding::lifecycle::clear_workspace_onboarding_questionnaire_completed(paths).map_err(Into::into)
}

pub(crate) fn clear_workspace_onboarding_completion(paths: &HatchPaths) -> Result<()> {
    hatch_workspace_identity::onboarding::lifecycle::clear_workspace_onboarding_completion(paths)
        .map_err(Into::into)
}

pub(crate) fn workspace_reset_cursor(paths: &HatchPaths) -> Result<WorkspaceResetCursor> {
    hatch_workspace_identity::onboarding::lifecycle::workspace_reset_cursor(paths)
        .map_err(Into::into)
}

pub(crate) fn bump_workspace_reset_cursor(paths: &HatchPaths) -> Result<WorkspaceResetCursor> {
    hatch_workspace_identity::onboarding::lifecycle::bump_workspace_reset_cursor(paths)
        .map_err(Into::into)
}

pub(crate) fn reset_workspace_onboarding_state(paths: &HatchPaths) -> Result<()> {
    hatch_workspace_identity::onboarding::lifecycle::reset_workspace_onboarding_state(paths)
        .map_err(Into::into)
}

fn ensure_workspace_onboarding_state(paths: &HatchPaths) -> Result<()> {
    hatch_workspace_identity::onboarding::lifecycle::ensure_workspace_onboarding_state(paths)
        .map_err(Into::into)
}

/// Ensure first-boot artifacts exist.
///
/// Behavior:
/// - Always ensure bootstrap *templates* exist (`