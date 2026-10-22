def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media
def situação(media):
    if media >= 6:
        return "Aprovado!"
    elif media >= 4:
        return "Recuperação!"
    else:
        return "Reprovado!"

continuar = "sim"
while continuar =="sim":
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    media = calcular_media(n1, n2, n3)
    print(f"Média: {media} - situação: {situação(media)}")
    continuar = input("Calcular outra média? (sim/não): ").lower()
