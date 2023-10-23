import os

arquivo = open('./ex04.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()

    novoTexto = texto.split('\n')

    if os.path.exists('ex04new.txt'):
        novoArquivo = open('./ex04new.txt', 'w')
    else:
        novoArquivo = open('./ex04new.txt', 'x')
    
    for item in novoTexto:
        novoArquivo.write(f'{item[::-1]}\n')

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close