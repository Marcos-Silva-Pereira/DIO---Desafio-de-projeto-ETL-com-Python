import csv

''' Extract '''

arquivo = open('tabela.csv')
dados = csv.reader(arquivo)

''' Transform '''

lista = list()

for dado in dados:
    if dado[2] == 'diamante':
        dado.append('Desconto de 50%')
        lista.append(dado)

    elif dado[2] == 'ouro':
        dado.append('Desconto de 35%')
        lista.append(dado)

    elif dado[2] == 'prata':
        dado.append('Desconto de 20%')
        lista.append(dado)
    
    elif dado[2] == 'bronze':
        dado.append('Desconto de 10%')
        lista.append(dado)

    else:
        dado.append('Desconto')
        lista.append(dado)

''' Load '''

novo_arquivo =  open('update.csv', 'w', newline='')
update = csv.writer(novo_arquivo, delimiter=',')
update.writerows(lista)


arquivo.close()
novo_arquivo.close()