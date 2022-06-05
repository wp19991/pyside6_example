from PySide6.QtCore import QTimer, QEvent
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow

from core.mySystemTrayIcon import MySystemTrayIcon
from core.customGrips import CustomGrip
from ui.main_window import Ui_MainWindow as main_window


class main_win(QMainWindow, main_window):
    def __init__(self):
        super(main_win, self).__init__()
        self.dragPos = None
        self.setupUi(self)

        # 程序托盘图标
        self.tray_icon = MySystemTrayIcon()
        self.tray_icon.init(self)  # 将自己传进去
        self.tray_icon.show()

        # 设置程序样式
        # str = open(r"ui\themes\dark.qss", 'r').read()
        # self.setStyleSheet(str)

        # 设置程序无框
        self.set_windows_hint()

    def set_windows_hint(self):
        # 设置程序无框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置右击标题栏可以移动框
        self.topBar_container_title_label.mouseMoveEvent = self.moveWindow
        # 设置双击右击标题栏可以最大化程序框
        self.topBar_container_title_label.mouseDoubleClickEvent = self.doubleClickMaximizeRestore

        # 设置最小化按钮
        self.top_minimize_pushButton.clicked.connect(self.showMinimized)

        # 设置最大化按钮
        self.is_max = False
        self.top_maximize_restore_pushButton.clicked.connect(self.maximize_restore)

        # 设置关闭按钮
        self.top_close_pushButton.clicked.connect(self.close)

        # 设置用户选择边框进行界面大小修改
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def resizeEvent(self, event):
        # 修改界面大小
        self.resize_grips()

    def doubleClickMaximizeRestore(self, event):
        # 如果双击了标题 最大最小化
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: self.maximize_restore())

    def maximize_restore(self):
        # 最大最小化
        if self.is_max:
            self.is_max = False
            self.showNormal()
        else:
            self.is_max = True
            self.showMaximized()

    def moveWindow(self, event):
        # 移动窗口
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        # 捕捉界面内部鼠标点击的情况
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
