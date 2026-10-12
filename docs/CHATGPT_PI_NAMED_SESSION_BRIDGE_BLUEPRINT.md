# ChatGPT ↔ Named Pi Sessions — Thin SOVOS Bridge Blueprint

**Status:** INCUBATING — owner-selected planning direction; **not implemented, installed, or runtime-verified**  
**Date:** 2026-10-11  
**Purpose:** Close the planning loop for a private ChatGPT → existing named Pi session → verified results workflow, with a future reusable customer-facing adapter.  
**Scope:** Blueprint only. No deployment, code change, live agent instruction, permission grant, or production migration authorized by this document.

## 1. One-sentence decision

**Build a thin, optional, name-first connection to existing Pi sessions, using existing SOVOS/Focusa owners and the GitHub connection as the temporary private transport.** Do not build another agent, duplicate the Focusa extension, require SSH/OAuth/MCP for the private pilot, or substitute Pi Durable/Focusa Silent Sessions until their relevant live contracts are proven.

Keep the human interface as simple as: **“Connect to the Focusa development session; ask it to do X; show me its result.”** The user should not need to retrieve IDs or open Termius to route each task.

## 2. Architecture ownership and boundaries

This blueprint is subordinate to `../OWNER_AUTHORITY_CONSTITUTION.md`, `../CURRENT_ECOSYSTEM_ARCHITECTURE.md`, `../CROSS_PRODUCT_SEAM_CONTRACT.md`, and `agent-os-golden-path/07-agent-operation-complete-software-contract.md`.

- **SOVOS:** portable integration design/contract, **not** a new runtime, database, or identity authority.
- **Wirebot Core / Wirebot App:** owner/customer identity, admission, entitlement, partner-facing experience and account linkage as owned by existing products.
- **OpenClaw:** customer's enduring Operating Partner/Chief of Staff and existing channel/automation runtime; does **not** become an alternate project-work authority.
- **Pi:** coding-agent execution and native JSONL session persistence. **Focusa does not replace Pi.**
- **Focusa:** verified project/Workstream/continuity binding, Workpoints, governed work, receipts/Evidence and the **single already-installed Focusa Pi extension**.
- **Focusa Silent Sessions / POSIX runner:** project-owned governed headless-process capability, subject to exact installed/runtime proof before reuse for this bridge.
- **UIAI Engine:** browser/computer actuation and visual proof when requested; never the default integration transport.
- **GitHub:** temporary private work-request/response transport and existing version-control evidence. Its issue/file state is **not** a grant, canonical work authority, or substitute for Focusa receipts.

The agent process's initial working directory (`/root`, for example) is not necessarily the project root. Never bind broad `/root` or `/` as project authority. Resolve exact verified Focusa project/Workstream identity separately from Pi launch location. Use the existing canonical project marker workflow; never hand-write `.focusa-project.json`.

### High-level path

```text
PRIVATE PILOT (initial)
ChatGPT --authenticated GitHub connector--> private inbox (one request/ref)
                                            |
                              existing host timer/dispatcher
                                            |
                            resolve exact owner + project +
                             named Pi JSONL session (pi -r UX)
                                            |
                      +---------------------+---------------------+
                      |                                           |
                 Pi ALIVE                                   Pi STOPPED
                      |                                           |
           existing Focusa Pi extension                 governed on-demand
           optional inbound capability                  Pi session startup
           inside same Pi process                       (verified single writer)
                      |                                           |
                      +--------------- Pi ------------------------+
                                       ↔ Focusa
                                         |
                                 progress + Evidence
                                         |
                                private GitHub reply
                                         |
                                      ChatGPT
```

**Optional future customer ingress** (Wirebot App, Discord, ChatGPT/MCP or narrow WordPress companion) reaches the **same canonical operation** via Wirebot Core, tenant admission and OpenClaw delegation. WordPress and Svelte are website/application targets; WordPress is at most an optional lightweight client doorway, not the system center. Full-Sovereign and managed isolated customer deployment profiles stay distinct.

