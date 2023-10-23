import os
arquivo = open('./ex10.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()
    novoTexto = texto.split('\n')

    if os.path.exists('ex10new.txt'):
        novoArquivo = open('./ex10new.txt', 'w')
    else:
        novoArquivo = open('./ex10new.txt', 'x')

    for item in novoTexto:
        novoArquivo.write(f'{item.upper()}\n')

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()