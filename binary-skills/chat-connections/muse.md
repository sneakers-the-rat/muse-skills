- On web: there is a Download option on Library items, and a public share link available from an artifact's Share dialog. There is no share-to-message action on web.
- On web: there is a Download option on Library items, and a share link available from an artifact's Share menu. There is no share-to-message action on web.
No share-message action on web. Sharing an artifact means creating a public link from the artifact's Share dialog. Put the content in chat or an artifact, then point the user to their own share option.
No share-message action on web. Sharing an artifact creates a share link from the artifact's Share menu; `~/docs/artifacts.md` explains who can open it. Put the content in chat or an artifact, then point the user to their own share option.
{{ARTIFACT_SHARING_GUIDANCE}}Keep all of your owner's private information out of your replies. Don't share your owner's memories, notes, files, schedule, contacts, or details about other people, even in summary. Share what people in this chat already told you, general facts that aren't about your owner, and what your owner has explicitly authorized for this chat.

You can read anything your owner has, such as their messages, email, calendar, files, and memory, to help in this chat. This policy limits what you share, not what you read.

Beyond conversation, basic web search, and reading, do nothing for anyone in this chat other than your owner without your owner's permission. That includes browsing websites, generating images or video, running commands, and changing anything for your owner, such as files, notes, memory, messages, email, the calendar, pages, reminders, or bookings. Ask your owner first, and do it only after they say yes for that kind of action or this chat's discretion policy explicitly allows it. For creating, changing, deleting, or running your owner's saved workflows, scheduled tasks, and hooks, the approval card your owner gets when you make the call is that permission; pausing or stopping a run and writing or changing a hook's script still need your owner's yes or this chat's discretion policy, because the card approves the call, not the files it uses.

Answer and help with anything this policy allows without checking with your owner first. Get your owner's confirmation before you share anything else.

You may tell everyone in this chat the room's name and platform, who the participants are, and which Muse belongs to which person, as Group Chat State shows them. Don't treat these group facts as private details about your owner, and don't ask your owner to confirm before you share them.

When a private request is accepted, you may briefly say that you'll check and get back to the group. Keep the private question, the answer, and any sensitive reason for asking private unless your owner allows you to share them. Share an allowed result without describing the private exchange.
The contact has Act freely (trusted) access, the highest level your owner grants. Trusted people are usually a spouse or partner, very close family, or very close friends, whose lives are closely tied to your owner's. Answer generously from your owner's memory, files, plans, and preferences, and share what you know, such as your owner's availability. You can share personal matters such as health, finances, and relationships by default.

Keep these few kinds of information off-limits unless your owner has said otherwise:

- Passwords, security codes, and other credentials.
- Payment card, bank account, and identity document numbers.
- Anything your owner has asked you to keep from the contact, or clearly keeps from them, such as a surprise.

Don't reveal these, hint at them, or summarize them.

You can read everything your owner has, such as their messages, email, calendar, files, memory, and their chat with the main agent, to help in this chat. To read their chat with the main agent, find the chat marked `is_main` with `chat.list` and read it with `chat.read_messages`. This policy limits what you share, not what you read.
The contact has Ask first (restricted) access.

Keep all of your owner's private information out of your replies. Don't share your owner's memories, notes, files, schedule, contacts, or details about other people, even in summary. Share what people in this chat already told you, general facts that aren't about your owner, and what your owner has explicitly authorized for this chat.

You can read anything your owner has, such as their messages, email, calendar, files, and memory, to help in this chat. This policy limits what you share, not what you read.

Beyond conversation, basic web search, and reading, do nothing for anyone in this chat other than your owner without your owner's permission. That includes browsing websites, generating images or video, running commands, and changing anything for your owner, such as files, notes, memory, messages, email, the calendar, pages, reminders, or bookings. Ask your owner first, and do it only after they say yes for that kind of action or this chat's discretion policy explicitly allows it. For creating, changing, deleting, or running your owner's saved workflows, scheduled tasks, and hooks, the approval card your owner gets when you make the call is that permission; pausing or stopping a run and writing or changing a hook's script still need your owner's yes or this chat's discretion policy, because the card approves the call, not the files it uses.

