from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from components import Button


class ValuesScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        self.setup_ui()
        self.initialize_table()
        self.populate_table()
        self.setup_next_button()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        widget_container = QWidget()
        self.layout.addWidget(widget_container, alignment=Qt.AlignmentFlag.AlignCenter)
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.space_label = QLabel()
        self.space_label.setFixedHeight(40)
        self.layout.addWidget(self.space_label, alignment=Qt.AlignmentFlag.AlignCenter)

    def initialize_table(self):
        if len(self.parent.matrix) > 0 and len(self.parent.criteria) != len(self.parent.matrix[0]):
            self.parent.matrix = [["" for _ in range(len(self.parent.criteria))] for _ in
                                  range(len(self.parent.alternatives))]


        self.table.setRowCount(len(self.parent.alternatives))
        self.table.setColumnCount(len(self.parent.criteria))
        self.table.setHorizontalHeaderLabels([criterion["criterion"] for criterion in self.parent.criteria])
        self.table.setVerticalHeaderLabels(self.parent.alternatives)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setWordWrap(True)
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #9ca3af;
                border-radius: 10px;
                padding: 10px;
            }
            QTableWidgetItem {
                padding: 10px;
                border-bottom: 1px solid #9ca3af;
            }
        """)

    def populate_table(self):
        if not self.parent.matrix:
            self.parent.matrix = [["" for _ in range(len(self.parent.criteria))] for _ in
                                  range(len(self.parent.alternatives))]

        for i in range(len(self.parent.alternatives)):
            for j in range(len(self.parent.criteria)):
                value = self.parent.matrix[i][j]  # Güncelleme gerekebilir
                if value is None:
                    value = ""
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)

        self.table.cellChanged.connect(self.cell_changed)


    def setup_next_button(self):
        self.next_button = Button("Analiz Yap", lambda: self.parent.next_screen(True))
        self.layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.next_button.setVisible(False)

        all_filled = self.check_all_filled()
        if all_filled:
            self.next_button.setVisible(True)

    def cell_changed(self, row, column):
        item = self.table.item(row, column)
        value = item.text()
        if not value.isdigit():
            item.setText("")
            self.parent.matrix[row][column] = ""
        else:
            self.parent.matrix[row][column] = value

        self.next_button.setVisible(False)
        if self.check_all_filled():
            self.next_button.setVisible(True)

    def check_all_filled(self):
        return all(
            all(self.parent.matrix[i][j] != "" for j in range(len(self.parent.criteria)))
            for i in range(len(self.parent.alternatives))
        )
