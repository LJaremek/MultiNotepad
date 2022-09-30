from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy
from PyQt5.QtWidgets import QFileDialog

from .mn_format import open_mn_file
from .ui.TextWidgets import TextField
from .ui.NotepadWidgets import NotepadsBar
from .ui.MenuBar import wear_menubar

Q_SIZE_POLICY_MAX = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
Q_SIZE_POLICY_MIN = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """READY"""
        super(MainWindow, self).__init__(*args, **kwargs)
        self.project_name: str = "New MN"

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.text_box = TextField(self._text_change)
        self.main_layout.addWidget(self.text_box)

        self.notepads_bar = NotepadsBar(self.text_box)
        self.main_layout.addWidget(self.notepads_bar)

        self.menu_bar = self.menuBar()
        wear_menubar(self)

        self.setWindowTitle(f"{self.project_name} - MultiNotepad")

        self.setCentralWidget(self.main_widget)

    def _text_change(self) -> None:
        self.setWindowTitle(f"{self.project_name} - MultiNotepad*")
        ...  # interact when text change

    def _file_open(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Select file to open", "", "*.mn"
            )

        files_data = open_mn_file(path)

        self.notepads_bar.clear_bar()

        first_button = True
        for file_name in files_data:
            file_content = files_data[file_name].file_content

            self.notepads_bar.create_notepad_button(
                file_name,
                file_content,
                first_button
                )

            first_button = False

    def _file_save(self) -> None:
        ...

    def _file_saveas(self) -> None:
        ...


def main():
    app = QApplication([])

    window = MainWindow()
    window.setFixedSize(900, 700)
    window.show()

    app.exec_()
    exit()
