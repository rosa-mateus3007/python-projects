def boas_vindas(nome):
    print(f'Bem-vindo(a) {nome}')
boas_vindas('Sarah')
boas_vindas('Mateus')



def retangulo(comprimento, largura):
    area = comprimento*largura
    print(f'area = {area}')
    return arear
comp = float(input("Qual o comprimento do retângulo? "))
larg = float(input("Qual a largura do retângulo? "))
retangulo(comp, larg)



def classificar_numero(numero):
    if numero > 0:
        classificar = "positivo"
    elif numero < 0:
        classificar = "negativo"
    else:
        classificar = "zero"
    print(classificar)

    return classificar
num = float(input("Insira um número: "))
classificar_numero(num)


