# hman-skills

Open-source skills for [Claude](https://claude.ai), packaged as Claude Code plugins and as zips you can upload to the Claude apps.

| Plugin | What it does |
|--------|--------------|
| [**mentor**](plugins/mentor/) | A learning mentor that teaches with Socratic questions and active recall, and keeps your progress between sessions |

## Install

### Claude Code (terminal, desktop app, web, mobile Code tab)

Add this marketplace once:

```
/plugin marketplace add ManGregory/hman-skills
```

Then install any plugin from it:

```
/plugin install mentor@hman
```

Update later with `/plugin marketplace update hman`.

### Claude app chat (web, desktop, mobile)

Each release attaches one zip per skill. Download it from [Releases](https://github.com/ManGregory/hman-skills/releases), then in Claude go to **Customize > Skills**, click **+**, then **Create skill > Upload a skill**. Skills need **Code execution and file creation** turned on in **Settings > Capabilities**.

## Repository layout

```
.claude-plugin/marketplace.json   the catalog: lists every plugin
plugins/<name>/
  .claude-plugin/plugin.json      plugin manifest and version
  skills/<skill>/SKILL.md         the skill, with references/ and templates/
  evals/                          eval cases for `claude plugin eval`
  starter/                        optional: files users copy to get started
scripts/                          validation and zip packaging
.github/workflows/                CI and releases
```

## Contributing

Issues and pull requests are welcome. Before opening a PR, run:

```
scripts/validate.sh
```

To release a plugin, bump `version` in its `plugin.json`, update [CHANGELOG.md](CHANGELOG.md), then run `claude plugin tag plugins/<name> --push` (or push a tag named `<name>--v<version>`). The release workflow builds the skill zips and publishes a GitHub release.

## License

[MIT](LICENSE)
