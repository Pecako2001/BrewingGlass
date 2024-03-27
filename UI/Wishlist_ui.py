# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wishlist.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)
import images_rc

class Ui_Wishlist(object):
    def setupUi(self, Wishlist):
        if not Wishlist.objectName():
            Wishlist.setObjectName(u"Wishlist")
        Wishlist.resize(399, 789)
        self.Background = QLabel(Wishlist)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 399, 800))
        self.SearchBar = QLineEdit(Wishlist)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setGeometry(QRect(10, 10, 379, 25))
        self.AddButton = QPushButton(Wishlist)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(340, 730, 40, 40))
        font = QFont()
        font.setFamilies([u"Ubuntu Thin"])
        font.setPointSize(28)
        font.setBold(True)
        self.AddButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/rescources/rescources/icons/Plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setIconSize(QSize(25, 25))
        self.scrollArea = QScrollArea(Wishlist)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 45, 379, 734))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 377, 732))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Background.raise_()
        self.SearchBar.raise_()
        self.scrollArea.raise_()
        self.AddButton.raise_()

        self.retranslateUi(Wishlist)

        QMetaObject.connectSlotsByName(Wishlist)
    # setupUi

    def retranslateUi(self, Wishlist):
        Wishlist.setWindowTitle(QCoreApplication.translate("Wishlist", u"Form", None))
        self.Background.setText("")
        self.AddButton.setText("")
    # retranslateUi

