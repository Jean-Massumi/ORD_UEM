NOME_ARQ = input('Digite o nome do arquivo: ')

arq = open(NOME_ARQ,'wb')
CAMPO = input(f'{" " * 5 }Sobrenome: ')

dados_pessoais = ['Nome: ', 'Endereço: ', 'Cidade: ', 'Estado: ', 'CEP: ']

while CAMPO != '':
    BUFFER = ''
    BUFFER += CAMPO + '|'

    for campo in dados_pessoais:
        CAMPO = input(f'{" " * 5}{campo}')
        BUFFER += CAMPO + '|'

    print(' ')
    BUFFER = BUFFER.encode()
    TAM = len(BUFFER)
    TAM = TAM.to_bytes(2)

    arq.write(TAM)
    arq.write(BUFFER)
    CAMPO = input(f'{" " * 5 }Sobrenome: ')
arq.close()
