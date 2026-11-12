- On web: there is a Download option on Library items, and a public share link available from an artifact's Share dialog. There is no share-to-message action on web.
- {{ARTIFACT_SHARE_MENU_ITEM}} in a page or app's menu gives its link.
No share-message action on web. Sharing an artifact means creating a public link from the artifact's Share dialog. Put the content in chat or an artifact, then point the user to their own share option.
{{ARTIFACT_SHARE_MENU_ITEM}}, in a page or app's menu, creates its link; `~/docs/artifacts.md` explains who can open it. Put the content in chat or an artifact, then point the user to their own share option.
{{ARTIFACT_SHARING_GUIDANCE}}ShareInviteShare link{{ARTIFACT_SHARE_MENU_ITEM}}Share link in the space's menu publishes a page or app as a public copy.
The copy starts with the space's data, then keeps its own. Platform
locations are in `~/docs/client-surfaces.md`.

- The copy updates only when the user taps Sync updates. Data never syncs.
- To publish, sync, or take a link down, open Share link with `ui.navigate`
  target `space.share` if `ui.list` shows it; the user decides there. Otherwise,
  tell them where it is. It's the only way to get a link
  others can open: an uploaded or exported page downloads as a file instead of
  opening.
Publishing gives a page or app a public share link. Invite is in its menu;
platform locations are in `~/docs/client-surfaces.md`.

- Shared pages and apps usually publish later successful builds.
  `artifact.unshare` takes a link down.
- To publish or change sharing, open Invite with `ui.navigate` target
  `space.share` if `ui.list` shows it; the user decides there. Otherwise,
  tell them where Invite is. Invite is the only way to get a link
  others can open: an uploaded or exported page downloads as a file instead of
  opening.
{{ARTIFACT_PUBLISHING}}companion_outbound_bridge_contextoperation_interruptedEarlier compacted context was removed after a group message was deleted.The available tool set has been modified. Do not attempt to use or call any tools that appear in the system prompt but do not appear in this developer message.

No tools available.
initialized by trim_to_budgetapp.dbyield_elapsedsentinel_evaluation_holdexplicit_backgroundget_connection_statusget_user_infolist_payment_methodsadd_payment_methodconfigure_balancelist_shipping_addressespersisteddiscardedassistant_item_idcheckpoint_reusedcheckpoint_reused_after_joinsync_compactedcheckpoint_superseded_syncinference_overflow_recoveryinference_retry_decisionwill_retrybackoff_msretry_not_before_utc_msdurable_inference_recovery_mergeduser_message_mergedask_for_informationsystem-update# Spaces and the sidebar

Space is the new name for a web artifact, a web page or app you build for
the user. `~/docs/artifacts.md` and the tool names still say web artifact.
Call it a space when you talk to the user.

A space is in the user's Library or their sidebar. In the sidebar, it can sit
in the navigation bar or in the spaces section below it. Moving it doesn't
change what it is. Side chats show up in the sidebar too, but they aren't
spaces and `ui.sidebar` doesn't list or move them. `~/docs/artifacts.md`
covers how publishing works.

## The sidebar

The sidebar has two sections.

- The navigation bar (`navbar`) holds Chat, Feed, Ideas, Goals, and Library
  by default. The mobile apps show it as the bottom bar. Chat is always first
  and can't be moved or removed. The mobile apps fit at most five tabs in the
  navbar, so keep it to five or fewer. To add a tab to a full navbar, move
  another tab down to the spaces section in the same save and tell the user
  which one.
- The spaces section sits below the navbar. A space put there goes at the
  top.

Any tab except Chat can move between the two sections, and the user can
remove Feed, Ideas, Goals, or Library from the navbar. If Chat is the only
tab left, the navbar goes away. The user can also reorder tabs within a
section. On the mobile apps they drag a tab.

Read the current order with a `ui.sidebar` read. Reorder it only when the
user asks you to, in chat or in a scheduled task. Leave tabs the user didn't
mention where they are.

## Availability

Only the latest Muse apps and web app show the spaces section. Older
versions show only Chat, Feed, Ideas, Goals, and Library, and every space is
in the Library. If someone on an older version can't find a space you made,
tell them it's in the Library and that updating the app adds the spaces
section.

## Creating, moving, and deleting

- Create a space with `artifact.create_web_static` or
  `artifact.create_web_fullstack`. Pick static or fullstack by what the app
  does. When the user asks for a space or wants it in their sidebar, set
  `place_in_sidebar: true`. Otherwise it goes in the Library.
- Use a `ui.sidebar` move to put an existing space in the sidebar or the
  Library, but only when the user asks. Opening, editing, pinning, or
  sharing it doesn't move it.
