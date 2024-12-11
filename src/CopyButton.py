import pyperclip
from PySide6.QtWidgets import (
    QPushButton,
    QTextEdit
)

class CopyButton(QPushButton):
    def __init__(self, output:QTextEdit, name="Copy"):
        super().__init__()
        self.output = output
        self.setText(name)
    
    def copy_to_clipboard(self):
        try:
            text = self.output.toPlainText()
            pyperclip.copy(text)
        except Exception as e:
            print(e)
    
    