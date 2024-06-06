NOME_ARQ = input('Digite o nome do arquivo: ')

arq = open(NOME_ARQ,'wb')
CAMPO = input('Sobrenome: ')

while CAMPO != '':
    BUFFER = ''
    BUFFER += CAMPO + '|'

    for campo in CAMPO:
        CAMPO = campo
        BUFFER += CAMPO + '|'

    TAM = len(BUFFER.encode())
    TAM.to_bytes(2)

    arq.write(TAM)
    arq.write(BUFFER)
    CAMPO = input('Sobrenome: ')

arq.close()
