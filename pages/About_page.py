# PySide import for QT 
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer, QDateTime, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

from UI.Information_ui import Ui_About 

# Libraries imports
import sys

# Local imports

# Code for page
class About(QWidget, Ui_About):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file