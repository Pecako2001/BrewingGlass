# PySide import for QT 
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer, QDateTime, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

from UI.Overview_ui import Ui_Overview 

# Libraries imports
import sys

# Local imports

# Code for page
class Overview(QWidget, Ui_Overview):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(Overview, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file

        self.AddButton.clicked.connect(lambda: self.requestPageChange.emit('Addition'))
