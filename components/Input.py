from PyQt6.QtWidgets import QLineEdit


class Input(QLineEdit):
    def __init__(self, placeholder_text, value="", width=380, height=40):
        super().__init__()
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setPlaceholderText(placeholder_text)
        self.setText(value)
        self.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #000000;
                border: 1px solid #9ca3af;
                border-radius: 5px;
                padding: 5px;
            }
        """)
