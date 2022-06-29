'''
email usado:
    joao@gmail.com
'''

lista_nomes = ["000webhost", "123RF", "500px", "8tracks", "Adobe", "Animal Jam", "AnimeGame", "Animoto",
    "Apollo", "Appen", "Aptoide", "Armor Games", "Army Force Online", "Audi", "Bitly",
    "Canva", "Chegg", "Dailymotion", "DataCamp", "Descomplica"]

lista_vazados = ["email, nome, senha", "email, nome, senha, telefone", "email, nome, senha", "email, senha",
    "email, ajuda de senha, senha", "email, nome, senha", "email, senha",
    "email, nome, senha", "email, nome, telefone", "email, senha, nome, telefone",
    "email, nome, senha", "email, senha", "email, nome, senha", "email, nome, telefone",
    "email, senha", "email, senha, nome", "email, nome, senha", "email, senha",
    "email, nome, senha", "email, senha, nome"]

lista_ano = ["2015-03-01", "2020-03-01", "2018-06-01", "2017-07-01", "2013-10-01", "2022-10-01",
    "2020-02-01", "2018-07-02", "2018-07-01", "2020-06-01", "2020-04-01", "2019-01-01",
    "2016-05-01", "2019-08-01", "2014-05-01", "2019-05-01", "2018-04-01", "2016-10-01",
    "2018-12-01", "2021-03-01"]

lista_pontuação = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Lê lista_vazados e adiciona a pontuação caso encontre as palavras-chave dentro do item da lista
for i in range (0, len(lista_nomes)):
    if "senha" in lista_vazados[i]:
        lista_pontuação[i] = lista_pontuação[i] + 10000
        lista_vazados[i] = ""
    if "ajuda de senha" in lista_vazados[i]:
        lista_pontuação[i] = lista_pontuação[i] + 400
    if "telefone" in lista_vazados[i]:
        lista_pontuação[i] = lista_pontuação[i] + 300
    if "nome" in lista_vazados[i]:
        lista_pontuação[i] = lista_pontuação[i] + 200
    if "email" in lista_vazados[i]:
        lista_pontuação[i] = lista_pontuação[i] + 100

#Cria uma cópia da lista de pontuação, para que a original não seja perdida após o sort() e possa ser usada para comparação
lista_pontuação_sorted = []
for i in range (0, len(lista_pontuação)):
    lista_pontuação_sorted.append(lista_pontuação[i])

#Cria uma cópia da lista de ano, para que ela não seja perdida após o sort() e possa ser utilizada para comparação
lista_ano_old = []
for i in range (0, len(lista_ano)):
    lista_ano_old.append(lista_ano[i])

#Organiza lista_ano da data mais atual até a mais antiga
lista_ano.sort()
lista_ano.reverse()

#Encontra o índice de lista_ano[i] em lista_ano_old,
#esse índice(j) é usado para subtrair "i" da lista nova e da antiga,
#para organizá-las por data e mantê-las com valores atualizados
for i in range(0, len(lista_ano)):
    j = lista_ano_old.index(lista_ano[i])
    lista_pontuação[j] = lista_pontuação[j] - i
    lista_pontuação_sorted[j] = lista_pontuação_sorted[j] - i

#Organiza a lista de pontuação da maior para a menor
lista_pontuação_sorted.sort()
lista_pontuação_sorted.reverse()

#Encontra o índice do valor de lista_pontuação_sorted[i] na lista_pontuação original
#Adiciona o lista_nomes[índice encontrado] em lista_resultados
lista_resultados = []
for i in range(0, len(lista_nomes)):
    j = lista_pontuação.index(lista_pontuação_sorted[i])
    lista_resultados.append(lista_nomes[j])

#Exibe os resultados
print("\nPrioridade do maior para o menor: ")
for i in range (0, len(lista_resultados)):
    print (f"{i + 1} - {lista_resultados[i]}")
