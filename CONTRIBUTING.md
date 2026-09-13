# Contributing to LC-MCP-eduagent_tayra

Thank you for your interest in contributing! Please follow the guidelines below to ensure a smooth contribution process.

**Code of Conduct**

All contributors must adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

**Issues and Discussions**

* Every contribution must be explicitly connected to one or more GitHub **issue(s)** or **discussion topic(s)**.
* Please reference the issue or discussion number in your pull request description (e.g., `Closes #123`).

**Branching Strategy**

* All work must be done on a new branch created within your **forked repository**.
* If an **AI agent** (such as Codex or Antigravity) assisted with any part of the contribution, your branch name must include the agent's name as a prefix:
* Example: `codex/feature-name` or `antigravity/fix-bug`
* Standard branches without AI assistance should use a descriptive name (e.g., `feature/short-description`).

**Development Setup with Hatch**

This project uses **Hatch** for project management, dependency management, and testing. Ensure you have Hatch installed on your system.

* **Run tests:**
```bash
hatch run test
```
* **Run linting and style checks:**
```bash
hatch run lint:all
```

**Testing Requirement**

* **Before submitting a pull request**, your contribution branch must pass **all tests** locally. PRs with failing CI checks or untested code will not be reviewed.

**Pull Request Guidelines**

* Submit your pull request to the main repository's default branch.
* Ensure your PR description strictly follows the provided template, detailing the changes made and linking the relevant issues or discussions.