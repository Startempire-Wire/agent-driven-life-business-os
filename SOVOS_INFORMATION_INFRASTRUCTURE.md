# SOVOS Information Infrastructure Doctrine

**Status:** LIVE PORTABLE DOCTRINE  
**Effective:** 2026-10-03  
**Architecture authority:** OWNER_AUTHORITY_CONSTITUTION.md  
**Current ecosystem architecture:** CURRENT_ECOSYSTEM_ARCHITECTURE.md  
**Cross-product seam contract:** CROSS_PRODUCT_SEAM_CONTRACT.md

## 1. Core clarification

**SOVOS is not merely an architecture for connecting several software products.**

It is a **sovereign operating doctrine expressed through an information infrastructure and then embodied by software architecture**.

The software topology is visible:

~~~text
Wirebot
Focusa
Focusa Workforce
UIAI Engine
Veragensia
Pi / workers
OpenClaw
W.I.N.S.
MeriFolio
Startempire Wire
~~~

But the deeper SOVOS layer is the set of portable laws that allow those independent systems to exchange meaning without collapsing identity, authority, provenance or truth.

The intended stack is:

~~~text
WORLDVIEW / DOCTRINE
why technology should exist and whom it serves
        ↓
INFORMATION CONSTITUTION
what identity, truth, authority, evidence and provenance mean
        ↓
SOVEREIGN INFORMATION INFRASTRUCTURE
typed references · semantics · relationships · freshness · scope · trust
        ↓
OPERATIONAL ARCHITECTURE
which concern belongs to which canonical owner
        ↓
SOFTWARE IMPLEMENTATIONS
Wirebot · Focusa · UIAI · Veragensia · others
        ↓
SURFACES / EXPERIENCES
apps · browsers · voice · APIs · agents · computers
~~~

A product diagram without the information layer is an incomplete description of SOVOS.

---

## 2. Information is not just data

SOVOS distinguishes **data** from **information that can safely participate in operation**.

A value is not operationally meaningful merely because it exists.

Useful SOVOS information carries enough context to answer questions such as:

- What is this?
- Who or what owns its canonical truth?
- Which principal does it concern?
- Where did it come from?
- What revision or observation does it represent?
- How fresh is it?
- What is verified, inferred, disputed or unknown?
- What relationships does it have to other objects?
- What authority, if any, accompanies it?
- What operations are valid?
- What happened as a result?
- What evidence supports the result?

Therefore:

~~~text
raw data
!= typed information
!= authority
!= Evidence
!= verified truth
!= accepted outcome
~~~

The information infrastructure exists to preserve those distinctions.

---

## 3. Foundational information laws

### 3.1 One concern, one canonical owner

A piece of state has an owning domain.

Many systems may reference or project it. Projection does not transfer ownership.

> **One concern, one canonical owner. Many surfaces may project it.**

This prevents convenient copies from silently becoming competing truths.

### 3.2 A reference is not the thing

Cross-product references identify source-owned state.

They do not duplicate that state and do not confer authority over it.

This is the foundation of SOVOS interoperability.

### 3.3 Information carries provenance

Consequential information should preserve where it came from and how it became trustworthy enough for its current use.

Relevant provenance may include:

- source domain;
- producer;
- source revision;
- observation or issue time;
- Evidence refs;
- verification refs;
- owner/tenant/environment scope;
- causal/correlation refs;
- promotion/approval refs.

### 3.4 Meaning has type

Important concepts remain semantically identifiable.

Examples include:

~~~text
Owner
Delegation
Operating Partner
Business / Domain
Project
Workstream
Foreman
Workpoint / Work
Routine
Role
Assignment
Attention / Needs You
Execution
Evidence
Receipt
Outcome
Credential-use request
Capability posture
Body / Runtime
Federation grant
~~~

A UI or model may summarize or compose them. It may not erase the distinction among them.

### 3.5 Authority is independent information

Possessing information does not imply permission to act on it.

Keep distinct:

