from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QCalendarWidget
)

from components.ClassTimetable import ClassTimetable

class HomeSection(QWidget):
    def __init__(self, *argv):
        super().__init__(*argv)
        name = ""
        label = QLabel("Home Page")
        welcomeback_label = QLabel("Welcome back, {name}")
        calendar = ClassTimetable()
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        # layout.addWidget(welcomeback_label)
        layout.addWidget(calendar)
        self.setLayout(layout)
