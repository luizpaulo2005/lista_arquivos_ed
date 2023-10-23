arquivo = open('./ex03.txt', 'r', encoding='utf-8')

if arquivo.readable():
    texto = arquivo.read()
    palavras = {}

    # print(texto.split())

    for item in texto.split():
        if item in palavras:
            palavras[item] += 1
        else:
            palavras[item] = 1

    print(palavras)

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()