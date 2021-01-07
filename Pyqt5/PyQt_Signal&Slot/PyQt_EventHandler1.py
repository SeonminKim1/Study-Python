import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # lcd, dial, btn 2개
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self); btn2 = QPushButton('Small', self)

        # 가로 layout
        hbox = QHBoxLayout()
        hbox.addWidget(btn1); hbox.addWidget(btn2)

        # 세로 Laout -> lcd, dial, hbox(button 2개) 순서
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # lcd display 값이 바뀔때마다
        dial.valueChanged.connect(lcd.display)

        # 버튼 눌릴때마다
        btn1.clicked.connect(self.resizeBig) # 전체 widget 화면 크기 변경
        btn2.clicked.connect(self.resizeSmall) # btn 크기 변경

        # 화면 관련
        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self):
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())