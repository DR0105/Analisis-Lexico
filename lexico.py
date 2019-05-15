# -*- coding: utf-8 -*-
def hacerAritmetica(operador, operandoIzq, operandoDer):
    if operador == "*":
        return operandoIzq * operandoDer
    elif operador == "/":
        return operandoIzq / operandoDer
    elif operador == "+":
        return operandoIzq + operandoDer
    else:
        return operandoIzq - operandoDer
    
f= open ('operaciones.txt','r')
o=f.read()
f.close()
oper=o.splitlines()
i=0
while i<len(oper):
    j=0
    separar = list(oper[i])
    while j<len(separar):  
       if separar[j].isdigit():
          separar[j] = separar[j] + "--->Numero"
       elif separar [j] == "+" or separar [j] == "-" or separar [j] == "*" or separar [j] == "/":
          separar[j] = separar[j] + "--->Operador"
       elif separar [j] == "=":
          separar[j] = separar[j] + "--->Igual"
       elif separar [j] == " ":
          separar[j] = separar[j] + ""
       else:
          separar[j] = separar[j] + "No reconocible"   
       j=j+1
    print (oper [i])
    pag = '\n'.join(separar)   
    print (pag)   
    i=i+1
       
   
     

   
