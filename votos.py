import enum
class erros(enum.Enum):
    TypeError = 1

votosX = list()
votosY = list()
votosZ = list()
votosNulos = list()
print('Para vota em Candidato X digite 889')
print('Para vota em Candidato Y digite 847')
print('Para vota em Candidato Z digite 515')
print('Para voto em branco digite 0')
print('Para voto nulo, digite qualquer numéro diferente dos citados acima')

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite novamente')
            continue
        else:
            return n
for cont in range(0,20):
    voto = leiaInt(input('Digite seu voto: '))
    if voto == 889:
        votosX.append(voto)
        print('Voto computado com sucesso!')
    elif voto == 847:
        votosY.append(voto)
        print('Voto computado com sucesso!')
    elif voto == 515:
        votosZ.append(voto)
        print('Voto computado com sucesso!')
    else:
        votosNulos.append(voto)
        print('Voto computado com sucesso!')
print(f'O candidato X recebeu {len(votosX)} votos')
print(f'O candidato Y recebeu {len(votosY)} votos')
print(f'O candidato Z recebeu {len(votosZ)} votos')
print(f'Total de votos nulos {len(votosNulos)} votos')

if votosX > votosZ and votosX > votosY:
    print('O vencedor foi o candidato X!')
elif votosY > votosX and votosY > votosZ:
    print('O vencedor foi o candidato Y!')
elif votosZ > votosY and votosZ > votosX:
    print('O vencedor foi o candidato Z!')