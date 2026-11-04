---
title: GhostShell: a haunted terminal that runs fully offline
tags: devchallenge, hacktoberfest, ai, opensource
---

*This is a submission for the Hacktoberfest Open-Source AI Challenge: Week 4 (Ghost in the Machine).*

## What I Built

GhostShell is a terminal wrapper that "possesses" your shell. Every command runs normally, then a ghost whispers one eerie sentence about what you just did. It is about 30 lines of Python, and the UI was designed with Figma Make (prompt in the README).

## Demo

Run `python ghostshell.py`, type `ls` or `git status`, and read what the spirit says. UI design (Figma Make): https://blush-curl-39070128.figma.site/ . Code: https://github.com/chatgaiyashenanigan-alt/ghostshell

## How It Works

The script runs your command with `subprocess`, then sends the command and its output to a local Ollama server (`llama3.2:1b`) with a ghost persona prompt. The reply is printed in purple under the output.

## Why Open Innovation Matters

Your shell history holds secrets: paths, hostnames, tokens in error messages. A closed API would send all of that to a server you don't control. With an open-weight model, nothing leaves the machine. It works on a plane with the Wi-Fi off, costs nothing per command, and I can swap the model by changing one string. A hosted model could change or disappear, but this ghost stays as long as the weights are on disk.

## Designing the UI with Figma Make

I pasted a single prompt (see README) into Figma Make: a marigold-and-violet terminal with fading whisper lines, an offline badge, a model picker, and an "ofrenda" sidebar of past whispers. It gave me a layout I could build from.
