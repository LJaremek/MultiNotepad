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
# from PyQt5.QtCore import Qt
import pytest

from ..run_app import MainWindow


class TestClass:
    @pytest.fixture
    def app(self, qtbot) -> MainWindow:
        app = MainWindow()
        qtbot.addWidget(app)
        return app

    def test_empty_start_app(self, app: MainWindow) -> None:
        assert app.notepads_bar.notepads_bar_layout.count() == 1
        assert app._mn_manager.size() == 1

        del app


# def test_new_notepad_1(app: MainWindow, qtbot) -> None:
#     """
#     1. Start app
#     2. Press "+" (new button)
#     3. Set notepad name "new_tab248"
#     """
#     def get_file_name_mock(*args) -> tuple[str, bool]:
#         return "new_tab248", True

#     app.notepads_bar._get_file_name = get_file_name_mock

#     assert app.notepads_bar.notepads_bar_layout.count() == 1

#     qtbot.mouseClick(
#         app.notepads_bar.new_notepad_button,
#         Qt.LeftButton
#         )

#     assert app.notepads_bar.notepads_bar_layout.count() == 2
#     assert app._mn_manager.get_notepad(0).content == ""
#     assert app._mn_manager.get_notepad(1).content == ""


# def test_new_notepad_2(app: MainWindow, qtbot) -> None:
#     """
#     1. Start app
#     2. Write text "aAa"
#     3. Press "+" (new button)
#     4. Set notepad name "new_tab248"
#     """
#     def get_file_name_mock(*args) -> tuple[str, bool]:
#         return "new_tab248", True

#     app.notepads_bar._get_file_name = get_file_name_mock

#     assert app.notepads_bar.notepads_bar_layout.count() == 1
#     assert app._mn_manager.get_notepad(0).content == ""

#     app.text_box.insertPlainText("aAa")

#     qtbot.mouseClick(
#         app.notepads_bar.new_notepad_button,
#         Qt.LeftButton
#         )

#     assert app.notepads_bar.notepads_bar_layout.count() == 2
#     assert app._mn_manager.get_notepad(0).content == "aAa"
#     assert app._mn_manager.get_notepad(1).content == ""


# def test_new_notepad_3(app: MainWindow, qtbot) -> None:
#     """
#     1. Start app
#     2. Press "+" (new button)
#     3. Set notepad name "new_tab248"
#     4. Write text "aAa"
#     5. Back to first tab
#     """
#     def get_file_name_mock(*args) -> tuple[str, bool]:
#         return "new_tab248", True

#     app.notepads_bar._get_file_name = get_file_name_mock

#     assert app.notepads_bar.notepads_bar_layout.count() == 1
#     assert app._mn_manager.get_notepad(0).content == ""

#     qtbot.mouseClick(
#         app.notepads_bar.new_notepad_button,
#         Qt.LeftButton
#         )

#     app.text_box.insertPlainText("aAa")

#     qtbot.mouseClick(
#         app.notepads_bar.notepads_bar_layout.itemAt(0).widget(),
#         Qt.LeftButton
#         )

#     assert app.notepads_bar.notepads_bar_layout.count() == 2
#     assert app._mn_manager.get_notepad(0).content == ""
#     assert app._mn_manager.get_notepad(1).content == "aAa"
