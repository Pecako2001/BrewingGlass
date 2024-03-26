# Import necessary modules
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, Signal
from PySide6.QtWidgets import QWidget, QMenu, QAction, QLabel, QHBoxLayout
from UI.Glass_Widget_ui import Ui_Glass_Widget  # Adjust the import path according to your project structure


class Glass_Widget(QDialog, Ui_Glass_Widget):
    def __init__(self, parent=None):
        super(Glass_Widget, self).__init__(parent)
        self.setupUi(self)

    def mousePressEvent(self, event):
        super(Glass_Widget, self).mousePressEvent(event)

        # Check if the right side of the widget is clicked
        if event.button() == Qt.RightButton and event.pos().x() > self.width() / 2:
            self.createContextMenu(event.pos())

    def createContextMenu(self, position):
        contextMenu = QMenu(self)

        # Add minus button
        minusAction = QAction('-', self)
        minusAction.triggered.connect(self.decrementAmount)
        contextMenu.addAction(minusAction)

        # Add amount label
        amountLabel = QLabel(str(self.amount))
        amountLabel.setAlignment(Qt.AlignCenter)
        actionAmount = QWidgetAction(self)
        actionAmount.setDefaultWidget(amountLabel)
        contextMenu.addAction(actionAmount)

        # Add plus button
        plusAction = QAction('+', self)
        plusAction.triggered.connect(self.incrementAmount)
        contextMenu.addAction(plusAction)

        # Add delete button
        deleteAction = QAction('Delete', self)
        deleteAction.triggered.connect(self.deleteItem)
        contextMenu.addAction(deleteAction)

        contextMenu.exec(self.mapToGlobal(position))

    def incrementAmount(self):
        self.amount += 1
        self.Amount.setText(str(self.amount))
        self.amountChanged.emit(self.amount, self.glass_id)

    def decrementAmount(self):
        if self.amount > 0:
            self.amount -= 1
            self.Amount.setText(str(self.amount))
            self.amountChanged.emit(self.amount, self.glass_id)

    def deleteItem(self):
        self.deleteRequested.emit(self.glass_id)
        self.deleteLater()