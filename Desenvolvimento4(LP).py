 
# Função 
def calculadora(num1, num2,operacao):
    
    resultado = 0
    if operacao == 1:
        resultado += num1 + num2
    elif operacao == 2:
        resultado += num1 - num2
    elif operacao == 3:
        resultado += num1 * num2
    elif operacao == 4:
        resultado += num1 / num2
    else: 
        print("0")
    return resultado 

# Entrada de dados
numero1 = int(input("Insira o primeiro número da operação: "))
numero2 = int(input("Insira o segundo número da operação: "))
oper = int(input("Insira\n1 para adição\n2 para subtração,\n3 para multiplicação,\n4 para divisão: "))

# Chamado da função e saída de dados
print("O resultado da sua operação é: ", calculadora(numero1,numero2,oper))
