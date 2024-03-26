# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'templatePage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 872)
        self.NL_active = QLabel(Form)
        self.NL_active.setObjectName(u"NL_active")
        self.NL_active.setGeometry(QRect(600, 60, 15, 15))
        self.TotalCountLabel = QLabel(Form)
        self.TotalCountLabel.setObjectName(u"TotalCountLabel")
        self.TotalCountLabel.setGeometry(QRect(20, 820, 85, 17))
        font = QFont()
        font.setBold(True)
        self.TotalCountLabel.setFont(font)
        self.TotalCountLabel.setAlignment(Qt.AlignCenter)
        self.Home = QPushButton(Form)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(20, 730, 85, 85))
        icon = QIcon()
        icon.addFile(u":/rescources/rescources/icons/icon placeholder donkersvg.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon)
        self.Home.setIconSize(QSize(60, 60))
        self.EN_active = QLabel(Form)
        self.EN_active.setObjectName(u"EN_active")
        self.EN_active.setGeometry(QRect(760, 60, 15, 15))
        self.PL_active = QLabel(Form)
        self.PL_active.setObjectName(u"PL_active")
        self.PL_active.setGeometry(QRect(680, 60, 15, 15))
        self.SeelectIcon = QLabel(Form)
        self.SeelectIcon.setObjectName(u"SeelectIcon")
        self.SeelectIcon.setGeometry(QRect(80, 20, 201, 41))
        self.SeelectIcon.setPixmap(QPixmap(u":/rescources/rescources/logo/logo m2 seelectsvg.svg"))
        self.Background = QLabel(Form)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(-10, -10, 1280, 872))
        self.Background.setPixmap(QPixmap(u":/rescources/rescources/overview/achtergrond middensvg.svg"))
        self.Button_template = QPushButton(Form)
        self.Button_template.setObjectName(u"Button_template")
        self.Button_template.setGeometry(QRect(690, 170, 175, 175))
        self.Button_template.setIconSize(QSize(89, 97))
        self.SettingTemplate = QPushButton(Form)
        self.SettingTemplate.setObjectName(u"SettingTemplate")
        self.SettingTemplate.setGeometry(QRect(880, 320, 23, 23))
        self.SettingTemplate.setIconSize(QSize(23, 23))
        self.Big_text_template = QLabel(Form)
        self.Big_text_template.setObjectName(u"Big_text_template")
        self.Big_text_template.setGeometry(QRect(710, 380, 141, 40))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.Big_text_template.setFont(font1)
        self.Big_text_template.setAlignment(Qt.AlignCenter)
        self.Small_text_template = QLabel(Form)
        self.Small_text_template.setObjectName(u"Small_text_template")
        self.Small_text_template.setGeometry(QRect(690, 360, 174, 17))
        self.Small_text_template.setFont(font)
        self.Small_text_template.setAlignment(Qt.AlignCenter)
        self.Background.raise_()
        self.TotalCountLabel.raise_()
        self.Home.raise_()
        self.EN_active.raise_()
        self.NL_active.raise_()
        self.PL_active.raise_()
        self.SeelectIcon.raise_()
        self.Button_template.raise_()
        self.SettingTemplate.raise_()
        self.Big_text_template.raise_()
        self.Small_text_template.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.NL_active.setText("")
        self.TotalCountLabel.setText(QCoreApplication.translate("Form", u"Home", None))
        self.Home.setText("")
        self.EN_active.setText("")
        self.PL_active.setText("")
        self.SeelectIcon.setText("")
        self.Background.setText("")
        self.Button_template.setText("")
        self.SettingTemplate.setText("")
        self.Big_text_template.setText(QCoreApplication.translate("Form", u"PLACEHOLDER", None))
        self.Small_text_template.setText(QCoreApplication.translate("Form", u"PLACEHOLDER", None))
    # retranslateUi

