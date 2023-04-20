import time

class Pessoa:

    def __init__(self, nome):

        self.nome = nome

nome = input('Olá novo jogador. Qual é o seu nome? ')

nome = nome.capitalize()

jogador = Pessoa(nome)

print(f'Olá {jogador.nome}!') 

while True:

    despertar = input('Deseja despertar? S/N ')

    if despertar.lower() == 'n':
        print(f'{jogador.nome} dormiu por mais um tempo.')
    
        time.sleep(1)

        print('.')

        time.sleep(1)

        print('.')

        time.sleep(1)

        print('.')
    
    elif despertar.lower() == 's':
        
        print(f'{jogador.nome} abre os olhos.')
        break