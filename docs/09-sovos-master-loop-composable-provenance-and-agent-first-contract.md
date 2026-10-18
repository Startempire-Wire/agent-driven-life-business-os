# SOVOS Master Loop — Composable, Transparent and Agent-First Components

**Status:** SPECIFIED owner requirement; implementation coverage is partial and
must be verified per owning component and consumer. This is not a new release.

## Owner clarification and applicability

The Master Loop is one coordinating loop containing multiple interacting and
nested loops. Together they create progress in an owner's life and businesses;
they are not one giant workflow, chatbot, scheduler or indistinguishable process.
This owner-requested clarification applies across the designs in02–08 and every
component's implementation, task and acceptance. It does not delete the existing
requirement coverage, expand execution permission or grant architecture authority
to a runtime system. Existing owner-rooted authority and source ownership remain.

## Composition without a blob

Distinguish owner outcomes, loop definitions, loop instances, nested loops,
component definitions, invocations, actions, effects, verification, follow-through
and accepted outcomes. Components have stable identities, readable names, purpose,
responsibility boundaries, owner, version and lifecycle. A reusable definition is
not an active instance; a compatible connection is not permission to execute.

Each component exposes typed inputs, outputs and errors; explicit dependencies,
preconditions, consequences, scope, permissions, budget, retry/idempotency,
unknown-result recovery, cancellation and compensation where applicable.
Composition must preserve source identity, authority, tenancy and evidence across
nesting, concurrency and delegation. Several loops may consume one originating
event without each claiming an independent accomplishment or duplicating effects.

## Feedback and reconstructable records

At every meaningful handoff compare expected and observed results. Record why
work began, source/input revisions and coverage, who initiated it, who performed
it, which permission/resource was used, what was attempted, what was acknowledged,
what independently changed, what remains unresolved, and why it was closed or
escalated. Separate initiator, performer and verifier even when one actor fills
several roles. A component's own success report is not independent verification.

Proposed, authorized, attempted, acknowledged, uncertain, verified and accepted
are different states. A sent message is not a resolved business outcome. Unknown
coverage is not absence; a failed read is not an empty history; an interrupted
action is not automatically safe to repeat.

Relationships have explicit meanings: triggered, delegated, supplied evidence,
blocked, changed, verified, superseded and compensated. Observed causal edges
reference their supporting evidence. Inference is labeled; temporal adjacency or
state-revision lineage cannot be presented as proven external causation.

Existing owners retain facts, execution, permissions, memory and outcomes. Their
records are linked and projected rather than copied into a competing universal
store. Evidence accompanying owned state changes is transactional. Corrections
append supersession; history is not silently rewritten or fabricated afterward.
Credentials never enter visible records. Protected content references/digests,
redaction, retention, access control and erasure rules apply to derived views too.

## Agent-first, human-friendly

Agents are the primary software users. At every hierarchy level they must be
able to discover purpose, components, versions, operations, scope, capabilities,
input/output schemas, effects, permissions, limits, failures, continuation,
evidence and safe recovery through machine-readable APIs and CLI. A model must
not need to scrape the GUI, guess IDs or infer supported behavior from prose.
Installed capability, registered metadata and granted authority are distinct.

The CLI consumes the same API and preserves versioned envelopes, explicit
unknowns, errors, references and pagination. GUI capabilities must not outrun
machine interfaces. Natural-language summaries are projections, not a second
source of truth. Human-friendly interfaces explain the system without becoming
its primary or exclusive control surface.

## Visible structure, origin and consequences

Provide a coherent operating map, interaction timeline and detailed trace from
the same owned records. Preserve the hierarchy while progressively disclosing
detail; make log locations prominent in the appropriate loop and component views.
Show readable identity/purpose, current work, origin, input/evidence, result,
blockers, next action, and local and cross-loop consequences. Text/icons carry
meaning; color only reinforces it. An overview may simplify presentation but may
not erase identities, hide uncertainty or invent completion.

Every component should answer:

> What am I? Why am I here? What am I doing? What triggered me? What did I
> actually change? What proves it? What happens next?

An owner must be able to trace a claimed accomplishment backward to its origin
and forward through its consequences without requiring an engineer to explain
an opaque graph or wall of logs. Missing producers, unavailable records and
historical gaps remain visible.

## Cross-component acceptance and delivery truth

A component is not complete until its producer and consumer demonstrate its
identity, composition contract, feedback, accomplishment evidence, failure and
recovery records, machine interfaces and appropriate visible trace. Qualification
includes replay, interruption, uncertain effects, correction, scope changes,
concurrent interactions and independent receiver verification. Held-out agents
must discover and use the software; humans must explain an actual trace.

Apply these conditions to existing tasks; do not replace the existing operating
model with a second registry, scheduler, permission store or workflow authority.
Track incomplete instrumentation explicitly rather than labelling a partial
activity panel as a complete audit system. A fixture is not live consumer proof,
a published source change is not deployment, and a diagram is not causal evidence.

## Reference implementation adapter

Wirebot maintains implementation-specific API, CLI, UI and existing-backlog
acceptance in [Core contract21](https://github.com/Startempire-Wire/wirebot-core/blob/reconcile/scoreboard-complete/docs/21-wirebot-master-loop-composability-provenance-and-agent-first-contract.md).
That adapter records its current coverage and gaps; its presence does not prove
that every portable component, runtime or consumer already implements this
contract. Portable deployments keep these semantics and replace local bindings.
