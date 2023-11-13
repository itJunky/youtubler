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
        self.ui.dobtn.clicked.connect(self.dodbtn)

    def dodbtn(self):
        print('жмак')
        videos = ytb_get_videos_list()
        print(videos)
        print(videos[0]['snippet']['thumbnails']['default']['url'])
        urllib.request.urlretrieve(videos[0]['snippet']['thumbnails']['default']['url'], 'default1.jpg')
        urllib.request.urlretrieve(videos[1]['snippet']['thumbnails']['default']['url'], 'default2.jpg')
        urllib.request.urlretrieve(videos[2]['snippet']['thumbnails']['default']['url'], 'default3.jpg')
        img1 = QPixmap('default1.jpg')
        img2 = QPixmap('default2.jpg')
        img3 = QPixmap('default3.jpg')
        self.ui.thmb1.setPixmap(img1)
        self.ui.thmb2.setPixmap(img2)
        self.ui.thmb3.setPixmap(img3)
        self.ui.lbl1.setText(videos[0]['snippet']['title'])
        self.ui.lbl2.setText(videos[1]['snippet']['title'])
        self.ui.lbl3.setText(videos[2]['snippet']['title'])
        self.ui.thmb1.adjustSize()
        self.ui.thmb2.adjustSize()
        self.ui.thmb3.adjustSize()
        self.ui.lbl1.adjustSize()
        self.ui.lbl2.adjustSize()
        self.ui.lbl3.adjustSize()
        #self.ui.thmb1.show()


    def viewbtn(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WorkWin()
    window.show()
    sys.exit(app.exec_())
