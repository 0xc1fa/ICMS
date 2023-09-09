# This Python file uses the following encoding: utf-8
import PySide6.QtCore as QtCore
from PySide6.QtCore import Qt, QRectF, QPoint
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
    QPixmap
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



class LoginSectionRight(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image = QPixmap(image_path)
        self.setFixedWidth(400)
        self.setFixedHeight(500)

    # def paintEvent(self, event):
    #     painter = QPainter(self)
        
    #     # Draw the image
    #     painter.drawPixmap(0, 0, self.width(), self.height(), self.image)
        
    #     # Draw the semi-transparent white overlay
    #     overlay_color = QColor(255, 255, 255, 128)  # The last value (128) is the alpha (transparency)
    #     painter.fillRect(self.rect(), overlay_color)
        
    def capture_face(self):
        self.cap = cv2.VideoCapture(0)
        
        if not self.cap.isOpened():
            print("Could not open camera!")
            return
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(20)
        
    def updateFrame(self):
        ret, frame = self.cap.read() # Read a frame from the camera
        if ret:
            # Convert the frame to RGB since OpenCV uses BGR format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.image.setPixmap(pixmap)


class LoginSectionLeft(QWidget):
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
        self.title = StyledLabel("Welcome Back...")
        self.username_field = SyledLineEdit(self)
        logo_action = QAction(self)
        logo_action.setIcon(qta.icon("fa.home", color='gray'))
        self.username_field.addAction(logo_action, QLineEdit.LeadingPosition)
        # self.username_field = AnimatedLineEdit("Username", self)
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
        
        self.setLayout(layout)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        rect_width = 300
        rect_height = 500

        # Calculate the position to center the rectangle
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
        login_section_right = LoginSectionRight("src/assets/photo01@750.jpg")
        layout.addWidget(login_section_left)
        layout.addWidget(login_section_right)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        
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
        
        # palette = QPalette()
        # palette.setColor(QPalette.Window, QColor(20, 20, 20))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)
        
        
        layout = QHBoxLayout()
        login_section = LoginSection()
        layout.setSpacing(0)
        # layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(login_section)
        layout.setSpacing(0)
        self.setLayout(layout)
        
