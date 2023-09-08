from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
)

class HomePage(QWidget):
    def __init__(self, *argv):
        super().__init__(*argv)
        
        label = QLabel("Home Page")
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
