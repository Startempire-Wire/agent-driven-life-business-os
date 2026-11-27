# Golden Path default: one server for a Wirebot-style agent

Use this default when the customer's approved deployment already calls for **OpenClaw on one persistent server**. One server can run the OpenClaw Gateway and, where supported, the Focusa service or adapter for that deployment. Put the Operating Partner's working files on that same server. **Do not provision a second server, set up server-to-server SSH, or require access to the original Wirebot repository.** An owner-controlled Git remote is optional for versioning source; it is not the live workspace or the continuity store.

This is a deployment reference, not an installer or a change to what any Expression includes. Proto does not acquire an OpenClaw or VPS requirement. Managed tenants keep their approved isolated runtime. A complete full-Sovereign deployment still requires its dedicated owner VPS, owner-specific private mesh and owner-controlled local body; that local body is not a second server. Start the first useful task on the approved existing surface when possible; do not wait for a server the task does not need.

## Default configuration

Example Linux paths only. Run under the deployment's scoped service identity, not as root. Use an authenticated local endpoint (loopback or a private socket, as supported), or a supported private network route for isolated services/containers. Use the approved private route if Focusa is already provided as a managed service. Do not expose the Focusa endpoint publicly to make the pairing work. Preserve owner, tenant and per-project permissions whichever route is used.

Copy this binding matrix into the customer’s private handoff and fill it from the owning services:

| Scope | `project_root` (example) | `continuity_id` (example) | Initial working subpath | Who selects it |
|---|---|---|---|---|
| Operating Partner | `/srv/operating-partner/workspaces/operations` | `example-operations` | `.` (root) | Default OpenClaw agent |
| Product A, if needed | `/srv/operating-partner/workspaces/product-a` | `example-product-a` | `.` (root) | Explicit product selection; never the default agent workspace |

Replace the sample paths and continuity IDs with values issued or verified for this deployment. `project_root` and `continuity_id` identify the Focusa scope; the working subpath must fit within that root. A session ID is temporary, not the continuity key. Record each mapping privately and verify it in Focusa; the table, a Git checkout, a current directory, a healthy connection, or a `Ready` card is not an authority check. Separate folders help avoid mix-ups but are not access isolation by themselves. Enforce grants through the owning service and use filesystem/tenant permissions appropriate to the deployment. Keep credentials, service state and private backups outside working trees, using their owning storage and recovery mechanisms.

On a new install, seed customer-owned workspace files with the supported [OpenClaw workspace setup](https://docs.openclaw.ai/concepts/agent-workspace). Do not copy another operator’s persona, history, state or credentials. For a single OpenClaw agent without a workspace override, merge **only** this fragment into the customer's existing configuration. Do not replace its configuration or change its model, channels or credentials:

```json
{
  "agents": {
    "defaults": {
      "workspace": "/srv/operating-partner/workspaces/operations"
    }
  }
}
```

For an explicit multi-agent roster, use the installed version's [per-agent workspace setting](https://docs.openclaw.ai/concepts/agent-workspace) for the intended agent. Changing the default base path alone does not pin that agent's workspace. This OpenClaw setting selects files, not a Focusa binding or a grant. Configure the Focusa adapter through its supported settings for the same verified scope; do not copy a saved Workpoint ID from another project.

## Setup and verification

1. **Plan at Stage 1.** Resolve the customer's Expression and hosting profile. Record the expected roots, the partner identity and the separate product scopes that are actually needed. For an existing install, audit and reuse the compatible Gateway, workspace, partner identity and Focusa state. Back up through the owning products before a change; do not create a second active runtime or move state merely to match an example path.
2. **Bind at Stage 4.** Confirm the effective OpenClaw workspace for the intended agent. In Focusa, resolve project identity and use Workpoint Resume for the exact root, continuity and working subpath. Require agreement on the canonical scope with no fallback. For product work, switch explicitly to that product's verified scope and use a separately authorized execution context; do not point the Operating Partner's default at a parent that contains all projects.
3. **Prove a durable result.** In an owner-approved test scope, make a harmless trajectory update through Focusa's scoped mutation interface. Require a success receipt for the exact scope and read back the update through Focusa. Start a fresh authorized OpenClaw session and verify the selected root and resumed Workpoint through the adapter and Focusa, not just the advisory card. Using a controlled test fixture, verify that a request with a mismatched root, continuity or out-of-scope subpath is rejected before effects. Do not try that write against a real unrelated project. If scope cannot be proven, hold only the affected Focusa operation; independently authorized work may continue.
4. **Handoff or rebind at Stage 6 if needed.** Record observed roots, runtime and adapter versions, the session/Workpoint check, scoped receipt references, isolation result and rollback point in the customer's private handoff. If runtime or root changes later, preserve the same Operating Partner and reconcile the exact continuity and root through the owning services. Repeat the checks before declaring cutover. A multi-server layout is a separately approved variation, not a prerequisite to recovering or handing off this setup.

See the [ordered Golden Path](02-agent-os-golden-path-ordered-tasks.md) for stage checks and the [Expression package bill of materials](16-wirebot-five-expression-package-bill-of-materials.md) for what to install. Executable installer coverage is tracked separately in [Golden Path installer #43](https://github.com/Startempire-Wire/agent-driven-life-business-os/issues/43).
