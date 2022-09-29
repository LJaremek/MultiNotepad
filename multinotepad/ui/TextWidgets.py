from PyQt5.QtWidgets import QPlainTextEdit


class TextField(QPlainTextEdit):
    def __init__(self, text_change_action: callable, *args, **kwargs) -> None:
        super(TextField, self).__init__(*args, **kwargs)
        self.textChanged.connect(text_change_action)
        self.setDisabled(True)
