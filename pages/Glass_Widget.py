from PySide6.QtCore import Qt, QPropertyAnimation, QRect, Signal, QEvent
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow
from UI.Glass_Widget_ui import Ui_Glass_Widget  # Adjust the import path

# Import the deletion widget class
from pages.Deletion_Widget import UserWidget  # Assuming Deletion_Widget.py is in the same directory

# Local imports
import sqlite3

ANIMATION_DURATION = 150  # Animation duration in milliseconds

class Glass_Widget(QDialog, Ui_Glass_Widget):
    glassUpdated = Signal(str, str, int)
    BrewInformation = Signal(list)
    def __init__(self, parent=None):
        super(Glass_Widget, self).__init__(parent)
        self.setupUi(self)
        self.deletion_widget = UserWidget(self)
        QApplication.instance().installEventFilter(self)
        self.deletion_widget.glassUpdated.connect(self.update_glass_amount)
        # Connect the click signal to a slot (replace with your actual logic)
        self.Extend.clicked.connect(self.on_glass_clicked)
    def update_glass_amount(self, brewery, glass_type, amount):
        self.glassUpdated.emit(brewery, glass_type, amount)
        
    def on_glass_clicked(self):
        print(f"Glass clicked for {self.Brewery.text()}, {self.GlassType.text()}")
        self.deletion_widget.setObjectName("deleteWidget")
        self.deletion_widget.setMinimumHeight(120)
        self.deletion_widget.setMaximumHeight(120)
        self.deletion_widget.AmountInput.setText(str(self.get_glass_amount(self.Brewery.text(), self.GlassType.text())))
        self.deletion_widget.animateIn()
        self.deletion_widget.Parseinformation(self.Brewery.text(), self.GlassType.text())

    def get_glass_amount(self, brewery, glass_type):
        """Fetches the current amount of glasses from the database for the given brewery and glass type.

        Args:
            brewery (str): Name of the brewery.
            glass_type (str): Type of the glass.

        Returns:
            int: The current amount of glasses in the database.
        """

        # Replace with your actual logic to connect to database and retrieve amount
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT amount FROM beer_data WHERE brewery = ? AND type = ?", (brewery, glass_type))
        result = cursor.fetchone()  # Store the fetched row (might be None)
        amount = 0 if result is None else result[0]  # Check for None before accessing index
        conn.close()
        return amount
