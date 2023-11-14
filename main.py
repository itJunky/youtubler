#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from subprocess import Popen, PIPE, run
import shlex
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
        print(self.ui.lineEdit.text())
        videos = ytb_get_videos_list(self.ui.lineEdit.text())
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

        self.ui.title1.setText(videos[0]['snippet']['title'])
        self.ui.title2.setText(videos[1]['snippet']['title'])
        self.ui.title3.setText(videos[2]['snippet']['title'])

        self.ui.date1.setText(videos[0]['snippet']['publishedAt'])
        self.ui.date2.setText(videos[1]['snippet']['publishedAt'])
        self.ui.date3.setText(videos[2]['snippet']['publishedAt'])

        self.ui.date1.adjustSize()
        self.ui.date2.adjustSize()
        self.ui.date3.adjustSize()
        self.ui.thmb1.adjustSize()
        self.ui.thmb2.adjustSize()
        self.ui.thmb3.adjustSize()
        self.ui.title1.adjustSize()
        self.ui.title2.adjustSize()
        self.ui.title3.adjustSize()
        self.ui.lnkbtn1.show()
        self.ui.lnkbtn2.show()
        self.ui.lnkbtn3.show()
        self.ui.lnkbtn1.clicked.connect(lambda: self.viewbtn(vid=videos[0]['id']['videoId']))
        self.ui.lnkbtn2.clicked.connect(lambda: self.viewbtn(vid=videos[1]['id']['videoId']))
        self.ui.lnkbtn3.clicked.connect(lambda: self.viewbtn(vid=videos[2]['id']['videoId']))
        #self.ui.lnkbtn1.clicked.connect(self.viewbtn)

    def viewbtn(self, vid=None):
        vid = f'https://www.youtube.com/watch?v={vid}'
        print(f'vewbtn {vid}')
        dirtyurl = [f'ytdl -q 18 --print-url "{vid}"']

        with Popen(dirtyurl, shell=True, stdout=PIPE) as process:
            for line in process.stdout:
                extractedurl = line.decode("utf-8")

        print(f'Raw url: {extractedurl}')
        cmd = shlex.split(f'mplayer -volume 80 "{extractedurl}"')
        Popen(cmd, start_new_session=True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WorkWin()
    window.show()
    sys.exit(app.exec_())
