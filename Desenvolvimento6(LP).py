def calculaIdade (nome,anoDeNasc):
    anoAtual = 2022
    if(dataDeNac >= 1922) and (dataDeNac <= 2021):
     resultado = anoAtual - anoDeNasc
    else:
       raise Exception("Ano invalido, informe entre 1992 e 2021, sem letras ou simobolos!")
    return print("Seu nome é: ", nome,"\nSua idade atual ou que vai completar em 2022 é: ", resultado)

nomeCompleto = input("Por favor, informe seu nome completo: ")
while True:
    try: 
       dataDeNac = int(input("Por favor informe agora o seu ano de nascimento. Exemplo 1998 "))
       calculaIdade(nomeCompleto, dataDeNac)
       break
    except Exception as err:
     print("Erro!")
     print(err)
    
   