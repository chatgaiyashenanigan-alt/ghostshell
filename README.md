# 👻 GhostShell

A haunted terminal that runs entirely on your machine. Run any shell command and a ghost, powered by a local open-weight model, whispers one eerie line about it. No cloud, no API key, no internet.

Built for the [Hacktoberfest Open-Source AI Challenge: Week 4](https://dev.to/challenges/hacktoberfest-week4-2026-10-26) ("Ghost in the Machine"). Read the write-up on DEV: [GhostShell: a haunted terminal that runs fully offline](https://dev.to/tayebbb/ghostshell-a-haunted-terminal-that-runs-fully-offline-15n7). The web UI was designed with Figma Make: [design preview](https://blush-curl-39070128.figma.site/).

## Features

- Two modes: a plain terminal (CLI) and a web UI.
- Local inference through [Ollama](https://ollama.com), with a model picker in the UI.
- Private by default: commands and output are sent only to `localhost:11434`.
- No dependencies beyond Python's standard library.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/download) running locally
- An open-weight model, e.g. `ollama pull llama3.2:1b`

## Quick start

```bash
git clone https://github.com/chatgaiyashenanigan-alt/ghostshell.git
cd ghostshell
ollama pull llama3.2:1b

python ghostshell.py          # terminal mode
python ghostshell.py --web    # web UI at http://127.0.0.1:8000
```

Type `exit` to leave terminal mode. If Ollama isn't running, commands still execute and the ghost reports that the spirit is silent.

## Configuration

| Setting | Where | Default |
|---|---|---|
| Model (CLI) | `MODEL` in `ghostshell.py` | `llama3.2:1b` |
| Model (web) | Model dropdown in the UI | `llama3.2:1b` |
| Ghost persona | `SYSTEM` in `ghostshell.py` | melancholy ghost |
| Web port | `serve(port=...)` in `ghostshell.py` | `8000` |

The dropdown lists `llama3.2:1b`, `qwen2.5` and `gemma`. Pull any model you select first (`ollama pull qwen2.5`).

## Security

GhostShell **executes the commands you type** with your user's permissions.

- The web server binds to `127.0.0.1` only. Never expose it to a network or put it behind a proxy.
- The API accepts only `application/json` POSTs, so other websites can't trigger it from your browser.
- Commands are limited to 30 seconds in web mode.

Treat it as a toy for your own machine, not a multi-user service.

## Project layout

```
ghostshell.py        CLI, local web server, Ollama client
index.html           Web UI (from the Figma Make design)
assets/figma.css     UI styles exported from the Figma Make design
```

## How it works

1. Your command runs with `subprocess`.
2. The command and the first 500 characters of its output go to Ollama's `/api/chat` with a ghost persona prompt.
3. The reply is shown under the output (and in the web UI's "Ofrenda" list).

## Why open models

Shell history holds paths, hostnames and secrets. With an open-weight model nothing leaves your machine, it works offline, costs nothing per command, and you can swap models by changing one string.

## Design prompt

<details>
<summary>Figma Make prompt used for the UI</summary>

> Design a single-screen responsive web UI for "GhostShell", a haunted terminal app for the Halloween / Día de los Muertos "Ghost in the Machine" theme. Dark violet-black background, marigold-orange accents, faint candle glow, monospace font for the terminal and a serif for headings. Top bar: app name with a ghost icon, a green "Running locally – offline" badge, and a model dropdown (llama3.2:1b, qwen2.5, gemma). Center: a terminal panel with a ghost-emoji prompt line and command output; under each output a translucent purple italic "ghost whisper" line that fades in with a gentle floating animation. Right sidebar: an "Ofrenda" list of recent whispers as candle-like cards with small marigold icons. Footer: "Open-weight. Private. Yours." Include hover states and a mobile layout where the sidebar collapses below the terminal.

</details>

## Notes

All of this project was built on Nov 4, 2026, after the challenge deadline (Oct 31, 2026).
