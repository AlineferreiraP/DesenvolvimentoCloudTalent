# Função
oper = 0
def calculadora(num1, num2,operacao):
    
    resultado = 0
    while True:
      
      if operacao == 1:
        resultado += num1 + num2
        return print("O resultado da sua operação é: ", resultado)
        
         
      elif operacao == 2:
        resultado += num1 - num2
        return print("O resultado da sua operação é: ", resultado)
        
      
      elif operacao == 3:
        resultado += num1 * num2
        return print("O resultado da sua operação é: ", resultado)
        
      elif operacao == 4:
        resultado += num1 / num2
        return print("O resultado da sua operação é: ", resultado)
        
      
#Repetição
while True:
 oper = int(input("Insira\n1 para adição\n2 para subtração,\n3 para multiplicação,\n4 para divisão, \n 0 para sair:  "))
 
 if(oper <= 4) and (oper != 0):
  numero1 = int(input("Insira o primeiro número da operação: "))
  numero2 = int(input("Insira o segundo número da operação: "))
  calculadora(numero1, numero2, oper)
  continue
 elif (oper > 4):
   print("Essa opção não existe")
   continue
 elif (oper == 0): 
   break
    



   

       
   


