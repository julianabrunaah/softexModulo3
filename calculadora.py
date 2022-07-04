
num1= int(input('Digite um valor de 0 a 10: '))
num2= int(input('Digite um valor de 0 a 10: '))
operador = str(input('digite e operação que deseja realizar''\n Exemplo: soma''\n digite a operação: '))

def soma (num2, num1, soma):
    soma = num1 + num2
    print(soma)
    return soma
    
def subtracao (num2, num1, subtracao):
    subtracao = num1 - num2
    print(subtracao)
    return subtracao

def multiplicacao (num2, num1, multiplicacao):
    multiplicacao = num1 * num2
    print(multiplicacao)
    return multiplicacao
    
def divisao (num2, num1, divisao):
    divisao = num1/num2
    print(divisao)
    return divisao
    
if 'soma' in operador:
  soma(num1, num2, soma)
elif 'subtracao' in operador:
  subtracao(num1, num2, subtracao)
elif 'multiplicacao' in operador:
  multiplicacao(num1, num2, multiplicacao)
elif 'divisao' in operador:
  divisao(num1, num2, divisao)
else:
  print('0')
