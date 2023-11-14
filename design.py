from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject, Qt


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

        self.thmb1 = QLabel('', self.centralwidget)
        self.thmb2 = QLabel('', self.centralwidget)
        self.thmb3 = QLabel('', self.centralwidget)
        self.title1 = QLabel('', self.centralwidget)
        self.title2 = QLabel('', self.centralwidget)
        self.title3 = QLabel('', self.centralwidget)
        self.date1 = QLabel('11', self.centralwidget)
        self.date2 = QLabel('11', self.centralwidget)
        self.date3 = QLabel('11', self.centralwidget)

        self.title1.setWordWrap(True)
        self.title2.setWordWrap(True)
        self.title3.setWordWrap(True)

        self.title1.setSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        self.title1.setAlignment(Qt.AlignCenter)
        #self.title1.setMinimumSize(100, 100)
        #layout = QGridLayout(centralWidget)
        #layout.addWidget(self.label)

        self.thmb1.move(10, 50)
        self.thmb2.move(10, 170)
        self.thmb3.move(10, 270)
        self.title1.move(140, 50)
        self.title2.move(140, 170)
        self.title3.move(140, 270)
        self.date1.move(140, 120)
        self.date2.move(140, 240)
        self.date3.move(140, 340)
        self.font_ttl = QFont()  # создаём объект шрифта
        self.font_dt = QFont()
        self.font_ttl.setFamily("DejaVuSerif")  # название шрифта
        self.font_dt.setFamily("Rubik")
        self.font_ttl.setPointSize(10)  # размер шрифта
        self.font_dt.setPointSize(8)
        self.font_ttl.setUnderline(False)  # подчёркивание
        self.title1.setFont(self.font_ttl)  # задаём шрифт метке
        self.title2.setFont(self.font_ttl)
        self.title3.setFont(self.font_ttl)
        self.date1.setFont(self.font_dt)
        self.date2.setFont(self.font_dt)
        self.date3.setFont(self.font_dt)
        #self.title.setGeometry(QRect(10, 10, 200, 15))
        self.thmb1.adjustSize()

        self.lnkbtn1 = QPushButton('Смотреть', self.centralwidget)
        self.lnkbtn2 = QPushButton('Смотреть', self.centralwidget)
        self.lnkbtn3 = QPushButton('Смотреть', self.centralwidget)
        self.lnkbtn1.resize(self.lnkbtn1.sizeHint())
        self.lnkbtn2.resize(self.lnkbtn2.sizeHint())
        self.lnkbtn3.resize(self.lnkbtn3.sizeHint())
        self.lnkbtn1.move(520, 50)
        self.lnkbtn2.move(520, 170)
        self.lnkbtn3.move(520, 270)
        self.lnkbtn1.hide()
        self.lnkbtn2.hide()
        self.lnkbtn3.hide()

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(10, 10, 620, 31))
        self.lineEdit.setText("Начни с поиска видео")

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


