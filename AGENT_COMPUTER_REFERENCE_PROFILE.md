# Agent Computer Reference Profile

**Status:** portable reference integration contract, revised 2026-09-05.
**Architecture authority:** deployment Canonical Owner Principal under `OWNER_AUTHORITY_CONSTITUTION.md`.
**Startempire binding:** Verious Smith III.

## 1. Purpose

The Agent-Driven Life & Business OS uses Veragensia as its reference Agent Computer implementation. This document records the **portable composition relationship** without duplicating Veragensia's detailed architecture.

For Startempire, the canonical detailed specifications live in `Startempire-Wire/veragensia`, especially:

- Doc 182 — product/root composition;
- Doc 190 — agent-first software, Agentability and capability resolution;
- Doc 191 — Elastic Agent Computing and Cloud Agent Computer runtime;
- Doc 192 — telemetry and improvement plane;
- Doc 193 — ExecutionPrincipal, WorkloadIdentity and enforceable machine capability;
- Doc 194 — trusted human control, Secure Attention and DesktopObservation/control leases;
- Doc 195 — stable ResourceRefs, runtime incarnation and state transfer;
- Doc 196 — platform trust, genesis, supply chain and runtime attestation;
- Doc 197 — voice-native Agent Computer and Audio UI;
- Doc 199 — Ambient Operator, Companion sync, mobile/wearable edge, and Omarchy integration.

Focusa Specs 181–184 own the reference Conversation, Project Foreman, Radar and Ambient Operator semantics.

Portable Ambient Operator behavior is summarized separately in [`AMBIENT_OPERATOR_REFERENCE_PROFILE.md`](./AMBIENT_OPERATOR_REFERENCE_PROFILE.md).

A client deployment may replace products while preserving the portable contracts in this repository.

## 2. Deliberately listed reference defaults

A supported full Startempire Veragensia Agent Computer deliberately composes:

1. **Focusa daemon/core** — scoped cognition, ProjectIdentity, Trajectory, Workpoints, Context Authority, Evidence, receipts, learning, recovery, Expression, and Voice/Conversation lineage.
2. **Focusa Desktop** — default governed human work/cognition/conversation presenter over Focusa authority.
3. **Pi + Focusa Pi extension** — default/reference Focusa-aware agent harness integration. Pi is fundamental to the reference Focusa agent experience but is not a second cognitive authority.
4. **UIAI Engine + Cockpit/browser/computer surfaces** — canonical first-party browser/computer execution, observation, diagnostics, operator oversight, control and proof stack. UIAI is deliberately listed; it is not merely an optional browser candidate in the reference composition.
5. **Veragensia enforcement/control substrate** — machine enforcement of semantic authority, trusted human control, stable resource/runtime identity and workload/platform trust.
6. **Voice/Conversation service** — trusted Audio UI bound to Focusa Voice/Conversation semantics, making keyboard and mouse optional peripherals in a full `voice_complete` profile.
7. **Veragensia session/shell integration** — host Agent Computer lifecycle, application composition, interruption, containment, review and recovery.

A personal/ambient profile may additionally bind a paired **Ambient Operator Companion**: mobile/wearable presence, meeting/conversation capture, Radar attention, Project Foreman/Chief-of-Staff routing and offline/private synchronization. The Companion remains a surface of the same governed system rather than a second cognitive store.

This list is a reference implementation binding, not portable vendor vocabulary. The portable requirement is that a deployment provide equivalent governed cognition, work presentation, agent harness, computer/browser execution, **machine-enforceable capability boundaries**, trusted human intervention, voice/nonvisual operation, attributable conversation history, Evidence, and host lifecycle contracts.

## 3. Authority and enforcement boundaries

The composition does not collapse authority:

```text
Canonical Owner Principal
    constitutional architecture authority

Focusa daemon/core
    scoped cognitive/operational/conversation/Foreman/Radar semantics

Focusa Desktop
    presenter over Focusa operations

Pi
    reference harness-edge consumer/producer

UIAI Engine
    browser/computer runtime authority in its execution domain

Veragensia
    Agent Computer host + machine enforcement + trusted control + audio/sync integration

Ambient Companion
    paired mobile/wearable interaction endpoint
```

A UI, harness, runtime, repository, service account, root shell, Unix UID, browser session, voiceprint, paired phone, wearable or deployment does not gain constitutional or application authority merely because it exists or is a default component.

### Portable enforcement invariant

A semantic capability is not considered fully governed merely because policy says it is allowed/denied.

The deployment needs an equivalent of:

