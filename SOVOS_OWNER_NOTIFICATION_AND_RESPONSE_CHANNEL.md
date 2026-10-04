# SOVOS Owner Notification & Response Channel Doctrine

**Status:** CURRENT architecture direction; transport implementation remains partial  
**Effective:** 2026-10-04  
**Architecture authority:** `OWNER_AUTHORITY_CONSTITUTION.md`  
**Attention semantics:** `CROSS_PRODUCT_SEAM_CONTRACT.md`  
**Freedom / momentum model:** `SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md`  
**Runtime / channels owner:** Wirebot / OpenClaw

## 1. Purpose

The Sovereign Operating System needs a dependable way for the Chief of Staff to reach the owner **outside the Wirebot App** without creating another source of truth or another inbox.

The channel must help the owner feel real momentum by delivering concise, source-backed signals such as:

- a genuine `Needs You` boundary;
- a Follow-Up becoming due;
- a Follow-Through thread progressing, stalling or closing;
- a verified business/life outcome;
- a material momentum/leverage gain;
- a routine failure/recovery that matters to the owner;
- a compact scheduled digest.

The transport is not the outcome.

~~~text
source-owned state / Evidence / outcome
→ operator.attention.v1 or source-linked follow-up/follow-through projection
→ Chief of Staff attention policy
→ delivery channel adapter
→ owner device
~~~

The same state remains available inside Wirebot App. A push notification is an additional surface, not a second canonical attention store.

---

## 2. Follow-Up and Follow-Through are different

SOVOS MUST preserve the distinction.

### Follow-Up — keep momentum alive

Follow-Up exists after an initial contact, message, action or handoff.

Its job is:

> **Make sure the next useful touch/action happens and the thread does not go cold.**

Examples:

- prospecting email → check/respond/re-contact;
- proposal sent → ask for decision at the right time;
- friend invited → reconcile availability;
- creditor validation letter sent → check response window;
- customer question answered → check whether the next handoff happened.

Follow-Up may repeat under policy.

It is not proof that the original objective was achieved.

Canonical family:

~~~text
follow_up
routine-template://cross-domain/follow-up
~~~

### Follow-Through — carry the objective to successful result

Follow-Through owns the larger thread:

> **Stay with the desired outcome until it is actually achieved, verified and translated into the expected momentum/leverage—or honestly escalated/abandoned/superseded.**

It may invoke Follow-Up many times.

Examples:

~~~text
prospect identified
→ follow up
→ conversation
→ proposal
→ follow up
→ agreement
→ invoice
→ settled cash
→ customer value
→ retained / expanded relationship
→ economic leverage

credit issue discovered
→ validation
→ follow up
→ correction / negotiation
→ settlement
→ reporting reconciliation
→ monthly cash flow returned
→ financial breathing room

social plan initiated
→ invitation
→ follow up
→ availability
→ reservation/logistics
→ actual experience
→ owner feedback
→ relationship/life-enrichment outcome
~~~

Canonical family:

~~~text
follow_through
routine-template://cross-domain/follow-through
~~~

A Follow-Up can complete successfully while Follow-Through remains open.

---

## 2A. Channel priority — SMS first

For owner-facing interruption and conversational continuity, **SMS is the preferred first-class channel when the deployment can provide it safely and lawfully**.

Default owner-channel hierarchy:

~~~text
PRIMARY
  true two-way SMS

SECONDARY / RICH PUSH
  ntfy / branded push

IN-APP
  Wirebot App exact object + full evidence/context

OPTIONAL ADDITIONAL
  iMessage / WhatsApp / Signal / Telegram / email
~~~

This is a delivery preference, not a rule that every routine sends SMS. Perpetua and the attention policy still decide whether interruption is useful.

### SMS paths that avoid 10DLC specifically

