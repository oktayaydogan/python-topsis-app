from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QDialogButtonBox


class Alert:
    @staticmethod
    def show(title, message):
        dialog = QDialog()
        dialog.setWindowTitle(title)

        layout = QVBoxLayout()
        dialog.setLayout(layout)

        message_label = QLabel(message)
        layout.addWidget(message_label)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)

        dialog.setStyleSheet("""
            QDialog {
                background-color: #FFFFFF;
                color: #000000;
                font-size: 16px;
            }
            QLabel {
                color: #000000;
                font-size: 16px;
            }
            QDialogButtonBox {
                background-color: #FFFFFF;
                color: #000000;
                font-size: 16px;
            }
            QPushButton {
                background-color: #065f46;
                color: #FFFFFF;
                border-radius: 5px;
                padding: 5px;
            }
            """)

        dialog.exec()
