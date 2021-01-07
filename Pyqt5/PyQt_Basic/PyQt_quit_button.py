# 시그널과 슬롯 메커니즘
# btn 클릭시  시그널이 만들어지고,
# 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됨
# 발신자(Sender)와 수신자(Receiver), 두 객체 간의 커뮤니케이션이 이루어짐
# 이 예제에서 발신자는 푸시버튼 (btn)이고, 수신자는 어플리케이션 (app)

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # QPush Button
        btn = QPushButton('Quit', self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300,300,400,200)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
