try:
    NOME_ARQ = input('Digite o nome do arquivo a ser aberto: ')
    ARQ = open( NOME_ARQ, 'rb')

except:
    print('O ARQUIVO NÃO EXISTE!')

else:
    CAP = ARQ.read(4)
    TOTAL_REG = int.from_bytes(CAP)
    RRN = ...

    if RRN >= TOTAL_REG:
        print("ERRO!")

    








