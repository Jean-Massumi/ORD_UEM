try:
    NOME_ARQ = input('Digite o arquivo para ser lido: ')

    arq = open(NOME_ARQ, 'r')
    print('Arquivo aberto!')

    def leia_campo(ENTRADA):
        CAMPO = ''
        C = ENTRADA.read(1)
        while C != '' and C != '|':
            CAMPO += C
            C = ENTRADA.read(1)
        
        return CAMPO


    CAMPO = leia_campo(arq)
    i = 1
    while CAMPO != '':
        print(f'{" "*8}Campo #{i}: {CAMPO}')
        CAMPO = leia_campo(arq)
        i += 1

    print('-----' * 15)
    arq.close()

except:
    print('O arquivo não foi aberto, fim do programa!')














