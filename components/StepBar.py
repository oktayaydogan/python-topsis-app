from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel


class StepBar(QFrame):
    def __init__(self, screens):
        super().__init__()
        self.screen_labels = []
        self.screen_number_labels = []
        self.screens = screens
        self.current_screen = 0
        self.primary_color = "#065f46"
        self.secondary_color = "#9ca3af"
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        for i, screen in enumerate(self.screens.values(), start=1):
            screen_label = QLabel(f"{screen['title']}")
            screen_label.setStyleSheet(self.label_style(self.secondary_color))
            screen_number_label = QLabel(str(i))
            screen_number_label.setStyleSheet(self.circle_style(self.secondary_color))
            screen_layout = QHBoxLayout()
            screen_layout.addWidget(screen_number_label, alignment=Qt.AlignmentFlag.AlignCenter)
            screen_layout.addWidget(screen_label, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addLayout(screen_layout)
            self.screen_labels.append(screen_label)
            self.screen_number_labels.append(screen_number_label)

        self.setStyleSheet(self.get_style())

    def set_current_screen(self, screen):
        if screen < 0 or screen >= len(self.screens):
            return

        self.current_screen = screen
        self.update_screen_labels()

    def update_screen_labels(self):
        for i, label in enumerate(self.screen_labels):
            if i == self.current_screen:
                label.setStyleSheet(self.label_style(self.primary_color))
            else:
                label.setStyleSheet(self.label_style(self.secondary_color))

        for i, label in enumerate(self.screen_number_labels):
            if i == self.current_screen:
                label.setStyleSheet(self.circle_style(self.primary_color))
            else:
                label.setStyleSheet(self.circle_style(self.secondary_color))

    @staticmethod
    def get_style():
        return """
            StepBar {
                border: 1px solid #9ca3af;
                border-radius: 30px;
                margin: 50px 0;
            }
            QLabel {
                margin: 5px 10px 5px 0;
            }
        """

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
