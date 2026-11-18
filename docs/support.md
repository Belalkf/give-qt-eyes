# Support and limits

Give Qt Eyes 0.1.0 is an early release for ordinary Qt Widgets apps. The skill can use the project's existing test tools. The optional Python helper has a narrower job: save widget images and measurements without changing the app's state.

## What is supported

The comparison command and skill installer need Python 3.9+ and use only Python's standard library. The capture helper needs PySide6 6.5–6.x. It supports normal raster Qt Widgets, which are controls drawn by Qt.

The helper records widget sizes, positions, visibility, and standard QTableView/QTableWidget row bounds. QtTest or pytest-qt handles input and waiting. A full vertical row may still have cut-off cells or text; row counts do not prove readability.

The skill folder is `skills/give-qt-eyes`. It can be installed without the Python package. The wheel includes that same complete folder, so its instructions and helpers have one source. `pip install` does not add the skill to an agent; that needs a separate install command.

## What has been checked

The code comes from an earlier tested edition. Its local checks used macOS 14.8.9 arm64, Python 3.9.6, and PySide6/Qt 6.10.3 in `offscreen` mode. This mode draws test windows in memory. Earlier hosted checks also used Ubuntu 24.04, macOS 15 Intel, and Windows Server 2025 with Python 3.9/PySide6 6.5.0 and Python 3.13/PySide6 6.10.3.

Those earlier results are background, not proof that this renamed edition passed the same hosted checks. Use this repository's [Actions](https://github.com/Belalkf/give-qt-eyes/actions) for current runs. A workflow file alone does not show that its jobs passed. Linux capture may need Qt system libraries such as libEGL.

The tests cover changed and unchanged row settings, hidden and partly visible rows, small datasets, scroll positions, valid and broken overlaps, clipping, opening and closing panels, and resizing. They also check saved images, Unicode text, invalid inputs, existing skill installs, missing measurements, and keeping earlier files unchanged.

Paragraph tests cover two columns, wrapping, rich text, right-to-left text, scrolling, partial clipping, scan limits, source-text privacy, and image preservation. The helper keeps focus, cursor, selection, scroll position, and document content unchanged. A test also checks that reading a QPlainTextEdit layout does not change its scroll range.

## What these checks do not prove

Native desktop appearance, exact fonts, real display scale, accessibility, and physical screen quality need separate checks. Qt test events do not prove desktop mouse routing. Agent skill discovery and correct behavior in every host are not promised. No private app code or assets are included.

Qt Quick/QML, OpenGL, video, and embedded native controls need other capture tools. Tree views, list views, custom row drawing, and precise text-fit checks are outside the table helper. It does not attach to running processes or load arbitrary app factories.

Rectangular clipping ignores masks and rounded shapes. Visible-region bounds can include holes. A widget that Qt calls visible may be covered by another window. Images and measurements are taken one after the other, so wait for a stable state first. Above 10,000 model rows, the table helper reports unknown rather than scanning without a limit.

## Paragraph maps

Paragraph maps are off by default. They support standard QTextEdit, QTextBrowser, and QPlainTextEdit layouts, including wrapping, alignment, and mixed text directions. Empty, hidden, or fully outside-view paragraphs are left out. Nested frames, tables, inline objects, custom text layouts, and other controls are reported as unmapped.

The map shows line layout bounds, not exact letter shapes. Block numbers can match across resizing and scrolling while the document structure stays the same; they are not permanent text identities. Images keep their display scale. The map does not prove real-screen exposure or readability.

JSON leaves text out unless `include_text=True` is requested. That option includes the full paragraph and may copy text outside the visible area. The scan stops at 1,000 blocks or 100,000 characters per document, 200 regions overall, and 2,000 lines per block.

## OCR and other tools

OCR reads text from an image. The helper does not run OCR, install language data, or send images elsewhere. An earlier local Tesseract trial mixed two columns into the same groups and did not reliably read mixed Arabic text with English language data. That is why OCR groups should stay estimates. Other engines and languages were not tested.

The earlier [tool comparison](alternatives.md) found that existing Qt tools were enough for its sample problem. No better-detection or speed claim is made here. Python 3.9 remains supported for existing projects; choose a maintained Python version for a new setup.
