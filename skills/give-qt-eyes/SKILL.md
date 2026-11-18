---
name: give-qt-eyes
description: Check Qt Widgets and PySide6 layout problems with screenshots, widget sizes, and normal control input. Use for missing table rows, clipped text, crowded controls, paragraph placement, or collapse and resize problems. Does not cover QML, web pages, screenshot cloning, or real-display approval.
---

# Give Qt Eyes

Check what the user can see, then show what changed. Use the project's existing QtTest or pytest-qt tests and the real affected widget. A separate demo app cannot prove that the user's app is fixed.

## Start with the complaint

Write down the expected result, sample data, starting state, window size, and actions. Make the result measurable. For example: changing a row setting from 3 to 6 should show six full rows when six rows exist and the window has room.

Check what the setting promises. A maximum of six rows may correctly show fewer in a small window. A changed setting or model count alone does not prove that more rows are visible.

Use safe sample data. Keep real content, saved settings, and other running work untouched. Record Python, PySide6/Qt, operating system, rendering mode, style, and display scale. Use the project's allowed test route. Do not silently install tools, change production settings, or switch to desktop input.

## Follow the normal action

1. Reproduce on the affected widget. Wait for a useful ready condition with a timeout. A fixed sleep or one `processEvents()` call is not proof that the layout is ready. Save a fresh starting image.
2. Measure the relevant controls in the same coordinate system. Check their size, visible area, parent clipping, and scroll viewport. For tables, separate model rows, hidden rows, full vertical rows, and partial rows. See [measurements](references/measurements.md).
3. Use `qtbot.mouseClick`, `keyClicks`, or `QTest` events. Check that the control is enabled and reachable at the click point, then check the result. Calling `.click()` or setting a value can check logic, but does not test normal input delivery. Qt test events also do not prove desktop mouse or focus behavior.
4. Save the new state. After a repair, repeat the same actions with the same data, size, style, and rendering mode. Try opening and closing again, or making the window narrow and wide again, where useful. Restore temporary settings and close only owned windows or jobs.

Use existing capture tools when they are enough. The optional [snapshot helper](scripts/snapshot.py) saves an image and measurements in a fresh folder. Import it into the existing test's UI thread. It does not attach to another app, wait for readiness, or change the window. [Helper usage](references/measurements.md#optional-helper) explains the details.

If the Python tool is installed, `give-qt-eyes compare BEFORE AFTER` compares the saved measurements. It keeps row identities and scroll positions, but does not inspect images or give a visual pass.

## Check the meaning, not just the rectangles

An overlap can be correct: badges, child controls, and stacked pages often share space. Hidden panels and scrolled content are not automatically broken. Check the intended layout, click area, clipping, and image together. A control that fits inside its parent can still have a cut-off label.

Add a regression test for each fixed defect. Include a nearby valid case, so the test cannot pass by flagging every overlap. Reproduce the failure before fixing it when possible. Keep the expected behavior; do not change unrelated sizes to make the test pass.

## When text placement matters

Read [paragraph maps](references/paragraphs.md) for text that looks split, clipped, crowded, or placed in the wrong column. Prefer Qt's text structure and line bounds over guessing from pixels.

The helper's `text_map=True` adds numbered bounds on a separate image for standard Qt text editors. `include_text=True` is a separate choice that copies source text. Inspect the original image too. Normal wrapping is not a split paragraph, and an unmapped area does not prove that text is missing.

If only an image or an unsupported text control is available, an existing OCR tool may help. OCR means reading text from an image. Treat its groups as estimates, keep coordinate changes and word confidence clear, and report failures as unknown. Do not join nearby columns, invent hidden text, or add a new OCR tool without need and permission. The helper does not run OCR.

## Report what the evidence shows

Start with what the user now sees. Then separate:

- **Measured:** actions, settings, sizes, full and partial rows, visibility, and the saved files before and after.
- **Seen in the image:** the affected area and what it appears to show. Explain judgments about spacing or readability.
- **Still unknown:** missing input, unsupported drawing, desktop checks not run, or unclear expected behavior.

Screenshots cannot prove exact fonts, hidden content, accessibility, or real-display quality. `QWidget.grab()` draws widget contents and may include areas covered by another window. An offscreen test draws in memory; it does not approve the app's desktop appearance. If you could not reproduce the problem or inspect the image, say so. A saved file or JSON result alone is not a visual pass.
