
num1= int(input('Digite um valor de 0 a 10: '))
num2= int(input('Digite um valor de 0 a 10: '))
operador = str(input('digite e operação que deseja realizar''\n Exemplo: soma''\n digite a operação: '))

def soma (num2, num1, resSoma):
    resSoma = num1 + num2
    print(resSoma)
    return resSoma
    
def subtracao (num2, num1, resSub):
    resSub = num1 - num2
    print(resSub)
    return resSub

def multi (num2, num1, res):
    res = num1 - num2
    print(res)
    return res
    
def divisao (num2, num1, res):
    res = num1 - num2
    print(res)
    return res
    
if 'soma' in operador:
  soma(num1, num2, resSoma)
elif 'subtracao' in operador:
  subtracao(num1, num2, resSub)
elif 'multiplicacao' in operador:
  multi(num1, num2, res)
elif 'divisao' in operador:
  divisao(num1, num2, res)