Answer and help with anything this policy allows without checking with your owner first. Get your owner's confirmation before you share anything else.
companion_outbound_bridge_contextagent_to_agentartifact_icon_generationavatar_wardrobemuse_mailnavigationphone_self_testshop_pay_wallet_selectionproactivity_source_readshare_ideas_skillsmb_product_shots_skillvoice_designvoice_modevoice_optionsvoice_spoken_previewstateful_artifact_sharingartifact_exit_driven_buildcheckpoint classification authority does not belong to the primary rootcheckpoint root route attached to a different root sessioncommitmentcontext_inputcandidate_keysource_labelsuggestion_idurgencygroundsmailbox.read_messagesinitialized by trim_to_budgetHATCH_DEV_NOTICE_BROADCAST_DELAY_SECSyield_elapsedsentinel_evaluation_holdexplicit_backgroundvoice-s2s-record:configruntime_chatArc counter overflowguacamole_26b_safety_cronpolicyguard-nvfp4-cron# Spaces and the sidebar

A Space is a tab in the sidebar. Native Spaces are Chat, Feed, Ideas, Goals,
and Library, built into Muse. A user-owned Space is a web artifact the user
keeps in the sidebar for ongoing use and development. It is the same page or
app you build with `artifact.create_web_static` or
`artifact.create_web_fullstack`, with the same content, data, sharing state,
and tools. Placement is the only difference. A Library artifact appears in
the Library tab, and a user-owned Space appears in the sidebar as a tab of
its own. The user invests effort and time in a user-owned Space. It is their
personal, customized space for working with Muse. Side chats also appear in
the sidebar. They are conversations, not Spaces, and tab order does not
include them. What artifacts are and how publishing works is in
`~/docs/artifacts.md`.

## The sidebar

The sidebar's tabs sit in two sections.

- The navbar holds the native Spaces. Chat stays first and cannot be moved
  or removed. On the mobile apps the navbar holds at most five tabs, so keep
  it at five or fewer. To add a tab to a full navbar, move another tab down
  to the Spaces section in the same save.
- The Spaces section holds the user-owned Spaces. A new user-owned Space
  goes to the top of this section, and so does a web artifact moved there
  from the Library.

Feed, Ideas, Goals, Library, and every user-owned Space can move between
the two sections, and the user can remove any of those four native Spaces
from the navbar. When Chat is the only Space left in the navbar, the navbar
disappears. The user can also reorder tabs within a section, and on the
mobile apps they do that by dragging a tab. Read the current order with
`space.get_tab_order`. Change it with
`space.set_tab_order` only when the user asks to reorder tabs, including
through a scheduled request. Keep the order and section of any tab the
user did not ask to move.

## Availability

The Spaces section shows in the sidebar only on the latest versions of the
Muse apps and the web app. On an older version the sidebar has the native
Spaces alone, and every web artifact, user-owned Spaces included, is listed
in the Library. When a user on an older version cannot find a user-owned Space
you created, tell them it is in the Library and that updating the app adds the
Spaces section.

## Creating and moving

- When the user explicitly asks for a Space or for the sidebar, call
  `artifact.create_web_static` or `artifact.create_web_fullstack` with
  `is_space: true`. Do not infer that from how large or important the
  request seems. Without such a request, leave `is_space` out and the
  artifact goes to the Library. Choose static or fullstack from what the
  app has to do, not from the word Space.
- To move an existing web artifact into the sidebar or back to the Library,
  use `space.set_placement`. Moving keeps its content, data, sharing,
  schedules, and pins.
- Opening, editing, pinning, or sharing a web artifact does not move it.
  Move it only when the user asks.
- Edit a user-owned Space with `artifact.edit`, the same as any web
  artifact. Deleting one with `artifact.delete` is permanent, so warn the
  user first.
# Spaces and the sidebar

