from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyautogui
import sys
import time
from PyQt5.QtGui import QIntValidator

UI_PATH='08.GUI개발/xy.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH, self)

        int_validator=QIntValidator()
        self.x_edit.setValidator(int_validator)
        self.y_edit.setValidator(int_validator)
        
        self.xy_btn.clicked.connect(self.xy_move)

    def xy_move(self):
        try:
            input_x=int(self.x_edit.text())
            input_y=int(self.y_edit.text())

            print(f'x좌표는 : {input_x}')
            print(f'y좌표는 : {input_y}')

            pyautogui.moveTo(input_x,input_y,duration=2)    
        except:
            self.staus.setText('숫자로 입력하세요')




QApplication.setStyle('fusion')
app =QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())





#      time.sleep(2)
        
 #      mes_dialog.show()
#       # pyautogui.alert(title='좌표이동', text='이동되었습니다.',button='확인')
#       time.sleep(3)
#
#        main_dialog.close()
 #       mes_dialog.close()

#class SubDialog(QDialog):
 #   def __init__(self):
 #       QDialog.__init__(self,None)
 #       uic.loadUi(UI_SUBMAS,self)
