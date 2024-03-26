# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Overview.ui'
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
import images_rc

class Ui_Overview(object):
    def setupUi(self, Overview):
        if not Overview.objectName():
            Overview.setObjectName(u"Overview")
        Overview.resize(399, 789)
        self.Background = QLabel(Overview)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 399, 789))
        font = QFont()
        font.setFamilies([u"Tlwg Typist"])
        self.Background.setFont(font)
        self.label_2 = QLabel(Overview)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 389, 779))
        self.label_2.raise_()
        self.Background.raise_()

        self.retranslateUi(Overview)

        QMetaObject.connectSlotsByName(Overview)
    # setupUi

    def retranslateUi(self, Overview):
        Overview.setWindowTitle(QCoreApplication.translate("Overview", u"Form", None))
        self.Background.setText("")
        self.label_2.setText(QCoreApplication.translate("Overview", u"Overview placeholder", None))
    # retranslateUi