~~~text
known
supported
entitled
connected
available
authorized
consented
~~~

Authority must be resolved through its owning contract.

### 3.6 Freshness is part of meaning

A true observation from yesterday may be unsafe authority today.

Information participating in consequential operation therefore needs explicit revision/freshness/expiry semantics.

### 3.7 Uncertainty remains visible

SOVOS should preserve distinctions such as:

~~~text
known
observed
inferred
proposed
verified
disputed
stale
unknown
unavailable
incompatible
~~~

Intelligence is weakened when uncertainty is silently flattened into confidence.

### 3.8 Evidence closes the loop

Operational information should be capable of connecting:

~~~text
intent
→ assignment
→ execution
→ Evidence
→ verification / receipt
→ accepted outcome
→ feedback / learning
~~~

The causal chain should remain inspectable without creating one universal database.

---

## 4. Distributed information infrastructure, not centralization

SOVOS does **not** require:

- one giant database;
- one universal event bus;
- one global object registry;
- one omniscient knowledge graph;
- one master ontology containing every private domain;
- one vendor-controlled identity provider;
- one application that owns all state.

Instead:

~~~text
canonical state stays with its owner
        +
portable references preserve identity
        +
contracts preserve semantics
        +
provenance preserves origin
        +
correlation preserves causal connection
        +
authority is revalidated at consequence
        =
coherent distributed operation
~~~

This is **coherence without erasure** applied to information itself.

---

## 5. Ontology and semantic infrastructure

SOVOS requires semantic discipline but does not mandate one global internal ontology implementation.

A SOVOS-compatible system should be able to represent, directly or through adapters:

- object identity;
- object type;
- typed relationships;
- valid actions / affordances;
- provenance;
- verification state;
- freshness;
- scope;
- authority-relevant references;
- evidence and outcome relationships.

### 5.1 Focusa as a strong reference implementation

Focusa already implements a deep ontology direction for its governed software/work world.

Its documented ontology intent includes:

- what exists;
- how things relate;
- what actions are valid;
- what currently matters;
- what has been verified;
- what remains uncertain;
- object identity and type rules;
- typed relations and actions;
- provenance;
- verification state;
- status and freshness.

That is highly aligned with SOVOS information-infrastructure principles.

However:

> **Focusa's ontology is not automatically the universal ontology of SOVOS.**

Focusa owns governed-work/software-world semantics in its domain.

SOVOS owns the portable law that independently owned semantic domains can interoperate without pretending one product owns every meaning.

---

## 6. The SOVOS information fabric

The term **information fabric** describes the relationships created by the portable infrastructure.

Current and emerging SOVOS contract families already form part of that fabric:

~~~text
owner / principal identity
human delegation
partner profile
surface handoff
attention
correlation
capability posture
closure
credential-use reference
routine template
routine blueprint
routine instance
leverage snapshot
federation grants / projections
~~~

These contracts do not constitute a new operational service.

Together they establish a portable grammar for joining independently owned information.

The fabric should let an authorized participant trace questions such as:

> Which owner does this concern?

> Which business or life domain?

> Who requested the work?

> Which delegation or authority applied?

> Which Workstream and worker executed it?

> Which computer/body/runtime performed the action?

> What Evidence was produced?

> What was verified?

> What outcome was accepted?

> What changed afterward?

---

## 7. Information infrastructure precedes product composition

The old ADLBOS framing could be read primarily as:

~~~text
several products
→ connected correctly
→ life/business operating system
~~~

SOVOS makes the deeper order explicit:

~~~text
foundational beliefs
→ information laws
→ semantic / authority / evidence infrastructure
→ product ownership boundaries
→ interoperable software
→ sovereign operation
~~~

This is why another innovator does not need to copy the Startempire software stack to learn from or implement SOVOS.

A different implementation could use different:

- models;
- agents;
- runtimes;
- databases;
- operating systems;
- browsers;
- work systems;
- user interfaces.

It can still embody SOVOS if it preserves the underlying sovereign information laws and human-agency doctrine.

---

