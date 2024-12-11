from PySide6.QtWidgets import (
    QTextEdit
)

class TextEdit(QTextEdit):
    def __init__(self, placeholder=""):
        super().__init__()
        self.setPlaceholderText(placeholder)
        self.setBaseSize(400, 100)
        self.setAcceptRichText(False)
    
    