# How this fits with other tools

You may already have most of what you need. Give Qt Eyes uses normal Qt tests and adds a repeatable way to connect a complaint, screenshots, and measurements.

| Tool | What it helps with |
| --- | --- |
| [pytest-qt](https://pytest-qt.readthedocs.io/en/latest/reference.html) | Test input, wait for a condition, save screenshots, and clean up widgets. Use it when the project already has it. |
| [Qt QWidget APIs](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html) | Read widget sizes and positions, check visibility, and draw widget contents. These supply the measurements used here. |
| [qt-testing in SLEAP](https://github.com/talmolab/sleap/tree/develop/.claude/skills/qt-testing) | A useful Qt testing skill to compare with your existing workflow. Check its current instructions before use. |

Give Qt Eyes adds saved comparison records and a small skill that follows the user's complaint through normal controls. It is not a new test runner. No code from these projects is included. Original project files use MIT; Qt keeps its [own licence terms](https://doc.qt.io/qtforpython-6/licenses.html).

## What the earlier trial showed

Before this renamed edition, two separate agents checked the same unseen sample widget. One used the earlier skill; the other used existing Qt tools without it. Both found the row-count problem and a clipped heading. Both checked a working Details toggle and resizing, rejected harmless overlaps, and kept real-display and font questions open.

The skill-guided run used the bundled capture helper. The other run inspected seven images; the skill-guided run inspected six. This was a small comparison, not a speed benchmark or proof of better detection. Both kept the sample unchanged and closed their test windows.

Existing tools were enough for that trial. This project is for people who want the steps and saved evidence in one place. It does not claim unique detection, better accuracy, time savings, or approval from the other projects. This edition has not had a new agent comparison.
