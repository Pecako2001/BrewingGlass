# PySide import for QT 
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer, QDateTime, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

from UI.Addition_ui import Ui_Addition 

# Libraries imports
import sys

# Local imports

# Code for page
class Addition(QWidget, Ui_Addition):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(Addition, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file

        self.Submit.clicked.connect(lambda: self.requestPageChange.emit('Overview'))