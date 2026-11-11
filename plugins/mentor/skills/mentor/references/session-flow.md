# Wrap-up protocol

Run these five steps in order, and don't hand control back to the student until all of them are done. After each step, confirm it in one short line (for example "✓ Learning plan updated").

## Step 1. Update the learning plan

Do this as soon as wrap-up is triggered.

- Mark completed concepts `[x]` in "Subtopics & Structure".
- Update "Current Progress": last session date, current subtopic, status, next steps.
- Record any newly learned facts about the student (background, goals, teaching-style preference) so they are never asked again.

Workspace mode: edit `{topic}/learning-plan.md`. Progress-file mode: update the "Learning plan" section of the progress file you will hand back.

## Step 2. Complete the session record

Workspace mode, `transcript: full`:
1. Read the session file completely.
2. Compare it with the conversation since the session started.
3. Append every exchange that is missing, with the student's words verbatim and your explanations in full.
4. Check that "Dialogue & Learning" ends with the last exchange before wrap-up.
5. Fill in "Concepts Covered", "Key Insights" and "Confusion Points".

Workspace mode, `transcript: summary`: make sure every concept covered has a short note, then fill in the same three sections.

Progress-file mode: write a short session summary (date, concepts covered, key insights, confusion points) into the "Session log" section. Don't paste the full transcript; the file must stay small enough to attach every time.

Don't move on until the record is complete.

## Step 3. Assessment

Ask: "How would you like to wrap up today's session?" and offer the options in `assessments.md`, with a recommendation based on session length. Then run the chosen assessment.

## Step 4. Update results

Skip this step for option D.

1. Read the existing `results.json` for the subtopic (workspace mode) or the "Results" block of the progress file. If none exists, create one with `schema_version: "1.0"`, `topic`, `subtopic`, an empty `sessions` array and `metadata.created`.
2. Build a session object that follows `templates/results.schema.json`: session id (`YYYYMMDD-HHMMSS-xxxx`, where `xxxx` is 4 random lowercase letters or digits), start and end timestamps (ISO 8601), duration, session type, assessment type and score, concepts covered, strong areas, areas to review, and the next-session recommendation.
3. Append it to `sessions` and set `metadata.last_updated`.
4. Write the result back.

## Step 5. Save

**Workspace mode.** Read `.mentor.json`:
- `autoCommit: true` (default): for options A, B and C, commit without asking. For option D, ask "Should I commit today's session notes?" first.
- `autoPush: true` (default): push after the commit if the repository has a remote.

```bash
git add "{topic}/"
git commit -m "Session: {topic}/{subtopic} - {YYYY-MM-DD}" \
  -m "Covered: {concepts}" \
  -m "Assessment: {type} - Score: {score}" \
  -m "Next: {next steps}"
git push
```

If git isn't available or the push fails, say so in one line; the files are still saved.

**Progress-file mode.** Write the complete updated progress file (format in `storage.md`) as a file named `{topic-slug}-progress.md` and give it to the student to download. Tell them to attach it at the start of the next session. If you can't create files, show the full file in one code block so they can copy it.

## Finish

End with one line: what was saved, the score if there was one, and what the next session should cover.

## Never do these

- Hand back control before step 5 is done.
- Skip the plan update or the results update (for A, B or C).
- Ask about committing for A, B or C when `autoCommit` is on.
- Treat a mid-session quiz as the final assessment.
