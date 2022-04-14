# Box Layout - Linear Layout 느낌이 강함
# 창의 가운데 아래에 두 개의 버튼을 배치
# 두 개의 버튼은 창의 크기를 변화시켜도 같은 자리에 위치

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 2개
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 총 4칸
        hbox = QHBoxLayout()
        hbox.addStretch(1); # 빈 공간 한 칸 추가 - stretch factor 임
        hbox.addWidget(okButton); hbox.addWidget(cancelButton);
        hbox.addStretch(1) # 빈 공간 한칸 추가 - stretch factor 임

        # 세로에 대한 비율 - 수평박스(hbox)를 수직박스(vbox)에 추가
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox) # 레이아웃 자체를 추가함
        vbox.addStretch(1)

        # 화면 관련
        self.setLayout(vbox)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

# main 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())