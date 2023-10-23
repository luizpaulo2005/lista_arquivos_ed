import os
arquivo = open('./ex05.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()

    if os.path.exists('ex05new.txt'):
        novoArquivo = open('./ex05new.txt', 'w')
    else:
        novoArquivo = open('./ex05new.txt', 'x')

    novoTexto = []

    for item in texto.split():
        novoTexto.append(item.strip('.,!?()[]{}"\'').lower())

    novoTexto.sort()
    
    for item in novoTexto:
        novoArquivo.write(f'{item} ')

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()