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
        self.PageSetup.setGeometry(QRect(50, 0, 349, 844))
        self.NL = QPushButton(self.centralwidget)
        self.NL.setObjectName(u"NL")
        self.NL.setGeometry(QRect(590, 20, 38, 38))
        icon = QIcon()
        icon.addFile(u":/rescources/rescources/languages/vlag nederlands.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NL.setIcon(icon)
        self.NL.setIconSize(QSize(40, 40))
        self.DateTimeLabel = QLabel(self.centralwidget)
        self.DateTimeLabel.setObjectName(u"DateTimeLabel")
        self.DateTimeLabel.setGeometry(QRect(1030, 40, 161, 17))
        self.EN_active = QLabel(self.centralwidget)
        self.EN_active.setObjectName(u"EN_active")
        self.EN_active.setGeometry(QRect(765, 60, 8, 8))
        self.Background = QLabel(self.centralwidget)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 399, 844))
        self.Background.setStyleSheet(u"background-color: #FBB117;")
        self.Balk_Boven = QLabel(self.centralwidget)
        self.Balk_Boven.setObjectName(u"Balk_Boven")
        self.Balk_Boven.setGeometry(QRect(0, 0, 50, 844))
        self.Balk_Boven.setStyleSheet(u"background-color: #f28e1c;")
        self.Bottom_1 = QPushButton(self.centralwidget)
        self.Bottom_1.setObjectName(u"Bottom_1")
        self.Bottom_1.setGeometry(QRect(150, 970, 38, 38))
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(70, 970, 38, 38))
        self.PL = QPushButton(self.centralwidget)
        self.PL.setObjectName(u"PL")
        self.PL.setGeometry(QRect(670, 20, 38, 38))
        icon1 = QIcon()
        icon1.addFile(u":/rescources/rescources/languages/vlag pools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PL.setIcon(icon1)
        self.PL.setIconSize(QSize(40, 40))
        self.NL_active = QLabel(self.centralwidget)
        self.NL_active.setObjectName(u"NL_active")
        self.NL_active.setGeometry(QRect(605, 60, 8, 8))
        self.EN = QPushButton(self.centralwidget)
        self.EN.setObjectName(u"EN")
        self.EN.setGeometry(QRect(750, 20, 38, 38))
        icon2 = QIcon()
        icon2.addFile(u":/rescources/rescources/languages/Vlag engels.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EN.setIcon(icon2)
        self.EN.setIconSize(QSize(40, 40))
        self.PL_active = QLabel(self.centralwidget)
        self.PL_active.setObjectName(u"PL_active")
        self.PL_active.setGeometry(QRect(685, 60, 8, 8))
        self.Bottom_2 = QPushButton(self.centralwidget)
        self.Bottom_2.setObjectName(u"Bottom_2")
        self.Bottom_2.setGeometry(QRect(230, 970, 38, 38))
        self.Balk_onder = QLabel(self.centralwidget)
        self.Balk_onder.setObjectName(u"Balk_onder")
        self.Balk_onder.setGeometry(QRect(0, 951, 1280, 73))
        self.Balk_onder.setPixmap(QPixmap(u":/rescources/rescources/overview/balk ondersvg.svg"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.Background.raise_()
        self.Balk_onder.raise_()
        self.PageSetup.raise_()
        self.NL.raise_()
        self.DateTimeLabel.raise_()
        self.EN_active.raise_()
        self.Bottom_1.raise_()
        self.Exit.raise_()
        self.PL.raise_()
        self.NL_active.raise_()
        self.EN.raise_()
        self.PL_active.raise_()
        self.Bottom_2.raise_()
        self.Balk_Boven.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NL.setText("")
        self.DateTimeLabel.setText(QCoreApplication.translate("MainWindow", u"13.02.2024 | 9:47", None))
        self.EN_active.setText("")
        self.Background.setText("")
        self.Balk_Boven.setText("")
        self.Bottom_1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.PL.setText("")
        self.NL_active.setText("")
        self.EN.setText("")
        self.PL_active.setText("")
        self.Bottom_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Balk_onder.setText("")
    # retranslateUi

