import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


# 자체 custom 시그널 만들기 - pyqtSignal 이용
class Communicate(QObject):
    closeApp = pyqtSignal()


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # c 객체 -> communicate () 커스텀 객체
        self.c = Communicate()
        self.c.closeApp.connect(self.close) # close슬롯에 연결

        # 화면 구성
        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # Mouse Event 시 시그널 방출 ~
    def mousePressEvent(self, e):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())