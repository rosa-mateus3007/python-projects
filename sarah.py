import random
def sorteia_dado():
    numero = random.randint(1,6)
    return numero
num1 = sorteia_dado()    
print(f"1° Número sorteado: {num1}")
num2 = sorteia_dado()    
print(f"1° Número sorteado: {num2}")

def conta_ate_o_alvo(alvo):
    contador = 0
    while True:
        contador += 1
        if contador == alvo:
            break
        print(contador)

alvo = int(input("Insira o alvo: "))
alvo += 1
conta_ate_o_alvo(alvo)

import random

def jogo_simples():
    numero = random.randint(1, 20)
    return numero

segredo = jogo_simples()
tentativas = 0
while tentativas != 5:
    tentativas += 1
    palpite = int(input("Palpite: "))
    if palpite == segredo:
        print("Acertou!")
        break
    elif palpite < segredo:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    if tentativas == 5:
        print(f"Você perdeu! O número era {segredo}")
