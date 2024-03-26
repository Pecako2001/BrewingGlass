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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)
import images_rc

class Ui_Wishlist(object):
    def setupUi(self, Wishlist):
        if not Wishlist.objectName():
            Wishlist.setObjectName(u"Wishlist")
        Wishlist.resize(399, 789)
        self.Background = QLabel(Wishlist)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 399, 789))
        self.verticalLayoutWidget = QWidget(Wishlist)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 391, 781))
        self.glassLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.glassLayout.setObjectName(u"glassLayout")
        self.glassLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.glassLayout.addWidget(self.label_2)


        self.retranslateUi(Wishlist)

        QMetaObject.connectSlotsByName(Wishlist)
    # setupUi

    def retranslateUi(self, Wishlist):
        Wishlist.setWindowTitle(QCoreApplication.translate("Wishlist", u"Form", None))
        self.Background.setText("")
        self.label_2.setText(QCoreApplication.translate("Wishlist", u"Wishlist Placeholder", None))
    # retranslateUi

