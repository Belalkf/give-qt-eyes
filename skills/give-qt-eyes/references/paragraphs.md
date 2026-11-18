# Find text paragraphs

Use a text map when text looks split, clipped, crowded, or placed beside the wrong content. Numbered regions connect Qt's text layout to a fresh image. They help review; they do not decide whether the design is right.

## Use Qt's text structure first

Call `capture(window, selected_widgets, output_dir, text_map=True)`. This adds `text-map.png` beside the unchanged `widget.png`, with paragraph numbers and line rectangles. It also adds a `text_map` section to JSON. Inspect the original image too, since markers cover some pixels.

Standard QTextEdit, QTextBrowser, and QPlainTextEdit layouts are supported. Qt supplies paragraph numbers and line bounds. Wrapping a paragraph onto more lines does not create more paragraphs. Controls in separate columns keep separate identities.

Empty, hidden, and fully outside-view text is left out. Unsupported controls, nested frames or tables, inline objects, missing layout, and scan limits appear in `unmapped`. An empty region list does not prove there is no text.

Bounds use logical coordinates from the captured root, including the viewport position and current scrolling. They describe line layout, not exact letter shapes. The marked image keeps the original display scale. Clipping checks the viewport, parent rectangles, and capture bounds. Other windows, masks, and physical display quality stay unknown.

Block numbers can match across resizing and scrolling while the document structure stays unchanged. They are not permanent identities across edits and do not prove the text stayed the same.

## Keep source text private

JSON leaves text out by default. `include_text=True` copies the full source paragraph, including any part outside the visible area. Use sample data or keep that file private. This option requires `text_map=True`.

The helper does not change the document, selection, cursor, focus, or scroll position. It scans at most 1,000 blocks or 100,000 characters per document, returns at most 200 regions overall, and checks at most 2,000 lines per block.

## When only an image is available

An existing local OCR tool may help. OCR means reading text from an image. Do not silently install a tool or language data. For example, installed Tesseract can return words, groups, and rectangles:

```sh
tesseract widget.png stdout -l eng tsv
```

Choose languages that are already installed and fit the content; English is just an example. Keep images local unless sending them elsewhere is allowed.

OCR paragraphs are estimated visual groups. Confidence about a word does not prove its paragraph is grouped correctly. Record the tool, language, image size, grouping source, and uncertainty. Map coordinates back only when crop, resize, and scale changes are known. Failed reading means unknown, not missing text or a broken interface. The helper does not run OCR or merge its output.

## Useful checks

Compare the same text before and after resizing, scrolling, and restoration. Include correct wrapping, nearby columns, blank lines, mixed text directions, a partly clipped paragraph, and an unsupported control. Check that columns stay separate, hidden text is not called visible, and normal wrapping is not called a split. Explain the intended grouping when it depends on design judgment.
