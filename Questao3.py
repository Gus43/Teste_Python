# -*- coding: utf-8 -*-
#Questao3.ipynb


'''Autor: Gustavo Montes Machado
   Data: 19/12/2020'''

print("Caso necessário, separe as casas decimais utilizando ponto ao invés de vírgula!\nE nao deixe caixa de nota vazia!\n") # Ressalvas para o funcionamento pleno do codigo
notas = {
        str(input("Insira o nome do Aluno 1: ")): float(input("Insira a nota do Aluno 1: ")),
        str(input("\nInsira o nome do Aluno 2: ")): float(input("Insira a nota do Aluno 2: ")),
        str(input("\nInsira o nome do Aluno 3: ")): float(input("Insira a nota do Aluno 3: ")),
        str(input("\nInsira o nome do Aluno 4: ")): float(input("Insira a nota do Aluno 4: ")),
        str(input("\nInsira o nome do Aluno 5: ")): float(input("Insira a nota do Aluno 5: "))
}                                                                                                                      # criando o dicionario com os comandos para receber as entradas
   
# printando todos os resultados 
print("\nO aluno com maior nota foi: " + str(max(notas, key=notas.get)))#Aqui ele printa o que se pede, o nome e a respectiva nota do aluno com a nota mais alta dentre todos.
print("e sua nota foi: " + str(float(notas[max(notas, key=notas.get)])))
print("Notas = ",notas)
