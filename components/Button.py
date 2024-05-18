from PyQt6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, text, function, width=380, height=40):
        super().__init__(text)
        self.function = function
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.clicked.connect(self.function)
        self.setStyleSheet("""
            QPushButton {
                background-color: #065f46;
                color: #FFFFFF;
                border-radius: 5px;
                padding: 5px;
            }
        """)