# PySide import for QT 
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import QTimer, QDateTime, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

from UI.Overview_ui import Ui_Overview 

# Libraries imports
import sys, sqlite3

# Local imports

# Code for page
class Overview(QWidget, Ui_Overview):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(Overview, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file
        self.Updatetags()
                
    def Updatetags(self):
        """
        Fetches brewery, glass, and total statistics from a database and updates the labels.
        Also finds the brewery with the most glasses and the most glasses for a single item.
        """
        connection = sqlite3.connect("data.sqlite")
        cursor = connection.cursor()

        # Get basic statistics
        cursor.execute("""
            SELECT
            COUNT(DISTINCT brewery) AS distinct_breweries,
            COUNT(*) AS total_glasses,
            SUM(amount) AS total_amount
            FROM beer_data;
        """)

        stats = cursor.fetchone()

        # Get brewery with most glasses
        cursor.execute("""
            SELECT brewery, SUM(amount) AS total_from_brewery
            FROM beer_data
            GROUP BY brewery
            ORDER BY total_from_brewery DESC
            LIMIT 1;
        """)

        brewery_with_most_glasses = cursor.fetchone()[0]

        # Get most glasses for a single item
        cursor.execute("""
            SELECT brewery, type, MAX(amount) AS max_from_item
            FROM beer_data
            GROUP BY brewery, type;
        """)

        # Find the row with the most glasses
        row_with_most_glasses = cursor.fetchone()
        most_glasses_brewery, most_glasses_type, most_glasses_from_single_item = row_with_most_glasses

        # Close the connection
        connection.close()

        # Update the labels
        self.DifferentBreweries.setText(str(stats[0]))
        self.TotalDifferentGlasses.setText(str(stats[1]))
        # Update with the correct label name (assuming it's self.TotalGlasses)
        self.TotalGlasses.setText(str(stats[2]))

        # Update labels for additional stats (you might need to adjust these names)
        self.MostGlassesBrewery.setText(brewery_with_most_glasses)
        self.MostGlasses.setText(f"{most_glasses_brewery} {most_glasses_type} ({most_glasses_from_single_item})")  # Combine brewery, type, and amount


