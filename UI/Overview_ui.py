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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
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
        self.verticalLayoutWidget = QWidget(Overview)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 761))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.TotalGlasses_Label = QLabel(self.verticalLayoutWidget)
        self.TotalGlasses_Label.setObjectName(u"TotalGlasses_Label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.TotalGlasses_Label.setFont(font1)
        self.TotalGlasses_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TotalGlasses_Label)

        self.TotalGlasses = QLabel(self.verticalLayoutWidget)
        self.TotalGlasses.setObjectName(u"TotalGlasses")
        font2 = QFont()
        font2.setItalic(True)
        self.TotalGlasses.setFont(font2)
        self.TotalGlasses.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TotalGlasses)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.TotalDifferentGlasses = QLabel(self.verticalLayoutWidget)
        self.TotalDifferentGlasses.setObjectName(u"TotalDifferentGlasses")
        self.TotalDifferentGlasses.setFont(font2)
        self.TotalDifferentGlasses.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TotalDifferentGlasses)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.DifferentBreweries = QLabel(self.verticalLayoutWidget)
        self.DifferentBreweries.setObjectName(u"DifferentBreweries")
        self.DifferentBreweries.setFont(font2)
        self.DifferentBreweries.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.DifferentBreweries)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.MostGlasses = QLabel(self.verticalLayoutWidget)
        self.MostGlasses.setObjectName(u"MostGlasses")
        self.MostGlasses.setFont(font2)
        self.MostGlasses.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.MostGlasses)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.MostGlassesBrewery = QLabel(self.verticalLayoutWidget)
        self.MostGlassesBrewery.setObjectName(u"MostGlassesBrewery")
        self.MostGlassesBrewery.setFont(font2)
        self.MostGlassesBrewery.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.MostGlassesBrewery)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_6 = QLabel(Overview)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 350, 379, 17))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Overview)

        QMetaObject.connectSlotsByName(Overview)
    # setupUi

    def retranslateUi(self, Overview):
        Overview.setWindowTitle(QCoreApplication.translate("Overview", u"Form", None))
        self.Background.setText("")
        self.TotalGlasses_Label.setText(QCoreApplication.translate("Overview", u"Total Glasses:", None))
        self.TotalGlasses.setText(QCoreApplication.translate("Overview", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Overview", u"Total Different Glasses:", None))
        self.TotalDifferentGlasses.setText(QCoreApplication.translate("Overview", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Overview", u"Different Breweries:", None))
        self.DifferentBreweries.setText(QCoreApplication.translate("Overview", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Overview", u"Most Glasses:", None))
        self.MostGlasses.setText(QCoreApplication.translate("Overview", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Overview", u"Most Glasses from Brewery:", None))
        self.MostGlassesBrewery.setText(QCoreApplication.translate("Overview", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Overview", u"TextLabel", None))
    # retranslateUi

