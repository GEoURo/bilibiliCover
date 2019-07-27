# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retriver_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cover_retriver(object):
    def setupUi(self, cover_retriver):
        cover_retriver.setObjectName("cover_retriver")
        cover_retriver.resize(200, 80)
        cover_retriver.setMinimumSize(QtCore.QSize(200, 80))
        cover_retriver.setMaximumSize(QtCore.QSize(200, 80))
        cover_retriver.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.formLayout = QtWidgets.QFormLayout(cover_retriver)
        self.formLayout.setObjectName("formLayout")
        self.aidlabel = QtWidgets.QLabel(cover_retriver)
        self.aidlabel.setMinimumSize(QtCore.QSize(30, 20))
        self.aidlabel.setMaximumSize(QtCore.QSize(30, 20))
        self.aidlabel.setObjectName("aidlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.aidlabel)
        self.aid_input = QtWidgets.QLineEdit(cover_retriver)
        self.aid_input.setMinimumSize(QtCore.QSize(130, 20))
        self.aid_input.setMaximumSize(QtCore.QSize(130, 20))
        self.aid_input.setText("")
        self.aid_input.setClearButtonEnabled(True)
        self.aid_input.setObjectName("aid_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aid_input)
        self.retriveButton = QtWidgets.QPushButton(cover_retriver)
        self.retriveButton.setMinimumSize(QtCore.QSize(180, 32))
        self.retriveButton.setMaximumSize(QtCore.QSize(180, 32))
        self.retriveButton.setObjectName("retriveButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.retriveButton)

        self.retranslateUi(cover_retriver)
        QtCore.QMetaObject.connectSlotsByName(cover_retriver)

    def retranslateUi(self, cover_retriver):
        _translate = QtCore.QCoreApplication.translate
        cover_retriver.setWindowTitle(_translate("cover_retriver", "B站封面提取器"))
        self.aidlabel.setText(_translate("cover_retriver", "AV号"))
        self.retriveButton.setText(_translate("cover_retriver", "提取"))

