from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QApplication
from PySide6.QtCore import Qt, Signal, QEvent
import sqlite3

from UI.Explore_ui import Ui_Explore 
from pages.Glass_Widget import Glass_Widget  # Ensure this is the correct path

class Explore(QWidget, Ui_Explore):
    requestPageChange = Signal(str)
    def __init__(self, parent=None):
        super(Explore, self).__init__(parent)
        self.setupUi(self)

        # Connect the button to the page change signal
        self.AddButton.clicked.connect(lambda: self.requestPageChange.emit('Addition'))
        self.SearchBar.setPlaceholderText("Search Brewery")
        self.SearchBar.textChanged.connect(self.filterGlasses) 
        self.scroll_layout = QVBoxLayout()  # This will hold the glass widgets
        self.displayGlasses()

    def displayGlasses(self):
        # Fetch glasses from the database
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM beer_data")  # Adjust if your table name is different
        glasses = cursor.fetchall()
        connection.close()
        
        # Create a container widget and set the layout
        container_widget = QWidget()
        container_widget.setObjectName("containerWidget")
        container_widget.setLayout(self.scroll_layout)

        self.scroll_layout.setSpacing(0)  # Minimize spacing between widgets
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)  # Minimize margins of the layout
        self.scroll_layout.addStretch(1)

        # Ensure that vertical scrolling is enabled
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Populate the container with glass widgets
        for glass in glasses:
            self.addGlassWidget(glass)
            
        self.scroll_layout.addStretch(1)
        # Set the container widget as the scroll area's widget
        self.scrollArea.setWidget(container_widget)

    def addGlassWidget(self, glass):
        # Instantiate the custom widget
        self.glass_widget = Glass_Widget()
        self.glass_widget.setObjectName("glassWidget")  # For styling in QSS

        # Set fixed heights for the widget
        self.glass_widget.setMinimumHeight(120)  # Minimum height
        self.glass_widget.setMaximumHeight(120)  # Maximum height to make all widgets uniform in size

        # Set the content of the labels
        self.glass_widget.Brewery.setText(glass[1])  # Assuming glass[1] is the brewery name
        self.glass_widget.GlassType.setText(glass[2])  # Assuming glass[2] is the glass type
        self.glass_widget.Amount.setText(str(glass[3]))  # Assuming glass[3] is the amount

        # Add the custom beer item to the scroll layout
        self.scroll_layout.addWidget(self.glass_widget)

    def refreshGlassesDisplay(self):
        # Clear the existing widgets in the layout
        for i in reversed(range(self.scroll_layout.count())): 
            widget_to_remove = self.scroll_layout.itemAt(i).widget()
            # Remove it from the layout list and delete it
            if widget_to_remove is not None:  # Check if the widget exists before removing
                self.scroll_layout.removeWidget(widget_to_remove)
                widget_to_remove.deleteLater()
        
        # Re-populate the container with glass widgets
        self.displayGlasses()

    def filterGlasses(self, query):
        # Loop through all widgets in the scroll layout
        for i in range(self.scroll_layout.count()):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                # If the search query is in the brewery name, show the widget, otherwise hide it
                brewery_name = widget.Brewery.text().lower()
                widget.setVisible(query.lower() in brewery_name)
