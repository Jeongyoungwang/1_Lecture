import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import uic
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import re
import datetime

#form_class = uic.loadUiType("C:/coding/python/6_GUI/ui/you_viewer_v1.0.ui")[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #초기화
        self.initAuthLock() #확인버튼 락

        self.initSignal()

        #로그인 관련 변수 선언
        self.user_id = None
        self.user_pw = None

        #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

        #기본 UI 비활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authcheck)

    @pyqtSlot()
    def authcheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

    # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
    # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣어주세요.
    # code
    # code
        #print("id: %s password: %s" %(self.user_id,self.user_pw))

        if True:
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)

        else:
            QMessageBox.about(self, "인증오류", "아이디 혹은 비밀번호 인증 오류")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
