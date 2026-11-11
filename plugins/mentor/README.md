# mentor

A learning mentor for Claude. It teaches any topic with Socratic questions, worked examples and active recall, and keeps your progress between sessions so it never asks the same questions twice.

- **Adapts to how you learn**: socratic (questions first), explanatory (explain first) or hybrid, remembered per topic.
- **Picks up where you left off**: reads your learning plan and last session before saying anything.
- **Knows what kind of session this is**: new topic, learning, continuation, review, or a quick question with no ceremony.
- **Checks understanding**: blurting essays, Feynman explanations, comprehension tests and quick recaps, scored and saved to `results.json`.
- **Saves everything**: in a git repo it commits and pushes after each session; in a regular chat it hands you a progress file to attach next time.

## Install

### Claude Code (terminal, desktop app, web, mobile Code tab)

```
/plugin marketplace add ManGregory/hman-skills
/plugin install mentor@hman
```

Or skip this and use the starter repository below: it installs the plugin automatically.

### Claude app chat (web, desktop, mobile)

1. Download `mentor-<version>.zip` from the [latest release](https://github.com/ManGregory/hman-skills/releases).
2. In Claude, make sure **Code execution and file creation** is on in **Settings > Capabilities**.
3. Go to **Customize > Skills**, click **+**, then **Create skill > Upload a skill**, and choose the zip.

Skills you upload belong to your account, so the mentor is available wherever you use Claude.

## Use it

Just say what you want, in any language:

> I want to learn Kubernetes from scratch

> Let's continue with git basics

> Quiz me on what we covered last week

> Wrap up

In Claude Code you can also call it directly with `/mentor:mentor`.

## Where your progress lives

### A learning repository (recommended with Claude Code)

1. Create a **private** GitHub repository, for example `my-learning`.
2. Copy the contents of [`starter/`](starter/) into it and push.
3. Open it in Claude Code anywhere (terminal, desktop, web or phone) and start learning.

```
my-learning/
├── .mentor.json            ← settings
├── .claude/settings.json   ← installs the mentor plugin for this repo
└── kubernetes/
    ├── learning-plan.md
    └── 01-pods/
        ├── session-2026-11-12-190512.md
        ├── feynman-test.md
        └── results.json
```

`.mentor.json`:

| Key | Default | Meaning |
|-----|---------|---------|
| `autoCommit` | `true` | Commit at wrap-up after an assessment without asking |
| `autoPush` | `true` | Push after committing |
| `transcript` | `"full"` | `"full"` records every exchange verbatim; `"summary"` keeps short notes |
| `defaultStyle` | `null` | `"socratic"`, `"explanatory"` or `"hybrid"` for new topics; `null` means ask |

### A progress file (regular chat)

In a chat there's no folder that survives between conversations, so at wrap-up the mentor gives you `{topic}-progress.md`. Attach it at the start of the next session. It holds the plan, a short log of each session and your results, in the same format as the repository, so you can move to a repository later.

## How a session ends

When you say "wrap up", the mentor:

1. Updates the learning plan.
2. Completes the session notes.
3. Asks how you want to finish: **quick recap**, **written** (blurting, Feynman or test), **full**, or **none**.
4. Saves the score and the areas to review to `results.json`.
5. Commits and pushes, or hands you the updated progress file.

## Develop

```
scripts/validate.sh                    # manifests, skill frontmatter, example data
scripts/build-skill-zip.sh mentor      # dist/mentor-<version>.zip
claude plugin eval plugins/mentor      # run the eval cases in evals/
```

Eval cases are in [`evals/`](evals/): each has a `prompt.md` and LLM-graded criteria.
