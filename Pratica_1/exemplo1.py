nomeArq = input('Digite o nome do arquivo: ')

try:
    arq = open(nomeArq, "r")
    c = arq.read(1)
    while c:
        print(c)
        c = arq.read(1)

except:
    print(f'Não foi possível abrir o arquivo {nomeArq}.')

