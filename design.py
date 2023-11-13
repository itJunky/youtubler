from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject


class MMainWindow(object):  # главное окно
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.move(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Youtube Native Player")  # заголовок окна
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 785, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.thmb1 = QLabel('Начни с поиска видео', self.centralwidget)
        self.thmb2 = QLabel('', self.centralwidget)
        self.thmb3 = QLabel('', self.centralwidget)
        self.lbl1 = QLabel('', self.centralwidget)
        self.lbl2 = QLabel('', self.centralwidget)
        self.lbl3 = QLabel('', self.centralwidget)
        self.thmb1.move(10, 10)
        self.thmb2.move(10, 130)
        self.thmb3.move(10, 230)
        self.lbl1.move(140, 10)
        self.lbl2.move(140, 130)
        self.lbl3.move(140, 230)
        self.font = QFont()  # создаём объект шрифта
        self.font.setFamily("Rubik")  # название шрифта
        self.font.setPointSize(12)  # размер шрифта
        self.font.setUnderline(False)  # подчёркивание
        self.thmb1.setFont(self.font)  # задаём шрифт метке
        #self.lbl.setGeometry(QRect(10, 10, 200, 15))
        self.thmb1.adjustSize()
        self.closeButton = QPushButton('Close', self.centralwidget)
        self.closeButton.resize(self.closeButton.sizeHint())
        self.closeButton.move(260, 400)
        self.closeButton.clicked.connect(QCoreApplication.instance().quit)
        self.dobtn = QPushButton('Действуй', self.centralwidget)
        self.dobtn.resize(self.dobtn.sizeHint())
        #self.dobtn.clicked.connect(self.dodobtn)
        self.dobtn.move(350, 400)
        #self.center()  # центрировать окно приложения

        QMetaObject.connectSlotsByName(MainWindow)

    def center(self):
        qr = self.frameGeometry()  # дополнительный прямоугольник
        cp = QDesktopWidget().availableGeometry().center()  # центральная точка экрана
        qr.moveCenter(cp)  # совместить центры экрана и прямоугольника
        self.move(qr.topLeft())  # переместить окно в угол отцентрированного прямоугольника