- Edit a space with `artifact.edit`. Deleting one with `artifact.delete`
  can't be undone, so tell the user and wait for them to confirm, unless they
  already have.
# Spaces and the sidebar

Space is the new name for a web artifact, a web page or app you build for
the user. `~/docs/artifacts.md` and the tool names still say web artifact.
Call it a space when you talk to the user.

A space is in the user's Library or their sidebar. In the sidebar, it can sit
in the navigation bar or in the spaces section below it. Moving it doesn't
change what it is. Side chats show up in the sidebar too, but they aren't
spaces and `ui.sidebar` doesn't list or move them. `~/docs/artifacts.md`
covers how publishing works.

## The sidebar

The sidebar has two sections.

- The navigation bar (`navbar`) holds Chat, Feed, Ideas, Goals, and Library
  by default. The mobile apps show it as the bottom bar. Chat is always first
  and can't be moved or removed. The mobile apps fit at most five tabs in the
  navbar, so keep it to five or fewer. To add a tab to a full navbar, move
  another tab down to the spaces section in the same save and tell the user
  which one.
- The spaces section sits below the navbar. A space put there goes at the
  top.

Any tab except Chat can move between the two sections, and the user can
remove Feed, Ideas, Goals, or Library from the navbar. If Chat is the only
tab left, the navbar goes away. The user can also reorder tabs within a
section. On the mobile apps they drag a tab.

Read the current order with a `ui.sidebar` read. Reorder it only when the
user asks you to, in chat or in a scheduled task. Leave tabs the user didn't
mention where they are.

## Availability

Only the latest Muse apps and web app show the spaces section. Older
versions show only Chat, Feed, Ideas, Goals, and Library, and every space is
in the Library. If someone on an older version can't find a space you made,
tell them it's in the Library and that updating the app adds the spaces
section.

## Creating, moving, and deleting

- Create a space with `artifact.create_web_static` or
  `artifact.create_web_fullstack`. Pick static or fullstack by what the app
  does. When the user asks for a space or wants it in their sidebar, set
  `place_in_sidebar: true`. Otherwise it goes in the Library.
- Use a `ui.sidebar` move to put an existing space in the sidebar or the
  Library, but only when the user asks. Opening, editing, pinning, or
  sharing it doesn't move it.
- Edit a space with `artifact.edit`. Deleting one with `artifact.delete`
  can't be undone, so tell the user and wait for them to confirm, unless they
  already have.

## Saved shares

The spaces section also holds saved shares: shared spaces the user has
saved. Saving a share places it in the spaces section by default.

A saved share gives the user the access its publisher currently allows: View
for a static share, and View or Use for a stateful share. Saving or moving it
does not make the user its owner, grant editing rights, or change that access.
The publisher is shown only while the share and profile permissions allow it.

To move a saved share between the spaces section and the Library when the
user asks, use a `ui.sidebar` move with the exact `saved_space:`
artifact_ref and `space_id` from the same `artifact.list` entry. A saved share
whose entry has no `space_id` cannot be moved. In tab order, a saved share
moves like any other tab.
spaces.mdconnection settings await the offline chat migrationrewrote home.yaml without its retired keysfailed to rewrite home.yaml without retired keysfailed to parse home.yaml for normalizationfailed to read home.yaml for normalizationSUBAGENTS_MONITORING.md.subagents_monitoring_prompt_refreshed_20260317.subagents_monitoring_prompt_refreshed_20260728.subagents_monitoring_prompt_refreshed_20260824ACTIVITY_LOG.mdfailed to remove retired root filefailed to inspect retired root file# Goals

Personal goals are enduring outcomes the user is working toward; help them
make real progress.

Separately, keep track of concrete plans, commitments, and outcomes the user
cares about beyond the immediate conversation, including reservations,
deliveries, reminders, and ongoing projects.

Both appear below, kept current for you automatically.

When clarifying a goal, ask questions one at a time; don't bombard.
Ask about conditions, medications, injuries, or limitations only when they
affect the safety of the proposed activity.
//! First-boot initialization for a brand-new Jarvis install.
//!
//! Historically this lived in the daemon crate. The current runtime is a
//! library (`hatch-agent`) used by both the daemon and the TUI, so we keep the
//! first-boot contract here.

use crate::error::{HatchError, Result};
use crate::onboarding::{
    GrowthOnboardingContext, WORKSPACE_ONBOARDING_STATE_VERSION, WorkspaceResetCursor,
    normalize_workspace_reset_cursor_state, now_iso, read_workspace_onboarding_state,
};
use hatch_config::config::HatchConfig;
use hatch_config::paths::HatchPaths;
use serde::{Deserialize, Serialize};
use tracing::warn;

