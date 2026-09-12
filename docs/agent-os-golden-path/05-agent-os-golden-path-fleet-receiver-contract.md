# Fleet audit receiver contract

## Purpose

The fleet audit receiver stores value-free readiness observations for comparison
across sweeps. Readiness is substrate state, not a W.I.N.S. business outcome.

## Input contract

- Individual reports use `agent-os-brownfield-audit.v5`.
- Fleet reports use `agent-os-fleet-audit.v2` and contain `fleet_score`, coverage,
  unseen-machine count, and machine-attributed blockers.
- The sender must provide `report_id`, `report_hash`, and the prior report hash
  when available. The receiver deduplicates by immutable `report_hash`.
- A report is accepted only for an operator-authorized project/mesh scope. Mesh
  discovery is observation, not enrollment; no machine is silently enrolled.
- Payloads remain value-free: no IP addresses, SSH keys, credentials, tokens,
  message content, or private environment dumps.

## Acceptance and readback

The receiver returns a durable receipt containing scope, schema, report hash,
accept/reject status, and timestamp. It must support readback by scope and report
hash, preserve rejected receipts for diagnosis, and never treat transport success
as audit acceptance.

## Retention and drift

Retention is bounded and operator-configured. The receiver keeps the latest
accepted observation plus an append-only audit trail needed for correction and
replay. `scripts/fleet-diff.py previous.json current.json` compares fleet score,
per-machine status/score, machine membership, and added/resolved blockers without
contacting machines. Drift is informational until an operator-authorized policy
promotes it to a work item.

## Planned binding

The natural first adapter is the private scoreboard receiver (`/v1/events`),
subject to its own authentication, scope, retention, and readback verification.
This document defines the contract; it does not claim that a production binding
has been deployed.
