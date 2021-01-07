
# 어플리케이션 구조

# ---- Menu Bar ---- (메뉴바 맨 상단)
# ---- Toolbars ---- ( 툴 바 )
# - central widget -
# -                -
# --- Status Bar --- (상태바 맨 하단)
# 메인창의 레이아웃
# QMenuBar, QtoolBar, QdockWidget, QStatusBar를 위한 고유의 레이아웃을 가지고 있음
# 또한 가운데 영역에 중심위젯 (Central Widge)을 위한 영역을 가짐
# QMainWindow 클래스를 이용해서 메인 어플리케이션 창을 만들 수 있음
#

# 상태바, 메뉴바 만들기


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 종료 Action 관련 action 만들기
        exitAction = QAction(QIcon('../img/exit.png'), 'Exit', self) # action 이미지 넣기
        exitAction.setShortcut('Ctrl+Q') # 파일메뉴안의 메뉴항목에 대한 바로가기 버튼
        exitAction.setStatusTip('Exit Application') # action 작동시 status bar 관련
        exitAction.triggered.connect(qApp.quit) # 생성된 시그널을 QApplication 위젯의 quit() 메서드에 연결 및 어플리케이션 종료

        # Edit Action 관련 action 만들기
        EditAction = QAction('edit test', self)
        EditAction.setShortcut('Ctrl+E')
        EditAction.setStatusTip('Edit Application')

        # 상태바 메서드
        self.statusBar().showMessage('Ready')

        # 메뉴바 메서드 (메뉴바에 항목 2개 붙이기)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 1. 파일메뉴
        filemenu = menubar.addMenu('&File') # Alt + F라는 뜻
        filemenu.addAction(exitAction) # filemenu에 Action 달기

        # 2. 편집메뉴
        EditMenu = menubar.addMenu('&Edit') # Alt + E라는 단축키
        EditMenu.addAction(EditAction)

        # 3. toolbar 부착
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # Window 옵션
        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())