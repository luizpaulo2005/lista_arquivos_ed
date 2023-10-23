import os
arquivo = open('./ex02.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()

    if os.path.exists('ex02new.txt'):
        novoArquivo = open('./ex02new.txt', 'w')
    else:
        novoArquivo = open('./ex02new.txt', 'x')

    novoArquivo.write('Codigo ASCII de cada caractere em um arquivo\n')
    
    for item in texto.strip():
        if item not in " ":
            novoArquivo.write(f'"{item}" - {ord(item)}\n') 

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')