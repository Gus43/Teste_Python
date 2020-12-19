# -*- coding: utf-8 -*-
#Questao1.ipynb

'''Autor: Gustavo Montes Machado
   Data: 19/12/2020'''

n = 1                                               # variável dos numeros  ue irao cobrir o intervalo pedido                                             #variável que soma a
lista = []                                          # criando a lista que vai armazenar os numeros que satisfazem as condiçoes 
while n <= 5000000:                                 # Criando um loop que acabará quando o n receber um valor maior que 5 milhoes
  if n%2 ==0 and n%37 == 0 and n%49 == 0:           # testando se é par, se é divizivel por 37 e 49
        lista.append(n)                             # satsfazendo, adicionar o numero n à lista
                                     
  n = n+1                                           # aumentando o n para o proximo numero , retornando para o loop
    
print(str(len(lista)) )                             # usando o len pra contar os elementos da lista
#print(lista) para evitar sobrecarga nao executarei essa linha - exibindo a lista com todos os numeros