## 3. Selected first version — simplest deliverable

1. Use an **existing operator-controlled private GitHub repository** as the inbox; choose/provision the actual repo at implementation time. Do not place private prompts, paths, JSONL content or credentials in public SOVOS/Focusa repositories.
2. ChatGPT submits a small, human-readable request to that private repo using its existing authenticated GitHub integration. One GitHub issue or one bounded request file is enough. Choose **one** transport representation in implementation, not both simultaneously.
3. A **small owner-user host dispatcher**, awakened by an existing OpenClaw automation or a systemd timer, reads pending requests through GitHub API/CLI. It is a transport/wake-up adapter, **not** another supervisor, cognitive runtime, database or new self-hosted GitHub Actions runner.
4. The dispatcher resolves owner, host, verified project binding, session name, session ID and canonical JSONL path; authorizes scope, liveness, expiry and single-writer admission. GitHub possession alone never grants permission to execute.
5. If that exact Pi process is **alive and opted into the extension ingress**, send through the existing process. If not alive, use a verified on-demand Pi launch/resume path and no second writer.
6. Return accepted → delivered → agent-finished / failed states, exact links to Git commits/preview when applicable, and Focusa evidence/receipts. A GitHub write or HTTP 202 is not task completion.
7. No production publishing without the owner/receiving system's current approval and proof.

**Not required for v1:** direct SSH, exposed port, OAuth server, OpenAI Secure MCP Tunnel, independent MCP package, Pi Durable migration, WordPress plugin, custom customer portal, separate Focusa Pi extension, new queue database, or continuous standalone Pi process. Any later real-time MCP connector is an **adapter replacement**, not an architecture rewrite.

## 4. Named Pi session resolution — adopt the `pi -r` user experience

Pi's native `pi -r` / `--resume` opens an **interactive picker**, not a headless IPC mechanism. Pi 1.0 documents `pi --session <path|id>`, `--mode rpc`, and `-p/--print` as programmable alternatives; exact installed-version semantics still require local confirmation.

Pi stores JSONL sessions in project-partitioned directories. The source `session_info` entry carries the friendly display name. Use **read-only** native session listing/SessionManager where possible, otherwise parse exact bounded metadata; never append or rewrite JSONL from the bridge.

Resolution algorithm:
1. Limit search to permitted Pi session roots for the **specific OS user and authorized environment**.
2. Read session metadata, including `session_info.name`, native session identity, file path, originating cwd and last activity; verify the requested name, not a fuzzy arbitrary path glob.
3. Resolve against Focusa's **verified** project root, Workstream/continuity, and attachment; the display name is just an alias.
4. If zero candidates, return `not_found`; if multiple, return bounded disambiguation choices, **never guess**. A renamed session does not rewrite its durable identity.
5. Carry exact session ref/path privately into delivery. It should not have to be spoken, pasted or remembered by the owner.
6. Before reopening large existing sessions, reuse the existing Focusa Pi native-session **preflight** (`focusa pi launch`) and its migration/retention safety; oversized sessions fail closed pending the approved recovery path.

Do not mistake reading a JSONL file for access to the already-running Pi process. JSONL stores conversation history, not an attached command channel.

## 5. Two execution paths and the idle/offline condition

### 5.1 Live Pi — use the **same existing** extension

After active process and exact session/attachment verification, register a small, **optional, default-off** inbound component within `Startempire-Wire/focusa/apps/pi-extension/src/` through the existing `index.ts` registration path. Do not install a second Pi extension or a second Focusa brain.

Proposed mechanism: a private same-user Unix-domain socket or equivalent narrowly scoped local IPC endpoint owned by the active Pi process, with a verified runtime registration/lease. The dispatcher uses it only after authenticating and matching exact session, project, attachment and process incarnation. A mere socket pathname/PID file is not liveness/authority proof.

