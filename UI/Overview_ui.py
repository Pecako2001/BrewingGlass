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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
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
        self.pushButton = QPushButton(Overview)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 30, 200, 200))
        self.pushButton_2 = QPushButton(Overview)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 280, 200, 200))
        self.pushButton_3 = QPushButton(Overview)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 530, 200, 200))
        self.AddButton = QPushButton(Overview)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(340, 730, 40, 40))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Thin"])
        font1.setPointSize(28)
        font1.setBold(True)
        self.AddButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/rescources/rescources/icons/Plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setIconSize(QSize(25, 25))

        self.retranslateUi(Overview)

        QMetaObject.connectSlotsByName(Overview)
    # setupUi

    def retranslateUi(self, Overview):
        Overview.setWindowTitle(QCoreApplication.translate("Overview", u"Form", None))
        self.Background.setText("")
        self.pushButton.setText(QCoreApplication.translate("Overview", u"Your Glasses", None))
        self.pushButton_2.setText(QCoreApplication.translate("Overview", u"Explore", None))
        self.pushButton_3.setText(QCoreApplication.translate("Overview", u"Wishlist", None))
        self.AddButton.setText("")
    # retranslateUi

