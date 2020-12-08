print('{:=^40}'.format('FARMÁCIA PREÇO BAIXO'))
preço = int(input('Valor total das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro
[2] à vista no cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual a opção?'))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totalp = int(input('Em quantas parcelas? '))
    parcela = total / totalp
    print('Sua compra será parcelada em {} de R${:.2f} COM JUROS'.format(totalp, parcela))
else:
    total = 0
    print('OPÇÃO DE PAGAMENTO INVÁLIDA!!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
