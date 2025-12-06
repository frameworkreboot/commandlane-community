# CommandLane Community

Welcome to the public community space for **CommandLane**.

CommandLane is a **local-first continuity layer for Windows, macOS, and Linux** that captures tasks and notes instantly with intelligent hybrid classification, and resurfaces relevant context when you return to work. This repository does **not** contain the main app source code – it exists to coordinate community resources, docs, and integrations.

- **Website**: https://www.commandlane.ai
- **Docs**: https://docs.commandlane.ai
- **Discord**: https://discord.com/channels/1445425782838005992
- **Support**: support@commandlane.ai

## What lives in this repo?

This repository is intended for community-facing materials, such as:

- Example **hooks** and automation scripts for CommandLane
- Public **documentation** and guides you’re comfortable sharing
- Community **FAQs**, troubleshooting notes, and tips
- Issue tracking for public bugs / feature requests

It’s a good place to collaborate without exposing the private core codebase.

## How CommandLane works (high level)

CommandLane focuses on:

- **Instant capture** via global hotkeys with <2s capture time
- **Hybrid classification** combining rules, TinyBERT, and (optionally) LLMs
- **Hybrid search** (semantic + keyword) on top of SQLite + FTS5 + vectors
- **Context resurfacing** so relevant notes/tasks appear when you return to work
- **Local-first privacy** – your data stays on-device by default

For deeper architectural details, see the private main repo docs or the public docs site.

## How to get involved

- **Ask questions / discuss ideas**: open a **Discussion** or join Discord.
- **Report a bug** (for public artifacts): open a **GitHub Issue**.
- **Suggest docs or examples**: open an Issue or PR against this repo.

Before filing an issue or PR, please read:

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

## License for this repo

Unless otherwise noted, text and example code in this repository may be used under the **MIT License**. This does **not** grant any rights to the proprietary CommandLane application code, which remains closed-source.
