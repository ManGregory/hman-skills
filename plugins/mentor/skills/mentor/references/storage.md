# Storage modes

The mentor keeps the same information in every mode: a learning plan per topic, session records, and assessment results. Only where it lives changes.

## Workspace mode

Used when a `.mentor.json` file exists in the current directory or a parent directory. Typical setups: a private git repository opened in Claude Code (terminal, desktop app, web or the mobile app), or any local folder.

### Layout

```
<mentor root>/
├── .mentor.json
├── {topic}/
│   ├── learning-plan.md
│   └── {subtopic}/
│       ├── session-YYYY-MM-DD-HHMMSS.md
│       ├── blurting-essay.md
│       ├── feynman-test.md
│       ├── comprehension-test.md
│       ├── checkpoint-quiz-YYYY-MM-DD.md
│       └── results.json
```

- Topic and subtopic folder names are lowercase slugs (`java-spring`, `01-core-idea`). Subtopics can be nested for big topics.
- New files start from the templates in `templates/`.

### `.mentor.json`

```json
{
  "autoCommit": true,
  "autoPush": true,
  "transcript": "full",
  "defaultStyle": null
}
```

| Key | Default | Meaning |
|-----|---------|---------|
| `autoCommit` | `true` | Commit at wrap-up after an assessment without asking. Only applies inside a git repository. |
| `autoPush` | `true` | Push after committing, if a remote is set. |
| `transcript` | `"full"` | `"full"`: record every exchange verbatim. `"summary"`: short notes per concept. |
| `defaultStyle` | `null` | `"socratic"`, `"explanatory"` or `"hybrid"` for new topics. `null` means ask. |

Missing keys use the defaults. To set up a new mentor root, create `.mentor.json` with the defaults above (or copy `templates/mentor.json`), and if the folder is a git repository, commit it.

## Progress-file mode

Used in a regular Claude chat (web, desktop or mobile), where files don't persist between conversations. Each topic's whole state lives in one markdown file that the student keeps and attaches at the start of each session.

### Rules

- One file per topic: `{topic-slug}-progress.md`, using `templates/progress-file.md`.
- Keep it small enough to attach every time: a session log entry is a short summary, not a transcript. When the session log grows past about 15 entries, merge the oldest ones into a single "Earlier sessions" summary.
- At wrap-up, always hand back the **complete** updated file, never a diff.
- If the student attaches files from workspace mode instead (a `learning-plan.md` and `results.json`), use them, and hand back a progress file at the end.

### Moving between modes

- **Progress file → workspace**: create `{topic}/learning-plan.md` from the "Learning plan" section, and one `results.json` per subtopic from the "Results" block.
- **Workspace → progress file**: combine the topic's `learning-plan.md`, a summary of recent sessions, and all `results.json` sessions into one progress file.
