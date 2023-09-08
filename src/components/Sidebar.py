import sys

from PySide6.QtCore import Signal, QRect, QPropertyAnimation
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QStackedWidget,
    QPushButton,
)
from PySide6.QtGui import QPalette, QColor
import qtawesome as qta


class SidebarButton(QPushButton):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.setFixedHeight(40)
        self.setStyleSheet(
            '''
            QPushButton {
                background-color: transparent;
                text-align: left;
                color: white;
                font-size: 16px;
                padding: 10px 10px 10px 0 ;
                border: none;
                padding-left: 15px;
                transition: 2s;
            }
            
            QPushButton:hover {
                background-color: rgb(60, 60, 60);;
            }
            ''')
        
class SidebarIcon(QLabel):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.setStyleSheet(
            '''
            background-color: transparent;
            text-align: left;
            color: white;
            font-size: 16px;
            '''
        )

class Sidebar(QWidget):
    
    home_singal = Signal()
    history_singal = Signal()
    settings_singal = Signal()
    
    def __init__(self):
        super().__init__()
        
        self.collasped = False
        self.setFixedWidth(150)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(50, 50, 50))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
        # icon = SidebarIcon("ICON")
        # icon.setAlignment(Qt.AlignCenter)
        self.home_button = SidebarButton(qta.icon("fa.home", color='white'), "Home")
        self.history_button = SidebarButton(qta.icon("fa.history", color='white'), "History")
        self.settings_button = SidebarButton(qta.icon("fa.cog", color='white'), "Settings")
        
        self.home_button.clicked.connect(self.home_singal.emit)
        self.history_button.clicked.connect(self.history_singal.emit)
        self.settings_button.clicked.connect(self.settings_singal.emit)
        
        toggle_button = SidebarButton(qta.icon("fa.columns", color="white"), '')
        toggle_button.clicked.connect(self.switch_sidebar)
        
        
        layout = QVBoxLayout()
        # layout.addWidget(icon)
        layout.addWidget(self.home_button)
        layout.addWidget(self.history_button)
        layout.addWidget(self.settings_button)   
        layout.addStretch()
        layout.addWidget(toggle_button)
        layout.setSpacing(0) 
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        
    def switch_sidebar(self):
        if self.collasped:
            self.setFixedWidth(150)
            for element, text in (
                (self.home_button, "Home"),
                (self.history_button, "History"),
                (self.settings_button, "Settings")
            ):
                element.setText(text) 
            self.collasped = False
        else:
            self.setFixedWidth(50)
            for element in (self.home_button, self.history_button, self.settings_button):
                element.setText("") 
            self.collasped = True