1. **Direct-SIM Android / Agent Computer SMS**
   - phone-capable Android node with a real SIM/eSIM;
   - OpenClaw can expose `sms.send` and `sms.search` when device permissions and Gateway policy both allow them;
   - best fit: Sovereign/private owner channel and low-volume two-way owner conversation;
   - no 10DLC registration because this is not a cloud 10-digit A2P long-code route;
   - carrier terms, anti-spam controls and practical throughput limits still apply.

2. **Apple Messages / carrier-SMS relay**
   - OpenClaw's iMessage path can explicitly address `sms:+1555...`;
   - best fit: a dedicated Mac/iPhone/SIM relay;
   - basic send/receive does not require advanced private-API mode.

3. **Verified Toll-Free SMS**
   - US/Canada toll-free messaging is outside A2P 10DLC;
   - toll-free verification is still required;
   - supports two-way SMS plus provider webhooks/delivery state;
   - best fit: scalable hosted Wirebot;
   - OpenClaw's official SMS plugin can use an SMS-capable Twilio toll-free number.

4. **Dedicated Short Code**
   - outside 10DLC and designed for high-throughput two-way A2P SMS;
   - use only when volume justifies the substantially higher monthly/onboarding cost.

Avoiding 10DLC does not remove consent, anti-spam, carrier or provider requirements. SOVOS should choose a sanctioned route rather than disguising business traffic as consumer messaging.

Recommended product posture:

~~~text
Sovereign / private owner
  dedicated Android SIM relay preferred
  Apple relay optional
  ntfy rich-push fallback

Hosted / scalable Wirebot
  verified toll-free SMS preferred
  ntfy rich-push fallback

High-volume platform
  toll-free or short code according to throughput and brand model
~~~

For white-label deployments, the SMS sender identity should match the actual commercial/brand posture. A client-branded sender should use its own appropriate sender/verification arrangement rather than silently reusing another brand's identity.

---

## 3. ntfy channel role

