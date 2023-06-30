from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyautogui
import sys
import time
from PyQt5.QtGui import QIntValidator
import requests
from bs4 import BeautifulSoup
import openpyxl

UI_PATH='08.GUI개발/naver_kin.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH, self)

        int_validator=QIntValidator()
        self.page.setValidator(int_validator)

        self.start_btn.clicked.connect(self.start_kin)
        self.reset_btn.clicked.connect(self.reset_kin)
        self.save_btn.clicked.connect(self.save_kin)
        self.close_btn.clicked.connect(self.clsoe_kin)


    def start_kin(self):
        keyword=self.keyword.text()
        page=int(self.page.text())

        self.result=[]
        
        for i in range(1,page+1):
            response = requests.get(f'https://kin.naver.com/search/list.naver?query={keyword}&https://kin.naver.com/search/list.naver?query={i}')
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            quesrions=soup.select('li>dl')

            self.textBrowser.append(f'{i} 페이지 크롤링 중...')
            QApplication.processEvents()

            for quesrion in quesrions:
                anchor=quesrion.select_one('dt>a')
                title=anchor.text
                link=anchor.attrs['href']
                data=quesrion.select_one('dl>dd').text
                contents=quesrion.select_one('dl>dd:nth-of-type(2)').text
                    
                self.textBrowser.append(f'제목 : {title} \n날짜 : {data} \n링크 : {link} \n내용 : {contents}')
                QApplication.processEvents()
                self.result.append([title, link, data, contents])


            
        self.textBrowser.append('크롤링 완료!!')

    def reset_kin(self):
        self.keyword.setText('')
        self.page.setText('')
        self.textBrowser.setText('')
        #self.keyword.clear()
        #self.page.clear()
        #self.textBrowser.clear()

    def save_kin(self):
        keyword_text=self.keyword.text()
        print(self.result[0])  
        print(type(self.result[0]))

        wb= openpyxl.Workbook()
        ws=wb.create_sheet(f'{keyword_text} 검색')
        ws.append(['제목','링크','날짜','내용'])
        for data in self.result:
            ws.append(data)
        wb.save(f'{keyword_text}.xlsx')

    def clsoe_kin(self):
        sys.exit()
        #main_dialog.close()
        



QApplication.setStyle('fusion')
app =QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())