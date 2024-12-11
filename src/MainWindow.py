from PySide6.QtWidgets import (
    QApplication,
    QWidget, 
    QMainWindow,
    QVBoxLayout
)
from src.TextEdit import TextEdit
from src.ConvertButton import ConvertButton
from src.CopyButton import CopyButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Dict To JSON")
        # self.setFixedSize(400, 300)
        self.button_is_checked = True
        self.input = TextEdit(f"{{'key1':'value1', 'key2':'value2'}}")
        self.output = TextEdit("Output")
        self.convert_button = ConvertButton(
            input=self.input, 
            output=self.output
        )
        self.copy_button = CopyButton(output=self.output)
        
        self.q_layout = QVBoxLayout()
        self.q_layout.addWidget(self.input)
        self.q_layout.addWidget(self.convert_button)
        self.q_layout.addWidget(self.output)
        self.q_layout.addWidget(self.copy_button)
        
        self.q_widget = QWidget()
        self.q_widget.setLayout(self.q_layout)
        
        self.setCentralWidget(self.q_widget)