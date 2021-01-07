# 기타
# 화면 중앙에 어플리케이션 오게하기
# QWidget - frameGeometry() : 창의 위치와 크기 정보 가져오기

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
from PyQt5.QtCore import QDate, Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 화면 관련
        self.setWindowTitle('Centering')
        self.setGeometry(300, 300, 500, 500)
        self.center()

        self.date_statusbar()
        self.show()

    def center(self):
        qr = self.frameGeometry() # 메서드를 이용한 창의 위치와 크기 정보 가져오기
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면의 중앙위치 파악하기
        qr.moveCenter(cp) # center로 움직이기 (창만 움직임)
        self.move(qr.topLeft()) # 실제 움직이기 (윈도우까지?)

    def date_statusbar(self):
        now = QDate.currentDate()
        self.statusBar().showMessage(now.toString(Qt.DefaultLocaleLongDate))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())