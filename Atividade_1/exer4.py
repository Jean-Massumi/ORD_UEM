def leia_reg(arquivo):
    TAM = arquivo.read(2)
    TAM = int.from_bytes(TAM)

    if TAM > 0:
        BUFFER = arquivo.read(TAM)
        BUFFER = BUFFER.decode()

        return BUFFER
    else:
        return ''

try:
    NOME_ARQ = input('Digite o nome do arquivo para ser lido: ')

    Arq = open(NOME_ARQ, 'rb')
    BUFFER = leia_reg(Arq)

    i = 1
    while BUFFER != '':
        LISTA = BUFFER.split(sep='|')
        print(f'Registro #{i} (Tam = {len(BUFFER)}):')
        cont_dados = 0

        for campo in LISTA:
            cont_dados += 1
            if campo != '':
                print(f'{" " * 8}Campo #{cont_dados}: {campo}')

        BUFFER = leia_reg(Arq)
        i += 1
        print(' ')

    Arq.close()

except:
    print('O arquivo ainda não foi aberto')






