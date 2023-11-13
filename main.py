#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from design import MMainWindow


class WorkWin(QMainWindow):
    def __init__(self):
        super(WorkWin, self).__init__()
        self.ui = MMainWindow()
        self.ui.setupUi(self)
        #self.ui.lbl.setText('ssss')
        self.ui.lbl.move(10, 10)
        self.ui.lbl.adjustSize()
        self.ui.dobtn.clicked.connect(self.dododobtn)

    def dododobtn(self):
        print('жмак')
        self.ui.lbl.setText('text')
        self.ui.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WorkWin()
    #window = MainWindow()
    window.show()
    sys.exit(app.exec_())
