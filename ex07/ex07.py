arquivo = open('./ex07.txt', 'r')

if arquivo.readable():
    texto = arquivo.read()
    novoTexto = texto.split('\n')
    
    maiorLinha = ""
    maiorTamanho = 0

    for item in novoTexto:
        tamanho = len(item.replace(" ", "").replace("\t", "").replace("\n", ""))

        if tamanho > maiorTamanho:
            maiorTamanho = tamanho
            maiorLinha = item
    
    print(f'A maior linha é a \n{maiorLinha}\ncom {maiorTamanho} letras\n')

    print('Operação Concluída')
    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()