# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Addition.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QWidget)
import images_rc

class Ui_Addition(object):
    def setupUi(self, Addition):
        if not Addition.objectName():
            Addition.setObjectName(u"Addition")
        Addition.resize(399, 789)
        self.Background = QLabel(Addition)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 399, 789))
        self.Submit = QPushButton(Addition)
        self.Submit.setObjectName(u"Submit")
        self.Submit.setGeometry(QRect(110, 720, 200, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Submit.setFont(font)
        self.label = QLabel(Addition)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 580, 191, 25))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_2 = QLabel(Addition)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 390, 191, 25))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Addition)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 210, 191, 25))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Addition)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 20, 191, 25))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Addition)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 70, 100, 100))
        self.SearchBar = QLineEdit(Addition)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setGeometry(QRect(50, 240, 250, 25))
        self.BreweriesList = QListView(Addition)
        self.BreweriesList.setObjectName(u"BreweriesList")
        self.BreweriesList.setGeometry(QRect(50, 270, 250, 100))
        self.PlusButton = QPushButton(Addition)
        self.PlusButton.setObjectName(u"PlusButton")
        self.PlusButton.setGeometry(QRect(270, 630, 40, 40))
        self.MinusButton = QPushButton(Addition)
        self.MinusButton.setObjectName(u"MinusButton")
        self.MinusButton.setGeometry(QRect(110, 630, 40, 40))
        self.AmountInput = QLabel(Addition)
        self.AmountInput.setObjectName(u"AmountInput")
        self.AmountInput.setGeometry(QRect(180, 630, 67, 40))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.AmountInput.setFont(font2)
        self.AmountInput.setAlignment(Qt.AlignCenter)
        self.TypeInput = QLineEdit(Addition)
        self.TypeInput.setObjectName(u"TypeInput")
        self.TypeInput.setGeometry(QRect(50, 420, 250, 25))
        self.Close = QPushButton(Addition)
        self.Close.setObjectName(u"Close")
        self.Close.setGeometry(QRect(340, 10, 50, 50))
        self.Close.setFont(font)
        self.PlusButton_2 = QPushButton(Addition)
        self.PlusButton_2.setObjectName(u"PlusButton_2")
        self.PlusButton_2.setGeometry(QRect(310, 240, 25, 25))
        self.PlusButton_3 = QPushButton(Addition)
        self.PlusButton_3.setObjectName(u"PlusButton_3")
        self.PlusButton_3.setGeometry(QRect(310, 420, 25, 25))

        self.retranslateUi(Addition)

        QMetaObject.connectSlotsByName(Addition)
    # setupUi

    def retranslateUi(self, Addition):
        Addition.setWindowTitle(QCoreApplication.translate("Addition", u"Form", None))
        self.Background.setText("")
        self.Submit.setText(QCoreApplication.translate("Addition", u"Submit", None))
        self.label.setText(QCoreApplication.translate("Addition", u"Aantal:", None))
        self.label_2.setText(QCoreApplication.translate("Addition", u"Type:", None))
        self.label_3.setText(QCoreApplication.translate("Addition", u"Brewery:", None))
        self.label_4.setText(QCoreApplication.translate("Addition", u"Glass", None))
        self.label_5.setText(QCoreApplication.translate("Addition", u"Photo", None))
        self.PlusButton.setText(QCoreApplication.translate("Addition", u"+", None))
        self.MinusButton.setText(QCoreApplication.translate("Addition", u"-", None))
        self.AmountInput.setText(QCoreApplication.translate("Addition", u"0", None))
        self.Close.setText(QCoreApplication.translate("Addition", u"X", None))
        self.PlusButton_2.setText(QCoreApplication.translate("Addition", u"+", None))
        self.PlusButton_3.setText(QCoreApplication.translate("Addition", u"+", None))
    # retranslateUi

