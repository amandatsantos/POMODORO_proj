#app pomodoro
from tqdm import tqdm
from time import time, sleep
import os
from math import floor
class Pomodoro():

    def __init__(self):
        self.tempo_inicial = time ()
        self.tempo_corrente = time()
        self.tempo_maximo = 10

    def tempo_var(self):
        return self.tempo_corrente - self.tempo_inicial

    def update(self):
        self.tempo_corrente = time()

    def display_update(self):
        print( ' TEMPO INICIAL : ', self.tempo_maximo )
        print( 'variação de tempo:', self.tempo_var() )
        print('Tempo restante', self.tempo_formatado())
        print(self.barra_progesso())

    def tempo_formatado(self):
        Xt = self.tempo_maximo - self.tempo_var()
        MIN = floor(Xt / 60 )
        SEC =  floor(Xt - MIN*60)
        return '(' + str(MIN) + ':'  + str(SEC) + ')'


    def barra_progesso(self):
        num_chr = 1
        data = [ ]
        X = floor((self.tempo_maximo - self.tempo_var())/ self.tempo_maximo * num_chr)
        Y = max(num_chr - X, 0) 
        for i in tqdm(range(Y)):
            data.append(i)
            print(data) 

    def mainLoop(self):
        while True:
            os.system("cls")
            self.update()
            self.display_update()
            
            sleep(1)

            if self.tempo_var() >self.tempo_maximo:
                print('cabo a hora de sofreeeerrr\n hora de ver u videozin :)\n ')
                os.system('pause')
                os.system("start https://...")
                break


print('POMODORO 0.1\n A Técnica Pomodoro é um método de gerenciamento de tempo desenvolvido por Francesco Cirillo no final dos anos 1980.\n[1] Ele usa um cronômetro para quebrar o trabalho em intervalos, tradicionalmente de 25 minutos de duração, separados por intervalos curtos.\n Cada intervalo é conhecido como pomodoro , da palavra italiana para " tomate ", \nem homenagem ao cronômetro de cozinha em forma de tomate que Cirillo usava quando era estudante universitário.')
os.system('pause')
M = Pomodoro()
M.mainLoop()
input()
