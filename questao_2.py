#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será
#   a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
#   escreva um programa na linguagem que desejar onde, informado um número,
#   ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

num1 = int(input("Informe um número: "))
a = 0
b = 1

print(a)
print(b)

for i in range(num1):
    c = a + b 
    a = b
    b = c
    
    if (num1 == c):
        valor = True
    
    print(c)
   
if(valor):
    print("Pertence a sequência")


