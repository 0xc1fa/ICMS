# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QStackedWidget
)
from PySide6.QtGui import QPalette, QColor

from components.Sidebar import Sidebar
from components.HomeSection import HomeSection
from components.HistorySection import HistorySection
from components.SettingsSection import SettingsSection


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        # palette = QPalette()
        # palette.setColor(QPalette.Window, QColor(20, 20, 20))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)
        
        layout = QHBoxLayout()
        self.sidebar = Sidebar()
        self.home_page = HomeSection()
        self.history_page = HistorySection()
        self.settings_page = SettingsSection()
        
        self.sections = QStackedWidget(self)
        self.sections.addWidget(self.home_page)
        self.sections.addWidget(self.history_page)
        self.sections.addWidget(self.settings_page)
        
        self.sidebar.home_singal.connect(lambda: self.sections.setCurrentIndex(0))
        self.sidebar.history_singal.connect(lambda: self.sections.setCurrentIndex(1))
        self.sidebar.settings_singal.connect(lambda: self.sections.setCurrentIndex(2))
                
        layout.addWidget(self.sidebar, 1)
        layout.addWidget(self.sections, 4)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self.setLayout(layout)
