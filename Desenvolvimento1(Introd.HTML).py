import numpy as np
from tabulate import tabulate

#Declaração de array np
produtos_loja_musica = np.array([])

# Entrada de dados pela estrutura for
for i in range(5):
 produtos_loja_musica = np.append(produtos_loja_musica, (input("Informe o nome do prudutos: ")), axis = None)

# Saída de dados 
print(produtos_loja_musica) 

 #_________________________________________________________________________

# Declaração de arrays np
nomes = np.array([])
ano_nascimento = np.array([])

## Entrada de dados pela estrutura for
for i in range(5):
 nomes = np.append(nomes, (input("Informe os nomes do seus amigos ou familiares: ")), axis = None)
 ano_nascimento = np.append(ano_nascimento, (int(input("Informe o anos de nascimento respectivamente: "))), axis = None)
 
 # Saída de dados 
print("Nomes: ", nomes,"\n","Ano: ", ano_nascimento)
