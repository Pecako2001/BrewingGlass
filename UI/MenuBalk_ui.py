# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuBalk.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MenuBalk(object):
    def setupUi(self, MenuBalk):
        if not MenuBalk.objectName():
            MenuBalk.setObjectName(u"MenuBalk")
        MenuBalk.resize(200, 844)
        self.verticalLayoutWidget = QWidget(MenuBalk)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 201, 841))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.NameLabel = QLabel(self.verticalLayoutWidget)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"URW Bookman [UKWN]"])
        font.setPointSize(19)
        self.NameLabel.setFont(font)
        self.NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.NameLabel)

        self.GlassesPage = QPushButton(self.verticalLayoutWidget)
        self.GlassesPage.setObjectName(u"GlassesPage")
        self.GlassesPage.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.GlassesPage)

        self.ExplorePage = QPushButton(self.verticalLayoutWidget)
        self.ExplorePage.setObjectName(u"ExplorePage")
        self.ExplorePage.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.ExplorePage)

        self.WishlistPage = QPushButton(self.verticalLayoutWidget)
        self.WishlistPage.setObjectName(u"WishlistPage")
        self.WishlistPage.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.WishlistPage)

        self.SettingsPage = QPushButton(self.verticalLayoutWidget)
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.SettingsPage.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.SettingsPage)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Text = QLabel(self.verticalLayoutWidget)
        self.Text.setObjectName(u"Text")
        self.Text.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamilies([u"URW Bookman [UKWN]"])
        font1.setPointSize(11)
        self.Text.setFont(font1)
        self.Text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Text)

        self.OverPage = QPushButton(self.verticalLayoutWidget)
        self.OverPage.setObjectName(u"OverPage")
        self.OverPage.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.OverPage)

        self.Contact = QPushButton(self.verticalLayoutWidget)
        self.Contact.setObjectName(u"Contact")
        self.Contact.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.Contact)

        self.Changelog = QPushButton(self.verticalLayoutWidget)
        self.Changelog.setObjectName(u"Changelog")
        self.Changelog.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.Changelog)

        self.Language = QPushButton(self.verticalLayoutWidget)
        self.Language.setObjectName(u"Language")
        self.Language.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.Language)


        self.retranslateUi(MenuBalk)

        QMetaObject.connectSlotsByName(MenuBalk)
    # setupUi

    def retranslateUi(self, MenuBalk):
        MenuBalk.setWindowTitle(QCoreApplication.translate("MenuBalk", u"Form", None))
        self.NameLabel.setText(QCoreApplication.translate("MenuBalk", u"GlassTapped", None))
        self.GlassesPage.setText(QCoreApplication.translate("MenuBalk", u"Overview", None))
        self.ExplorePage.setText(QCoreApplication.translate("MenuBalk", u"Explore", None))
        self.WishlistPage.setText(QCoreApplication.translate("MenuBalk", u"Wishlist", None))
        self.SettingsPage.setText(QCoreApplication.translate("MenuBalk", u"Settings", None))
        self.Text.setText(QCoreApplication.translate("MenuBalk", u"    GlassTapped", None))
        self.OverPage.setText(QCoreApplication.translate("MenuBalk", u"Over", None))
        self.Contact.setText(QCoreApplication.translate("MenuBalk", u"Contact", None))
        self.Changelog.setText(QCoreApplication.translate("MenuBalk", u"Changelog", None))
        self.Language.setText(QCoreApplication.translate("MenuBalk", u"Language", None))
    # retranslateUi

