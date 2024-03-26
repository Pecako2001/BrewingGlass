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
from pages.Addition import Addition
from pages.Overview import Overview

# Code for page
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.setupUi(self) 
        # Setup for person icon screen
        QApplication.instance().installEventFilter(self)
        self.UserPopout = None

        # Dictionary to hold the pages
        self.pages = {
            'Overview': Overview(self.PageSetup),
            'Addition': Addition(self.PageSetup),
        }

        self.change_language(LANGUAGE)
        # # Add pages to the QStackedWidget
        for page_name, page in self.pages.items():
            self.PageSetup.addWidget(page)
            page.setObjectName(page_name)

        # Connect everything inside this current page
        self.NL.clicked.connect(lambda: self.change_language("NL"))
        self.PL.clicked.connect(lambda: self.change_language("PL"))
        self.EN.clicked.connect(lambda: self.change_language("EN"))

        self.pages['Overview'].requestPageChange.connect(self.changePage)
        self.pages['Addition'].requestPageChange.connect(self.changePage)

        self.Exit.clicked.connect(self.quitApplication)
        self.changePage("Overview")
        self.show()

    def quitApplication(self):
        """Slot to handle the Exit button click and quit the application."""
        sys.exit(0)

    def changePage(self, page_name):
        """Find the index of the page by name and set it as the current page."""
        page = self.pages.get(page_name)
        if page:
            index = self.PageSetup.indexOf(page)
            self.PageSetup.setCurrentIndex(index)
        else:
            print(f"Page {page_name} not found.")

    def change_language(self, language_code):
        """Changes the language to the given language code"""
        try:
            translator = QTranslator(self)
            language_path = f"translations/translation_{language_code}.qm"

            translator.load(language_path)
            QApplication.instance().installTranslator(translator)
            buttons = {
                'EN': self.EN_active,
                'PL': self.PL_active,
                'NL': self.NL_active,
                # add the rest of the languages accordingly
            }
            for name, button in buttons.items():
                if name == language_code:
                    button.setProperty("active", True)
                    button.style().polish(button)
                else:
                    button.setProperty("active", False)
                    button.style().polish(button)

            for name, page in self.pages.items():
                page.retranslateUi(page) 

        except Exception as e:
            print(f"{e}")

    def eventFilter(self, source, event):
        """This function filters the events to check if the UserPopout should be closed"""
        if event.type() == QEvent.MouseButtonPress and self.UserPopout:
            # Check if the click is outside the UserPopout
            if not self.UserPopout.geometry().contains(event.globalPos()):
                self.UserPopout.close()
                self.UserPopout = None
        return super(MainWindow, self).eventFilter(source, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("rescources/style.qss", "r") as style_file:
            app.setStyleSheet(style_file.read())
    except FileNotFoundError:
        print("Style file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

    main_window = MainWindow()
    main_window.show() 
    sys.exit(app.exec())
