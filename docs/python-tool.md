# Use the Python tool

The Python tool is optional. It saves images and measurements from an existing Qt test, then compares two saved captures. It does not attach to a running app or decide whether a design is good.

## Install

```sh
python -m pip install give-qt-eyes
```

Choose the Python environment used by your app. If it has no PySide6 installation, you can request the optional Qt dependency:

```sh
python -m pip install 'give-qt-eyes[qt]'
```

Do not replace a project's Qt version just to use this tool. The comparison command needs no Qt installation.

## Capture a state

Call this from the UI thread, which is the thread that owns the app's controls. Wait for your test's expected layout before each capture.

```python
from give_qt_eyes import capture

folder = capture(window, {"table": window.table}, evidence_dir)
```

The window must already be shown inside Qt. Tests can use Qt's `offscreen` mode to draw it in memory without showing a desktop window. The helper does not show hidden windows or change their size, values, focus, or scroll position.

Each call creates a new `capture-*` folder with `widget.png` and `measurements.json`. These files can show private content. Use sample data or keep them private. If saving fails, the partial folder stays for inspection; it is not a finished capture.

## Mark paragraphs

```python
folder = capture(window, {"left": window.left_text}, evidence_dir,
                 text_map=True)
```

This adds `text-map.png` with paragraph numbers and line bounds. Standard QTextEdit, QTextBrowser, and QPlainTextEdit controls are supported. Unsupported regions stay unknown. The original image is kept.

Text is left out of JSON by default. Adding `include_text=True` copies the full source paragraph, which may include text outside the visible area. See [paragraph maps](../skills/give-qt-eyes/references/paragraphs.md).

## Compare captures

```sh
give-qt-eyes compare before/capture-folder after/capture-folder
```

The JSON output lists changed sizes, row counts, scroll positions, and environment details. Exit code 0 means the comparison finished; it does not mean the layout passed. Missing data stays unknown. Input files are not changed. See [measurement details](../skills/give-qt-eyes/references/measurements.md).

## Install the skill through Python

If you prefer not to use the skills CLI:

```sh
give-qt-eyes install-skill --user
```

This creates `~/.agents/skills/give-qt-eyes` for Codex. Use `--project /path/to/project` for one project instead. Existing files, folders, and links are refused. A failed write can leave a partial install for inspection. Installing the Python package alone never changes your agent settings.

In Codex, ask for `$give-qt-eyes`. Installing the skill does not install Qt or prove that the agent has followed its steps.
