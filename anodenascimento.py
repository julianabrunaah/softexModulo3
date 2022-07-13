
nome = str(input('Digite seu nome: '))
aniversario = True
while aniversario:
    ano = int(input('Digite o seu ano de nascimento: '))
    try:
        if ano>=1920 and ano<=2021:
            atual = 2022
            idade = atual - ano
            print('Olá ', nome)
            print('Sua idade é ', idade)
            aniversario= False
        # else incluido para corrigir erro
        else:
            print('Ano de nascimento inválido')
    except:
        # a mensagem
        print('Dado inválido. Tente novamente')
        # por algum erro que não identifiquei não aparecia no terminal
        continue