Inside the active Pi process, the existing ExtensionAPI may deliver an authorized user message using the **installed Pi-version** semantics, with explicit `followUp` versus `steer` handling. Do not inject during headless bootstrap or while an unsafe competing turn is active. Acknowledge receipt **only after** the process accepts the message and distinguish that from agent completion.

Extension activation must respect Focusa's existing single-package discovery root, exact attachment runtime binding, native reload/activation receipt and no duplicate handlers. A source commit does not prove the older running process loaded the new module.

### 5.2 Pi stopped — wake the owning executor, not the extension

The extension cannot listen after its Pi process exits. The GitHub inbox must therefore be observed by **an existing durable host facility** (OpenClaw automation if appropriate, or one small systemd timer/service) outside Pi. The dispatcher must:
1. Verify owner/project/session; reject expired requests and stale authority.
2. Establish **exclusive OS-user/session writer ownership** and reconcile possibly-running interactive Pi, tmux/Termius sessions, RPC children and Focusa-owned runs. **Do not assume an unlocked session file means the process is absent**; noncooperating/ambiguous live processes block cold start.
3. Invoke Pi 1.0 headlessly **against the exact saved session**, with the canonical Focusa extension **loaded and verified** if the requested task needs Focusa capabilities. The implementation chooses the installed Pi-supported `--session` plus `--mode rpc` or bounded `--print` execution after smoke tests, preserving the user's chosen provider/model and session history.
4. Observe process exit and actual agent outcomes; publish receipts and release the writer claim. Recover ambiguous crashes by reconciling effects before retry; never resend on a blind timeout.
5. If the **VPS itself is offline**, leave the GitHub request pending. The next healthy scheduled check may reconcile and dispatch it after revalidating expiry/authorization.

Never automatically overwrite, compact, fork, migrate, delete or clean another session's JSONL. Preserve all project state, Workpoints, evidence and operator context.

### 5.3 Existing Focusa implementation — critical reconciliation

At Focusa source commit `511e6cc7a480ab53d7fd317be1de97c1de99fafb` (inspected 2026-10-11):

