from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
)

class HistoryPage(QWidget):
    def __init__(self, *argv):
        super().__init__(*argv)
        
        label = QLabel("History Page")
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
