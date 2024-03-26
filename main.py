#!/usr/bin/python3

# PySide import for QT 
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator, QDateTime, QEvent, QTimer
from UI.pagesetup_ui import Ui_MainWindow 

# Libraries imports
import sys, os
import rescources

# Local imports
from config import LANGUAGE
from pages.Addition_Page import Addition
from pages.Overview_Page import Overview
from pages.MenuBalk_widget import UserWidget
from pages.Explore_Page import Explore
from pages.About_page import About
from pages.Settings_Page import Settings
from pages.Wishlist_Page import Wishlist    

# Code for page
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.setupUi(self) 
        # Setup for person icon screen
        QApplication.instance().installEventFilter(self)

        # Create the UserWidget and connect the signal to change pages
        self.userWidget = UserWidget(self)
        self.userWidget.requestPageChange.connect(self.changePage)

        # Dictionary to hold the pages
        self.pages = {
            'Overview': Overview(self.PageSetup),
            'Addition': Addition(self.PageSetup),
            'Explore': Explore(self.PageSetup),
            'About': About(self.PageSetup),
            'Settings': Settings(self.PageSetup),
            'Wishlist': Wishlist(self.PageSetup),
        }

        # Add pages to the QStackedWidget
        for page_name, page in self.pages.items():
            self.PageSetup.addWidget(page)
            page.setObjectName(page_name)

        self.pages['Overview'].requestPageChange.connect(self.changePage)
        self.pages['Addition'].requestPageChange.connect(self.changePage)
        self.pages['Explore'].requestPageChange.connect(self.changePage)
        self.pages['Addition'].requestPageChange.connect(self.pages['Explore'].refreshGlassesDisplay)

        self.MenuButton.clicked.connect(self.showUserWidget)
        self.changePage("Explore")
        self.show()

    def changePage(self, page_name):
        """Find the index of the page by name and set it as the current page."""
        page = self.pages.get(page_name)
        if page:
            index = self.PageSetup.indexOf(page)
            self.PageSetup.setCurrentIndex(index)
            self.PageName.setText(page_name)
            self.userWidget.setActivePage(page_name)  
        else:
            print(f"Page {page_name} not found.")

    def eventFilter(self, source, event):
        """This function filters the events to check if the UserWidget should be closed"""
        if event.type() == QEvent.MouseButtonPress and self.userWidget.isVisible():
            # Convert the globalPosition (QPointF) to QPoint
            globalPos = event.globalPosition().toPoint()
            
            # Check if the click is outside the UserWidget
            if not self.userWidget.geometry().contains(self.userWidget.mapFromGlobal(globalPos)):
                self.userWidget.animateOut()
        return super(MainWindow, self).eventFilter(source, event)

    def showUserWidget(self):
        """Show the UserWidget and animate it in."""
        self.userWidget.animateIn()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    style_path = os.path.join(application_path, 'rescources', 'style.qss')

    try:
        with open(style_path, "r") as style_file:
            app.setStyleSheet(style_file.read())
    except FileNotFoundError:
        print(f"Style file not found at {style_path}. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

    main_window = MainWindow()
    main_window.show() 
    sys.exit(app.exec())
