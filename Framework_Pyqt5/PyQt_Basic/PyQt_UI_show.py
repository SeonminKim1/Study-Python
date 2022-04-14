import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyAPP(QWidget):
    def __init__(self): # self 란 MyAPP 객체를 말함
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('../img/web.png'))
        self.setGeometry(300,300, 400, 200) # move() + resize()

        # self.move(300, 300) # 스크린의 x=300, y=300
        # self.resize(400, 200) # resize

        self.show() #


if __name__ == '__main__':
    app = QApplication(sys.argv) # 어플리케이션 객체 생성
    ex = MyAPP()
    sys.exit(app.exec_())
