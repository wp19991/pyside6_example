# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import app_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(749, 470)
        icon = QIcon()
        icon.addFile(u":/icon/icon/app.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
" color: rgb(221, 221, 221);\n"
" font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/*appFrame*/\n"
"#appFrame  {\n"
" background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/*leftMenuBar*/\n"
"#leftMenuBar  {\n"
" background-color: rgb(33, 37, 43);\n"
"}\n"
"#leftMenuBar QPushButton {\n"
" background-color: rgba(255, 255, 255, 0);\n"
" border: none;\n"
"}\n"
"\n"
"#leftMenuBar QPushButton:hover {\n"
" background-color: rgb(40, 44, 52);\n"
"}\n"
"#leftMenuBar QPushButton:pressed {	\n"
" background-color: rgb(189, 147, 249);\n"
" color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*pagesContainer*/\n"
"#pagesContainer  {\n"
" background-color: rgb(44, 49, 58);\n"
"}\n"
"#pagesContainer QWidget {\n"
" background-color: rgb(44, 49, 58);\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
" border: 2px solid rgb(52, 59, 72);\n"
" border-radius: 5px;	\n"
" background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
" background-color: rgb(57, 65, 80);\n"
" border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pages"
                        "Container QPushButton:pressed {	\n"
" background-color: rgb(35, 40, 49);\n"
" border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/*topBar*/\n"
"#topBar {\n"
" background-color: rgb(44, 49, 58);\n"
"}\n"
"#topBar  QLabel {\n"
" font-size: 11px;\n"
" color: rgb(113, 126, 149);\n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
" padding-bottom: 2px;\n"
"}\n"
"\n"
"#top_right_buttons QPushButton#top_close_pushButton {\n"
" background-color:  rgb(206, 81, 55);\n"
" border-radius:14px;\n"
"}\n"
"#top_right_buttons QPushButton#top_close_pushButton:hover {\n"
" background-color: rgba(206, 81, 55,150);\n"
"}\n"
"#top_right_buttons QPushButton#top_maximize_restore_pushButton {\n"
" background-color: rgb(232, 201, 73);\n"
" border-radius:14px;\n"
"}\n"
"#top_right_buttons QPushButton#top_maximize_restore_pushButton:hover {\n"
" background-color: rgba(232, 201, 73,150);\n"
"}\n"
"#top_right_buttons QPushButton#top_minimize_pushButton {\n"
" background-color: rgb(161, 198, 97);\n"
" border-radius:14px;\n"
"}\n"
"#top_ri"
                        "ght_buttons QPushButton#top_minimize_pushButton:hover {\n"
" background-color: rgba(161, 198, 97,150);\n"
"}\n"
"\n"
"/*bottomBar*/\n"
"#bottomBar {\n"
" background-color: rgb(44, 49, 58);\n"
"}\n"
"#bottomBar  QLabel {\n"
" font-size: 11px;\n"
" color: rgb(113, 126, 149);\n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
" padding-bottom: 2px;\n"
"}\n"
"#frame_size_grip{\n"
" width: 20px;\n"
" height: 20px;\n"
" margin: 0px;\n"
" padding: 0px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.appFrame = QFrame(self.centralwidget)
        self.appFrame.setObjectName(u"appFrame")
        self.appFrame.setFrameShape(QFrame.StyledPanel)
        self.appFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.appFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBar = QFrame(self.appFrame)
        self.leftMenuBar.setObjectName(u"leftMenuBar")
        self.leftMenuBar.setMinimumSize(QSize(60, 0))
        self.leftMenuBar.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBar.setLayoutDirection(Qt.LeftToRight)
        self.leftMenuBar.setFrameShape(QFrame.StyledPanel)
        self.leftMenuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.leftMenuBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logo_pushButton = QPushButton(self.leftMenuBar)
        self.logo_pushButton.setObjectName(u"logo_pushButton")
        self.logo_pushButton.setMinimumSize(QSize(60, 60))
        self.logo_pushButton.setMaximumSize(QSize(16777215, 60))
        self.logo_pushButton.setStyleSheet(u"image: url(:/icon/icon/app.ico);")

        self.verticalLayout_5.addWidget(self.logo_pushButton)

        self.toggleButton = QPushButton(self.leftMenuBar)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(45, 45))
        self.toggleButton.setMaximumSize(QSize(16777215, 45))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"image: url(:/icon/icon/icon_menu.png);")

        self.verticalLayout_5.addWidget(self.toggleButton)

        self.speed_pushButton = QPushButton(self.leftMenuBar)
        self.speed_pushButton.setObjectName(u"speed_pushButton")
        self.speed_pushButton.setMinimumSize(QSize(45, 45))
        self.speed_pushButton.setMaximumSize(QSize(16777215, 45))
        self.speed_pushButton.setStyleSheet(u"image: url(:/icon/icon/cil-speedometer.png);")
        self.speed_pushButton.setAutoRepeat(False)

        self.verticalLayout_5.addWidget(self.speed_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.exit_pushButton = QPushButton(self.leftMenuBar)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setMinimumSize(QSize(45, 45))
        self.exit_pushButton.setMaximumSize(QSize(16777215, 45))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_pushButton.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.exit_pushButton)


        self.horizontalLayout_4.addWidget(self.leftMenuBar)

        self.contentBox = QFrame(self.appFrame)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.StyledPanel)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.contentBox)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 50))
        self.topBar.setMaximumSize(QSize(16777215, 50))
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.topBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_right_buttons = QFrame(self.topBar)
        self.top_right_buttons.setObjectName(u"top_right_buttons")
        self.top_right_buttons.setMinimumSize(QSize(0, 28))
        self.top_right_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_right_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_right_buttons)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBar_container_title_label = QLabel(self.top_right_buttons)
        self.topBar_container_title_label.setObjectName(u"topBar_container_title_label")
        self.topBar_container_title_label.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_2.addWidget(self.topBar_container_title_label)

        self.top_minimize_pushButton = QPushButton(self.top_right_buttons)
        self.top_minimize_pushButton.setObjectName(u"top_minimize_pushButton")
        self.top_minimize_pushButton.setMinimumSize(QSize(28, 28))
        self.top_minimize_pushButton.setMaximumSize(QSize(28, 28))
        self.top_minimize_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.top_minimize_pushButton.setIcon(icon2)
        self.top_minimize_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.top_minimize_pushButton)

        self.top_maximize_restore_pushButton = QPushButton(self.top_right_buttons)
        self.top_maximize_restore_pushButton.setObjectName(u"top_maximize_restore_pushButton")
        self.top_maximize_restore_pushButton.setMinimumSize(QSize(28, 28))
        self.top_maximize_restore_pushButton.setMaximumSize(QSize(28, 28))
        self.top_maximize_restore_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.top_maximize_restore_pushButton.setIcon(icon3)
        self.top_maximize_restore_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.top_maximize_restore_pushButton)

        self.top_close_pushButton = QPushButton(self.top_right_buttons)
        self.top_close_pushButton.setObjectName(u"top_close_pushButton")
        self.top_close_pushButton.setMinimumSize(QSize(28, 28))
        self.top_close_pushButton.setMaximumSize(QSize(28, 28))
        self.top_close_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.top_close_pushButton.setIcon(icon4)
        self.top_close_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.top_close_pushButton)


        self.horizontalLayout_3.addWidget(self.top_right_buttons)


        self.verticalLayout_2.addWidget(self.topBar)

        self.pagesContainer = QFrame(self.contentBox)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setFrameShape(QFrame.StyledPanel)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.pagesContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"x")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.pushButton = QPushButton(self.home_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 50, 75, 24))
        self.stackedWidget.addWidget(self.home_page)
        self.second_page = QWidget()
        self.second_page.setObjectName(u"second_page")
        self.stackedWidget.addWidget(self.second_page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.pagesContainer)

        self.bottomBar = QFrame(self.contentBox)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setFrameShape(QFrame.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottomBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomBar_log_label = QLabel(self.bottomBar)
        self.bottomBar_log_label.setObjectName(u"bottomBar_log_label")
        self.bottomBar_log_label.setMinimumSize(QSize(0, 22))
        self.bottomBar_log_label.setMaximumSize(QSize(16777215, 22))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setItalic(False)
        self.bottomBar_log_label.setFont(font)
        self.bottomBar_log_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.bottomBar_log_label)

        self.bottomBar_version_label = QLabel(self.bottomBar)
        self.bottomBar_version_label.setObjectName(u"bottomBar_version_label")
        self.bottomBar_version_label.setMinimumSize(QSize(0, 22))
        self.bottomBar_version_label.setMaximumSize(QSize(16777215, 22))
        self.bottomBar_version_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.bottomBar_version_label)


        self.verticalLayout_2.addWidget(self.bottomBar)


        self.horizontalLayout_4.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.appFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toggleButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyside6_app", None))
        self.logo_pushButton.setText("")
        self.toggleButton.setText("")
        self.speed_pushButton.setText("")
        self.exit_pushButton.setText("")
        self.topBar_container_title_label.setText(QCoreApplication.translate("MainWindow", u"pyside6", None))
        self.top_minimize_pushButton.setText("")
        self.top_maximize_restore_pushButton.setText("")
        self.top_close_pushButton.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.bottomBar_log_label.setText(QCoreApplication.translate("MainWindow", u"By: github@wp19991", None))
        self.bottomBar_version_label.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

