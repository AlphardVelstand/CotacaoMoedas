# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Princ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.pushButtonAtualizar = QPushButton(Form)
        self.pushButtonAtualizar.setObjectName(u"pushButtonAtualizar")
        self.pushButtonAtualizar.setGeometry(QRect(150, 200, 111, 41))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(16)
        self.pushButtonAtualizar.setFont(font)
        self.pushButtonAtualizar.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 311, 51))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label_Resul_Bitc = QLabel(Form)
        self.label_Resul_Bitc.setObjectName(u"label_Resul_Bitc")
        self.label_Resul_Bitc.setGeometry(QRect(90, 150, 231, 41))
        self.label_Resul_Bitc.setFont(font1)
        self.label_Resul_Euro = QLabel(Form)
        self.label_Resul_Euro.setObjectName(u"label_Resul_Euro")
        self.label_Resul_Euro.setGeometry(QRect(90, 110, 231, 41))
        self.label_Resul_Euro.setFont(font1)
        self.pushButtonSair = QPushButton(Form)
        self.pushButtonSair.setObjectName(u"pushButtonSair")
        self.pushButtonSair.setGeometry(QRect(160, 250, 91, 41))
        self.pushButtonSair.setFont(font)
        self.pushButtonSair.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.label_Resul_Dollar = QLabel(Form)
        self.label_Resul_Dollar.setObjectName(u"label_Resul_Dollar")
        self.label_Resul_Dollar.setGeometry(QRect(90, 70, 231, 41))
        self.label_Resul_Dollar.setFont(font1)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 331, 281))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.raise_()
        self.pushButtonAtualizar.raise_()
        self.label.raise_()
        self.label_Resul_Bitc.raise_()
        self.label_Resul_Euro.raise_()
        self.pushButtonSair.raise_()
        self.label_Resul_Dollar.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonAtualizar.setText(QCoreApplication.translate("Form", u"Atualizar", None))
        self.label.setText(QCoreApplication.translate("Form", u"Consultar valor atual da moeda", None))
        self.label_Resul_Bitc.setText(QCoreApplication.translate("Form", u"Bitcoin", None))
        self.label_Resul_Euro.setText(QCoreApplication.translate("Form", u"Euro", None))
        self.pushButtonSair.setText(QCoreApplication.translate("Form", u"Sair", None))
        self.label_Resul_Dollar.setText(QCoreApplication.translate("Form", u"Dollar", None))
    # retranslateUi

