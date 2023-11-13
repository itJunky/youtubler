from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject


class MMainWindow(object):  # главное окно
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.move(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Youtube Native Player")  # заголовок окна
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 785, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.lbl = QLabel('Начни с поиска видео', self.centralwidget)
        #self.lbl2 = QLabel('<i>Hello</i>, <b>world</b>!!zxcvbnm,./ <s><b>123</b></s>', self)
        self.lbl.move(10, 20)
        #self.lbl2 = QLabel('test string 22224', self)
        #self.lbl2.move(30, 30)
        self.font = QFont()  # создаём объект шрифта
        self.font.setFamily("Rubik")  # название шрифта
        self.font.setPointSize(12)  # размер шрифта
        self.font.setUnderline(False)  # подчёркивание
        self.lbl.setFont(self.font)  # задаём шрифт метке
        #self.lbl.setGeometry(QRect(10, 10, 200, 15))
        self.lbl.adjustSize()
        self.closeButton = QPushButton('Close', self.centralwidget)
        self.closeButton.resize(self.closeButton.sizeHint())
        self.closeButton.move(150, 150)
        self.closeButton.clicked.connect(QCoreApplication.instance().quit)
        self.dobtn = QPushButton('Действуй', self.centralwidget)
        self.dobtn.resize(self.dobtn.sizeHint())
        #self.dobtn.clicked.connect(self.dodobtn)
        self.dobtn.move(150, 125)
        #self.center()  # центрировать окно приложения

        QMetaObject.connectSlotsByName(MainWindow)

    def center(self):
        qr = self.frameGeometry()  # дополнительный прямоугольник
        cp = QDesktopWidget().availableGeometry().center()  # центральная точка экрана
        qr.moveCenter(cp)  # совместить центры экрана и прямоугольника
        self.move(qr.topLeft())  # переместить окно в угол отцентрированного прямоугольника


