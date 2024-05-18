from . import Input
from . import Button

from PyQt6.QtWidgets import QWidget, QHBoxLayout


class ButtonInput(QWidget):
    def __init__(self, placeholder, button_text, button_callback, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()

        self.input = Input(placeholder, width=300)
        layout.addWidget(self.input)

        self.button = Button(button_text, button_callback, width=70)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_input(self):
        return self.input.text()

    def set_input(self, text):
        self.input.setText(text)

    def clear_input(self):
        self.input.clear()
