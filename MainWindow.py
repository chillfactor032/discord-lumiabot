# Python Imports
import sys
import json
import os
import datetime
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QLineEdit, QDialog
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, Signal, QObject, QTimer, QThreadPool
from PySide6.QtGui import QPixmap, QIcon, QMovie

import Resources_rc
from loglevel import LogLevel
from discordbot import DiscordBotRunner
from UI_Components import Ui_MainWindow, Ui_SettingsDialog, Ui_DebugDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        #Load UI Components
        self.setupUi(self)

        #Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        self.project_name = self.app_name.title().replace(" ", "")
        self.setWindowTitle(f"{self.app_name} {self.version}")
        
        #Load Settings
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        if(not os.path.isdir(self.config_dir)):
            os.mkdirs(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"{self.project_name}.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)
        self.refreshSettings()

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)

        # Button Signals
        self.actionDebugOutput.triggered.connect(self.viewDebugOutput)
        self.actionSettings.triggered.connect(self.viewSettingsDialog)
        self.actionSettingsFile.triggered.connect(self.viewConfigDir)

        # Create Debug Output Dialog but don't show it
        self.debug_dialog = DebugDialog()

        ## ThreadPool
        self.threadpool = QThreadPool()

        #Status Timer
        self.status_timer = QTimer(self)
        self.status_timer.setInterval(5000)
        self.status_timer.timeout.connect(self.check_status)
        self.status_timer.start()

        # Disord Bot Thread Obj
        self.discord_bot = None

        #Finally, Setup and Show the UI
        self.check_pixmap = QPixmap(":resources/img/check.png")
        self.x_pixmap = QPixmap(":resources/img/x.png")
        self.discordStatusIcon.setScaledContents(True)
        self.lumiaStatusIcon.setScaledContents(True)
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)

        self.log("Discord Lumia Bot Started")
        self.check_status()
        self.show()

    # Show the settings ini file
    def viewConfigDir(self):
        os.startfile(self.config_dir)

    # Show the settings dialog
    def viewSettingsDialog(self):
        dialog = SettingsDialog(self.settings, self)
        dialog.signals.log.connect(self.log)
        result = dialog.exec()
        if result == QDialog.Accepted:
            #Attempt to restart connections when settings are saved
            self.refreshSettings()
            self.discord_bot = DiscordBotRunner(self.discord_token, self.discord_channel_id, self.lumia_token, self.lumia_host, self.lumia_port)
            self.discord_bot.signals.log.connect(self.log)
            self.discord_bot.start()

    # Show the debug window
    def viewDebugOutput(self):
        self.debug_dialog.show()

    def refreshSettings(self):
        self.discord_token = self.settings.value(f"{self.project_name}/DiscordToken","")
        self.discord_channel_id = self.settings.value(f"{self.project_name}/DiscordChannelId","")
        self.lumia_token = self.settings.value(f"{self.project_name}/LumiaToken","")
        self.lumia_host = self.settings.value(f"{self.project_name}/LumiaHost","")
        self.lumia_port = self.settings.value(f"{self.project_name}/LumiaPort","")

    def check_status(self):
        discord_status = False
        lumia_status = False
        discord_status_msg = "Not Running"
        lumia_status_msg = "Not Running"

        if self.discord_bot is not None:
            discord_status, discord_status_msg = self.discord_bot.discord_status()
            lumia_status, lumia_status_msg = self.discord_bot.lumia_status()

        if discord_status:
            self.discordStatusIcon.setPixmap(self.check_pixmap)
        else:
            self.discordStatusIcon.setPixmap(self.x_pixmap)
        if lumia_status:
            self.lumiaStatusIcon.setPixmap(self.check_pixmap)
        else:
            self.lumiaStatusIcon.setPixmap(self.x_pixmap)
            if self.discord_bot is not None:
                self.log("Attempting to reconnect to LumiaStream Websocket")
                self.discord_bot.lumia_start()
        self.discordStatusLabel.setText(discord_status_msg)
        self.lumiaStatusLabel.setText(lumia_status_msg)

    # Forward log messages to the log window
    def log(self, msg, level=LogLevel.INFO):
        self.debug_dialog.log(msg, level)

    # App is closing, cleanup
    def closeEvent(self, evt):
        # Close Debug Window if its opened
        self.debug_dialog.close()

        # Stop Threads
        if self.discord_bot is not None:
            self.discord_bot.close()

        # Remember the size and position of the GUI
        self.settings.setValue(f"{self.project_name}/geometry", self.saveGeometry())
        self.settings.setValue(f"{self.project_name}/windowState", self.saveState())
        self.settings.sync()
        evt.accept()

