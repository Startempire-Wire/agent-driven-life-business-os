# Ambient Operator Reference Profile

**Status:** portable reference integration contract, 2026-09-05.  
**Architecture authority:** deployment Canonical Owner Principal under `OWNER_AUTHORITY_CONSTITUTION.md`.  
**Startempire binding:** Verious Smith III.  
**Reference implementation:** Focusa Specs 181–184 + Veragensia Doc 199 + UIAI Engine + Wirebot Context Core/Chief-of-Staff adapters.

## 1. Purpose

A life/business OS should not stop at the desktop. The portable architecture includes an **Ambient Operator** pattern: a paired phone, earbuds, wearable, car audio or future surface can keep the owner continuously connected to the same governed agent/work system while preserving authority, privacy, provenance and exact project boundaries.

This is not a requirement to record everything or centralize a person's life in the cloud.

The portable law is:

> **The system can be ambiently available without being ambiently omniscient, always-recording, or globally authoritative.**

## 2. Portable role hierarchy

```text
Canonical Owner Principal
        |
Chief of Staff / life-business intelligence
        |
        +-- Project/Workstream Foreman A
        +-- Project/Workstream Foreman B
        +-- Project/Workstream Foreman C
                |
             workers/tools
```

The Chief of Staff may reason across owner-authorized life/business domains.

A **Project Foreman** remains responsible for one exact project/Workstream and is a projection of persistent project intelligence, not merely the current LLM session.

## 3. Project Foreman invariant

Portable equivalent of Focusa Foreman must provide:

- stable project/workstream identity independent of model/provider/session;
- bounded hydration from project genesis, goals/trajectory, current work, decisions, evidence, history, constraints and environment;
- worker delegation/supervision under existing authority;
- recovery after model/session/worker/device loss;
- same project intelligence through desktop, mobile, voice, API and other surfaces;
- Evidence/Receipt-backed claims about consequential/completed work.

A Foreman role does not self-grant permission.

## 4. Radar invariant

Portable **Radar** means proactive, scoped observation/attention rather than a notification or surveillance product.

```text
source event/observation
→ structured capture
→ fingerprint/deduplication
→ Episode/pattern
→ signal economics
→ policy/authority posture
→ remember / notice / prepare / investigate / act-under-grant / escalate
```

Radar should optimize the owner's attention.

It must:

- be scope-bearing;
- preserve source/freshness/evidence;
- prefer structured/semantic observations over screenshots;
- group duplicate observations into Episodes;
- account for interruption, privacy, compute, risk and uncertainty cost;
- never mint permission or canonical mission truth merely by observing something;
- never require hidden keystroke/microphone/screen surveillance.

## 5. Ambient Operator invariant

The mobile/wearable surface may support modes such as:

```text
off
context_only
wake_word
conversation
meeting
private_note
execution_supervision
```

The exact product names are replaceable. The semantics are not.

### Wake word

- local/on-device detection preferred when practical;
- pre-trigger buffer volatile/discarded by default;
- attention event only, not authentication/authorization.

### Conversation

- same canonical operations as other modalities;
- stable human/agent speaker identity or explicit unknown;
- transcript correction lineage;
- utterance → action → Evidence/Receipt traceability;
- full-duplex/interruption where supported.

### Meeting

- explicit capture/recording state;
- participant/speaker attribution and confidence;
- raw audio/transcript as separate retention classes;
- commitments/decisions/tasks become candidates, not automatic durable truth;
- recording/consent policy configured for the deployment rather than assumed from a generic mode flag.

## 6. Conversation is not memory

A portable system may preserve rich, even exhaustive, conversation provenance without injecting it wholesale into canonical agent memory.

```text
source audio
→ speech hypothesis
→ corrected/accepted transcript
→ interpreted candidate
→ governed promotion/operation
→ durable state if accepted
```

Raw transcript history remains searchable/auditable according to policy.

## 7. Life-context boundary

Location, motion, device state, health, interruptibility and other owner-life context belong first to an **owner-domain context service**.

Project/workstream systems consume bounded projections when relevant.

Portable location classes SHOULD distinguish:

```text
none
on_device_only
coarse
precise_task_scoped
```

Precise GPS should not be copied into every project or global agent prompt by default.

## 8. Mobile/wearable identity

A paired phone or wearable is:

