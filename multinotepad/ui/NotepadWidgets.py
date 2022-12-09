from PyQt5.QtWidgets import QSpacerItem, QPushButton, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import QWidget, QInputDialog, QAction, QMenu, QMessageBox
from PyQt5 import QtCore

from .TextWidgets import TextField

Q_SIZE_POLICY_MIN = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)


class NotepadsBar(QWidget):
    def __init__(self, text_box: TextField, *args, **kwargs) -> None:
        super(NotepadsBar, self).__init__(*args, **kwargs)
        self.main_notepad_index: int = 0
        self._notepads_content: list[str] = []
        self.text_box = text_box

        self._main_layout = QHBoxLayout()
        self.setSizePolicy(Q_SIZE_POLICY_MIN)
        self.setLayout(self._main_layout)

        self.new_notepad_button = QPushButton("+")
        self.new_notepad_button.clicked.connect(self._new_notepad_button)
        self.new_notepad_button.setMaximumWidth(
            self.new_notepad_button.height()
        )
        self._main_layout.addWidget(
            self.new_notepad_button, alignment=QtCore.Qt.AlignLeft
        )

        self.notepads_bar_widget = QWidget()
        self.notepads_bar_layout = QHBoxLayout()
        self.notepads_bar_widget.setLayout(self.notepads_bar_layout)
        self._main_layout.addWidget(self.notepads_bar_widget)

        self._main_layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self.create_notepad_button("NewNotepad")

    def _new_notepad_button(self) -> None:

        file_name, done = QInputDialog.getText(
            self,
            "Creating new notepad",
            "Notepad name:"
        )

        if done and file_name != "":
            self.create_notepad_button(file_name, "")

    def create_notepad_button(
            self, button_name: str, text: str = "", first_button: bool = False
            ) -> None:

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

        self._notepads_content.append(text)

        if first_button:
            clear_plain_text = False
        else:
            clear_plain_text = True

        self._update_notepad_buttons(
            self.notepads_bar_layout.count() - 1, clear_plain_text
            )

    def _handle_right_click(self, button: QPushButton) -> None:
        point = button.pos()
        point.setX(point.x()//2)
        point.setY(point.y()//2)

        notepad_button_menu = self._create_notepad_button_menu(button)
        notepad_button_menu.exec_(button.mapToGlobal(point))

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

    def _delete_notepad_button(self, button: QPushButton) -> None:
        """
        Delete 'notepad' button,
        update 'notepad' buttons colors and plain text.

        Input:
         * button: QPushButton - button to delete
        """
        delete_message = QMessageBox()

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
                del self._notepads_content[b_index]
                button.setParent(None)

                first_button_not_the_only: bool = (
                    b_index == 0 != len(self._notepads_content)
                )

                the_only_button: bool = (
                    b_index == 0 == len(self._notepads_content)
                )

                not_first_button_not_the_only: bool = (
                    0 != b_index <= len(self._notepads_content) != 0
                )

                not_first_button_the_only: bool = (
                    b_index != 0 == len(self._notepads_content)
                )

                if not_first_button_not_the_only:
                    self.main_notepad_index -= 1

                    new_main_button = self.notepads_bar_layout. \
                        itemAt(b_index-1).widget()

                    self._change_notepad(new_main_button, False)

                elif not_first_button_the_only:
                    print("[!] NOT_FIRST_BUTTON_THE_ONLY")  # never used?
                    self.main_notepad_index += 1

                    new_main_button = self.notepads_bar_layout. \
                        itemAt(b_index+1).widget()

                    self._change_notepad(new_main_button, False)

                elif the_only_button:
                    self.text_box.setPlainText("")
                    self.text_box.setDisabled(True)

                elif first_button_not_the_only:
                    self.main_notepad_index = 0

                    new_main_button = self.notepads_bar_layout. \
                        itemAt(0).widget()

                    self._change_notepad(new_main_button, False)

                else:
                    print("[!] A NEW OPTION")  # exists?

                return

    def _change_notepad(
            self,
            button: QPushButton,
            save_old: bool = True
            ) -> None:

        if save_old:
            self._notepads_content[self.main_notepad_index] = \
                self.text_box.toPlainText()

        notepads_count = self.notepads_bar_layout.count()
        for index in range(notepads_count):
            tmp_widget = self.notepads_bar_layout.itemAt(index).widget()
            if tmp_widget is button:
                tmp_widget.setStyleSheet("background-color : lightgray")
                self.text_box.setPlainText(self._notepads_content[index])
                self.main_notepad_index = index
            elif type(tmp_widget) == QPushButton:
                tmp_widget.setStyleSheet("")

    def _update_notepad_buttons(
            self,
            button_to_be_painted: int,
            clear_plain_text: bool = True
            ) -> None:
        """
        Update buttons colors and text content.
        """

        if clear_plain_text:
            self._notepads_content[self.main_notepad_index] = \
                self.text_box.toPlainText()

        notepads_count = self.notepads_bar_layout.count()
        for index in range(notepads_count):
            tmp_widget = self.notepads_bar_layout.itemAt(index).widget()
            if type(tmp_widget) == QPushButton:
                if index == button_to_be_painted:
                    tmp_widget.setStyleSheet("background-color : lightgray")
                    self.text_box.setPlainText(self._notepads_content[index])
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

    def get_notepads_count(self) -> int:
        return self.notepads_bar_layout.count()

    def get_notepad_button(self, index: int) -> QPushButton:
        return self.notepads_bar_layout.itemAt(index).widget()

    def get_notepads_content(self) -> dict[str, str]:
        content = {}

        for index in range(self.get_notepads_count()):
            notepad_name = self.get_notepad_button(index).text()

            notepad_content = self._notepads_content[index]
            content[notepad_name] = notepad_content

        return content

    def clear_bar(self) -> None:
        notepads_count = self.get_notepads_count()
        for _ in range(notepads_count):
            b_to_delete = self.get_notepad_button(0)
            b_to_delete.setParent(None)
        self._notepads_content = []
