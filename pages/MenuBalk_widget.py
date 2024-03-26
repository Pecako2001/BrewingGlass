# Import necessary modules
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, Signal
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow
from UI.MenuBalk_ui import Ui_MenuBalk  # Adjust the import path according to your project structure

import webbrowser

ANIMATION_DURATION = 175  # Animation duration in milliseconds

class UserWidget(QDialog, Ui_MenuBalk):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(UserWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # Create a dictionary that maps page names to buttons
        self.page_buttons = {
            'Overview': self.GlassesPage,
            'Explore': self.ExplorePage,
            'Wishlist': self.WishlistPage,
            'Settings': self.SettingsPage,
            'About': self.OverPage,
        }
        # Connect all the buttons on this page
        self.GlassesPage.clicked.connect(lambda: self.changePage('Overview'))
        self.ExplorePage.clicked.connect(lambda: self.changePage('Explore'))
        self.WishlistPage.clicked.connect(lambda: self.changePage('Wishlist'))
        self.SettingsPage.clicked.connect(lambda: self.changePage('Settings'))
        self.OverPage.clicked.connect(lambda: self.changePage('About'))
        self.Changelog.clicked.connect(lambda: webbrowser.open('https://github.com/Pecako2001/BrewingGlass/blob/main/CHANGELOG.md'))
        self.Contact.clicked.connect(lambda: webbrowser.open('mailto:koenvanwijlick@gmail.com?subject=GlassApplication'))
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

    def changePage(self, page_name):
        """Emit the signal to change the page and animate the UserWidget in."""
        self.animateOut()
        self.requestPageChange.emit(page_name)

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

    def setActivePage(self, page_name):
        """Set the active page button style."""
        # Reset all buttons to their default style
        for button in self.page_buttons.values():
            button.setObjectName('')
            button.style().unpolish(button)  # Unpolish to ensure QSS is reapplied
            button.style().polish(button)    # Reapply QSS

        # Set the active page button style
        active_button = self.page_buttons.get(page_name)
        if active_button:
            active_button.setObjectName('ActivePageButton')
            active_button.style().unpolish(active_button)  # Unpolish to ensure QSS is reapplied
            active_button.style().polish(active_button)    # Reapply QSS

        # Reapply the stylesheet to update the styles
        self.setStyleSheet(self.styleSheet())