```text
semantic authority / grant
→ enforceable execution plan
→ workload/execution identity
→ filesystem/network/device/credential/input restrictions
→ evidence of enforcement
```

Specific Linux mechanisms are replaceable; the law is not.

## 4. Agent-first software doctrine

The reference Agent Computer prefers:

```text
structured capability
→ semantic application automation
→ visual computer use
```

Full computer use remains required because real life/business work includes legacy, unfamiliar and non-API applications.

Default application selection should optimize for **agentability, enforceability, attestability, and human modality parity** as well as human usability. A good Agent Computer application exposes stable machine-operable state, typed/structured actions where possible, clear authority boundaries, inspectable outcomes, Evidence/receipt paths, and a containment model that actually matches its granted capabilities.

The detailed Agentability classes and resolver belong to Veragensia Doc 190. This portable repository should not fork them into an incompatible local taxonomy.

## 5. Voice-native human interaction

The portable full Agent Computer contract now includes this invariant:

> **Keyboard and mouse are optional peripherals.** A person must be able to accomplish ordinary supported outcomes through natural voice interaction in a declared `voice_complete` profile.

That includes, through the same canonical operations:

- work/project navigation;
- search/retrieval;
- document/file editing;
- browser/computer work;
- agent/team creation and steering;
- pause/stop/takeover/return control;
- approvals and clarifications;
- status and recovery;
- Evidence/Receipt review;
- conversation/audit search.

Voice is primarily semantic intent, not a macro layer that forces the user to describe pointer mechanics.

A client can use any suitable ASR/TTS/speech-to-speech technology. The portable contract requires provider-neutral conversation objects, authority, attribution, transcript lineage, and outcome parity.

## 6. Conversation and audit contract

The reference system preserves a local-first, searchable conversational history without turning conversation into canonical memory.

Portable semantics include:

```text
ConversationSession
Participant
AudioSegment or source handle
Speech hypothesis
Utterance
Transcript revision/correction
Expression output
Spoken output
Action/Evidence/Receipt links
```

Required laws:

- every human/agent speaker is attributable or explicitly unknown;
- every agent/expert speaker binds a stable principal independently of its synthetic voice;
- ASR uncertainty is explicit;
- transcript/speaker corrections append/supersede rather than erase history;
- overlapping/interrupted speech is preserved where possible;
- human barge-in/new steering supersedes stale agent conversational momentum;
- voice recognition/voiceprint alone does not authorize consequential actions;
- spoken agent output is traceable to the semantic content it rendered;
- conversation is provenance/audit, not automatic Workpoint/memory/policy/knowledge promotion.

A user should be able to ask:

```text
"What exactly did the security expert say before I approved that?"
"Which agent disagreed?"
"Go back to the conversation where we decided the migration."
"What did you hear me say?"
```

and traverse the relevant utterances, corrections, actions and outcomes.

## 7. Ambient Operator relationship

The portable **Ambient Operator** pattern extends the same governed system beyond the desktop.

It distinguishes:

```text
Chief of Staff
    broad owner-authorized life/business intelligence

Project Foreman
    one exact project/Workstream's persistent operating intelligence

Radar
    scoped proactive observation/attention

Ambient Companion
    phone/earbuds/wearable interaction and presence edge
```

The Companion may provide context-only, wake-word, conversation, meeting, private-note or execution-supervision modes, but must preserve the separate ownership/retention/authority boundaries in `AMBIENT_OPERATOR_REFERENCE_PROFILE.md`.

A mobile or wearable endpoint never becomes a new project brain merely because it is always nearby.

## 8. Capability-first profiles

Life/business roles should request capabilities rather than hardcode packages wherever practical.

For example:

```yaml
role: client-onboarding-specialist
needs:
  - browser_work
  - correspondence
  - scheduling
  - document_editing
  - crm
interaction:
  voice_complete: true
  ambient_operator: true
```

The Agent Computer may satisfy those needs using desktop-native applications, Agent Apps, web applications through UIAI, headless services, or remote specialist runtimes according to policy and platform.

Exact application pins remain valid when a workflow/customer requires them.

## 9. Elastic workforce relationship

A request such as:

> Give this project another team.

may resolve into a mixed Veragensia topology:

- additional Focusa Silent Sessions;
- headless workcells;
- browser execution contexts;
- Agent Apps;
- a full Cloud Agent Computer;
- or a combination.

The Chief of Staff/workforce layer requests outcomes/capability. It should not need to manually design VM/container topology.

