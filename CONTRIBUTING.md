# Help improve Give Qt Eyes

A small example of a real Qt problem is a good place to start. Use sample data, explain what should happen, and show what happens instead. Please include Python, PySide6/Qt, operating system, and rendering mode.

## Run the tests

Use a separate Python environment with the package and PySide6 installed:

```sh
python -m pip install -e '.[qt]'
QT_QPA_PLATFORM=offscreen python -m unittest discover -s tests -t . -v
```

On PowerShell, set `$env:QT_QPA_PLATFORM='offscreen'` first. This draws test windows in memory. It checks the test cases, not native display quality or accessibility. The tests close their own windows and normally remove temporary captures. Set `GIVE_QT_EYES_OUTPUT` to a folder if you want to keep them. Ctrl-C cancels the foreground run.

For changes that need no Qt, run:

```sh
python -m unittest tests.test_compare tests.test_text_compare tests.test_install -v
```

Add a failing test before fixing a defect when possible. Keep a valid case too, especially for clipping or overlap checks. Preserve existing captures and app settings. Keep each source, test, and documentation file below 150 lines by splitting separate jobs into clear files.

## Keep the claims clear

Use short, everyday English. Say what a user would notice before explaining the code. Keep documentation paragraphs on one line.

Tests, measured values, image review, and real-display checks are different kinds of evidence. Say which ones you used. Do not turn a configured workflow or successful screenshot save into a claim that everything works.

Before a release, test a fresh install outside the source folder, check the complete installed skill, and review the actual archive and Git history for private data. Publish only with the owner's permission. Check the hosted jobs and saved protections after publishing.

Use [Issues](https://github.com/Belalkf/give-qt-eyes/issues) for ordinary bugs. Do not share real app images before checking their contents. Use [private reporting](SECURITY.md) for sensitive problems.