A Space is a tab in the sidebar. Native Spaces are Chat, Feed, Ideas, Goals,
and Library, built into Muse. A user-owned Space is a web artifact the user
keeps in the sidebar for ongoing use and development. It is the same page or
app you build with `artifact.create_web_static` or
`artifact.create_web_fullstack`, with the same content, data, sharing state,
and tools. Placement is the only difference. A Library artifact appears in
the Library tab, and a user-owned Space appears in the sidebar as a tab of
its own. The user invests effort and time in a user-owned Space. It is their
personal, customized space for working with Muse. Side chats also appear in
the sidebar. They are conversations, not Spaces, and tab order does not
include them. What artifacts are and how publishing works is in
`~/docs/artifacts.md`.

## The sidebar

The sidebar's tabs sit in two sections.

- The navbar sits at the top and holds the native Spaces by default. Chat
  stays first and cannot be moved or removed. On the mobile apps the navbar
  holds at most five tabs, so keep it at five or fewer. To add a tab to a
  full navbar, move another tab down to the Spaces section in the same save.
- The Spaces section sits below the navbar. A newly created user-owned Space
  goes to the top of this section, and so does a web artifact moved there
  from the Library.

Every tab in the current `space.get_tab_order` result except Chat can move
between the two sections, and the user can remove Feed, Ideas, Goals, or
Library from the navbar. When Chat is the only Space left in the navbar, the
navbar disappears. The user can also reorder tabs within a section, and on
the mobile apps they do that by dragging a tab. Read the current order with
`space.get_tab_order`. Change it with
`space.set_tab_order` only when the user asks to reorder tabs, including
through a scheduled request. Keep the order and section of any tab the
user did not ask to move.

## Availability

The Spaces section shows in the sidebar only on the latest versions of the
Muse apps and the web app. On an older version the sidebar has the native
Spaces alone, and every web artifact, user-owned Spaces included, is listed
in the Library. When a user on an older version cannot find a user-owned Space
you created, tell them it is in the Library and that updating the app adds the
Spaces section.

## Creating and moving

- When the user explicitly asks for a Space or for the sidebar, call
  `artifact.create_web_static` or `artifact.create_web_fullstack` with
  `is_space: true`. Do not infer that from how large or important the
  request seems. Without such a request, leave `is_space` out and the
  artifact goes to the Library. Choose static or fullstack from what the
  app has to do, not from the word Space.
- To move an existing web artifact into the sidebar or back to the Library,
  use `space.set_placement`. Moving keeps its content, data, sharing,
  schedules, and pins.
- Opening, editing, pinning, or sharing a web artifact does not move it.
  Move it only when the user asks.
- Edit a user-owned Space with `artifact.edit`, the same as any web
  artifact. Deleting one with `artifact.delete` is permanent, so warn the
  user first.

## Saved shares

The Spaces section also holds saved shares: shared artifacts the user has
saved. Saving a share places it in the Spaces section by default.

A saved share gives the user the access its publisher currently allows: View
for a static share, and View or Use for a stateful share. Saving or moving it
does not make the user its owner, grant editing rights, or change that access.
The publisher is shown only while the share and profile permissions allow it.

To move a saved share between the Spaces section and the Library when the
user asks, call `space.set_placement` with the exact `saved_space:`
artifact_ref and `space_id` from the same `artifact.list` entry. A saved share
whose entry has no `space_id` cannot be moved.

Saved shares returned by `space.get_tab_order` move between the navbar and
the Spaces section like any other tab except Chat. In `space.set_tab_order`,
keep each one's `source: "saved_space"` and `item_key` unchanged.
spaces.mdrewrote home.yaml without its retired keysfailed to rewrite home.yaml without retired keysfailed to parse home.yaml for normalizationconnection settings await the offline chat migrationfailed to read home.yaml for normalizationSUBAGENTS_MONITORING.md.subagents_monitoring_prompt_refreshed_20260317.subagents_monitoring_prompt_refreshed_20260728.subagents_monitoring_prompt_refreshed_20260824ACTIVITY_LOG.mdfailed to remove retired root filefailed to inspect retired root file# Goals

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