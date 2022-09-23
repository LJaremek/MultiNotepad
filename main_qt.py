from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import QPlainTextEdit, QPushButton, QSpacerItem
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5 import QtCore

Q_SIZE_POLICY_MAX = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """READY"""
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
        """READY"""
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
        """READY"""
        self.text_box = QPlainTextEdit()
        self.main_layout.addWidget(self.text_box)

    def _delete_notepad_button(self, button: QPushButton) -> None:
        """READY"""
        delete_message = QMessageBox

        response = delete_message.question(
            self,
            "Deleting notepad!",
            "Are you sure to reset all the values?",
            delete_message.Yes | delete_message.No
        )

        if response == delete_message.Yes:
            notepads_count = self.notepads_bar_layout.count()
            for i in range(notepads_count):
                tmp_button = self.notepads_bar_layout.itemAt(i).widget()
                if tmp_button is button:
                    button.setParent(None)
                    return

    def _create_notepad_button_menu(self, button: QPushButton) -> QMenu:
        """READY"""
        notepad_button_menu = QMenu(self)

        rename_action = QAction("Rename", self)
        rename_action.triggered.connect(
            lambda: self._rename_notepad_button(button)
        )
        notepad_button_menu.addAction(rename_action)

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(
            lambda: self._delete_notepad_button(button)
        )
        notepad_button_menu.addAction(delete_action)

        return notepad_button_menu

    def _create_notepads_bar(self) -> None:
        self.notepads_bar_widget = QWidget()
        self.notepads_bar_layout = QHBoxLayout()
        self.notepads_bar_widget.setLayout(self.notepads_bar_layout)

        self.new_notepad_button = QPushButton("+")
        self.new_notepad_button.clicked.connect(self._new_notepad_button)
        self.new_notepad_button.setMaximumWidth(
            self.new_notepad_button.height()
        )
        self.notepads_bar_layout.addWidget(
            self.new_notepad_button, alignment=QtCore.Qt.AlignLeft
        )

        self.notepads_bar_layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self._create_new_notepad_button("NewNotepad")

        # self.notepads_bar_layout.count()
        # self.notepads_bar_layout.itemAt(0).widget().text()
        # type(self.notepads_bar_layout.itemAt(2))
        # the last - PyQt5.QtWidgets.QSpacerItem

        self.main_layout.addWidget(self.notepads_bar_widget)

    def _file_open(self) -> None:
        ...

    def _file_save(self) -> None:
        ...

    def _file_saveas(self) -> None:
        ...

    def _handle_right_click(self, button: QPushButton) -> None:
        point = button.pos()
        point.setX(point.x()//2)
        point.setY(point.y()//2)

        notepad_button_menu = self._create_notepad_button_menu(button)
        notepad_button_menu.exec_(button.mapToGlobal(point))

    def _create_new_notepad_button(self, button_name: str) -> None:

        new_button = QPushButton(button_name)
        new_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        new_button.customContextMenuRequested.connect(
            lambda: self._handle_right_click(button=new_button)
        )

        self.notepads_bar_layout.insertWidget(
            self.notepads_bar_layout.count() - 1,
            new_button,
            alignment=QtCore.Qt.AlignLeft
        )

    def _rename_notepad_button(self, button: QPushButton) -> None:
        new_file_name, done = QInputDialog.getText(
            self,
            "Renaming notepad",
            "New notepad name:"
        )

        if done and new_file_name != "":
            button.setText(new_file_name)

    def _new_notepad_button(self) -> None:

        file_name, done = QInputDialog.getText(
            self,
            "Creating new notepad",
            "Notepad name:"
        )

        if done and file_name != "":
            self._create_new_notepad_button(file_name)


def main():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
    exit()


if __name__ == "__main__":
    main()
