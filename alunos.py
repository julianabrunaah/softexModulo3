nomes = ['Ana', 'Maria','Pedro','Lucas','João']


print('___AGENDA DE CLASSE___')
for nome in nomes:
    print(nome)
    nota1 = float(input('Digite a primeira nota :'))
    nota2 = float(input('Digite a segunda nota: '))
    faltas = int(input('Digite a quantidade de faltas: '))
    media = (nota1 + nota2)/2

    if faltas>=3:
        print(nome,' Reprovado por falta')
    if media<7:
        print(nome,' Reprovado por nota')
    if media>=7 and faltas<3:
        print(nome,' Aprovado/a')










