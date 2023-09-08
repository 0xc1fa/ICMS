from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QVBoxLayout,
    QWidget,
    QLabel,
    QStackedWidget
)


class MainContent(QStackedWidget):
    def __init__(self):
        super().__init__()
        
        self.addWidget(QLabel("Home Page"))
        self.addWidget(QLabel("Settings Page"))
        self.addWidget(QLabel("About Page"))
    
    def display_content(self, i):
        self.setCurrentIndex(i)
