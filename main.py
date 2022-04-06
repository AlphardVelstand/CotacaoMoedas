import sys

import requests
import json
import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_Form
from datetime import datetime
from datetime import date
import time
#from PyQt5 import uic, QtWidgets

cotacao_dollar = 0
cotacao_euro = 0
cotacao_bitcoin = 0

#classe principal
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Consultar valor atual da moeda")

        #Chamando os botoes
        self.pushButtonAtualizar.clicked.connect(pegar_cotacoes)
        self.pushButtonSair.clicked.connect(self.sair)

        #atualizar()

    def sair(self):
        sys.exit()

#while True:
def atualizar():
    time.sleep(5)
    pegar_cotacoes()


def pegar_cotacoes():
    global cotacao_dollar, cotacao_euro, cotacao_bitcoin
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    # print(requisicao_dic)

    cotacao_dollar = requisicao_dic["USD"]["bid"]
    cotacao_euro = requisicao_dic['EUR']['bid']
    cotacao_bitcoin = requisicao_dic['BTC']['bid']

    # print(f"EURO:{cotacao_euro}, \nDOLLAR{cotacao_dollar}, \nBITCOIN{cotacao_bitcoin}")

    texto = f'''
                Euro: {cotacao_euro}
                Dollar: {cotacao_dollar}
                Bitcoin: {cotacao_bitcoin}'''

    window.label_Resul_Dollar.setText(f"Dollar: " + cotacao_dollar)
    window.label_Resul_Euro.setText(f"Euro: " + cotacao_euro)
    window.label_Resul_Bitc.setText(f"Bitcoin: " + cotacao_bitcoin)

    #Capturando a data e Convertendo para D/M/A
    hoje = datetime.today()
    #print(today_date)
    printHoje = hoje.strftime("%d/%m/%Y %H:%M:%S")
    #print(new_today_date)

    window.labelTime.setText(f"Ultima Atualização: {printHoje}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()