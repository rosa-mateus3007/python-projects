import random
def calcular_total(preco, quantidade):
    valor_total = quantidade *  preco
    return valor_total

resposta = input("Continuar atendendo (digite C) ou encerrar o expediente (digite qualquer coisa): ").upper()
contador = 0
while resposta == "C":
    nome = input("Qual é o nome do cliente? ")
    preco_unitario = float(input("Insira o preço unitário: "))
    quantidade_comprada = int(input("Insira a quantidade comprada: "))
    total = calcular_total(preco_unitario, quantidade_comprada)
    if total > 160:
        desconto = 0.11
        desconto_conta = desconto * total
        
    elif total > 85:
        desconto = 0.05
        desconto_conta = desconto * total

    else:
        desconto = 0
        desconto_conta = desconto * total

    valor_final = total - desconto_conta
    desconto_porcentagem = desconto * 100
    print()
    print(f'Nome: {nome} | Valor Total: R${total:.2f} | Desconto: {desconto_porcentagem}%')
    print(f'Valor final a pagar: R${valor_final:.2f}')
    print()
    contador += 1
    resposta = input("Continuar atendendo (digite C) ou encerrar o expediente (digite qualquer coisa): ").upper()
print("Expediente encerrado")

    

