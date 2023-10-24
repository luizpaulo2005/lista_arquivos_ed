arquivo = open('./ex01.txt', 'r', encoding='utf-8')
vogal = 0
consoante = 0

if arquivo.readable():
    vogais = list('aãáàeèéiíìoõóòuúù')
    for item in arquivo.read().strip():
        if item.lower() in vogais:
            vogal += 1
        elif item not in vogais and item not in ' ':
            consoante += 1

    print(f'A quantidade de vogais é {vogal}')
    print(f'A quantidade de consoantes é {consoante}')

    arquivo.close()
else:
    print('Arquivo não legível')
    arquivo.close()