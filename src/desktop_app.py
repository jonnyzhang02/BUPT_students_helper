import os
import sys
import random
import tkinter

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import show_class
import choose_back
import choose_color
'''配置文件'''


class Config():
    ROOT_DIR = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'resources')


'''桌面挂件'''


class DesktopAPP(QWidget):

    def __init__(self, app_type='bupt', parent=None, **kwargs):
        super(DesktopAPP, self).__init__(parent)
        self.app_type = app_type
        self.cfg = Config()
        for key, value in kwargs.items():
            if hasattr(self.cfg, key): setattr(self.cfg, key, value)
        # 初始化
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()
        # 导入图标
        if not os.path.exists('./resources/{}'.format(app_type)): app_type = None
        if app_type is None:
            self.app_images, iconpath = self.LoadImages('bingdwendwen')
        else:
            self.app_images, iconpath = self.LoadImages(app_type)
        # 设置退出选项
        quit_action = QAction('退出', self, triggered=self.quit)
        quit_action.setIcon(QIcon(iconpath))
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(iconpath))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()
        # 当前显示的图片
        self.image = QLabel(self)
        self.setImage(self.app_images[0][0])
        # 是否跟随鼠标
        self.is_follow_mouse = False
        # 宠物拖拽时避免鼠标直接跳到左上角
        self.mouse_drag_pos = self.pos()
        # 显示
        self.resize(self.app_images[0][0].size().width(), self.app_images[0][0].size().height())
        self.randomPosition()
        self.show()
        # 宠物动画动作执行所需的一些变量
        self.is_running_action = False
        self.action_images = []
        self.action_pointer = 0
        self.action_max_len = 0
        # 每隔一段时间做个动作
        self.timer_act = QTimer()
        self.timer_act.timeout.connect(self.randomAct)
        self.timer_act.start(500)

    '''随机做一个动作'''

    def randomAct(self):
        if not self.is_running_action:
            self.is_running_action = True
            self.action_images = random.choice(self.app_images)
            self.action_max_len = len(self.action_images)
            self.action_pointer = 0
        self.runFrame()

    '''完成动作的每一帧'''

    def runFrame(self):
        if self.action_pointer == self.action_max_len:
            self.is_running_action = False
            self.action_pointer = 0
            self.action_max_len = 0
        self.setImage(self.action_images[self.action_pointer])
        self.action_pointer += 1

    '''设置当前显示的图片'''

    def setImage(self, image):
        self.image.setPixmap(QPixmap.fromImage(image))

    '''导入一个桌面挂件的图片'''

    def LoadImages(self, name):
        cfg = self.cfg
        _images = []
        object_number = len(os.listdir('./resources/{}'.format(name)))
        _images.append(
            [self.loadImage(os.path.join(cfg.ROOT_DIR, name, 'shime{}.png'.format(item + 1))) for item in
             range(1, object_number)])
        iconpath = os.path.join(cfg.ROOT_DIR, name, 'shime1.png')
        return _images, iconpath

    '''鼠标左键按下时, 挂件将和鼠标位置绑定；鼠标右键按下时, 打开主界面'''


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        if event.button() == Qt.RightButton:
            color_temp = '#000000'
            try:
                color_temp = choose_color.color_return()
                show_class.show_calendar(color_temp, save_file.bg_change())
                print(save_file.bg_change())
            except:
                show_class.show_calendar(color_temp)

            # 写入页面函数

    '''鼠标移动, 则挂件也移动'''

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            event.accept()

    '''鼠标释放时, 取消绑定'''

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    '''导入图像'''

    def loadImage(self, imagepath):
        image = QImage()
        image.load(imagepath)
        return image

    '''随机到一个屏幕上的某个位置'''

    def randomPosition(self):
        screen_geo = QDesktopWidget().screenGeometry()
        app_geo = self.geometry()

        # 真随机
        # width = (screen_geo.width() - app_geo.width()) * random.random()
        # height = (screen_geo.height() - app_geo.height()) * random.random()
        # self.move(width, height)

        # 固定在某一位置
        width = (screen_geo.width() - app_geo.width()) - 300
        height = (screen_geo.height() - app_geo.height()) - 800
        self.move(width, height)

    '''退出程序'''

    def quit(self):
        self.close()
        sys.exit()


class bupt_study():
    def __init__(self, **kwargs):
        self.supported_tools = self.initialize()
        print(self)

    '''执行对应的小程序'''

    def execute(self, config={}):
        self.supported_tools = {'desktopapp': DesktopAPP}
        app = QApplication(sys.argv)
        client = self.supported_tools['desktopapp'](**config)
        client.show()
        sys.exit(app.exec_())

    '''初始化'''

    def initialize(self):
        supported_tools = {'desktopapp': DesktopAPP}
        return supported_tools

def haha():
    client = bupt_study()
    client.execute()
