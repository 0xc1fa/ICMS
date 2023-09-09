from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
)

class HomeSection(QWidget):
    def __init__(self, *argv):
        super().__init__(*argv)
        name = ""
        label = QLabel("Home Page")
        welcomeback_label = QLabel("Welcome back, {name}")
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
