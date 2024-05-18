from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from components import Button, Alert, ButtonInput


class AlternativesScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        self.populate_table()
        self.update_next_button_visibility()

    def setup_ui(self):
        widget_container = QWidget()
        widget_layout = QVBoxLayout(self)
        widget_container.setLayout(widget_layout)

        layout = QVBoxLayout(self)
        layout.addWidget(widget_container, alignment=Qt.AlignmentFlag.AlignCenter)

        self.table = self.create_table()
        widget_layout.addWidget(self.table)

        self.space_label = QLabel()
        self.space_label.setFixedHeight(40)
        widget_layout.addWidget(self.space_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.alternative_name_input = ButtonInput("Alternatif Adı", "Ekle", self.add_alternative)
        widget_layout.addWidget(self.alternative_name_input)

        self.next_button = Button("İleri", self.next_screen)
        widget_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.next_button.setVisible(False)

    def create_table(self):
        table = QTableWidget()
        table.setRowCount(len(self.parent.alternatives))
        table.setColumnCount(1)
        table.setHorizontalHeaderLabels(["Alternatifler"])
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setVisible(False)
        table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #9ca3af;
                border-radius: 10px;
                padding: 10px;
            }
            QTableWidgetItem {
                padding: 10px;
                border-bottom: 1px solid #9ca3af;
                border-color: #9ca3af;
            }
        """)
        return table

    def populate_table(self):
        for i, alternative in enumerate(self.parent.alternatives):
            self.table.setItem(i, 0, QTableWidgetItem(alternative))
            self.table.item(i, 0).setFlags(Qt.ItemFlag.ItemIsEnabled)

    def add_alternative(self):
        alternative_name = self.alternative_name_input.get_input()

        if not alternative_name:
            Alert.show("Hata", "Alternatif adı boş bırakılamaz!")
            return

        self.alternative_name_input.clear_input()
        self.parent.alternatives.append(alternative_name)
        self.add_table_row(alternative_name)
        self.update_next_button_visibility()

    def add_table_row(self, alternative_name):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        self.table.setItem(row_count, 0, QTableWidgetItem(alternative_name))
        self.table.item(row_count, 0).setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.add_alternative()
        else:
            super().keyPressEvent(event)

    def update_next_button_visibility(self):
        self.next_button.setVisible(len(self.parent.alternatives) >= 1)

    def next_screen(self):
        self.parent.next_screen()
