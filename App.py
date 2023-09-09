# This Python file uses the following encoding: utf-8
import sys
import os

from dotenv import load_dotenv

from providers.DatabaseProvider import DatabaseProvider
from providers.UserProvider import UserProvider
from components.Sidebar import Sidebar
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QHBoxLayout,
    QWidget,
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
        self.pages = QStackedWidget(self)
        self.login_page = LoginPage()
        # self.login_page.setStyleSheet("background-image: url(./assets/photo01@750.jpg); background-attachment: fixed")
        self.main_page = MainPage()
        self.pages.addWidget(self.login_page)
        self.pages.addWidget(self.main_page)
        self.pages.setCurrentIndex(0)  # set login page as default page
        layout.addWidget(self.pages)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    load_dotenv()
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
