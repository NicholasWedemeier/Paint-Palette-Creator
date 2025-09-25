#test for color picker pyqt

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QColor
from PaletteCreatorPrograms import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Paint Palette Creator'

        screen = QGuiApplication.primaryScreen()
        screenGeometry = screen.geometry()
        availableGeometry = screen.availableGeometry()

        screenWidth = availableGeometry.width()
        screenHeight = availableGeometry.height()

        self.width = 750
        self.height = 500

        self.left = int(screenWidth / 2 - self.width / 2)
        self.top = int(screenHeight / 2 - self.height / 2)        
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #THIS IS A TEST

        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.move(10,10)
        button.clicked.connect(self.on_click)

        #TODO: RENAME BUTTONS TO SOMETHING BETTER THAN BUTTON2

        button2 = QPushButton('Create New Palette', self)
        button2.setToolTip('Creates new user palette')
        button2.move(150,10)
        button2.clicked.connect(paletteCreator)

        button3 = QPushButton('Load Saved Palettes', self)
        button3.setToolTip('Loads Palettes from storage')
        button3.move(10,50)
        button3.clicked.connect(loadPalettesFromStorage)
    
        self.show()

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(color.name())
    @pyqtSlot()    
    def on_click(self):
        self.openColorDialog()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())