def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4)/4
    return media
def situação(media):
    if media >= 6:
        return "Aprovado. Parabéns!"
    elif media >= 4:
        return "Recuperação. Estude mais!"
    else:
        return "Reprovado."
print(f"{"-"*30}")
print(f"{'Calculadora de Média':^30}")
print(f"{"-"*30}")
print("\nDigite as notas do aluno para calcular a média anual e verificar a situação.")
continuar = "sim"
while continuar =="sim":
    n1 = float(input("Nota 1° Bimestre: "))
    n2 = float(input("Nota 2° Bimestre: "))
    n3 = float(input("Nota 3° Bimestre: "))
    n4 = float(input("Nota 4° Bimestre: "))
    media = calcular_media(n1, n2, n3, n4)
    print(f"\nMédia anual: {media:.01f} | Situação: {situação(media)}")
    continuar = input("\nDeseja calcular outra média? (sim/não): ").lower()
print("\nPrograma encerrado. Até a próxima!")
