""" Classificador de nivel de ranqueada 
deve receber o numero de vitorias e derrotas do heroi para determinar seu saldo de ranqueadas
seu nivel deve ser com base no numero de vitorias obtidas
niveis do heroi 
ferro = 10
bronze 11 a 20
prata 21 a 50 
ouro 51 a 80 
diamante 81 a 90 
lenadrio 91 a 100
imortal 101 ou mais

Deve conter: 
variaveis
operadores 
laços de repetição 
estruturas de decisoes 
funçoes """

def saldo(w,l):
    return w-l

print("infomre o numero de vitorias: ")
v = int(input())
print("infomre o numero de derrotas: ")
d = int(input())
x = saldo(v,d)

def nivel():
    if x < 10:
        level = "Ferro"
    elif x <=20:
        level = "Bronze"
    elif x <=20:
        level = "Prata"
    elif x <=50:
        level = "Ouro"
    elif x <=80:
        level = "Diamante"
    elif x <=90:
        level = "Lendario"
    else:
        level = "Imortal"

    return level

print("O Herói tem de saldo de: ", saldo(v,d), "E está no nível de ", nivel())
