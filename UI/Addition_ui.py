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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
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
        self.label = QLabel(Addition)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 580, 191, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Addition)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 390, 191, 25))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Addition)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 210, 191, 25))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Addition)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 30, 191, 25))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Addition)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 50, 100, 100))

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
    # retranslateUi

