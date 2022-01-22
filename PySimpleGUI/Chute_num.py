from random import randint

class ChuteONumero:
    def __init__(self) -> None:
        self.valor_aleatório = 0
        self.valor_minimo = 0   
        self.valor_maximo = 100


    def Iniciar(self):
        self.GerarNumAleatorio()
        self.PedirValorAleatorio()

        while True:
            try:
                if int(self.valor_chute) > self.valor_aleatório:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valor_chute) < self.valor_aleatório:
                    print('Chute um valor mais alto')
                    self.PedirValorAleatorio()
                elif int(self.valor_chute) == self.valor_aleatório:
                    print(f'Na mosca o número aleatório gerado foi {self.valor_aleatório}')
                    break
            except:
                print('Digite um número inteiro válido')
                self.PedirValorAleatorio()
    
    def PedirValorAleatorio(self):
        self.valor_chute = input('Chute um número: ')
        
    
    def GerarNumAleatorio(self):
        self.valor_aleatório = randint(self.valor_minimo,self.valor_maximo)

program = ChuteONumero()
program.Iniciar()