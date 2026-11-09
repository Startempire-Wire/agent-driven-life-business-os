# Owner engineering stack & open-ended extensibility — context profile

**Date:** November 8, 2026  
**Status:** Owner-stated engineering preferences and source-verified repo examples. **Not** a constitutional architecture amendment, a mandatory universal programming language, a current server inventory, or authorization to change live systems. Read with `AGENTS.md`, `CROSS_PRODUCT_SEAM_CONTRACT.md` and the owner's authority rules.

## Explicit owner priorities

- **Inspect actual GitHub repositories and deployed APIs before choosing implementation language, technology or external service.** No backend decision merely because Svelte/OpenClaw uses TypeScript.
- **Architecture has no fixed domain cardinality for agents, APIs, providers, projects, models, books, workers, tools, workstreams or future capabilities.** Owner mentions of "ten" or "one hundred" are illustrative—not counts, caps, roster size, or compulsory platform assumptions.
- **Support open-ended extensibility through typed ports, plug-in/provider capabilities, dynamic service discovery, schema/version negotiation, runtime admission, replaceable models and backends, and hierarchical independently governed agent workforces.**
- **Resource capacity is finite and must be enforced by observed policy/backpressure at runtime** (memory, CPU, network, provider quotas, cost, permission, tenant and human authority); no arbitrary fixed maxima in domain schemas. Must also run under severely constrained resources while expanding as infrastructure permits.
- **Object-oriented discipline / DRY / portability:** use language-idiomatic encapsulation, composition/DI, explicit authority and single owned truth, CLI/API parity, source-based reproducibility, human-friendly surfaces, versioned evidence/receipts. A domain module must be reusable in independent projects without copy/paste and without becoming a monolithic control plane.
- **Preferred existing ecosystem:** Focusa cognitive/epistemic authority and durable work continuity, Wirebot/OpenClaw orchestration, UIAI Engine browser/computer on servers, SOVOS constitutional architecture/Master Loop/Workforce. Never duplicate their truth in a new publishing module.
- **Mixed-language architecture is deliberate and open-ended:** choose based on actual implemented module contracts rather than universal stack restrictions.

## Evidence-backed technologies — examples, not a closed registry

| System | Verified GitHub evidence | Practical pattern |
|---|---|---|
| Focusa | `Startempire-Wire/focusa/Cargo.toml` includes `focusa-core`, `focusa-api`, `focusa-cli` and Rust/Tokio/Axum/Serde/Clap stack | Existing Rust core, typed API, CLI and cognition |
| SignalOS | `Startempire-Wire/signalos/Cargo.toml` with Rust server, schema, SDK, CLI crates | Rust modular engine and contract generation |
| Flow Mesh | `Startempire-Wire/flow-mesh/go.mod`, Go implementation with SQLite, APIs and CLI | Existing Go services retained on their established contracts |
| Wirebot App | `Startempire-Wire/Wirebot-App/package.json` Svelte/Vite/TS | JS/TS for UI and thin clients, not mandatory backend |
| Startempire Wire Network | `Startempire-Wire/Startempire-Wire-Network/package.json` SvelteKit, lucide-svelte | Svelte web/UI surfaces |
| UIAI Engine | Owner direct statement + ecosystem records describe Go-based browser/action engine on servers | Canonical agent browser, not an ad hoc independent Chrome automation tool |
| Wirebot/OpenClaw | `Startempire-Wire/wirebot-core/AGENTS.md` and current plugin/CLI architecture | Governed operator, agent runtime and tool layer |
| Other Go APIs | Owner describes many Go APIs on current servers | **Actual number, endpoint inventory, health and ownership not yet authenticated**. Never silently promote 10/100 to discovered facts. |

## Architecture decision logic (mandatory when a new system is proposed)

1. **Inventory before invention:** inspect repository tree, language, runtime version, existing modules, exact server/host, supported CLI/API/SDK, service ownership, live health. Record source SHA and observed timestamp.
2. **Reuse first:** does an existing service/primitive/contract already own the concern? If yes, integrate its adapter; don't clone its authority or build a redundant server.
3. **Choose the new implementation language contextually:** an existing Rust domain may favor Rust; an existing Go API should remain Go; a Svelte UI uses Svelte/TS. Language is not a global rule or a proxy for OOP/DRY quality.
4. **Versioned open extension points:** typed inputs/outputs, plugin/provider descriptors, dynamic registration, capability discovery, constrained invocation, no closed max list or title-/provider-specific switches in core.
5. **Runtime resource adaptation:** configurable scaling, backpressure and quotas, evidence-based concurrency/resource limits; no claim of literal infinite physical capacity.
6. **Prove portability:** two independent workloads/projects, two adapters, fresh install/restore, provider swap, cross-tenant separation, no duplication and real source-qualified receipts.
7. **Bound agent change authority:** Focusa/Workstream/Foreman and owner-granted permissions govern identities, workpoints and roles. Dynamic agents can multiply without creating independent architecture authority.

## Example correction: SovPress

For genuinely new publisher core services, Rust is **an evidence-backed initial candidate/default** because the owner already uses mature Rust CLI/API projects; the engineering requirement is not "Rust at all costs." A real existing Go service may already implement the necessary provider feature, in which case wrap its verified typed API rather than rewrite it. The Svelte player/OpenClaw plugin consumes a thin SDK; there is no reason for TypeScript UI dependencies to dictate the core engine.

The ten original SovPress agent work packages are **initial role templates**, not ten fixed agent identities, a cap, or an implementation topology. See the book repo's `incubation/sovpress/ADR-006-OPEN-ENDED-CAPABILITIES-DYNAMIC-WORKFORCE-2026-11-08.md` and its capability/workforce dispatch schema. No live services are changed here.

**This profile is a durable repository-context reference for future builder agents.** It is not a claim of editing ChatGPT's separate account Memory summary, and it does not enumerate every future API.