[ntfy](https://ntfy.sh/) is a strong optional owner-notification transport for SOVOS because it supports:

- HTTP PUT/POST publishing;
- Android, iOS and web clients;
- topic subscription;
- message priority/tags;
- click/deep-link destinations;
- up to three notification action buttons;
- HTTP action buttons;
- CLI/API subscription streams;
- Android/web publishing back into topics;
- sequence IDs for updating/clearing/deleting an existing notification;
- self-hosting with users, ACLs and access tokens.

SOVOS treats ntfy as a **channel adapter under Wirebot/OpenClaw**, not as:

- an authority;
- a task system;
- a scheduler;
- an Evidence store;
- an outcome ledger;
- a replacement for Wirebot App;
- a replacement for `operator.attention.v1`.

A deployment may choose another transport with equivalent semantics.

### 3A. ntfy downside analysis

ntfy is useful because it is simple, open and self-hostable, but SOVOS MUST preserve these downsides:

| Downside | Architectural consequence |
|---|---|
| **Not SMS** | Owner must install/use ntfy app/PWA or a branded client |
| **Lower reach than SMS** | Enrollment, notification permission and client health become prerequisites |
| **No portable inline free-text notification reply** | Free text usually requires opening ntfy/Wirebot; one-tap actions fit bounded choices better |
| **Self-hosted iOS instant push has an upstream dependency by default** | Official iOS client normally needs an APNs/FCM-capable upstream such as ntfy.sh unless Wirebot builds its own push stack |
| **Self-hosted Android can require a persistent connection** | Avoiding Firebase can increase background/battery/operability burden |
| **Browser/PWA behavior varies** | Background delivery/actions depend on browser/platform and long-unused web push can pause |
| **Topic/ACL setup is a security footgun** | Never use guessable public topics for Sovereign control; require auth/default-deny ACLs |
| **Messages are cached, not a durable ledger** | ntfy must never own Evidence, conversation truth or Follow-Through state |
| **No built-in E2E guarantee for message content** | Use TLS, self-hosting, redacted payloads and deep links for sensitive detail |
| **Hosted ntfy is best-effort** | Critical routine continuity cannot depend on ntfy delivery |
| **Full white-label mobile UX is not turnkey** | Native rebranding means maintaining client forks, signing and push credentials |
| **Payload/push size limits** | Keep owner alerts concise; use Wirebot for detail |

### 3B. White-label posture

**Yes, ntfy can be made effectively white-label.**

1. **Invisible backend — recommended**
   - self-host ntfy;
   - disable its web UI if desired;
   - expose no ntfy branding to the owner;
   - keep Wirebot App and SMS as the branded owner experience.

2. **Branded endpoint / web surface**
   - serve on a Wirebot/client domain;
   - fork/rebrand the open-source web app if exposed;
   - preserve required open-source notices;
   - do not use ntfy trademarks/logo as if owned by Wirebot.

3. **Fully branded native client**
   - Android source is open under Apache 2.0;
   - iOS source is open under MIT;
   - use Wirebot/client app IDs, icons, signing and push credentials;
   - maintain the fork as ntfy evolves.

For Wirebot, the default SHOULD be **invisible ntfy backend + branded Wirebot App + SMS primary**.

### 3C. Mandatory downside-review law

Before adopting any owner channel, record:

~~~text
reach / install friction
two-way reply quality
latency / delivery guarantees
carrier / provider compliance
privacy / lock-screen exposure
identity / white-label behavior
platform dependencies
self-host burden
cost / scaling
failure / outage mode
replay / duplication
revocation
accessibility
fallback path
~~~

No channel is promoted merely because its happy-path API is easy.

---

## 4. Chief-of-Staff notification loop

~~~text
important source state / routine event / verified outcome
        ↓
Wirebot / Perpetua relevance + attention policy
        ↓
Should the owner be interrupted?
        ├─ no → remain quiet / digest later
        └─ yes
             ↓
source-linked notification projection
correlation · source ref · expiry · action class
             ↓
OpenClaw Owner Channel Router
             ↓
primary SMS when available
        + ntfy / Wirebot App / approved fallbacks
             ↓
owner device
             ↓
optional response/action
             ↓
authenticated Wirebot ingress
             ↓
typed owner response / intent
             ↓
revalidate source + authority
             ↓
Chief of Staff continues the same thread
~~~

No owner prompt is required for notifications already allowed by attention policy.

No notification itself grants permission to perform a consequential action.

---

## 5. Notification classes

Every notification SHOULD declare its semantic class rather than treating all pushes alike.

| Class | Owner meaning | Default posture |
|---|---|---|
| **needs_you** | real human judgment/authority boundary | interrupt according to urgency |
| **follow_up_due** | momentum-preserving action/check is due | notify only if owner must act or policy wants visibility |
| **follow_through_progress** | important thread materially advanced | quiet update / sequence update |
| **follow_through_stalled** | expected progress failed to appear | surface when intervention/strategy change is useful |
| **verified_outcome** | real accepted result happened | positive momentum update |
| **momentum_leverage** | verified result created meaningful downstream capacity/cash/time/opportunity | momentum update / digest |
| **failure_recovery** | routine failed/recovered materially | exception-oriented |
| **digest** | bounded summary of useful changes | scheduled/quiet |

Raw tool calls, agent chatter, polling, routine heartbeats and trivial micro-events SHOULD NOT become owner notifications.

---

## 6. Psychological momentum without engagement theater

The owner should be able to **feel the system working** because notifications reveal real movement.

Good examples:

- “$4,200 in receivables settled today. Cash is verified.”
- “12 qualified prospects entered the CRM; 3 conversations are now active.”
- “The collector confirmed the settlement. Credit-report reconciliation is still open.”
- “The dinner is confirmed for Saturday; logistics are complete.”
- “This routine bought back 2.3 owner hours this week.”
- “No action needed: payment recovery completed automatically.”

Do not send:

- “Agent completed 17 tasks.”
- “You have a 14-day streak.”
- “Five tools ran successfully.”
- repeated low-value reminders merely to create product engagement.

Psychological momentum must be grounded in real outcome/margin/leverage, not notification volume.

---

## 7. Sequence identity and evolving notifications

Where the channel supports it, one meaningful thread SHOULD retain one stable correlation/sequence identity.

For ntfy, `sequence_id` can update an existing notification.

Conceptual mapping:

~~~text
operator.correlation.v1 / follow-through ref
            ↓
ntfy sequence_id
~~~

Example evolution on the owner's phone:

~~~text
FT-8K2
Waiting on proposal response

→ updated same notification →

FT-8K2
Reply received — meeting requested

→ updated →

FT-8K2
Agreement signed — invoice pending

→ updated →

FT-8K2
$8,000 settled — outcome verified
~~~

The ntfy sequence ID is a transport correlation aid. It does not become the canonical Follow-Through ID.

Clearing/deleting the notification does not resolve the source thread.

---

## 8. Action buttons

ntfy supports `view`, `http`, `broadcast` (Android) and `copy` actions.

Recommended SOVOS usage:

### View

Default safe action:

~~~text
Open in Wirebot
→ exact owner/workspace/follow-through detail
~~~

### HTTP actions

Use only for explicitly bounded operations such as:

- defer 1 day;
- snooze;
- acknowledge receipt;
- choose one pre-approved low-consequence option.

An HTTP action MUST use an exact short-lived single-purpose action reference or signed capability.

Never place reusable credentials, broad API tokens or ambient authority in notification action URLs/headers.

High-consequence actions SHOULD deep-link to Wirebot for current source/authority revalidation.

### Broadcast

Android-only automation may be useful in private deployments but is not a portable SOVOS requirement.

---

## 9. Two-way communication

Two-way owner communication is a first-class goal.

### 9.1 What ntfy can do natively

The ntfy Android app and web app can publish messages into a topic. Therefore the owner can respond through ntfy itself.

This is **two-way ntfy/pub-sub**, not carrier SMS.

### 9.2 Recommended duplex topology

For production Owner/Chief-of-Staff communication, prefer a private/self-hosted instance with authenticated identities and ACLs.

Conceptual topics:

~~~text
owner_out
  Wirebot/Chief of Staff → publish
  owner device          → read

owner_in
  owner device          → publish
  Wirebot ingress       → read

optional reply_<correlation>
  transient/thread-specific owner response route
~~~

A thread-specific reply topic gives the cleanest free-text correlation.

A notification may include a `view` action that opens the appropriate ntfy reply topic or the exact Wirebot response composer.

### 9.3 Inbound response path

~~~text
owner publishes response
→ ntfy authenticated topic
→ Wirebot subscriber / ingress adapter
→ validate server/topic/principal/scope
→ attach correlation/source refs
→ sanitize and preserve raw owner text as attributed input
→ deliver into the owner's persistent OpenClaw/Wirebot relationship
→ interpret as owner response / typed intent
→ revalidate consequential authority separately
→ act / ask / update thread
~~~

An incoming ntfy message is **not automatically a tool command**.

Transport access never becomes work authority.

### 9.4 Inline notification reply limitation

Do not claim a free-text OS-notification inline-reply capability unless it is independently implemented and proven.

As of the 2026-10-04 architecture review, ntfy documents action buttons and publishing from the Android/web app, but not a portable free-text inline reply action type.

The preferred first implementation is therefore:

- action buttons for bounded one-tap responses;
- tap-to-open exact ntfy/Wirebot response context for free text.

---

## 10. SMS is separate

ntfy push notifications may look and feel like text-message alerts, but **ntfy is not carrier SMS**.

If true SMS send/reply is required, add a separately owned SMS adapter under the same channel contract:

~~~text
operator attention / response
→ Wirebot/OpenClaw channel abstraction
   ├─ ntfy
   ├─ Telegram / WhatsApp / Signal / etc.
   └─ SMS provider / approved Android bridge
~~~

The same correlation, owner identity, response parsing and authority laws apply.

Do not make the SOVOS routine depend on one transport.

---

## 11. Routine embedding

Every compiled routine may already bind an `attention_policy_ref`.

The portable machine contract for that reference is `contracts/operator-attention-policy.v1.schema.json` / `operator.attention_policy.v1`.

Use that seam to specify:

~~~text
when_to_notify
  needs_you
  verified_outcome
  material_momentum
  stalled
  failed
  recovered
  digest

channel_refs
  ntfy owner channel
  Wirebot App
  other approved channels

quiet_hours
priority policy
dedupe / coalesce
correlation / sequence behavior
reply_allowed
reply_consequence_ceiling
expiry
fallback channel
~~~

The routine template remains transport-neutral.

The owner-specific Blueprint/Instance binds the actual channel policy.

---

## 12. Follow-Up / Follow-Through notification examples

### Prospecting

~~~text
Follow-Up:
  “No reply after 4 business days. Next touch prepared.”
  usually quiet unless owner-sensitive

Follow-Through:
  “Proposal accepted. $8,000 invoice created.”
  progress update

Follow-Through:
  “$8,000 settled and delivery kickoff accepted.”
  verified outcome + momentum notification
~~~

### Financial recovery

~~~text
Follow-Up:
  “Collector response window elapsed; reconciliation due.”

Follow-Through:
  “Settlement accepted.”
  remains open

Follow-Through:
  “Settlement paid, creditor receipt verified, report correction pending.”
  remains open

Follow-Through:
  “Reporting reconciled; $410/month obligation removed.”
  verified financial-margin outcome
~~~

### Relationship / life

~~~text
Follow-Up:
  “Marcus has not replied to Saturday invitation; one gentle follow-up is due.”

Follow-Through:
  “Saturday dinner is confirmed and reservation complete.”

Follow-Through:
  “Outcome recorded; owner said the evening was valuable.”
  relationship/life-enrichment closure
~~~

---

## 13. Security posture

For a Sovereign deployment:

1. prefer self-hosted ntfy on private/controlled infrastructure where practical;
2. configure authentication and default-deny ACLs;
3. separate publisher/subscriber roles where possible;
4. use TLS;
5. treat topics as sensitive routing identifiers;
6. never embed reusable Wirebot/OpenClaw/Focusa secrets in notifications;
7. minimize private payload in lock-screen-visible text;
8. use exact deep links for sensitive detail;
9. treat attachments and inbound text as untrusted content;
10. rate-limit and dedupe responses;
11. preserve response attribution and correlation;
12. revalidate owner/session/authority for consequential action.

A public `ntfy.sh` topic may be acceptable for bounded prototypes only when its privacy/access posture is explicitly accepted. It is not the preferred Sovereign control plane.

---

## 14. Acceptance

The ntfy owner-channel integration is not complete until it proves:

- source item → correct notification class;
- attention policy suppresses low-value noise;
- quiet hours work;
- one Follow-Through uses one stable sequence identity;
- update/clear does not change canonical source resolution;
- owner opens exact Wirebot context;
- bounded action button returns an attributable response;
- free-text owner response returns through authenticated ingress;
- response enters the correct persistent Chief-of-Staff relationship thread;
- wrong owner/topic/correlation is rejected;
- duplicate inbound messages do not duplicate effects;
- stale/expired action links fail safely;
- consequential reply requires current authority;
- verified outcome produces a truthful momentum notification;
- notification outage does not stop the underlying routine;
- alternative channel/fallback remains possible.

The end state is:

> **The Chief of Staff can quietly keep the owner informed, ask only when human input matters, receive the owner's response from the same mobile communication surface, and continue the exact SOVOS thread without losing context or sovereignty.**
