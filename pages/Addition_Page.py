# PySide imports
from PySide6.QtWidgets import QWidget, QLineEdit, QListView, QVBoxLayout
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

# SQLite database access
import sqlite3

from UI.Addition_ui import Ui_Addition  # Make sure this UI file has QLineEdit and QListView

class Addition(QWidget, Ui_Addition):
    requestPageChange = Signal(str)

    def __init__(self, parent=None):
        super(Addition, self).__init__(parent)
        self.setupUi(self)  # Load the UI from the .ui file
        
        # Assuming your Ui_Addition has these objects: SearchBar and BreweriesList
        self.SearchBar.textChanged.connect(self.updateSearchResults)
        
        self.model = QStandardItemModel(self.BreweriesList)
        self.BreweriesList.setModel(self.model)
        self.Amount = 0  # Initialize the amount
        self.Submit.clicked.connect(self.submitForm)
        self.PlusButton.clicked.connect(self.incrementAmount)
        self.MinusButton.clicked.connect(self.decrementAmount)
        self.Close.clicked.connect(lambda: self.requestPageChange.emit('Explore'))
    
    def updateSearchResults(self, query):
        self.model.clear()  # Clear current search results
        if not query:  # If the query is empty, don't display any results
            return
        connection = sqlite3.connect('breweries.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM breweries WHERE name LIKE ?", ('%' + query + '%',))
        for row in cursor.fetchall():
            item = QStandardItem(row[0])
            self.model.appendRow(item)
        connection.close()

    def showEvent(self, event):
        super().showEvent(event)
        self.resetPage()

    def resetPage(self):
        self.SearchBar.clear()
        self.AmountInput.setText("0")   
        self.TypeInput.clear()     
        self.model.clear()

    def incrementAmount(self):
        self.Amount += 1
        self.AmountInput.setText(str(self.Amount))

    def decrementAmount(self):
        self.Amount = max(0, self.Amount - 1)  # Prevent negative amounts
        self.AmountInput.setText(str(self.Amount))

    def submitForm(self):
        # Get the current selection from the list view
        currentIndex = self.BreweriesList.currentIndex()
        if not currentIndex.isValid():
            print("Please select a brewery from the list.")
            return

        # Retrieve the brewery name from the model
        brewery = self.model.itemFromIndex(currentIndex).text()
        beer_type = self.TypeInput.text()
        amount = self.AmountInput.text()
        if not brewery or not beer_type or not amount:
            # Show some error to the user
            print("All fields are required!")
            return
        
        # If all fields are filled in, insert into the database
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()

        # Assuming you have a table created for the form data
        cursor.execute("INSERT INTO beer_data (brewery, type, amount) VALUES (?, ?, ?)",
                       (brewery, beer_type, amount))
        connection.commit()
        connection.close()

        # Call the resetPage to clear the form after submission
        self.resetPage()

        # Emit the signal to change the page if necessary
        self.requestPageChange.emit('Explore')