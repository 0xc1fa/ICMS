# This Python file uses the following encoding: utf-8
import PySide6.QtCore as QtCore
from PySide6.QtCore import Qt, QRectF, QPoint, QTimer, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QGraphicsDropShadowEffect,
    QFrame,
)
from PySide6.QtGui import (
    QPalette,
    QColor,
    QPainter,
    QBrush,
    QPen,
    QPainterPath,
    QAction,
    QPixmap,
    QImage,
)
import qtawesome as qta
import cv2
import numpy as np

class StyledLabel(QLabel):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.setFixedHeight(35)
        self.setStyleSheet("""
            QLabel {
                margin: 0;
                font-size: 25pt;
                background-color: transparent;
                border: none;
                text-align: center;
                color: #666666;
            }
        """)


class StyledLoginButton(QPushButton):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.disabled = False
        self.setStyleSheet("""
            QPushButton {
                margin: 0;
                background-color: #8ec63f;
                border-radius: 5px;
                color: #111111;
                padding: 10px;
                border: none
            }
            QPushButton:hover {
                background-color: #7db52e;
            }
            QPushButton:pressed {
                background-color: #8ec63f;
            }
        """)
    
    def toggle(self):
        if self.disabled:
            self.enable()
        else:
            self.disable()
        self.disabled = not self.disabled
    
    def disable(self):
        self.setText("Cancel")
        self.setStyleSheet("""
            QPushButton {
                margin: 0;
                background-color: #aaaaaa;
                border-radius: 5px;
                color: #111111;
                padding: 10px;
                border: none
            }
            QPushButton:hover {
                background-color: #999999;
            }
            QPushButton:pressed {
                background-color: #aaaaaa;
            }
        """)
        
    def enable(self):
        self.setText("LOG IN")
        self.setStyleSheet("""
            QPushButton {
                margin: 0;
                background-color: #8ec63f;
                border-radius: 5px;
                color: #111111;
                padding: 10px;
                border: none
            }
            QPushButton:hover {
                background-color: #7db52e;
            }
            QPushButton:pressed {
                background-color: #8ec63f;
            }
        """)


class StyledButton(QPushButton):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.setStyleSheet("""
            QPushButton {
                margin: 0;
                background-color: white;
                border-radius: 5px;
                color: #111111;
                padding: 10px;
                border-color: #aaaaaa;
            }
            QPushButton:hover {
                background-color: #ade85f;
            }
            QPushButton:pressed {
                background-color: #8ec63f;
            }
        """)

class SyledLineEdit(QLineEdit):
    def __init__(self, *argv):
        super().__init__()
        self.setStyleSheet("""
            QLineEdit {
                margin: 0;
                background-color: #ffffff;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                color: #333;
                padding: 10px;
            }
            QLineEdit:hover {
                border: 1px solid #8ec63f;
            }
            QLineEdit:pressed {
                background-color: #4f4f4f;
                border: 1px solid #4f4f4f;
            }
        """)
        
    def toggle(self):
        if self.isEnabled():
            self.setEnabled(False)
        else:
            self.setEnabled(True)


class LoginSectionRight(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.bgimage = QPixmap(image_path)
        self.image = QPixmap(image_path)
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.timer = QTimer()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        
        painter.drawPixmap(0, 0, self.width(), self.height(), self.image)
        
        overlay_color = QColor(255, 255, 255, 0)
        painter.fillRect(self.rect(), overlay_color)
        
    def toggle_camera(self):
        if self.timer.isActive():
            self.timer.stop()
            self.image = self.bgimage
            self.update()
            self.cap.release()
        else:
            self.capture_face()
            self.timer.start(20)
    
    def capture_face(self):
        self.cap = cv2.VideoCapture(0)
        
        if not self.cap.isOpened():
            print("Could not open camera!")
            return
        
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(20)
        
    def updateFrame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            x_start = (width - 400) // 2
            y_start = (height - 500) // 2
            cropped_frame = frame[y_start:y_start+500, x_start:x_start+400]
            
            cropped_frame = np.ascontiguousarray(cropped_frame)
            
            bytesPerLine = 3 * 400
            qImg = QImage(cropped_frame.data, 400, 500, bytesPerLine, QImage.Format_RGB888)
            self.image = QPixmap.fromImage(qImg)
            self.update()


class LoginSectionLeft(QWidget):
    
    login_singal = Signal()
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QWidget {
                background-color: #3498db;
                border: 1px solid #2f2f2f;
                color: #fff;
                padding: 5px;
            }
        """)
        
        layout = QVBoxLayout()
        
        self.setFixedWidth(300)
        self.setFixedHeight(500)
        self.title = StyledLabel("WELCOME BACK...")
        self.username_field = SyledLineEdit(self)
        logo_action = QAction(self)
        logo_action.setIcon(qta.icon("fa.home", color='gray'))
        self.username_field.addAction(logo_action, QLineEdit.LeadingPosition)
        self.login_button = StyledLoginButton("LOG IN", self)
        self.faq_button = StyledButton("FAQ", self)
        self.contectus_button = StyledButton("Contect Us", self)
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background-color: none; border-color: #888888; border-top: none; border-left: none; border-right: none; margin: 0 40px;")
        layout.addStretch()
        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.username_field)
        layout.addWidget(self.login_button)
        layout.addWidget(separator)
        layout.addWidget(self.faq_button)
        layout.addWidget(self.contectus_button)
        layout.addStretch()
        layout.setSpacing(15)
        
        self.login_button.clicked.connect(self.login_singal.emit)
        
        self.setLayout(layout)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        rect_width = 300
        rect_height = 500

        top_left_x = (self.width() - rect_width) / 2
        top_left_y = (self.height() - rect_height) / 2

        rect = QRectF(top_left_x, top_left_y, rect_width, rect_height)
        path = QPainterPath()
        # path.addRoundedRect(rect, 15, 15)
        path.addRoundedRect(rect, 0, 0)
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawPath(path)
        
        
class LoginSection(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("border-radius: 5px;")
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        
        self.setFixedWidth(700)
        self.setFixedHeight(500)
        layout = QHBoxLayout()
        login_section_left = LoginSectionLeft()
        login_section_right = LoginSectionRight("public/images/retro-vaporwave-cropped.png")
        layout.addWidget(login_section_left)
        layout.addWidget(login_section_right)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        login_section_left.login_singal.connect(login_section_right.toggle_camera)
        login_section_left.login_singal.connect(login_section_left.login_button.toggle)
        login_section_left.login_singal.connect(login_section_left.username_field.toggle)
        self.draw_shadow()
        
    def draw_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(100)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            LoginPage {
                background-color: #2f2f2f";
            }
        """)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        
        layout = QHBoxLayout()
        login_section = LoginSection()
        layout.setSpacing(0)
        layout.addWidget(login_section)
        layout.setSpacing(0)
        self.setLayout(layout)
