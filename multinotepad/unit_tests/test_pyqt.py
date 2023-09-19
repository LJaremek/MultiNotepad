"""
TODO:
    * Add testing buttons colorus in "test_new_notepad_*".
        This shit does not work, always is the same numbers:
            from PyQt5.QtGui import QPalette
            notepads_count = self.notepads_bar_layout.count()
            for index in range(notepads_count):
                tmp_widget = self.notepads_bar_layout.itemAt(index).widget()
                print(index, tmp_widget.palette().color(
                    tmp_widget.backgroundRole()).getRgb()
                    )
"""
from PyQt5.QtCore import Qt
import pytest

from ..run_app import MainWindow


@pytest.fixture
def app(qtbot) -> MainWindow:
    app = MainWindow()
    qtbot.addWidget(app)
    return app


def test_empty_start_app(app: MainWindow) -> None:
    assert app._tmp_notepads_content == {}
    assert app.notepads_bar.notepads_bar_layout.count() == 1
    assert app.notepads_bar._notepads_content[0] == ""


def test_new_notepad_1(app: MainWindow, qtbot) -> None:
    """
    1. Start app
    2. Press "+" (new button)
    3. Set notepad name "new_tab248"
    """
    def get_file_name_mock(*args) -> tuple[str, bool]:
        return "new_tab248", True

    app.notepads_bar._get_file_name = get_file_name_mock

    assert app.notepads_bar.notepads_bar_layout.count() == 1

    qtbot.mouseClick(
        app.notepads_bar.new_notepad_button,
        Qt.LeftButton
        )

    assert app.notepads_bar.notepads_bar_layout.count() == 2
    assert app.notepads_bar._notepads_content[0] == ""
    assert app.notepads_bar._notepads_content[1] == ""


def test_new_notepad_2(app: MainWindow, qtbot) -> None:
    """
    1. Start app
    2. Write text "aAa"
    3. Press "+" (new button)
    4. Set notepad name "new_tab248"
    """
    def get_file_name_mock(*args) -> tuple[str, bool]:
        return "new_tab248", True

    app.notepads_bar._get_file_name = get_file_name_mock

    assert app.notepads_bar.notepads_bar_layout.count() == 1
    assert app.notepads_bar._notepads_content[0] == ""

    app.text_box.insertPlainText("aAa")

    qtbot.mouseClick(
        app.notepads_bar.new_notepad_button,
        Qt.LeftButton
        )

    assert app.notepads_bar.notepads_bar_layout.count() == 2
    assert app.notepads_bar._notepads_content[0] == "aAa"
    assert app.notepads_bar._notepads_content[1] == ""


def test_new_notepad_3(app: MainWindow, qtbot) -> None:
    """
    1. Start app
    2. Press "+" (new button)
    3. Set notepad name "new_tab248"
    4. Write text "aAa"
    5. Back to first tab
    """
    def get_file_name_mock(*args) -> tuple[str, bool]:
        return "new_tab248", True

    app.notepads_bar._get_file_name = get_file_name_mock

    assert app.notepads_bar.notepads_bar_layout.count() == 1
    assert app.notepads_bar._notepads_content[0] == ""

    qtbot.mouseClick(
        app.notepads_bar.new_notepad_button,
        Qt.LeftButton
        )

    app.text_box.insertPlainText("aAa")

    qtbot.mouseClick(
        app.notepads_bar.notepads_bar_layout.itemAt(0).widget(),
        Qt.LeftButton
        )

    assert app.notepads_bar.notepads_bar_layout.count() == 2
    assert app.notepads_bar._notepads_content[0] == ""
    assert app.notepads_bar._notepads_content[1] == "aAa"
