
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
print('Sabendo que: \n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão')
operador = str(input('Digite o valor correspondente a operação que deseja realizar: '))



def soma(num1, num2, soma):
    soma = num1 + num2
    print('Resuldado =', soma)
    return soma


def subtracao(num1, num2, subtracao):
    subtracao = num1 - num2
    print('Resuldado =', subtracao)
    return subtracao


def multiplicacao(num1, num2, multiplicacao):
    multiplicacao = num1 * num2
    print('Resuldado =', multiplicacao)
    return multiplicacao


def divisao(num1, num2, divisao):
    divisao = num1 / num2
    print('Resuldado =', divisao)
    return divisao


if '1' in operador:
    soma(num1, num2, soma)
elif '2' in operador:
    subtracao(num1, num2, subtracao)
elif '3' in operador:
    multiplicacao(num1, num2, multiplicacao)
elif '4' in operador:
    divisao(num1, num2, divisao)
else:
    print('0')
