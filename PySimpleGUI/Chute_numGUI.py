from random import randint
import PySimpleGUI as sg
from time import sleep

class ChuteONumero:
    def __init__(self) -> None:
        self.valor_aleatório = 0
        self.valor_minimo = 0   
        self.valor_maximo = 100
        self.Valor_Chute = 0
        self.layout = [
            [sg.Text('Seu número',size=(20,0))],
            [sg.Input(size=(30,0),key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(30,10))]
        ]

    def Iniciar(self):
        self.GerarNumAleatorio()
        self.janela = sg.Window('Chute o número!', self.layout)
        while True:
            try:
                self.evento, self.valores = self.janela.Read()
                self.Valor_Chute = self.valores['ValorChute']
                if  int(self.Valor_Chute) >  self.valor_aleatório:
                    print('Chute um valor mais baixo!')
                elif  int(self.Valor_Chute) < self.valor_aleatório:
                    print('Chute um valor mais alto')
                elif int(self.Valor_Chute) == self.valor_aleatório:
                    print(f'Na mosca o número aleatório gerado foi {self.valor_aleatório}')
                    sleep(10)
                    break
            except:
                print('Digite um número inteiro válido')
    
    def GerarNumAleatorio(self):
        self.valor_aleatório = randint(self.valor_minimo,self.valor_maximo)
        
program = ChuteONumero()
program.Iniciar()