- `crates/focusa-api/src/routes/work_loop.rs` **actually spawns** a Pi RPC child and accepts a `resume_session` parameter via the Work Loop driver, but currently seeds `--no-session --no-extensions --no-skills --no-prompt-templates`. **Do not presume this path will load the Focusa extension or safely resume an existing named JSONL session** just because `--session` can also be appended; reconcile CLI precedence, consumer activation and evidence first. It is a separate Work Loop path.
- `crates/focusa-api/src/routes/silent_sessions_lifecycle.rs` records a start request with HTTP 202, **not** a proven launched runner.
- `crates/focusa-api/src/routes/silent_sessions_input.rs` records delivery status `queued`, **not** proven user-message delivery.
- `crates/focusa-core/src/silent_sessions/runner_protocol.rs` and `crates/focusa-session-runner/src/main.rs` implement POSIX runner `Launch`, `Signal`, `Query`, `Heartbeat`, `Adopt`; they do **not** expose `SendInput`/prompt/steer on that runner wire.
- `crates/focusa-harness-adapters/src/pi_rpc.rs` implements a Pi RPC adapter including native session switch, but code presence and isolated tests are not an installed daemon-to-runner end-to-end confirmation.
- **Focusa issue [#679](https://github.com/Startempire-Wire/focusa/issues/679)** tracks the distinct missing/unproven protected-runner launch/input handoff. Reuse that issue; do not silently bypass it or make a duplicate runtime.
- Focusa's package manifest has an older `@earendil-works/pi-coding-agent` development version than the owner's reported working local Pi **1.0**. Treat the installed runtime's extension API, flags, active package digest, and interaction mode as the only compatibility truth; **do not downgrade Pi or change active installations to match the dev manifest**.

**Disposition:** v1 must work independently of the unproven daemon-native Silent Session handoff by choosing a locally verified Pi-supported cold start path, or report an explicit blocker. Subsequently converge any production execution path on the canonical Focusa owner after #679 closes with real producer/consumer proof. No new always-on supervisor is authorized in this blueprint.

## 6. Request/receipt shape (illustrative, not a new canonical schema)

Use existing SOVOS reference/authority contracts first. Example private transport envelope, subject to owning-domain validation:

```json
{
  "version": "pilot-1",
  "request_id": "opaque-replay-safe-id",
  "origin": "chatgpt-github",
  "operator_ref": "resolved-authorized-principal",
  "environment_ref": "resolved-existing-environment",
  "target": {
    "pi_session_name": "Focusa development",
    "project_ref": "resolved-existing-project",
    "workstream_ref": "resolved-existing-workstream"
  },
  "action": "submit_user_instruction",
  "mode": "follow_up",
  "instruction": "Inspect the next authorized task; report proposed changes first.",
  "idempotency_key": "one-delivery-attempt-per-intent",
  "created_at": "producer-verified-timestamp",
  "expires_at": "producer-verified-expiry",
  "approval_ref": "required-only-when-authorized-by-owner-policy"
}
```

The receiving adapter obtains actual GitHub actor identity through authenticated provider metadata, binds it to the authorized operator, enforces allowed actions and refreshes current authority. A hand-edited actor/ref string in the body is not proof. Do not encode API keys, SSH passwords, private source, customer PII or native session transcripts in GitHub instructions.

Receipt/status sequence: `requested` → `admitted` / `blocked` → `target_resolved` → `process_accepted` / `cold_started` → `instruction_delivered` → `running` → `completed` / `failed` / `unknown_effects_reconciling`. Every step has a source, correlation/idempotency and accurate proof or reason; duplicates return the same reconciled receipt. Owner-facing responses summarize the result and link to source evidence rather than claiming completion from a queued GitHub issue.

## 7. Private pilot implementation order — small, dependency-first

**Planning complete; implementation not requested.** An authorized build agent should carry out only an owner-approved future implementation scope:

1. **Inventory without mutation:** report `pi --version`, installed Focusa Pi extension path/version/digest and one owner-selected named session. Verify GitHub connector permissions, host's existing scheduler, daemon, Work Loop and Silent Session capabilities without touching production processes.
2. **Read-only resolver:** make name-first session discovery return exact verified target, ambiguity, status and project binding. Confirm it matches the user's `pi -r` picker on one pilot host.
3. **Cold start / single writer:** choose the smallest verified Pi 1.0 native headless invocation; prove extension availability and persistence with a harmless read-only prompt in a nonproduction clone or explicitly approved safe session. Prove refusal when active writer is uncertain. Do not run unsafe launch commands from an unauthenticated GitHub request.
4. **Hot delivery:** opt-in one active Focusa Pi extension instance to exact-session local IPC, prove receipt, rebind and shutdown/reload isolation; do not inject into unrelated sessions.
5. **Transport/replies:** accept an authorized private GitHub request, dispatch through the chosen path, return one response with exact results/receipt and idempotent retry/recovery. Polling interval, quotas, outage backlog and GitHub rate budget are host-specific choices, not invented global constants.
6. **Negative tests:** duplicate names, wrong project/user/tenant, stale grants, stopped/ambiguous session, two simultaneous requests, restart mid-delivery, GitHub outage, corrupt/oversized JSONL, extension missing, and required approval denied.
7. **Close one real slice:** `ChatGPT request → name resolution → exact original Pi session → Focusa context preserved → confirmed agent output → reply visible to ChatGPT`. Record actual versions, logs and outcomes before calling it operational.
8. **Then consider faster transport:** same operations via a scoped HTTPS/MCP/OAuth adapter or an authenticated SOVOS channel, if needed; the bridge must remain transport-neutral and customer tenant-isolated. Reuse owner credentials/entitlement authority, not a general-purpose remote shell.

Do not spawn self-hosted GitHub Actions runners, Docker builds, duplicate sessions or expansive cache directories simply to perform this pilot. Existing disk-retention risk is tracked in [Focusa #662](https://github.com/Startempire-Wire/focusa/issues/662); preserve native JSONL and Focusa durable data.

## 8. Customer surfaces / publication — deferred packaging, same operation

Customer distribution **does not change the primary product architecture**:
- Wirebot App is the principal partner application; OpenClaw is the Chief of Staff runtime; Focusa governs project work.
- A customer **ChatGPT plugin/MCP connector** can be published later as an authenticated Wirebot/SOVOS adapter with exact tenant routing, scoped operation discovery and receipts; never unrestricted SSH/root shell. Public review/hosting/auth requirements must be rechecked at publication time.
- A **WordPress plugin** may provide a thin website-scoped entry point or marketing-site integration without becoming the SOVOS application. Svelte sites/apps use equivalent web adapters. Do not build WordPress integration for the private Pi pilot.
- Hosting entitlement/profile varies. **Dedicated full-Sovereign** uses the customer's own VPS/private mesh/local body under `operator.environment.v1`; **managed Wirebot** may use verified isolated operator-managed workloads. Neither a WordPress login nor a ChatGPT connector confers architecture authority or a Sovereign certification.

Future interfaces should bind to canonical typed operations and reuse the same correction/follow-through receipts, not duplicate the project database, approval store, inbox/scheduler or Operating Partner memory.

## 9. Decision/verification ledger

| Item | Planning disposition | Runtime evidence |
|---|---|---|
| Name-first session UX based on `pi -r` | **SELECTED** | Pi documented; bridge not built |
| Exact JSONL path/ID internal, verified Focusa project binding | **SELECTED** | Target integration not built |
| Existing Focusa Pi extension as the *only* Pi extension | **SELECTED** | Source exists; bridge ingress not built |
| GitHub private inbox/reply as temporary transport | **SELECTED FOR PRIVATE PILOT** | Existing ChatGPT GitHub connection; new dispatcher not built |
| Pi running → extension-delivered instruction | **TARGET** | Not yet verified |
| Pi stopped → guarded native Pi cold resume | **TARGET** | Existing Work Loop RPC spawn source; exact extension/session parity not verified |
| POSIX Silent Session runner as complete input delivery | **BLOCKED/UNPROVEN** | Focusa [#679](https://github.com/Startempire-Wire/focusa/issues/679) |
| Direct SSH, OAuth, MCP tunnel or Pi Durable needed in private pilot | **NOT REQUIRED** | Reconsider only if chosen transport fails |
| ChatGPT/WordPress/OpenClaw customer packaging | **FUTURE OPTIONAL ADAPTERS** | Not implemented by this plan |
| Existing code/server modifications | **NONE AUTHORIZED BY THIS BLUEPRINT** | Planning artifact only |

### Handoff / reopen instruction

When resuming this work, read **this blueprint**, the latest `CURRENT_ECOSYSTEM_ARCHITECTURE.md`, Focusa `apps/pi-extension/src/index.ts`, Focusa `crates/focusa-api/src/routes/work_loop.rs`, the protected runner protocol and issue #679. Obtain up-to-date installation evidence from the actual host. **Do not start with a new agent, alternate extension, or duplicate work queue.** Owner must authorize implementation separately; close the task only with the first end-to-end live receipt.

## Sources

- [Pi CLI/session options](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/usage.md)
- [Pi JSONL session format — `session_info` name](https://pi.dev/docs/latest/session-format)
- [Pi RPC mode](https://pi.dev/docs/latest/rpc)
- [Focusa extension source](https://github.com/Startempire-Wire/focusa/blob/main/apps/pi-extension/src/index.ts)
- [Focusa Work Loop Pi RPC driver](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-api/src/routes/work_loop.rs)
- [Focusa Silent Sessions lifecycle](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-api/src/routes/silent_sessions_lifecycle.rs)
- [Focusa Silent Sessions input](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-api/src/routes/silent_sessions_input.rs)
- [Focusa POSIX runner protocol](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-core/src/silent_sessions/runner_protocol.rs)
- [Focusa issue #679 — delivery-path proof gap](https://github.com/Startempire-Wire/focusa/issues/679)
