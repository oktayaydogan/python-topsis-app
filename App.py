import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget

from components import NavBar, StepBar
from screens import StartScreen, AlternativesScreen, CriteriaScreen, ValuesScreen, ResultsScreen


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TOPSIS Analizi Uygulaması")
        self.setMinimumSize(1000, 700)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setStyleSheet(
            "background-color: #fff;"
            "color: #000000;"
            "font-size: 16px;"
        )
        self.setWindowIcon(QIcon("assets/icon.png"))

        self.project_name = ""
        self.alternatives = []
        self.criteria = []
        self.matrix = {}
        self.screens = {}

        self.fill_values()
        self.setup_ui()

    def setup_ui(self):
        self.set_screens()
        self.first_screen = StartScreen(self)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.addWidget(self.first_screen)

        self.step_bar = StepBar(self.screens)
        self.nav_bar = NavBar(self)

        self.step_bar.set_current_screen(0)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.step_bar, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(self.nav_bar, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def change_screen(self, index, reload=False):
        if 0 <= index:
            screen_name = list(self.screens.keys())[index]
            screen_data = self.screens[screen_name]
            screen_instance = screen_data["component"](self)

            if self.stacked_widget.count() > index:
                self.stacked_widget.removeWidget(self.stacked_widget.widget(index))

            if reload:
                # remove screen from stacked widget
                self.stacked_widget.removeWidget(self.stacked_widget.widget(index + 1))

            self.stacked_widget.addWidget(screen_instance)
            self.stacked_widget.setCurrentWidget(screen_instance)
            self.nav_bar.update_button_visibility()
            self.step_bar.set_current_screen(index)

    def next_screen(self, reload=False):
        self.change_screen(self.step_bar.current_screen + 1)

    def prev_screen(self, reload=False):
        self.change_screen(self.step_bar.current_screen - 1)

    def set_screens(self):
        self.screens = {
            "StartScreen": {
                "title": "Proje Adı",
                "component": StartScreen,
                "completed": True
            },
            "AlternativesScreen": {
                "title": "Alternatifler",
                "component": AlternativesScreen,
                "completed": True
            },
            "CriteriaScreen": {
                "title": "Kriterler",
                "component": CriteriaScreen,
                "completed": True
            },
            "ValuesScreen": {
                "title": "Değerler",
                "component": ValuesScreen,
                "completed": False
            },
            "ResultsScreen": {
                "title": "Sonuçlar",
                "component": ResultsScreen,
                "completed": False
            },
        }

    def fill_values(self):
        self.project_name = "Otomasyon Sistemleri Karşılaştırma Analizi"

        self.alternatives = [
            "Promer",
            "Yüksek İnovasyon",
            "Prolojik",
            "Mertay",
            "3E Otomasyon",
            "Rovimek",
        ]

        self.criteria = [
            {"criterion": "Güvenlik", "weight": 30, "type": "+"},
            {"criterion": "Destek ve Bakım Hizmetleri", "weight": 19, "type": "+"},
            {"criterion": "Entegrasyon ve Uyum Yetenekleri", "weight": 18, "type": "+"},
            {"criterion": "Referanslar ve Müşteri Geri Bildirimleri", "weight": 14, "type": "+"},
            {"criterion": "Teknoloji ve Altyapı", "weight": 19, "type": "+"},
        ]

        self.matrix = [
            [10, 8, 7, 7, 8],
            [10, 7, 7, 8, 7],
            [9, 8, 5, 6, 6],
            [9, 6, 6, 9, 7],
            [9, 8, 6, 7, 6],
            [8, 7, 7, 6, 6],
        ]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
