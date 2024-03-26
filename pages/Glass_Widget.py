# Import necessary modules
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, Signal
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow
from UI.Glass_Widget_ui import Ui_Glass_Widget  # Adjust the import path according to your project structure


class Glass_Widget(QDialog, Ui_Glass_Widget):
    def __init__(self, parent=None):
        super(Glass_Widget, self).__init__(parent)
        self.setupUi(self)

    def mousePressEvent(self, event):
        super(Glass_Widget, self).mousePressEvent(event)
        # Emit a signal or perform an action
        print(f"{self.Brewery.text()} clicked!")  # For example