## 8. Truth and information

SOVOS inherits the Philoveracity principle:

> **Truth precedes invention.**

An information system does not create truth by storing a value.

It creates an **expression or claim about reality** that must preserve enough context to be interpreted responsibly.

That leads to a SOVOS epistemic chain:

~~~text
reality
→ observation
→ source-bearing information
→ typed relation / claim
→ evidence
→ verification
→ accepted domain truth or outcome
→ bounded learning / revision
~~~

This creates a technological expression of:

> **Discover truth. Give it form.**

Information infrastructure is the bridge between discovery and operational form.

---

## 9. Sovereignty is informational before it is computational

Human sovereignty cannot be preserved merely by placing an "Approve" button in a UI.

The system must know:

- who the human principal is;
- what belongs to that principal;
- which authority was delegated;
- to whom;
- for what purpose;
- for what resources;
- under what limits;
- when it expires;
- how it is revoked;
- what happened under that grant;
- whether the resulting outcome was accepted.

Therefore, sovereignty depends on **information structures capable of carrying identity, meaning, scope and authority through computation**.

Without that infrastructure, "human in control" becomes a slogan rather than an enforceable architecture.

---

## 10. Information infrastructure and One Song

The One Song metaphor applies directly.

Harmony requires more than instruments existing near each other.

They require:

- identity;
- relationship;
- timing;
- role;
- constraint;
- shared structure;
- intelligible signals.

Likewise, multiple software systems do not become one operating system merely because APIs connect them.

They become coherent when information can travel among them without losing:

- meaning;
- source;
- identity;
- authority;
- provenance;
- evidence;
- context.

This is the informational form of:

> **Many instruments. One Song.**

---

## 10A. Information infrastructure makes Driverless Business possible

A Driverless Business depends on more than task automation.

The system must preserve a durable, correctable representation of:

- owner purpose and desired outcomes;
- business/domain identity;
- routines and triggers;
- decision classes and thresholds;
- accepted preferences and operating patterns;
- provenance of learned behavior;
- delegated authority;
- exception boundaries;
- evidence and accepted outcomes.

The most important distinction is:

~~~text
learned owner pattern
!= authority
~~~

A capable agent may infer how the owner is likely to decide. That can improve recommendations and routine operation. But durable learning must remain source-aware and correctable, and consequential authority must remain separately delegated.

This prevents hyper-personalization from becoming invisible power transfer.

See `SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md`.

---

## 11. Design test for future SOVOS innovations

When adding a product, protocol, ontology, data source, agent, device or integration, ask:

1. What canonical information does it own?
2. What does it merely project or reference?
3. What semantic objects does it introduce?
4. How are identity and scope represented?
5. How is provenance preserved?
6. How is freshness represented?
7. How is uncertainty represented?
8. What authority is required for consequential action?
9. How is authority revoked or expired?
10. What Evidence and receipts are produced?
11. How are outcomes connected back to source truth?
12. Can another implementation interoperate without adopting the same internal database?
13. Does the design increase human capability while preserving human sovereignty?

If these questions cannot be answered, the architecture is not yet SOVOS-complete.

---

## 12. Non-regression

This doctrine does not create a new canonical database, universal ontology owner, or information-service product.

Preserve:

~~~text
SOVOS
  portable information + architecture doctrine

product/domain owners
  canonical state and behavior

Focusa
  governed-work semantics and ontology in its domain

Wirebot
  operating-partner / portfolio synthesis in its domain

UIAI Engine
  execution truth in its domain

Veragensia
  body/runtime/placement truth in its domain

source life/business systems
  domain truth in their domains
~~~

The purpose of SOVOS information infrastructure is **interoperable truth with sovereign boundaries**, not centralized ownership.

---

## 13. Compact definition

> **SOVOS is a sovereign operations doctrine built on an information infrastructure that preserves identity, meaning, provenance, authority, evidence and relationships across independently owned systems, allowing many software instruments to operate coherently without erasing their boundaries or displacing the human source of intent.**
