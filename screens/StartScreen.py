from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtCore import Qt
from components import Alert, Button, Input, Image


class StartScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        widget_container = QWidget()
        widget_layout = QVBoxLayout(self)
        widget_container.setLayout(widget_layout)

        layout = QVBoxLayout(self)
        layout.addWidget(widget_container, alignment=Qt.AlignmentFlag.AlignCenter)

        self.image_label = Image("assets/logo.png")
        widget_layout.addWidget(self.image_label)

        self.space_label = QLabel()
        self.space_label.setFixedHeight(40)
        widget_layout.addWidget(self.space_label)

        self.project_name_input = Input("Proje Adı", self.parent.project_name)
        widget_layout.addWidget(self.project_name_input)

        self.save_button = Button("Kaydet", self.save_project_name)
        widget_layout.addWidget(self.save_button)

    def save_project_name(self):
        project_name = self.project_name_input.text()
        if not project_name:
            Alert.show("Hata", "Proje adı boş bırakılamaz!")
            return

        self.parent.project_name = project_name
        if self.parent is not None and hasattr(self.parent, 'change_screen') and callable(self.parent.change_screen):
            self.parent.next_screen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.save_project_name()
        else:
            super().keyPressEvent(event)
