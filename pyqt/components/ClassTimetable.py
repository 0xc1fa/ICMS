from PySide6.QtCore import (
    Qt,
    QDate
)

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QCalendarWidget
)
from PySide6.QtGui import (
    QPainter,
    QColor,
    QFont
)

import providers.DatabaseProvider as db 

class ClassTimetable(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.event_data = {
            QDate.currentDate(): "Today",
            QDate(2023, 9, 11): "Database class",  # just a demo data, remove it after finish
        }
    
    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        if date in self.event_data:
            painter.save()

            painter.setPen(QColor(0, 128, 0))  # Setting the text color to green
            font = painter.font()
            font.setPointSize(8)  # Setting font size to 8
            painter.setFont(font)
            
            custom_text = self.event_data[date]
            painter.drawText(rect, Qt.AlignCenter, "\n\n" + custom_text)
            
            painter.restore()

    def get_class_time(self):
        # TODO: implement this function to fetch the time table from the database
        # store the data in self.event_data
        db.init_connection()
        data = db.fetch_data("SELECT * FROM class_timetable")  # just a demo query
        ...

    