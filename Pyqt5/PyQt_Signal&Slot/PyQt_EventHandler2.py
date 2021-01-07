# 이벤트 핸들러 설명
# keyPressEvent	키보드를 눌렀을 때 동작합니다.
# keyReleaseEvent	키보드를 눌렀다가 뗄 때 동작합니다.
# mouseDoubleClickEvent	마우스를 더블클릭할 때 동작합니다.
# mouseMoveEvent	마우스를 움직일 때 동작합니다.
# mousePressEvent	마우스를 누를 때 동작합니다.
# mouseReleaseEvent	마우스를 눌렀다가 뗄 때 동작합니다.
# moveEvent	위젯이 이동할 때 동작합니다.
# resizeEvent	위젯의 크기를 변경할 때 동작합니다.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 화면 관련
    def initUI(self):

        # 마우스 관련 UI
        x, y = 0, 0
        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)
        self.setMouseTracking(True)

        # 화면 구성
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 500, 500)
        self.show()

    # Key Event 등록 - Esc, F, N 기능
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape: # 창 종료
            self.close()
        elif e.key() == Qt.Key_F: # 최대화
            self.showFullScreen()
        elif e.key() == Qt.Key_N: # 보통 크기
            self.showNormal()

    # mouse event 등록 - 현재 마우스 위치 label에 나타내주기
    def mouseMoveEvent(self, e):
        x, y = e.x(), e.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())