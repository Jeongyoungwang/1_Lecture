import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TestForm(QMainWindow):
    def __init__(self):
        super().__init__() #부모 슈퍼 초기화 함수
        self.setupUI()

    def setupUI(self): #창에다가 붙이는것들
        self.setWindowTitle("PyQT Test") #제목
        self.setGeometry(800,400,500,300) #창크기

        btn_1 = QPushButton("Click1", self)
        btn_2 = QPushButton("Click2", self)
        btn_3 = QPushButton("Click3", self)

        btn_1.move(20, 20)
        btn_2.move(20, 60)
        btn_3.move(20, 100)

#시그널과 슬롯 기능 예시
        btn_1.clicked.connect(self.btn_1_clicked) #버튼 함수
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)
#끄기 기능 호출

    def btn_1_clicked(self):
        QMessageBox.about(self,"message","clicked") #qt 신호

    def btn_2_clicked(self):
        print("Button Clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
