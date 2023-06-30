from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

UI_PATH ='08.GUI개발\design.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH, self)

        # 이벤트 받는 방법
        # self.객체이름.clicked.connect(self.실행할함수이름)
        self.log_btn.clicked.connect(self.login_start)

    def login_start(self):
        input_id=self.id_edit.text()
        input_pw=self.pw_edit.text()
        print(f'입력한 아이디는 : {input_id}')
        print(f'입력한 비밀번호는 : {input_pw}')
        main_dialog.close()



QApplication.setStyle('fusion')
app =QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())


