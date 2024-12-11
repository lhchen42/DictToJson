from PySide6.QtWidgets import (
    QApplication
)
from src.MainWindow import MainWindow
    
app = QApplication([])

window = MainWindow()
window.show()

app.exec()