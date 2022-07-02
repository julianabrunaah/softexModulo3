
print('Responda algumas perguntas e o ajudaremos a escolher o melhor veículo')
capacidade = int(input('Digite a capacidade de transporte de pessoas que deseja que seu veículo possua: '))
rodas = int(input('Digite a quantidade de rodas: '))
peso = int(input('Digite o peso bruto em quilogramas: '))

if rodas>=2 and rodas<4 and capacidade<=2:
    print('Seu veículo deve ser uma moto ou triciclo')
elif rodas==4 and capacidade<=8 and peso<=3500:
    print('Seu carro ideal deve ser um Kia Carvival ou Ford Expedition')
elif rodas>=4 and capacidade>8 and capacidade<=20:
    print('Seu veículo ideal é um Micro-ônibus. Os dois modelos disponíveis são: Macopolo Senior Midi 2010 e Volare fly 10')
    #necessario adicionar opção 
elif rodas>4 and capacidade>20:
    print('Seu carro ideal deve um ônibus')
    #necessario especificar a capacidade para não ocorrer erros
elif rodas>=4 and peso>3500 and peso<=6000 and capacidade<=3:
    print('Seu veículo ideal é um caminhão leve. Os dois principais modelos no mercado hoje são: Hyundai HD 80 e Mercedes-Benz Accelo 1016')
elif rodas>=4 and peso>=6000 and capacidade<=3:
    print('Sei veículo ideal é um caminhão')
else:
    print('No momento não possuimos veículos com as especificações sugeridas')