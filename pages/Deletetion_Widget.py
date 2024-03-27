from PySide6.QtCore import Qt, QPropertyAnimation, QRect, Signal
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from UI.Deletion_Widget_ui import Ui_Deletion_Widget  # Adjust the import path

import sqlite3

ANIMATION_DURATION = 175  # Animation duration in milliseconds

class UserWidget(QDialog, Ui_Deletion_Widget):
    def __init__(self, parent=None):
        super(UserWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # Connect all the buttons on this page
        self.MinusButton.clicked.connect(self.MinusGlasses)
        self.PlusButton.clicked.connect(self.PlusGlasses)
        self.Deletion.clicked.connect(self.DeletionGlasses)
        self.Collapse.clicked.connect(self.animateOut)

        # Assuming your UI design has these dimensions or set them as needed
        self.targetWidth = 250  # Width of the UserWidget
        self.startPosition = QRect(self.parent().width(), 0, self.targetWidth, self.parent().height())
        self.endPosition = QRect(self.parent().width() - self.targetWidth, 0, self.targetWidth, self.parent().height())
        self.setGeometry(self.startPosition)  # Start off-screen on the right

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

    def Parseinformation(self, brewery, glass_type):
        self.Brewery = brewery
        self.GlassType = glass_type

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

    def MinusGlasses(self):
        """Decrements the amount of glasses in the database."""
        current_amount = int(self.AmountInput.text())
        if current_amount > 0:
            new_amount = current_amount - 1
            self.update_glass_amount(self.Brewery, self.GlassType, new_amount)
            self.AmountInput.setText(str(new_amount))

    def PlusGlasses(self):
        """Increments the amount of glasses in the database."""
        current_amount = int(self.AmountInput.text())
        new_amount = current_amount + 1
        self.update_glass_amount(self.Brewery, self.GlassType, new_amount)
        self.AmountInput.setText(str(new_amount))

    def update_glass_amount(self, brewery, glass_type, new_amount):
        """Updates the amount of glasses for the given brewery and glass type in the database.

        Args:
            brewery (str): Name of the brewery.
            glass_type (str): Type of the glass.
            new_amount (int): The new amount of glasses.
        """

        # Replace with your actual logic to connect to database and update amount
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE beer_data SET amount = ? WHERE brewery = ? AND type = ?", (new_amount, brewery, glass_type))
        conn.commit()
        conn.close()

    def DeletionGlasses(self):
        """Deletes the glass entry from the database."""

        # Replace with your actual logic to connect to database and delete record
        brewery = self.Brewery
        glass_type = self.GlassType
        confirmation = QMessageBox.question(self, "Confirmation", f"Are you sure you want to delete {glass_type} from {brewery}?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            conn = sqlite3.connect('data.sqlite')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM beer_data WHERE brewery = ? AND type = ?", (brewery, glass_type))
            conn.commit()
            conn.close()
            # Emit signal or perform other actions to indicate deletion
            self.hide()  # Assuming you want to hide the widget after deletion
