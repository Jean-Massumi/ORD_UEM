try:
    NOME_ARQ = input("Entre com o nome do arquivo a ser aberto: ")

    ARQ = open( NOME_ARQ, 'rb')
    print(" ")

except:
    print("O arquivo não existe!")

else:
    def leia_reg(arquivo):
        TAM = arquivo.read(2)
        TAM = int.from_bytes(TAM)

        if TAM > 0:
            BUFFER = arquivo.read(TAM)
            BUFFER = BUFFER.decode()

            return BUFFER
        else:
            return ''

    CHAVE = input("Digite o sobrenome a ser buscado: ")
    print(" ")
    ACHOU = False
    REG = leia_reg(ARQ)

    while REG != "" and not(ACHOU):
        sobrenome = REG.split(sep='|')[0]
        if sobrenome == CHAVE:
            ACHOU = True
        else:
            REG = leia_reg(ARQ)

    if ACHOU:
        cont = 1
        for campo in REG.split(sep= '|'):
            if campo != '':
                print(f'{"   " * 4} Campo {cont}: {campo}')
                cont += 1

        print(" ")
    else:
        print("Arquivo não encontrado!")

    ARQ.close()
