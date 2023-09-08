# This Python file uses the following encoding: utf-8
import sys
from components.Sidebar import Sidebar
from components.MainContent import MainContent
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QStackedWidget
)
from components.HomePage import HomePage
from components.HistoryPage import HistoryPage
from components.SettingsPage import SettingsPage


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ICMS")
        self.setGeometry(100, 100, 800, 600)

        
        main_layout = QHBoxLayout()
        self.sidebar = Sidebar()
        self.pages = QStackedWidget(self)
        self.sidebar.home_singal.connect(lambda: self.pages.setCurrentIndex(0))
        self.sidebar.history_singal.connect(lambda: self.pages.setCurrentIndex(1))
        self.sidebar.settings_singal.connect(lambda: self.pages.setCurrentIndex(2))
        self.home_page = HomePage()
        self.history_page = HistoryPage()
        self.settings_page = SettingsPage()
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.history_page)
        self.pages.addWidget(self.settings_page)
        
        # self.sidebar.currentRowChanged.connect(self.main_content.display_content)
        
        main_layout.addWidget(self.sidebar, 1)
        main_layout.addWidget(self.pages, 4)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
