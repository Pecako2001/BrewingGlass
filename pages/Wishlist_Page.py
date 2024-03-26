# PySide import for QT 
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer, QDateTime, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

from UI.Wishlist_ui import Ui_Wishlist 

# Libraries imports
import sys

# Local imports

# Code for page
class Wishlist(QWidget, Ui_Wishlist):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(Wishlist, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file
