"""Sample text in two columns, with wrapping and mixed text directions."""
from PySide6.QtWidgets import QHBoxLayout, QPlainTextEdit, QTextEdit, QWidget


class ParagraphWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sample paragraph map')
        layout = QHBoxLayout(self)
        self.left = QTextEdit()
        self.left.setPlainText(
            'A paragraph stays together while its words wrap into more lines. '
            'Changing the width should change its bounds without inventing new paragraphs.\n'
            'A separate paragraph belongs below the first one.\n'
            'English and العربية can share a paragraph.')
        self.right = QPlainTextEdit()
        self.right.setPlainText(
            'This text belongs to the other column, even when it is nearby.\n'
            'A short independent paragraph.')
        layout.addWidget(self.left)
        layout.addWidget(self.right)
        self.resize(720, 280)
