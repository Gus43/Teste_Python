# -*- coding: utf-8 -*-
#Questao2.ipynb

'''Autor: Gustavo Montes Machado
   Data: 19/12/2020'''

import math as mt                                    # importando o math para usar as feraamentas de vetor a afins
i = 0                                                
v = []                                               # criando o vetor v
for i in range (10):                                 # criando um loop que acabará antes de chegar no 10(de zero até 9 somando 10 elementos)
    if i%2 == 0: 
      v.insert(i, 3**i + 7 * math.factorial(i))                                    # testando se a posiçao é par e sendo par, cria uma nova formula para posiçoes pares
    else:                                            # não sendo par, cria uma nova fórmula para elementos em posições ímpares
      v.insert(i, 2**i + 4 * mt.log(i))
    i = i + 1                                        # aumentando o i para o proximo numero , retornando para o loop
print("V =",v)                                       # Printando o vetor
print("\nA posição do maior elemento do vetor é: " + str(v.index(max(v))))
print("\nA média dos valores contidos nesse vetor é: " + str(round(sum(v)/len(v),2)))
