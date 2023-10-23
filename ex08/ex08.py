arquivo = open('./ex08.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()
    novoTexto = texto.split('\n')

    palavra = input('Digite a palavra que deseja procurar: ')

    for item in novoTexto:
        if palavra.lower() in item.strip('.,!?()[]{}"\'').lower():
            print(item)

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()