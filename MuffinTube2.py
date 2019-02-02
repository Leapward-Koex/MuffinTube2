# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from convertingclass import ConvertingClass
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot)
import configparser
import traceback, sys
import os
import subprocess
import requests
import webbrowser

currentVersion = 160


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        #Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 445)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(420, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.gridLayout_4.addWidget(self.plainTextEdit, 1, 0, 1, 4)
        
        self.audioFolderOpen = QtWidgets.QPushButton(self.page)
        self.audioFolderOpen.setObjectName("audioFolderOpen")
        self.gridLayout_4.addWidget(self.audioFolderOpen, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.settingsOpen = QtWidgets.QPushButton(self.page)
        self.settingsOpen.setObjectName("settingsOpen")
        self.gridLayout_2.addWidget(self.settingsOpen, 0, 1, 1, 1)
        self.audioRadiobutton = QtWidgets.QRadioButton(self.page)
        self.audioRadiobutton.setChecked(True)
        self.audioRadiobutton.setObjectName("audioRadiobutton")
        self.gridLayout_2.addWidget(self.audioRadiobutton, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 2, 1, 1)
        self.URLinput = QtWidgets.QLineEdit(self.page)
        self.URLinput.setObjectName("URLinput")
        self.gridLayout_4.addWidget(self.URLinput, 0, 1, 1, 3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.saveSettings = QtWidgets.QPushButton(self.page_2)
        self.saveSettings.setObjectName("saveSettings")
        self.gridLayout_3.addWidget(self.saveSettings, 3, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)
        self.audioDownloadLocation = QtWidgets.QLineEdit(self.page_2)
        self.audioDownloadLocation.setObjectName("audioDownloadLocation")
        self.gridLayout_3.addWidget(self.audioDownloadLocation, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        photo = self.resource_path("photo.png")
        MainWindow.setWindowIcon(QtGui.QIcon(photo))

        self.setupConnections()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MuffinTube2", "MuffinTube2"))
        self.audioFolderOpen.setText(_translate("MainWindow", "Open Audio Folder"))
        self.settingsOpen.setText(_translate("MainWindow", "Settings"))
        self.audioRadiobutton.setText(_translate("MainWindow", "Fire"))
        self.URLinput.setPlaceholderText(_translate("MainWindow", "Paste your URL here"))
        self.saveSettings.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Audio Download Location"))

    def setupConnections(self):
        self.audioRadiobutton.clicked.connect(self.save)                #Audio option (saving)
        self.saveSettings.clicked.connect(self.save)                    #Saving settings (saving)
        #self.saveSettings.clicked.connect(self.changepage)              #Saving settings (Changing page)
        self.settingsOpen.clicked.connect(self.changepage)              #Opening settings
        self.audioFolderOpen.clicked.connect(self.openAudioFolder)
        self.URLinput.returnPressed.connect(self.convertAction)         #URL pressed enter
        self.audioRadiobutton.clicked.connect(self.addLyrics)

        self.loadSettings()
        self.threads = []                                               #Keep track of those pesky QThreads
        self.URLinput.setFocus()                                        #Making sure you can easily past URL's
        self.lyric_count = 0

    def changepage(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 2)
        self.audioDownloadLocation.setPlaceholderText(
            self.audioDownloadLocation.text())

    def save(self):
        try:
            if os.path.isdir(self.audioDownloadLocation.text()):
                config = configparser.ConfigParser() #use config[].getboolean()
                config['Main'] = {
                    'Audio directory':self.audioDownloadLocation.text()
                              }
                with open(os.getcwd() + "\\" + 'config.ini', 'w') as configfile:
                    config.write(configfile)
                self.changepage()
                self.URLinput.setFocus()
            else:
                self.audioDownloadLocation.clear()
                self.audioDownloadLocation.setPlaceholderText("Invalid directory")
        except:
            traceback.print_exc()
        
        
    def loadSettings(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.audioDownloadLocation.setText(config['Main']['Audio directory'])
        except KeyError:
            print("First time running, making config file...")
            self.save()

    def checkURL(self):
        url = self.URLinput.text()
        if "youtube.com" in url or "youtu.be" in url:
            return True
        return False

    def checkVersion(self):
        contents = requests.get("https://api.github.com/repos/Leapward-Koex/MuffinTube2/releases").json() #Json obj of version
        #contents = json.loads(contents)
        releaseVersion = contents[0]["tag_name"][1:]
        releaseVersion = int(releaseVersion.replace('.', ""))
        if releaseVersion > currentVersion:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setWindowTitle("New version available")
            msg.setText("Do you want to download the new version?")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            retval = msg.exec_()

            if retval == QtWidgets.QMessageBox.Yes:
                newReleaseUrl = "https://github.com/Leapward-Koex/MuffinTube2/releases/tag/v" + contents[0]["tag_name"][1:]
                webbrowser.open_new_tab(newReleaseUrl)

    def openAudioFolder(self):
        subprocess.call("explorer " + self.audioDownloadLocation.text(), shell=True)

    def convertAction(self):
        if self.checkURL():
            self.plainTextEdit.appendPlainText("Valid URL, starting download...")
            job = ConvertingClass(self.URLinput.text(), self.audioDownloadLocation.text())
            job.log.connect(self.appendStatus)
            job.start()
            self.threads += [job]
            print("Thread started")
        else:
            self.plainTextEdit.appendPlainText("Invalid URL")
        self.URLinput.clear()
        

    def addLyrics(self):
        self.lyrics = ["Light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "...",
                        "Light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y"
                        "Light up the sky-y-y-y",
                        "...",
                        "Boom! here comes the hurricane monsoon",
                        "Boom! Boom! here comes the hurricane monsoon",
                        "Boom! Boom! Boom! here comes the hurricane monsoon",
                        "Hurricane monsoon redecorate the room",
                        "...",
                        "Boom! here comes the hurricane monsoon",
                        "Boom! Boom! here comes the hurricane monsoon",
                        "Boom! Boom! Boom! here comes the hurricane monsoon",
                        "The hurricane monsoon", 
                        "The hurricane monsoon switched up",
                        "...",
                        "Boom! My ears are ringing from hearing the same sound",
                        "The same sound the walls just came down",
                        "...",
                        "Someday I'll die but not tonight"
                        "Excuse me while I"
                        "...",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky",
                        "Light up the sky-y-y-y",
                        "...",
                        "kick up the bass",
                        "kick up the bass and the treble",
                        "cause faith that's rebel",
                        "kick up the bass",
                        "kick up the bass and the tremble",
                        "cause faith that's rebel",
                        "...",
                        "I blaze a trail like the rays from taillights",
                        "Sound shaking the ground",
                        "Like earthquakes and hail might",
                        "...",
                        "Someday I'll die but not tonight",
                        "Excuse me while I",
                        "...",
                        "Light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "...",
                        "Nowhere else have I seen such lions led by lambs",
                        "So if you're not afraid of us",
                        "Stand up and take my hand",
                        "We got a battle upfront",
                        "But beyond that's the promised land",
                        "And when we all shout together",
                        "Man, believe me they'll understand",
                        "...",
                        "Nowhere else have I seen such lions led by lambs",
                        "(Light up the sky-y-y-y)",
                        "So if you're not afraid of us",
                        "(Light up the sky-y-y-y)",
                        "Stand up and take my hand",
                        "(Light up the sky-y-y-y)",
                        "We got a battle upfront",
                        "Light up the sky-y-y-y)",
                        "But beyond that's the promised land",
                        "(Light up the sky-y-y-y)",
                        "And when we all shout together",
                        "(Light up the sky-y-y-y)",
                        "Man, believe me they'll understand",
                        "...",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "Light up the sky-y-y-y",
                        "Watch me light up the sky-y-y-y",
                        "fin."]
                    
                    
        self.plainTextEdit.appendPlainText(self.lyrics[self.lyric_count % len(self.lyrics)])
        self.lyric_count += 1
        

    @pyqtSlot(str)
    def appendStatus(self, text):
        self.plainTextEdit.appendPlainText(text)

if QtCore.QT_VERSION >= 0x50501:
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        QtCore.qFatal('')
sys.excepthook = excepthook
       
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.checkVersion()
    sys.exit(app.exec_())


