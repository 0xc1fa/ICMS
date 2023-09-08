# This Python file uses the following encoding: utf-8
import sys
from components.Sidebar import Sidebar
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QVBoxLayout,
    QStackedWidget,
    QHBoxLayout,
    QWidget,
    QLabel,
    QStackedWidget
)

from components.MainPage import MainPage
from components.LoginPage import LoginPage


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ICMS")
        self.setGeometry(100, 100, 800, 600)

        
        layout = QHBoxLayout()
        # self.sidebar = Sidebar()
        self.pages = QStackedWidget(self)
        self.main_page = MainPage()
        self.pages.addWidget(self.main_page)
        # self.sidebar.home_singal.connect(lambda: self.pages.setCurrentIndex(0))
        # self.sidebar.history_singal.connect(lambda: self.pages.setCurrentIndex(1))
        # self.sidebar.settings_singal.connect(lambda: self.pages.setCurrentIndex(2))
        # self.home_page = HomeSection()
        # self.history_page = HistorySection()
        # self.settings_page = SettingsSection()
        # self.pages.addWidget(self.home_page)
        # self.pages.addWidget(self.history_page)
        # self.pages.addWidget(self.settings_page)
        
        # self.sidebar.currentRowChanged.connect(self.main_content.display_content)
        
        layout.addWidget(self.pages)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
