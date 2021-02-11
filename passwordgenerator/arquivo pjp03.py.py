print('Projeto Programa 3 – Gerador de Senhas')
print('''\nIntegrantes\n
ANTONIA CAROLAINE ALVES DA SILVA
JONATHAN NUNES DE ALMEIDA
MATEUS DOS SANTOS PEREIRA
ODILON ALVES DE REZENDE NETO
SAIMON RIBEIRO DOS SANTOS\n''')

from random import *
#Tipo da senha 
Mat = []
Alu = open('MATR.txt','r')#Abre o arquivo da Matricula para ser lido

lendo = Alu.readline()
while lendo != '':
        lendo = lendo.rstrip()
        Mati = int(lendo)
        Mat.append(Mati)
        lendo = Alu.readline()
Alu.close()

senha = open('SENHAS.txt','w')# Abre o arquivo com as senhas
 

print("a. Numérica\nb. Alfabética\nc. Alfanumérica 1\nd. Alfanumérica 2\ne. Geral")
def GeraSenha(tipo,tamanho):
    # gerar senha aleatória NÚMEROS
    sen = ''
    forsen = str(tipo) 
    tamsen = int(tamanho)
    x = 0
    if forsen == "a":
        while x != tamsen:
            bas = chr(randint(48,57))
            sen += bas
            x+=1
    elif forsen == "b":
        while x != tamsen:
            car2,car1 = randint(97,122),randint(65,90)
            bas = chr(randint(car1,car2))
            if bas != chr(91) and bas != chr(92)and bas != chr(93)and bas != chr(94)and bas != chr(95)and bas != chr(96):
                sen += bas
                x+=1
    elif forsen == "c":
        while x != tamsen:
            car1, car2 = randint(48,57), randint(65,90)
            bas = chr(randint(car1,car2))
            if bas != chr(58) and bas != chr(59)and bas != chr(60)and bas != chr(61)and bas != chr(62)and bas != chr(63)and bas != chr(64):
                sen += bas
                x+=1
    elif forsen == "d":
        while x != tamsen:
            bas = chr(randint(48,122))
            if bas != chr(58) and bas != chr(59)and bas != chr(60)and bas != chr(61)and bas != chr(62)and bas != chr(63)and bas != chr(64) != bas != chr(91) and bas != chr(92)and bas != chr(93)and bas != chr(94)and bas != chr(95)and bas != chr(96):
               sen += bas
               x+=1
    elif forsen == "e":
        while x != tamsen:
            bas = chr(randint(35,122))
            if bas != chr(58) and bas != chr(59)and bas != chr(60)and bas != chr(61)and bas != chr(62)and bas != chr(63)and bas != chr(64) != bas != chr(91) and bas != chr(92)and bas != chr(93)and bas != chr(94)and bas != chr(95)and bas != chr(96)and bas != chr(37)and bas != chr(39)and bas != chr(40)and bas != chr(41)and bas != chr(42)and bas != chr(43)and bas != chr(44)and bas != chr(46)and bas != chr(47)and bas != chr(59)and bas != chr(60)and bas != chr(61)and bas != chr(62) :
               sen += bas
               x+=1
    return sen
formato = str(input("Escolha o tipo da senha :"))
comp = int(input("Informe o Tamanho da senha: "))
for i  in range (len(Mat)):
    senhas = GeraSenha(formato,comp)
    senha.write("{};{};\n".format(Mat[i], senhas))
    print(senhas)
senha.close()
