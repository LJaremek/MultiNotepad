from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import QWidget, QAction, QPlainTextEdit, QPushButton
from PyQt5 import QtCore

Q_SIZE_POLICY_MAX = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("MultiNotepad")

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self._create_text_box()
        self._create_menu_bar()
        self._create_notepads_bar()

        self.setCentralWidget(self.main_widget)

    def _create_menu_bar(self) -> None:
        self.menu_bar = self.menuBar()

        self.menu_bar_file = self.menu_bar.addMenu("&File")

        open_file_action = QAction("Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self._file_open)
        self.menu_bar_file.addAction(open_file_action)

        save_file_action = QAction("Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self._file_save)
        self.menu_bar_file.addAction(save_file_action)

        saveas_file_action = QAction("Save As...", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self._file_saveas)
        self.menu_bar_file.addAction(saveas_file_action)

        self.menu_bar_edit = self.menu_bar.addMenu("&Edit")

        undo_action = QAction("Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.text_box.undo)
        self.menu_bar_edit.addAction(undo_action)

        redo_action = QAction("Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.text_box.redo)
        self.menu_bar_edit.addAction(redo_action)

        cut_action = QAction("Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.text_box.cut)
        self.menu_bar_edit.addAction(cut_action)

        copy_action = QAction("Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.text_box.copy)
        self.menu_bar_edit.addAction(copy_action)

        paste_action = QAction("Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.text_box.paste)
        self.menu_bar_edit.addAction(paste_action)

        select_action = QAction("Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.text_box.selectAll)
        self.menu_bar_edit.addAction(select_action)

    def _create_text_box(self) -> None:
        self.text_box = QPlainTextEdit()
        self.main_layout.addWidget(self.text_box)

    def _create_notepads_bar(self) -> None:
        self.notepads_bar_widget = QWidget()
        self.notepads_bar_layout = QHBoxLayout()
        self.notepads_bar_widget.setLayout(self.notepads_bar_layout)

        self.new_notepad_button = QPushButton("+")
        self.new_notepad_button.setMaximumWidth(
            self.new_notepad_button.height()
            )
        self.notepads_bar_layout.addWidget(
            self.new_notepad_button, alignment=QtCore.Qt.AlignLeft
            )

        self.main_layout.addWidget(self.notepads_bar_widget)

    def _file_open(self) -> None:
        ...

    def _file_save(self) -> None:
        ...

    def _file_saveas(self) -> None:
        ...


def main():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
    exit()


if __name__ == "__main__":
    main()
