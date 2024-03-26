# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Glass_Widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Glass_Widget(object):
    def setupUi(self, Glass_Widget):
        if not Glass_Widget.objectName():
            Glass_Widget.setObjectName(u"Glass_Widget")
        Glass_Widget.resize(379, 120)
        self.Brewery = QLabel(Glass_Widget)
        self.Brewery.setObjectName(u"Brewery")
        self.Brewery.setGeometry(QRect(120, 20, 250, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.Brewery.setFont(font)
        self.GlassType = QLabel(Glass_Widget)
        self.GlassType.setObjectName(u"GlassType")
        self.GlassType.setGeometry(QRect(120, 45, 250, 17))
        self.GlassType_2 = QLabel(Glass_Widget)
        self.GlassType_2.setObjectName(u"GlassType_2")
        self.GlassType_2.setGeometry(QRect(120, 75, 67, 17))
        self.Amount = QLabel(Glass_Widget)
        self.Amount.setObjectName(u"Amount")
        self.Amount.setGeometry(QRect(190, 75, 100, 17))
        self.Image = QLabel(Glass_Widget)
        self.Image.setObjectName(u"Image")
        self.Image.setGeometry(QRect(20, 20, 75, 80))

        self.retranslateUi(Glass_Widget)

        QMetaObject.connectSlotsByName(Glass_Widget)
    # setupUi

    def retranslateUi(self, Glass_Widget):
        Glass_Widget.setWindowTitle(QCoreApplication.translate("Glass_Widget", u"Form", None))
        self.Brewery.setText(QCoreApplication.translate("Glass_Widget", u"Brewery", None))
        self.GlassType.setText(QCoreApplication.translate("Glass_Widget", u"GlassType", None))
        self.GlassType_2.setText(QCoreApplication.translate("Glass_Widget", u"Amount:", None))
        self.Amount.setText(QCoreApplication.translate("Glass_Widget", u"Amount", None))
        self.Image.setText(QCoreApplication.translate("Glass_Widget", u"Image", None))
    # retranslateUi

