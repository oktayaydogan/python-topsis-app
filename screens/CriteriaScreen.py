from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt6.QtCore import Qt
from components import Button, Input, Alert


class CriteriaScreen(QWidget):
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

        button_container = QHBoxLayout()
        widget_layout.addLayout(button_container)

        self.criterion_name_input = Input("Kriter Adı", width=220)
        button_container.addWidget(self.criterion_name_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.criterion_weight_input = Input("Ağırlık", width=70)
        button_container.addWidget(self.criterion_weight_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.save_button = Button("Ekle", self.add_criterion, 70)
        button_container.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.next_button = Button("İleri", self.next_screen)
        widget_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.next_button.setVisible(False)

    def create_table(self):
        table = QTableWidget()
        table.setRowCount(len(self.parent.criteria))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Kriter", "Ağırlık"])
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
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
        for i, criterion in enumerate(self.parent.criteria):
            self.table.setItem(i, 0, QTableWidgetItem(criterion["criterion"]))
            self.table.setItem(i, 1, QTableWidgetItem(str(criterion["weight"])))
            self.table.item(i, 0).setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.table.item(i, 1).setFlags(Qt.ItemFlag.ItemIsEnabled)

    def add_criterion(self):
        criterion_name = self.criterion_name_input.text()
        criterion_weight = self.criterion_weight_input.text()

        if not criterion_name or not criterion_weight:
            Alert.show("Hata", "Kriter adı ve ağırlık boş bırakılamaz!")
            return

        self.criterion_name_input.clear()
        self.criterion_weight_input.clear()

        self.parent.criteria.append({"criterion": criterion_name, "weight": criterion_weight, "type": "+"})

        self.add_table_row(criterion_name, criterion_weight)
        self.update_next_button_visibility()

    def add_table_row(self, criterion_name, criterion_weight):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        self.table.setItem(row_count, 0, QTableWidgetItem(criterion_name))
        self.table.setItem(row_count, 1, QTableWidgetItem(criterion_weight))
        self.table.item(row_count, 0).setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.table.item(row_count, 1).setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.add_criterion()
        else:
            super().keyPressEvent(event)

    def update_next_button_visibility(self):
        if len(self.parent.criteria) >= 0:
            self.next_button.setVisible(True)

    def next_screen(self):
        self.parent.next_screen()

