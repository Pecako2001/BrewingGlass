# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Deletion_Widget.ui'
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

class Ui_Deletion_Widget(object):
    def setupUi(self, Deletion_Widget):
        if not Deletion_Widget.objectName():
            Deletion_Widget.setObjectName(u"Deletion_Widget")
        Deletion_Widget.resize(250, 120)
        self.PlusButton = QPushButton(Deletion_Widget)
        self.PlusButton.setObjectName(u"PlusButton")
        self.PlusButton.setGeometry(QRect(140, 40, 40, 40))
        self.AmountInput = QLabel(Deletion_Widget)
        self.AmountInput.setObjectName(u"AmountInput")
        self.AmountInput.setGeometry(QRect(90, 40, 50, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.AmountInput.setFont(font)
        self.AmountInput.setAlignment(Qt.AlignCenter)
        self.MinusButton = QPushButton(Deletion_Widget)
        self.MinusButton.setObjectName(u"MinusButton")
        self.MinusButton.setGeometry(QRect(50, 40, 40, 40))
        self.Deletion = QPushButton(Deletion_Widget)
        self.Deletion.setObjectName(u"Deletion")
        self.Deletion.setGeometry(QRect(200, 40, 40, 40))
        self.AnimationWidget = QLabel(Deletion_Widget)
        self.AnimationWidget.setObjectName(u"AnimationWidget")
        self.AnimationWidget.setGeometry(QRect(5, 5, 240, 110))
        font1 = QFont()
        font1.setFamilies([u"Tlwg Typist"])
        self.AnimationWidget.setFont(font1)
        self.Collapse = QPushButton(Deletion_Widget)
        self.Collapse.setObjectName(u"Collapse")
        self.Collapse.setGeometry(QRect(0, 40, 40, 40))
        self.AnimationWidget.raise_()
        self.PlusButton.raise_()
        self.AmountInput.raise_()
        self.MinusButton.raise_()
        self.Deletion.raise_()
        self.Collapse.raise_()

        self.retranslateUi(Deletion_Widget)

        QMetaObject.connectSlotsByName(Deletion_Widget)
    # setupUi

    def retranslateUi(self, Deletion_Widget):
        Deletion_Widget.setWindowTitle(QCoreApplication.translate("Deletion_Widget", u"Form", None))
        self.PlusButton.setText(QCoreApplication.translate("Deletion_Widget", u"+", None))
        self.AmountInput.setText(QCoreApplication.translate("Deletion_Widget", u"0", None))
        self.MinusButton.setText(QCoreApplication.translate("Deletion_Widget", u"-", None))
        self.Deletion.setText(QCoreApplication.translate("Deletion_Widget", u"D", None))
        self.AnimationWidget.setText("")
        self.Collapse.setText(QCoreApplication.translate("Deletion_Widget", u">", None))
    # retranslateUi

