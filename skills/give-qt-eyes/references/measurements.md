# Read the measurements

A measurement is one part of the evidence. Check it against the expected behavior and the matching image.

## Positions and visible areas

Use Qt's logical coordinates and map each selected control to the same root with `mapTo`. A control's `geometry()` is relative to its parent. Check parent bounds and scroll viewports too.

`visibleRegion()` gives an estimate. Its outer rectangle can include holes, and `isVisible()` does not prove that a real display shows the window without anything covering it. Check whether the click point lies inside the visible region and whether `childAt` reaches the intended control or its child.

Parents and children normally share space. Badges, overlays, stacked pages, and closed panels also need their intended state considered. Rectangle clipping ignores masks and rounded shapes. A rectangle that fits does not prove that the text inside fits.

## Table rows

For QTableView or QTableWidget, count row sections that meet the viewport after scrolling has settled. Separate full vertical rows from partial rows and skip hidden rows. Keep the model row count and viewport height, so a changed setting cannot look like a changed display by itself.

A model with two rows cannot show six filled rows. A maximum-row setting may correctly show fewer rows in a small window. Check that intended meaning before calling the result a bug.

The helper counts vertical row bounds only. It does not check horizontal cell visibility, text quality, other windows covering the view, row spans, custom cell drawing, or content loaded later. Tree views, list views, QML, and custom lists need their own checks. Above 10,000 model rows, it reports unknown.

## Optional helper

Use an existing QApplication, its UI thread, a shown QWidget root, selected child controls, and a chosen output folder. A root shown inside Qt can use `offscreen` mode; it need not appear on a desktop. Import the installed skill's `scripts/snapshot.py`, or use `give_qt_eyes.capture` from the optional Python package.

Inside a project's existing test:

```python
# snapshot is the imported scripts/snapshot.py module.
qtbot.waitUntil(lambda: widget.table.model().rowCount() == 12, timeout=1000)
before = snapshot.capture(widget, {"table": widget.table}, evidence_dir)
widget.row_setting.selectAll()
qtbot.keyClicks(widget.row_setting, "6")
qtbot.waitUntil(lambda: widget.row_setting.value() == 6, timeout=1000)
qtbot.waitUntil(
    lambda: len(snapshot.table_rows(widget.table)["full_vertical_rows"]) == 6,
    timeout=1000,
)
after = snapshot.capture(widget, {"table": widget.table}, evidence_dir)
```

Wait for the expected layout, not just the setting value. Use `qtbot.screenshot` and local checks instead if they already give enough evidence.

The helper saves environment details, root size, selected positions, visibility, click-point facts, and table row numbers. It leaves widget text and object names out of JSON by default. The optional [paragraph map](paragraphs.md) has a separate source-text option. Images still show rendered content, so use sample data or keep them private.

Each call creates a new `capture-*` folder with `widget.png` and `measurements.json`. Labels do not choose file names. Earlier captures are kept. A save failure raises an error and can leave a partial folder; that is not a complete capture. Remove only your own temporary files when they are no longer needed.

The helper does not show hidden roots, change display flags, focus, size, values, or panel state. It rejects controls from another root and separate child windows. Capture dialogs separately. It does not create an app, run an event loop, wait for readiness, attach to another process, or give a pass/fail result. Give test runs a deadline and cancel only their owned process if needed.

## Image limits

Use the helper for ordinary Qt Widgets. OpenGL, Qt Quick, native embedded windows, video, and desktop effects need other tools. A widget grab may repaint content and may leave out window frames, cursors, menus, or separate popups. Capture those separately when needed.

Keep image pixels separate from Qt logical coordinates when display scale is not one. Font settings can help with a font complaint, but a screenshot cannot identify the exact font or fallback letters. Offscreen images do not prove native sizing, focus, accessibility, or display quality.