mod ensure;
mod legacy_spaces_tombstone;
mod maintenance;
mod operation;
mod product_doc;
mod space_agents_backfill;
mod ssh_identity;
mod workflow_content;

pub(crate) use ensure::{
    ensure_first_boot_with_observer, ensure_first_boot_with_report, prepare_first_boot_with_report,
};
pub(crate) use maintenance::{FirstBootMaintenance, finish_first_boot_maintenance};
pub(crate) use operation::{FirstBootOperationObserver, FirstBootOperationReport, FirstBootPhase};
pub use product_doc::reconcile_product_doc;
pub(crate) use workflow_content::activate as activate_workflow_content;

const FIRST_BOOT_IDEA_CARDS_WARMUP_META_KEY: &str = "idea_cards_first_boot_warmup";
const FIRST_BOOT_ENSURE_STAMP_SCHEMA_VERSION: u32 = 1;
const FIRST_BOOT_ENSURE_STAMP_FINGERPRINT_VERSION: &str = "first_boot_ensure/2026-06-08.1";
const FIRST_BOOT_ENSURE_STAMP_FILE: &str = "first-boot-ensure-stamp.json";
const HATCH_RESUME_DIR_ENV: &str = "HATCH_RESUME_DIR";

#[derive(Debug, Deserialize, Serialize)]
struct FirstBootEnsureStamp {
    schema_version: u32,
    fingerprint: String,
    // Fences failed-publication rollback; supported older stamps omit it.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    publication_id: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    setup_completion: Option<maintenance::FirstBootSetupCompletion>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub(crate) enum FirstBootEnsureMode {
    Full,
    Skipped,
}

impl FirstBootEnsureMode {
    pub(crate) const fn as_str(self) -> &'static str {
        match self {
            Self::Full => "full",
            Self::Skipped => "skipped",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub(crate) struct FirstBootEnsureReport {
    pub(crate) mode: FirstBootEnsureMode,
    pub(crate) marker_valid: bool,
    pub(crate) invalidation_reason: Option<String>,
    pub(crate) degraded: bool,
    pub(crate) ssh_identity_degraded: bool,
    pub(crate) fastpath_enabled: bool,
    pub(crate) fingerprint: String,
    pub(crate) maintenance_complete: bool,
}

fn first_boot_ensure_stamp_path_with_resume_dir(
    paths: &HatchPaths,
    resume_dir: Option<&std::path::Path>,
) -> std::path::PathBuf {
    resume_dir
        .map(std::path::Path::to_path_buf)
        .unwrap_or_else(|| paths.var_lib_dir().join("startup"))
        .join(FIRST_BOOT_ENSURE_STAMP_FILE)
}

fn first_boot_ensure_stamp_path(paths: &HatchPaths) -> std::path::PathBuf {
    let resume_dir = std::env::var_os(HATCH_RESUME_DIR_ENV)
        .filter(|value| !value.is_empty())
        .map(std::path::PathBuf::from);
    first_boot_ensure_stamp_path_with_resume_dir(paths, resume_dir.as_deref())
}

fn hash_first_boot_component(hash: &mut u64, value: &str) {
    // FNV-1a: tiny, deterministic, and sufficient for a local invalidation
    // stamp over embedded first-boot seed text.
    for byte in value.as_bytes() {
        *hash ^= u64::from(*byte);
        *hash = hash.wrapping_mul(0x100000001b3);
    }
    *hash ^= 0xff;
    *hash = hash.wrapping_mul(0x100000001b3);
}

fn first_boot_ensure_fingerprint() -> String {
    let mut hash = 0xcbf29ce484222325;
    let is_internal_test = hatch_config::deployment_channel::is_internal_test();
    hash_first_boot_component(&mut hash, FIRST_BOOT_ENSURE_STAMP_FINGERPRINT_VERSION);
    for source in [
        include_str!("first_boot.rs"),
        include_str!("first_boot/ensure.rs"),
        include_str!("first_boot/maintenance.rs"),
        // Seeding logic only: the backfill is write-if-missing, so template
        // content changes never need to re-run it — no template bytes here.
        include_str!("first_boot/space_agents_backfill.rs"),
        include_str!("first_boot/legacy_spaces_tombstone.rs"),
        // The tombstone module rewrites its seeded workspace files whenever a
        // shipped template changes; the template bytes are include_str!'d
        // there, invisible to the .rs source hash above, so they must move
        // this fingerprint themselves or the fastpath skips the rewrite.
        include_str!("