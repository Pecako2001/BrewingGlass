from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QGraphicsOpacityEffect

class OverlayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_StyledBackground, False)
        self.setGeometry(parent.rect())
        self.setStyleSheet("background-color: rgba(0, 0, 255, 127);")  # Bright blue, semi-transparent

        self.opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacityEffect)
        self.opacityEffect.setOpacity(0)

    def fadeIn(self, duration=500):
        self.show()
        animation = QPropertyAnimation(self.opacityEffect, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.start()

    def fadeOut(self, duration=500):
        animation = QPropertyAnimation(self.opacityEffect, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(self.opacityEffect.opacity())
        animation.setEndValue(0)
        animation.finished.connect(self.hide)
        animation.start()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: orange;")  # Bright orange background

        fadeInButton = QPushButton("Fade In Overlay", self)
        fadeInButton.clicked.connect(self.showOverlay)
        fadeInButton.move(50, 50)

        fadeOutButton = QPushButton("Fade Out Overlay", self)
        fadeOutButton.clicked.connect(self.hideOverlay)
        fadeOutButton.move(50, 100)

        self.overlay = OverlayWidget(self)

    def showOverlay(self):
        self.overlay.fadeIn()

    def hideOverlay(self):
        self.overlay.fadeOut()

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
