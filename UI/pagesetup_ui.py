# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesetup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(399, 844)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PageSetup = QStackedWidget(self.centralwidget)
        self.PageSetup.setObjectName(u"PageSetup")
        self.PageSetup.setGeometry(QRect(0, 50, 399, 800))
        self.Balk_Boven = QLabel(self.centralwidget)
        self.Balk_Boven.setObjectName(u"Balk_Boven")
        self.Balk_Boven.setGeometry(QRect(0, 0, 399, 50))
        self.Balk_Boven.setStyleSheet(u"")
        self.MenuButton = QPushButton(self.centralwidget)
        self.MenuButton.setObjectName(u"MenuButton")
        self.MenuButton.setGeometry(QRect(10, 5, 40, 40))
        font = QFont()
        font.setFamilies([u"Ubuntu Thin"])
        font.setPointSize(28)
        font.setBold(True)
        self.MenuButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/rescources/rescources/icons/three_stripes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuButton.setIcon(icon)
        self.MenuButton.setIconSize(QSize(25, 25))
        self.PageName = QLabel(self.centralwidget)
        self.PageName.setObjectName(u"PageName")
        self.PageName.setGeometry(QRect(70, 0, 200, 50))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.PageName.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Balk_Boven.setText("")
        self.MenuButton.setText("")
        self.PageName.setText(QCoreApplication.translate("MainWindow", u"PageName", None))
    # retranslateUi

