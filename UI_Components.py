# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DebugDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_DebugDialog(object):
    def setupUi(self, DebugDialog):
        if not DebugDialog.objectName():
            DebugDialog.setObjectName(u"DebugDialog")
        DebugDialog.resize(800, 600)
        self.logBrowser = QTextBrowser(DebugDialog)
        self.logBrowser.setObjectName(u"logBrowser")
        self.logBrowser.setGeometry(QRect(10, 10, 781, 581))

        self.retranslateUi(DebugDialog)

        QMetaObject.connectSlotsByName(DebugDialog)
    # setupUi

    def retranslateUi(self, DebugDialog):
        DebugDialog.setWindowTitle(QCoreApplication.translate("DebugDialog", u"Debug Log", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DiscordBot.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(366, 262)
        self.actionDebugOutput = QAction(MainWindow)
        self.actionDebugOutput.setObjectName(u"actionDebugOutput")
        self.actionSettingsFile = QAction(MainWindow)
        self.actionSettingsFile.setObjectName(u"actionSettingsFile")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 43, 40))
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.discordStatusIcon = QLabel(self.centralwidget)
        self.discordStatusIcon.setObjectName(u"discordStatusIcon")
        self.discordStatusIcon.setGeometry(QRect(70, 10, 40, 40))
        self.discordStatusIcon.setMinimumSize(QSize(40, 40))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 60, 351, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 43, 40))
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lumiaStatusIcon = QLabel(self.centralwidget)
        self.lumiaStatusIcon.setObjectName(u"lumiaStatusIcon")
        self.lumiaStatusIcon.setGeometry(QRect(70, 80, 40, 40))
        self.lumiaStatusIcon.setMinimumSize(QSize(40, 40))
        self.discordStatusLabel = QLabel(self.centralwidget)
        self.discordStatusLabel.setObjectName(u"discordStatusLabel")
        self.discordStatusLabel.setGeometry(QRect(130, 10, 231, 41))
        self.discordStatusLabel.setMinimumSize(QSize(0, 40))
        self.lumiaStatusLabel = QLabel(self.centralwidget)
        self.lumiaStatusLabel.setObjectName(u"lumiaStatusLabel")
        self.lumiaStatusLabel.setGeometry(QRect(130, 80, 231, 41))
        self.lumiaStatusLabel.setMinimumSize(QSize(0, 40))
        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(10, 170, 75, 24))
        self.debug_button = QPushButton(self.centralwidget)
        self.debug_button.setObjectName(u"debug_button")
        self.debug_button.setGeometry(QRect(100, 170, 75, 24))
        self.config_button = QPushButton(self.centralwidget)
        self.config_button.setObjectName(u"config_button")
        self.config_button.setGeometry(QRect(190, 170, 75, 24))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 150, 351, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 366, 22))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuEdit.addAction(self.actionSettings)
        self.menuView.addAction(self.actionDebugOutput)
        self.menuView.addAction(self.actionSettingsFile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Discord-Lumia Bot", None))
        self.actionDebugOutput.setText(QCoreApplication.translate("MainWindow", u"Debug Output", None))
        self.actionSettingsFile.setText(QCoreApplication.translate("MainWindow", u"Config Directory", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Discord:", None))
        self.discordStatusIcon.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lumia:", None))
        self.lumiaStatusIcon.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.discordStatusLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lumiaStatusLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.debug_button.setText(QCoreApplication.translate("MainWindow", u"Debug Log", None))
        self.config_button.setText(QCoreApplication.translate("MainWindow", u"Config Dir", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(400, 428)
        self.groupBox = QGroupBox(SettingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 181))
        self.discord_token_line_edit = QLineEdit(self.groupBox)
        self.discord_token_line_edit.setObjectName(u"discord_token_line_edit")
        self.discord_token_line_edit.setGeometry(QRect(80, 30, 291, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 61, 21))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 61, 21))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.discord_channel_line_edit = QLineEdit(self.groupBox)
        self.discord_channel_line_edit.setObjectName(u"discord_channel_line_edit")
        self.discord_channel_line_edit.setGeometry(QRect(80, 70, 291, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 341, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 341, 16))
        self.groupBox_2 = QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 200, 381, 181))
        self.lumia_host_line_edit = QLineEdit(self.groupBox_2)
        self.lumia_host_line_edit.setObjectName(u"lumia_host_line_edit")
        self.lumia_host_line_edit.setGeometry(QRect(80, 20, 151, 22))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 61, 21))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lumia_token_line_edit = QLineEdit(self.groupBox_2)
        self.lumia_token_line_edit.setObjectName(u"lumia_token_line_edit")
        self.lumia_token_line_edit.setGeometry(QRect(80, 50, 291, 22))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 50, 61, 21))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 90, 341, 16))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 140, 341, 16))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 110, 341, 16))
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 20, 51, 21))
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lumia_port_line_edit = QLineEdit(self.groupBox_2)
        self.lumia_port_line_edit.setObjectName(u"lumia_port_line_edit")
        self.lumia_port_line_edit.setGeometry(QRect(300, 20, 71, 22))
        self.saveButton = QPushButton(SettingsDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(220, 390, 75, 24))
        self.cancelButton = QPushButton(SettingsDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(310, 390, 75, 24))

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Discord", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Token:", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Channel ID:", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Token will be used to authenticate itself to Discord", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Channel ID will be the channel the bot will monitor. ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"LumiaStream", None))
        self.lumia_host_line_edit.setText(QCoreApplication.translate("SettingsDialog", u"localhost", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Host:", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Token:", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Host/Port are found in LumiaStream > Settings > API", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Token will be used to authenticate itself to LumiaStream", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"      e.g. http://localhost:39231/api", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Port:", None))
        self.lumia_port_line_edit.setText(QCoreApplication.translate("SettingsDialog", u"39231", None))
        self.saveButton.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("SettingsDialog", u"Cancel", None))
    # retranslateUi



