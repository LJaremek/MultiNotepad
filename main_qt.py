from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import QPlainTextEdit, QPushButton, QSpacerItem
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtWidgets import QMenu, QAction
# from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore

Q_SIZE_POLICY_MAX = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
Q_SIZE_POLICY_MIN = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.main_notepad_index: int = 0
        self.notepads_content: list[str] = []
        self.project_name: str = "New MN"

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self._create_text_box()
        self._create_menu_bar()
        self._create_notepads_bar()

        self.setWindowTitle(f"{self.project_name} - MultiNotepad")

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
        self.text_box.textChanged.connect(self._text_change)
        self.text_box.setDisabled(True)
        self.main_layout.addWidget(self.text_box)

    def _text_change(self) -> None:
        self.setWindowTitle(f"{self.project_name} - MultiNotepad*")
        ...  # interact when text change

    def _delete_notepad_button(self, button: QPushButton) -> None:
        """READY"""
        delete_message = QMessageBox

        response = delete_message.question(
            self,
            "Deleting notepad!",
            "Are you sure to reset all the values?",
            delete_message.Yes | delete_message.No
        )

        if response == delete_message.No:
            return

        notepads_count = self.notepads_bar_layout.count()
        for b_index in range(notepads_count):
            tmp_button = self.notepads_bar_layout.itemAt(b_index).widget()
            if tmp_button is button:
                del self.notepads_content[b_index]
                button.setParent(None)

                if b_index == len(self.notepads_content) != 0:
                    self.main_notepad_index -= 1

                    last_button = self.notepads_bar_layout. \
                        itemAt(b_index-1).widget()

                    self._change_notepad(last_button, False)

                elif b_index == 0 == len(self.notepads_content):
                    self.text_box.setPlainText("")
                    self.text_box.setDisabled(True)

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
        self.bottom_bar_widget = QWidget()
        self.bottom_bar_layout = QHBoxLayout()
        self.bottom_bar_widget.setSizePolicy(Q_SIZE_POLICY_MIN)
        self.bottom_bar_widget.setLayout(self.bottom_bar_layout)

        self.new_notepad_button = QPushButton("+")
        self.new_notepad_button.clicked.connect(self._new_notepad_button)
        self.new_notepad_button.setMaximumWidth(
            self.new_notepad_button.height()
        )
        self.bottom_bar_layout.addWidget(
            self.new_notepad_button, alignment=QtCore.Qt.AlignLeft
        )

        self.notepads_bar_widget = QWidget()
        self.notepads_bar_layout = QHBoxLayout()
        self.notepads_bar_widget.setLayout(self.notepads_bar_layout)
        self.bottom_bar_layout.addWidget(self.notepads_bar_widget)

        self.bottom_bar_layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self._create_notepad_button("NewNotepad")

        # self.notepads_bar_layout.count()
        # self.notepads_bar_layout.itemAt(0).widget().text()
        # type(self.notepads_bar_layout.itemAt(2))
        # the last - PyQt5.QtWidgets.QSpacerItem

        self.main_layout.addWidget(self.bottom_bar_widget)

    def _file_open(self) -> None:
        ...  # QFileDialog.getExistingDirectory(self, "Select file to open", )

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

    def _create_notepad_button(self, button_name: str) -> None:
        new_button = QPushButton(button_name)
        new_button.clicked.connect(lambda: self._change_notepad(new_button))
        new_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        new_button.customContextMenuRequested.connect(
            lambda: self._handle_right_click(button=new_button)
        )

        self.notepads_bar_layout.insertWidget(
            self.notepads_bar_layout.count(),
            new_button,
            alignment=QtCore.Qt.AlignLeft
        )

        if not self.text_box.isEnabled():
            self.text_box.setEnabled(True)

        self.notepads_content.append("")

        self._update_notepad_buttons(
            self.notepads_bar_layout.count() - 1,
            new_button=True
            )

    def _change_notepad(
            self,
            button: QPushButton,
            save_old: bool = True
            ) -> None:

        if save_old:
            self.notepads_content[self.main_notepad_index] = \
                self.text_box.toPlainText()

        notepads_count = self.notepads_bar_layout.count()
        for index in range(notepads_count):
            tmp_widget = self.notepads_bar_layout.itemAt(index).widget()
            if tmp_widget is button:
                tmp_widget.setStyleSheet("background-color : lightgray")
                self.text_box.setPlainText(self.notepads_content[index])
                self.main_notepad_index = index
            elif type(tmp_widget) == QPushButton:
                tmp_widget.setStyleSheet("")

    def _update_notepad_buttons(
            self,
            button_to_be_painted: int,
            new_button: bool = False
            ) -> None:
        """
        Update buttons colors and text content.
        """

        self.notepads_content[self.main_notepad_index] = \
            self.text_box.toPlainText()

        notepads_count = self.notepads_bar_layout.count()
        for index in range(notepads_count):
            tmp_widget = self.notepads_bar_layout.itemAt(index).widget()
            if type(tmp_widget) == QPushButton:
                if index == button_to_be_painted:
                    tmp_widget.setStyleSheet("background-color : lightgray")
                    self.text_box.setPlainText(self.notepads_content[index])
                    self.main_notepad_index = index
                else:
                    tmp_widget.setStyleSheet("")

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
            self._create_notepad_button(file_name)


def main():
    app = QApplication([])

    window = MainWindow()
    window.setFixedSize(900, 700)
    window.show()

    app.exec_()
    exit()


if __name__ == "__main__":
    main()
