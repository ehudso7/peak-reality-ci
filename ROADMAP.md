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

## Epic 2: IDE & Devcontainer Integrations
| Purpose | Provide plug‑and‑play VS Code extension and Devcontainer templates so developers instantly get the full Peak‑Reality experience in their IDE and containerized workspace. |
|:--------|:---------------------------------------------------------------------------------------------------------|
| Why     | Lower the barrier to entry with zero‑config IDE setup, built‑in lint/test runner UI, and reproducible devcontainers. |
| Inputs  | `.devcontainer/` folder and `vscode-extension/` source code.                                                |
| Outputs | `.devcontainer/devcontainer.json`, `.devcontainer/Dockerfile`; VS Code extension package in `vscode-extension/`. |
| Depends | Epic 1 (CLI & SDK installed globally), VS Code Extension API.                                              |
| Used by | Developer onboarding; Codespaces; GitHub Desktop/VS Code users                                                   |

### Tests
- Devcontainer: lint JSON schema; smoke start via `devcontainer build --workspace .` (best‑effort)
- VS Code extension: unit tests via `vscode-test` harness; ensure commands register.

### Ops
- Publish VS Code extension to VS Code Marketplace on Git tag
- Provide Devcontainer badge in README

### Risk
- R2 (developer tooling); ephemeral blast radius; gated by CI + manual review of extension manifest.