import ast
import json
from PySide6.QtWidgets import (
    QPushButton,
    QTextEdit
)

class ConvertButton(QPushButton):
    def __init__(self, input:QTextEdit, output: QTextEdit, name="Convert"):
        super().__init__()
        self.input = input
        self.output = output
        self.setText(name)
        self.clicked.connect(self.convert_dict_to_json)
    
    def convert_dict_to_json(self):
        try:
            text = self.input.toPlainText()
            if text.strip() == "":
                return
            d = ast.literal_eval(text)   
            json_formatted_str = json.dumps(d, indent=4)
            self.output.setText(json_formatted_str)
        except Exception as e:
            self.output.setText(str(e))