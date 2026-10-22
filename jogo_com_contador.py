def jogo_com_contador():
    numero = random.randint(1, 20)
    return numero
tentativas = 0
segredo = jogo_simples()
while True:
    tentativas += 1
    palpite = int(input("Palpite: "))
    if palpite == segredo:
        print("Acertou em", tentativas, "tentativas!")
        break
    elif palpite < segredo:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
