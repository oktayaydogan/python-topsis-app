from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class Image(QLabel):
    def __init__(self, image_path):
        super().__init__()
        self.setPixmap(QPixmap(image_path))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 16px;
            }
        """)