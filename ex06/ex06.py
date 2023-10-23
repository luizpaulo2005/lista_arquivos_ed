import os
arquivo = open('./ex06.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()
    novoTexto = texto.split('\n')
    novoTexto.sort()

    if os.path.exists('ex06new.txt'):
        novoArquivo = open('./ex06new.txt', 'w')
    else:
        novoArquivo = open('./ex06new.txt', 'x')

    for item in novoTexto:
        novoArquivo.write(f'{item}\n')

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()