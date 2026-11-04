# GhostShell

A haunted terminal: run commands, and a local ghost whispers eerie commentary. Powered by an open-weight model through [Ollama](https://ollama.com). No internet or API key needed.

```
ollama pull llama3.2:1b
python ghostshell.py          # terminal mode
python ghostshell.py --web    # Figma Make UI at http://127.0.0.1:8000
```

The web UI's markup and CSS (`index.html`, `assets/figma.css`) come from the Figma Make design: https://blush-curl-39070128.figma.site/

Commits made after the challenge deadline (Oct 31, 2026) are noted here: all of this project was built Nov 4, 2026.

## Figma Make prompt (UI)

Paste into Figma Make:

> Design a single-screen web UI for "GhostShell", a haunted terminal app for the Día de los Muertos / Halloween "Ghost in the Machine" theme. Dark violet-black background with marigold-orange accents and faint candle glow. Center: a terminal panel with monospace text, a prompt line starting with a ghost emoji, and command output. Below each output, a translucent purple italic "ghost whisper" line that fades in with a subtle floating animation. Top bar: app name, a green "Running locally - offline" badge, and a model selector dropdown (llama3.2:1b, qwen2.5, gemma). Right sidebar: "Ofrenda" list of recent whispers as candle-like cards with small marigold icons. Footer: "Open-weight. Private. Yours." Include hover states and a responsive mobile layout.