class DebugDialog(QDialog):

    def __init__(self, icon=None, parent=None):
        super().__init__(None)
        self.setModal(False)
        self.ui = Ui_DebugDialog()
        self.ui.setupUi(self)

        #Set window Icon
        if icon is None:
            # If not icon is provided, use a Qt default
            default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
            icon = self.style().standardIcon(default_icon_pixmap)
        self.setWindowIcon(icon)

        

    def log(self, msg, level=LogLevel.INFO):
        if not msg:
            return
        print(msg)
        if(level == LogLevel.ERROR):
            style = "color: #cc0000;"
        elif(level == LogLevel.DEBUG):
            style = "color: #006600;"
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
        self.ui.logBrowser.append(msg)
        
    def reject(self):
        self.hide()

class SettingsDialog(QDialog):

    class Signals(QObject):
        log = Signal(str, LogLevel)
    
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.signals = self.Signals()
        self.parent_obj = parent
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.saveButtonClick)
        self.ui.cancelButton.clicked.connect(self.cancelButtonClick)
        self.ui.discord_token_line_edit.setEchoMode(QLineEdit.Password)
        self.settings = settings
        self.ui.discord_token_line_edit.setText(settings.value(f"{self.parent_obj.project_name}/DiscordToken",""))
        self.ui.discord_channel_line_edit.setText(settings.value(f"{self.parent_obj.project_name}/DiscordChannelId",""))
        self.ui.lumia_host_line_edit.setText(settings.value(f"{self.parent_obj.project_name}/LumiaHost",""))
        self.ui.lumia_port_line_edit.setText(settings.value(f"{self.parent_obj.project_name}/LumiaPort",""))
        self.ui.lumia_token_line_edit.setText(settings.value(f"{self.parent_obj.project_name}/LumiaToken",""))

    def log(self, msg, level=LogLevel.INFO):
        self.signals.log.emit(msg, level)

    def saveButtonClick(self):
        discord_token = self.ui.discord_token_line_edit.text()
        discord_channel_id = self.ui.discord_channel_line_edit.text()
        lumia_token = self.ui.lumia_token_line_edit.text()
        lumia_host = self.ui.lumia_host_line_edit.text()
        lumia_port = self.ui.lumia_port_line_edit.text()
        self.settings.setValue(f"{self.parent_obj.project_name}/DiscordToken",discord_token)
        self.settings.setValue(f"{self.parent_obj.project_name}/DiscordChannelId",discord_channel_id)
        self.settings.setValue(f"{self.parent_obj.project_name}/LumiaHost",lumia_host)
        self.settings.setValue(f"{self.parent_obj.project_name}/LumiaPort",lumia_port)
        self.settings.setValue(f"{self.parent_obj.project_name}/LumiaToken",lumia_token)
        self.settings.sync()
        self.log("Settings Saved")
        self.accept()
        
    def cancelButtonClick(self):
        self.reject()

# Start the PySide6 App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    version_file = QFile(":version.json")
    version_file.open(QFile.ReadOnly)
    text_stream = QTextStream(version_file)
    version_file_text = text_stream.readAll()
    version_dict = json.loads(version_file_text)
    org_name = version_dict["company_name"]
    app_name = version_dict["product_name"]
    version = version_dict["version"]
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    window = MainWindow()
    sys.exit(app.exec())