Elastic creation itself requires a bounded topology grant equivalent: permitted runtime classes, fanout/depth, agent/machine/session maxima, spend, duration, region/data locality, and delegation limits. A spawned agent does not automatically inherit the ability to spawn more agents.

Infrastructure placement never grants broader business or application authority.

## 10. Human/agent collaboration

The reference Veragensia implementation provides Agent Assist semantics such as observe, guide, shared control and delegated control.

Portable invariant: any collaborative computer session binds the actor, task/work unit, machine/runtime incarnation, capability/authority, observation/action scope, control holder/generation, revocation, re-observation, and Evidence/receipt posture.

Human takeover must fence stale agent input. Returning control must reconcile what changed before an agent resumes.

Remote-control transport is not permission.

Voice-complete and Ambient profiles expose the same takeover/stop/continue semantics through speech/mobile controls without creating a separate permission path.

## 11. Stable resource and runtime identity

Portable deployments must not use paths, PIDs, window titles, browser target IDs or container names as if they were durable identity.

Consequential actions should bind:

```text
stable logical resource
+ expected revision
+ current runtime incarnation
+ current locator/projection
```

Restarts, migrations and restores invalidate or rebind stale runtime references explicitly. Local/cloud replicas cannot silently overwrite each other. Filesystem/process rollback is distinct from reversal of external real-world effects.

## 12. Platform/workload trust

A deployment should distinguish:

```text
owner principal
agent principal
node identity
workload identity
execution principal
runtime attestation
capability grant
```

Trust posture may range from an owner-controlled developer machine to signed/measured/hardware-attested environments. Lower-trust hardware can remain useful while higher-risk roles require stronger posture.

Software/image/app descriptors do not self-attest their own trust or Agentability.

## 13. Software catalog boundary

The exact best applications for coding, office work, notes/knowledge, communications, meetings, CRM, finance, media, data and vertical workflows are deliberately not frozen here.

Future software evaluation should choose applications using measured agentability, human quality, voice/nonvisual outcome parity, enforceability, provenance/attestation, stable resource semantics, portability, privacy, isolation, resource use, licensing and accepted-outcome evidence.

Do not promote a software package into portable architecture merely because it appears in one reference image.

## 14. Telemetry boundary

The reference implementation may use Veragensia's privacy-tiered telemetry/improvement plane.

Portable invariant:

```text
allowlisted bounded metrics / events / sampled traces / explicit Evidence
conversation content and private content are separate local-first domains
```

Telemetry schemas should use field allowlists and cardinality limits so filenames, URLs, transcript/audio, prompts, speaker names, customer data or arbitrary model strings cannot leak as labels.

Voice quality can be measured through content-free metrics such as ASR correction rate, barge-in latency, TTS-start latency, speaker-attribution uncertainty, voice-task success and keyboard/mouse fallback rate.

Ambient telemetry may also measure content-free sync/wake/route metrics, but raw audio, transcript, precise location and owner-life context remain separate privacy domains.

Telemetry may identify improvement candidates. It is evidence, not owner authority or automatic policy change.

## 15. Full-profile acceptance direction

A portable deployment should not claim equivalent full Agent Computer behavior until applicable evidence proves:

1. semantic permissions are backed by actual machine enforcement;
2. human stop/takeover remains available under workload pressure;
3. stale resource/runtime/control identities fail closed;
4. workload/runtime trust is explicit;
5. representative supported work can be completed in the declared voice-complete profile without keyboard/pointer;
6. group agent conversation preserves speaker/principal attribution;
7. spoken instructions trace through actions to Evidence/Receipts;
8. conversation/transcript history survives restart under its retention policy without becoming canonical memory;
9. conversation/audio content remains outside generic telemetry by default;
10. Chief-of-Staff vs Project Foreman routing preserves exact project scope;
11. Radar attention is scoped/deduplicated and cannot self-authorize work;
12. mobile/wearable sync is authenticated, replay-safe, idempotent and acknowledged;
13. raw owner-life context such as exact GPS does not become project cognition by default;
14. mobile OS suspension/background restrictions are surfaced honestly.

## 16. Drift rule

When this document and canonical Veragensia specifications conflict for the Startempire implementation, use the newer owner-authorized Veragensia architecture for Agent Computer implementation details and update this portable reference accordingly.

For Ambient behavior, also consult `AMBIENT_OPERATOR_REFERENCE_PROFILE.md` and the canonical Focusa 181–184 ownership model.

Do not silently copy temporary implementation quirks, public-demo trust assumptions, customer identities or infrastructure topology into this portable substrate.
