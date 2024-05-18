from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from utils import topsis


class ResultsScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.topsis = topsis.TOPSIS(self.parent.alternatives, self.parent.criteria, self.parent.matrix)
        self.result = self.topsis.run_topsis()
        self.calculations = self.topsis.get_all_calculations()

        self.table = QTableWidget()

        self.setup_ui()

    def setup_ui(self):
        self.table.setRowCount(len(self.parent.alternatives))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Alternatif", "Skor"])

        self.set_vertical_headers()
        self.populate_table()

        self.set_table_style()

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)

    def set_vertical_headers(self):
        self.table.setVerticalHeaderLabels([str(i + 1) for i in range(len(self.parent.alternatives))])

    def populate_table(self):
        for i in range(len(self.parent.alternatives)):
            alternative_item = self.create_table_item(self.result[i]['name'])
            score_item = self.create_table_item(str(self.result[i]['values']['score']))

            self.table.setItem(i, 0, alternative_item)
            self.table.setItem(i, 1, score_item)

    def create_table_item(self, text):
        item = QTableWidgetItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return item

    def set_table_style(self):
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
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
