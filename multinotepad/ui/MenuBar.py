from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QAction


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        self.menu_bar: QMenuBar = None


def wear_menubar(main_window: MainWindow) -> None:
    main_window.menu_bar_file = main_window.menu_bar.addMenu("&File")

    open_file_action = QAction("Open file...", main_window)
    open_file_action.setStatusTip("Open file")
    open_file_action.triggered.connect(main_window._file_open)
    main_window.menu_bar_file.addAction(open_file_action)

    save_file_action = QAction("Save", main_window)
    save_file_action.setStatusTip("Save current page")
    save_file_action.triggered.connect(main_window._file_save)
    main_window.menu_bar_file.addAction(save_file_action)

    saveas_file_action = QAction("Save As...", main_window)
    saveas_file_action.setStatusTip("Save current page to specified file")
    saveas_file_action.triggered.connect(main_window._file_saveas)
    main_window.menu_bar_file.addAction(saveas_file_action)

    main_window.menu_bar_edit = main_window.menu_bar.addMenu("&Edit")

    undo_action = QAction("Undo", main_window)
    undo_action.setStatusTip("Undo last change")
    undo_action.triggered.connect(main_window.text_box.undo)
    main_window.menu_bar_edit.addAction(undo_action)

    redo_action = QAction("Redo", main_window)
    redo_action.setStatusTip("Redo last change")
    redo_action.triggered.connect(main_window.text_box.redo)
    main_window.menu_bar_edit.addAction(redo_action)

    cut_action = QAction("Cut", main_window)
    cut_action.setStatusTip("Cut selected text")
    cut_action.triggered.connect(main_window.text_box.cut)
    main_window.menu_bar_edit.addAction(cut_action)

    copy_action = QAction("Copy", main_window)
    copy_action.setStatusTip("Copy selected text")
    copy_action.triggered.connect(main_window.text_box.copy)
    main_window.menu_bar_edit.addAction(copy_action)

    paste_action = QAction("Paste", main_window)
    paste_action.setStatusTip("Paste from clipboard")
    paste_action.triggered.connect(main_window.text_box.paste)
    main_window.menu_bar_edit.addAction(paste_action)

    select_action = QAction("Select all", main_window)
    select_action.setStatusTip("Select all text")
    select_action.triggered.connect(main_window.text_box.selectAll)
    main_window.menu_bar_edit.addAction(select_action)
