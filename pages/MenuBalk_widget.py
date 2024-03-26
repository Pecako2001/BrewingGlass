# Import necessary modules
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, Signal
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow
from UI.MenuBalk_ui import Ui_MenuBalk  # Adjust the import path according to your project structure

import webbrowser

ANIMATION_DURATION = 250  # Animation duration in milliseconds

class UserWidget(QDialog, Ui_MenuBalk):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(UserWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # Connect all the buttons on this page
        self.GlassesPage.clicked.connect(lambda: self.requestPageChange.emit('Overview'))
        self.ExplorePage.clicked.connect(lambda: self.requestPageChange.emit('Addition'))
        self.WishlistPage.clicked.connect(lambda: self.requestPageChange.emit('Overview'))
        self.SettingsPage.clicked.connect(lambda: self.requestPageChange.emit('Addition'))
        self.OverPage.clicked.connect(lambda: webbrowser.open('https://github.com/Pecako2001/BrewingGlass'))
        # Assuming your UI design has these dimensions or set them as needed
        self.targetWidth = 200  # Width of the UserWidget
        self.startPosition = QRect(-self.targetWidth, 0, self.targetWidth, parent.height())
        self.endPosition = QRect(0, 0, self.targetWidth, parent.height())
        self.setGeometry(self.startPosition)  # Start off-screen

        # Initialize the animation object for animating in
        self.animationIn = QPropertyAnimation(self, b"geometry")
        self.animationIn.setDuration(ANIMATION_DURATION)
        self.animationIn.setStartValue(self.startPosition)
        self.animationIn.setEndValue(self.endPosition)

        # Initialize the animation object for animating out
        self.animationOut = QPropertyAnimation(self, b"geometry")
        self.animationOut.setDuration(ANIMATION_DURATION)
        self.animationOut.setStartValue(self.endPosition)  # Will be updated during animateOut
        self.animationOut.setEndValue(self.startPosition)
        self.animationOut.finished.connect(self.onAnimationOutFinished)

    def animateIn(self):
        """Animate the UserWidget in from the left side of the parent widget."""
        self.show()
        self.setGeometry(self.startPosition)
        self.animationIn.start()

    def animateOut(self):
        """Animate the UserWidget out to the left side of the parent widget."""
        self.animationOut.setStartValue(self.geometry())
        self.animationOut.start()

    def onAnimationOutFinished(self):
        """Hide the UserWidget after the animation is complete."""
        self.hide()
