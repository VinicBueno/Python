from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

        # Layout
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer algo com esses valores
        try:
            if self.eventos == 'Sim':
                self.GerarValorDoDado()
            elif self.eventos == 'Não':
                print('Agradeço sua participação!')
            else:
                print('Por favor digite sim ou não')
        except:
            print('Ocorreu um erro ao registrar a sua resposta')

    def GerarValorDoDado(self):
        print(randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()