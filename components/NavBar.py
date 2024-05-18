from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QFrame, QPushButton


class NavBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.primary_color = "#065f46"
        self.secondary_color = "#9ca3af"

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.back_button = QPushButton("Geri")
        self.back_button.clicked.connect(self.previous_screen)
        self.forward_button = QPushButton("İleri")
        self.forward_button.clicked.connect(self.next_screen)

        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)

        self.update_button_visibility()
        self.setStyleSheet("""
            QPushButton {
                margin: 0;
                font-size: 16px;
                border: 1px solid #9ca3af;
                border-radius: 10px;
                padding: 10px 15px;
            }
        """)

    def previous_screen(self):
        current_index = self.parent.stacked_widget.currentIndex()
        self.parent.step_bar.set_current_screen(current_index - 1)
        if current_index > 0:
            self.parent.stacked_widget.setCurrentIndex(current_index - 1)
        self.update_button_visibility()

    def next_screen(self):
        current_index = self.parent.stacked_widget.currentIndex()
        self.parent.step_bar.set_current_screen(current_index + 1)
        if current_index < self.parent.stacked_widget.count() - 1:
            self.parent.stacked_widget.setCurrentIndex(current_index + 1)
        self.update_button_visibility()

    def update_button_visibility(self):
        current_index = self.parent.stacked_widget.currentIndex()
        self.back_button.setVisible(current_index > 0)
        self.forward_button.setVisible(current_index < self.parent.stacked_widget.count() - 1 & current_index != 0)

    @staticmethod
    def circle_style(color):
        return f"""
            border: 1px solid {color};
            border-radius: 15px;
            padding: 5px;
            min-width: 20px;
            min-height: 20px;
            font-size: 16px;
            qproperty-alignment: 'AlignCenter';
            margin-right: 0px;
            color: {color};
        """

    @staticmethod
    def label_style(color):
        return f"""
            color: {color};
            font-size: 16px;
        """
