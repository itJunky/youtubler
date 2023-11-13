#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from design import MMainWindow
from ytb import ytb_get_videos_list


class WorkWin(QMainWindow):
    def __init__(self):
        super(WorkWin, self).__init__()
        self.ui = MMainWindow()
        self.ui.setupUi(self)
        self.ui.lbl.move(10, 10)
        self.ui.lbl.adjustSize()
        self.ui.dobtn.clicked.connect(self.dodbtn)

    def dodbtn(self):
        print('жмак')
        videos = ytb_get_videos_list()
        print(videos)
        print(videos[0]['snippet']['thumbnails']['default']['url'])
#        with urllib.request.urlopen(videos[0]['snippet']['thumbnails']['default']['url']) as thumburl:
#            preview = thumburl.read()
        urllib.request.urlretrieve(videos[0]['snippet']['thumbnails']['default']['url'], 'default.jpg')
        img = QPixmap('default.jpg')
        self.ui.lbl.setPixmap(img)
       # self.ui.lbl.setText(videos[0]['snippet']['title'])
        self.ui.lbl.adjustSize()
        self.ui.lbl.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WorkWin()
    window.show()
    sys.exit(app.exec_())
