# ROADMAP

This file tracks the upcoming epics and priorities for the Peak Reality++ platform.

## Epic 1: CLI & SDK Packages

| Purpose | Provide an installable CLI & language SDKs so developers can scaffold, inspect, and enforce Peak‑Reality guardrails programmatically. |
|:--------|:-----------------------------------------------------------------------------------------------------|
| Why     | Without an easy-to‑install package and `peak init`, no one can adopt the framework. This is the gateway for all other integrations. |
| Inputs  | None (fresh repo/workdir)                                                                           |
| Outputs | `peak` CLI binary; JavaScript/TypeScript SDK package (`peak-platform`); initial project scaffolding.   |
| Depends | Existing CI framework under branch `ci/live-peak-index`; core helper scripts in `/scripts`.         |
| Used by | IDE extensions, dashboard generators, starter templates                                                |

### Tests
- Unit tests for each CLI command (`--version`, `--help`, `review`, `scan`, etc.)
- Contract tests for package metadata
- Docs build/doctest for CLI README examples
- Property/fuzz sampling on CLI argument parsing

### Ops
- Publish to npm on tag via GitHub Actions
- GitHub Release on tag with changelog
- Telemetry/usage opt‑in via CLI (disabled by default)

### Risk
- R2 (internal dev-tool);
- limited blast radius; CI gates protect stability and quality.