# PySide import for QT 
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer, QDateTime, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

from templates.templatePage_ui import Ui_Form 

# Libraries imports
import sys

# Local imports

# Code for page
class mainPage(QWidget, Ui_Form):
    requestPageChange = Signal(str)

    def __init__(self, parent=None):
        super(mainPage, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file

        self.Home.clicked.connect(lambda: self.requestPageChange.emit('main_page'))

    def closeapplication(self):
        sys.exit(0)

            