- a device principal/endpoint;
- a source of bounded observations;
- a conversation/audio endpoint;
- potentially a trusted presence factor under explicit policy.

It is not:

- architecture authority;
- application permission by itself;
- proof of speaker identity by Bluetooth connection alone;
- a new canonical project-memory store.

Physical controls may resolve exact pending operations only when paired, fresh, scoped and policy-authorized.

## 9. Sync contract

Portable Ambient sync is transport-independent:

```text
nearby BLE/Bluetooth
local LAN
private overlay network
explicit relay
encrypted offline queue
```

Use Bluetooth for audio/proximity/small controls where useful; do not require it for hours of transcript/audio/Evidence data.

Sync needs:

- paired device identity;
- encrypted transport/storage;
- sequence/replay defense;
- idempotency;
- acknowledgement/reconciliation;
- exact privacy class;
- stale/offline state;
- revocation/device-loss recovery.

A mobile edge submits typed observations/proposals/conversation segments. It does not write the canonical reducer/database directly.

## 10. Computer execution

Ambient voice/mobile intent does not create a special actuator path.

Portable flow:

```text
human ambient intent
→ exact Chief-of-Staff or Foreman scope
→ canonical authority
→ execution adapter / agent computer / browser
→ observation + action
→ verification
→ Evidence/Receipt
→ spoken/visual result
```

For the Startempire reference, Veragensia owns machine enforcement and UIAI Engine owns browser/computer execution/proof.

## 11. Proactive attention example

```text
Radar notices deployment instability
→ project Foreman investigates
→ safe response prepared
→ owner-domain context reports low interruptibility while driving
→ Chief of Staff waits
→ owner becomes interruptible
→ earbuds surface one bounded question
→ owner approves/denies through normal authority
→ work executes and settles
→ verified result is spoken back
```

This is the desired difference between a living operating environment and a notification feed.

## 12. Privacy classes

At minimum distinguish:

```text
PRESENCE_SIGNAL
TRANSCRIPT
RAW_AUDIO
PRETRIGGER_WAKE_BUFFER
PRECISE_LOCATION
PROMOTED_SEMANTIC_STATE
```

Each has separate purpose, storage, retention, export and deletion rules.

Generic telemetry does not inherit permission to collect conversation/audio/location content.

## 13. Mobile platform honesty

Mobile operating systems may suspend background tasks or restrict microphone/location use.

The portable state model therefore includes:

```text
ambient_ready
wake_listening
active_conversation
meeting_recording
audio_interrupted
background_restricted
suspended_by_platform
offline
syncing
recovering
```

Never market or report `always listening` when the platform actually suspended capture.

## 14. Reference deployment mapping

| Portable role | Startempire reference |
|---|---|
| Chief of Staff | Wirebot / OpenClaw |
| Project Foreman | Focusa Spec 182 |
| Radar | Focusa Spec 183 |
| Conversation/meeting | Focusa Spec 181 |
| Ambient Operator | Focusa Spec 184 |
| owner-life context | Wirebot Context Core / future Companion sensor layer |
| Agent Computer | Veragensia |
| browser/computer hands | UIAI Engine |
| reference harness | Pi + Focusa extension |
| mobile runtime | future native Companion; existing Phone Bridge is context-only proving ground |

## 15. Implementation/adoption checklist

A deployment should not claim Ambient Operator parity until it proves:

- [ ] exact owner/device pairing and revocation;
- [ ] Chief-of-Staff vs Project Foreman identity routing;
- [ ] Foreman continuity across model/session changes;
- [ ] scoped Radar Episodes/Signals with deduplication;
- [ ] local/private wake-word posture or explicit alternative;
- [ ] auditable voice/meeting transcript lineage;
- [ ] raw-audio/transcript/precise-location retention separation;
- [ ] bounded context projection into project scope;
- [ ] encrypted replay-safe offline sync;
- [ ] normal authority before computer/browser execution;
- [ ] Evidence/Receipt-backed result reporting;
- [ ] honest mobile background/suspension state;
- [ ] no surveillance/default ambient recording requirement;
- [ ] no keyboard/mouse dependency where the deployment claims voice-complete Agent Computer behavior.

## 16. Final principle

> **A living agent OS can accompany the owner through life while still knowing the difference between presence and surveillance, conversation and memory, noticing and authority, a project Foreman and a Chief of Staff, and an interface and a brain.**
