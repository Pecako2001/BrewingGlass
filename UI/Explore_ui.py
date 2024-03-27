# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Explore.ui'
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

class Ui_Explore(object):
    def setupUi(self, Explore):
        if not Explore.objectName():
            Explore.setObjectName(u"Explore")
        Explore.resize(399, 789)
        self.AddButton = QPushButton(Explore)
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
        self.scrollArea = QScrollArea(Explore)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 45, 379, 734))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 377, 732))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.SearchBar = QLineEdit(Explore)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setGeometry(QRect(10, 10, 379, 25))
        self.Background = QLabel(Explore)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 399, 800))
        self.Background.raise_()
        self.scrollArea.raise_()
        self.AddButton.raise_()
        self.SearchBar.raise_()

        self.retranslateUi(Explore)

        QMetaObject.connectSlotsByName(Explore)
    # setupUi

    def retranslateUi(self, Explore):
        Explore.setWindowTitle(QCoreApplication.translate("Explore", u"Form", None))
        self.AddButton.setText("")
        self.Background.setText("")
    # retranslateUi

