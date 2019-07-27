from retriver_ui import Ui_cover_retriver
from cover_retriver import bilibili_cover_retriver
from PyQt5.QtWidgets import *
from Error import *
import os
import sys


class SuperUIForm(QWidget):

    def __init__(self):
        super(SuperUIForm, self).__init__()
        self.ui = Ui_cover_retriver()
        self.ui.setupUi(self)

        self.__save_dir = None
        self.ui.retriveButton.clicked.connect(self.but_Retrive)


    def but_Retrive(self):
        try:
            self.__save_dir = QFileDialog.getExistingDirectory(self,  
                                                           "选取保存路径",  
                                                           './')
            if len(self.__save_dir) == 0:
                return

            else:
                aid = self.ui.aid_input.text()
                retriver = bilibili_cover_retriver(verbose=False)
                retriver.get(aid)
                retriver.save(self.__save_dir)

                msgbox = QMessageBox()
                msgbox.setWindowTitle("成功")
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("封面下载成功")
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.setDefaultButton(QMessageBox.Ok)
                msgbox.exec()
        
        except aidError as error:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("错误")
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setText("视频资源错误")
            msgbox.setInformativeText(error.msg)
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.setDefaultButton(QMessageBox.Ok)
            msgbox.exec()

        return

if __name__ == "__main__":
    gui = QApplication(sys.argv)
    gui_window = SuperUIForm()
    gui_window.show()
    sys.exit(gui.exec_())