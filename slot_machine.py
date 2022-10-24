###################HACHERSCHOOL####################
###########Python Project - Slot Machine###########

#     Quando iniciada deve perguntar ao utilizador quantos créditos quer depositar
#     Antes de cada rodada deve perguntar ao utilizador se quer parar de jogar
#     Se a decisao for para continuar deve-se perguntar quantos créditos vao ser apostados(se nao houver créditos suficientes o jogador e informado e repete-se a pergunta)
#     Uma Rodada consiste em gerar 3 simbolos de um conjunto de 7 símbolos(há vossa escolha)
#     Os simbolos devem ter as seguintes probabilidades 50/156 simbolo 1 40/156 simbolo 2 30/156 simbolo 3 20/156 simbolo 4 10/156 simbolo 5 5/156 simbolo 6 1/156 simbolo 7
#     Se os 3 símbolos forem iguais então o utilizador ganha créditos em função da sua aposta e do simbolo 5aposta simbolo 1 10aposta simbolo 2 20aposta simbolo 3 70aposta simbolo 4 200aposta simbolo 5 1000aposta simbolo 6 100_000*aposta simbolo 7
#     se o utilizador fica sem créditos o programa deve fechar

# O vosso código deve usar pelo menos uma classe Os símbolos sao a vossa escolha mas exemplos de conjuntos podem ser A,B,C,D,E,F,G #,$,%,&,@,£,€

# Perguntas acerca deste enunciado devem ser feitas no discord @Manuel Soares

import random

#Apresentação da Slot Machine
print("#########################################Bem-Vindo ao Casino do IST#########################################\n")
print("\tObrigado pela sua preferência em querer apostar na nossa casa e nas nossas Slot Machines!!\n")
print("\tMuito boa sorte e que sai daqui vencerdor :D\n")
nome = input("Por favor, introduza o seu nome: ")
creditos = int(input("Escreva o número de créditos que deseja inserir na máquina (atenção que a máquina não aceita moedas menor que 1 euro): "))


#CONSTANTES:
simbolos = ["A", "B", "C", "D", "E", "F", "G"]
probabilidade = [50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156]
    
class Jogo:
    def __init__(self, nome, creditos):
        self.nome = nome
        self.creditos = creditos
    
    def spinWheel(self):
        #retorna um item random da lista de simbolos com as devidas probabilidades
        self.primeira = random.choices(simbolos, probabilidade)
        self.segunda = random.choices(simbolos, probabilidade)
        self.terceira = random.choices(simbolos, probabilidade)
        
        return self.primeira, self.segunda, self.terceira
        
    def perguntarJogador(self):
        if int(self.creditos) > 0:
            while True:
                self.continuar_jogar = input(f"\tTem, {self.creditos}. Quer continuar a jogar? (responda só \"sim\" ou \"nao\") ")
                self.continuar_jogar = self.continuar_jogar.lower()
                if self.continuar_jogar == "sim":
                    self.creditos_jogados = int(input(f"\tTem, {self.creditos}, quantos quer gastar nesta rodada? "))
                    return True
                elif self.continuar_jogar == "nao":
                    print(f"Acabou o jogo com {self.creditos}.")
                    quit()
                else:
                    print("Input errado!!!")
        else:
            print("\n\tOs créditos acabaram! Better luck next time!")
            quit()
            
    def jogar(self):
        pergunta = self.perguntarJogador()
        while (int(self.creditos) != 0 and pergunta == True):
            print("\n\t", self.spinWheel())
            print("\n\tFicou com ", self.calculo_score())
            pergunta = self.perguntarJogador()
    
    def calculo_score(self):
        if self.primeira == self.segunda == self.terceira == ["A"]:
            print("Parabéns!! Ganhou", ((5*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (5*self.creditos_jogados)
            return self.creditos
        elif self.primeira == self.segunda == self.terceira == ["B"]:
            print("Parabéns!! Ganhou", ((10*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (10*self.creditos_jogados)
            return self.creditos
        elif self.primeira == self.segunda == self.terceira == ["C"]:
            print("Parabéns!! Ganhou", ((20*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (20*self.creditos_jogados)
            return self.creditos
        elif self.primeira == self.segunda == self.terceira == ["D"]:
            print("Parabéns!! Ganhou", ((70*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (70*self.creditos_jogados)
            return self.creditos
        elif self.primeira == self.segunda == self.terceira == ["E"]:
            print("Parabéns!! Ganhou", ((200*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (200*self.creditos_jogados)
            return self.creditos
        elif self.primeira == self.segunda == self.terceira == ["F"]:
            print("Parabéns!! Ganhou", ((1000*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (1000*self.creditos_jogados)
            return self.creditos
        elif self.primeira == self.segunda == self.terceira == ["G"]:
            print("Parabéns!! Ganhou", ((100000*self.creditos_jogados)))
            self.creditos = (self.creditos - self.creditos_jogados) + (100000*self.creditos_jogados)
            return self.creditos    
        else:
            self.creditos = int(self.creditos) - int(self.creditos_jogados)
            return self.creditos
            
    
    
    
#Está quase, falta interligar tudo


player = Jogo(nome, creditos)
print("\n\t" + player.nome + " tem " + str(player.creditos) + "!!!\n")


print(player.jogar())