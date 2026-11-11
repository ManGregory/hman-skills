# Changelog

## mentor 1.0.0 — 2026-11-11

First public release, rebuilt from a personal set of Claude Code commands.

- One `mentor` skill replaces the separate `mentor`, `mentor-compact` and `mentor-quick` commands. Quick Q&A is now a session type.
- Detailed protocols moved to `references/`, loaded only when needed.
- Two storage modes: a workspace with `.mentor.json` (replaces the `MENTOR_ROOT` variable and fixed paths), and a progress file for regular Claude chats.
- Auto-commit, auto-push, transcript detail and default teaching style are configurable.
- JSON Schema for `results.json`, a starter repository and eval cases.
