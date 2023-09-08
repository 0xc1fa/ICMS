# This Python file uses the following encoding: utf-8
import sys
from components.Sidebar import Sidebar
from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
)
from components.HomeSection import HomeSection
from components.HistorySection import HistorySection
from components.SettingsSection import SettingsSection

class AnimatedLineEdit(QWidget):
    def __init__(self, label, *argv):
        self.label = QLabel("")
        self.line_edit = QLineEdit(*argv)


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        self.username_field = AnimatedLineEdit("Username", self)
        self.login_button = QPushButton("Login")
                
        layout.addWidget(self.username_field, 1)
        layout.addWidget(self.login_button, 4)
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(0)
        
        self.setLayout(layout)
