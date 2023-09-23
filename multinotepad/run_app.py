from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QAction

from .tools.text_tools import get_file_name_from_path
from .mn_format import open_mn_file
from .mn_manager import MultiNotepadManager
from .ui.NotepadWidgets import NotepadsBar
from .ui.TextWidgets import TextField


class TemporaryBlocker:
    main_notepad_index = 0

    def get_notepad_content(self, index: int = 0) -> str:
        return ""

    def get_notepads_content(self) -> dict:
        return {}


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.project_name: str = "my notes"
        self.file_path: str = None

        self._mn_manager = MultiNotepadManager()

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # >>>>>> DELETE AFTER TESTING
        from PyQt5.QtWidgets import QPushButton
        from PyQt5 import QtCore
        b = QPushButton("Check")
        b.clicked.connect(lambda: print("CHECK:", self._mn_manager._content))
        b.setStyleSheet("background-color: red; color: white;")
        self.main_layout.addWidget(
            b,
            alignment=QtCore.Qt.AlignLeft
            )
        # <<<<<< DELETE AFTER TESTING

        self.notepads_bar: NotepadsBar = TemporaryBlocker()
        self.text_box = TextField(self._text_change_action)
        self.main_layout.addWidget(self.text_box)

        self.notepads_bar = NotepadsBar(self.text_box, self._mn_manager)
        self.main_layout.addWidget(self.notepads_bar)

        self.menu_bar = self.menuBar()
        self._set_up_menubar()

        self.setWindowTitle(f"{self.project_name} - MultiNotepad")
        self.setCentralWidget(self.main_widget)

    def __del__(self) -> None:
        del self._mn_manager
        del self.notepads_bar
        del self.text_box
        del self.main_layout

    def _set_up_menubar(self) -> None:
        menus: dict[str, tuple[tuple]] = {
            "&File": (
                ("Open file...", "Open file", self._file_open),
                ("Save", "Save current page", self._file_save),
                ("Save As...", "Save current page as", self._file_saveas)
            ),
            "&Edit": (
                ("Undo", "Undo last change", self.text_box.undo),
                ("Redo", "Redo last change", self.text_box.redo),
                ("Cut", "Cut selected text", self.text_box.cut),
                ("Copy", "Copy selected text", self.text_box.copy),
                ("Paste", "Paste from clipboard", self.text_box.paste),
                ("Select all", "Select all text", self.text_box.selectAll)
            )
        }

        for menu_name in menus:
            menu_tmp = self.menu_bar.addMenu(menu_name)
            actions = menus[menu_name]
            for action in actions:
                action_tmp = QAction(action[0], self)
                action_tmp.setStatusTip(action[1])
                action_tmp.triggered.connect(action[2])

                menu_tmp.addAction(action_tmp)

    def _get_current_notepad_index(self) -> int:
        return self.notepads_bar.main_notepad_index

    def _text_change_action(
            self,
            star: bool = True,
            check_contensts: bool = True
            ) -> None:

        notepad_index = self._get_current_notepad_index()
        notepad_content = self.text_box.toPlainText()

        self._mn_manager.update_notepad_content(
            new_content=notepad_content,
            index=notepad_index
            )

        # if check_contensts and self._tmp_notepads_content == \
        #         self.notepads_bar.get_notepads_content():
        #     return

        self.setWindowTitle(
            f"{self.project_name} - MultiNotepad" + ("*" if star else "")
            )

    def _file_open(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Select file to open", "", "*.mn"
            )

        if path == "":
            return

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

        self.project_name = get_file_name_from_path(path)
        self._text_change_action(False, False)

    def _file_save(self) -> None:

        if self.file_path is None:
            path, _ = QFileDialog.getSaveFileName(
                self, "Save as", self.project_name, "*.mn"
                )

            if path == "":
                return
            self.file_path = path

        self._mn_manager.save_mn_file(self.file_path)

        self.project_name = get_file_name_from_path(self.file_path)
        self._text_change_action(False, False)

    def _file_saveas(self) -> None:
        path, _ = QFileDialog.getSaveFileName(
            self, "Save as", self.project_name, "*.mn"
            )

        if path == "":
            return
        self.file_path = path

        self._mn_manager.save_mn_file(self.file_path)

        self.project_name = get_file_name_from_path(path)
        self._text_change_action(False, False)


def main():
    app = QApplication([])

    window = MainWindow()
    window.setFixedSize(900, 700)
    window.show()

    app.exec_()
    exit()
