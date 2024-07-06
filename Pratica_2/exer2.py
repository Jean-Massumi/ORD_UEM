NOME_ARQ = input('Digite o nome do arquivo a ser aberto: ')

try:
    ARQ = open( NOME_ARQ, 'rb')
    print("ARQUIVO ENCONTRADO!")

except:
    print('O ARQUIVO NÃO EXISTE!')

else:
    CAB = ARQ.read(4)
    TOTAL_REG = int.from_bytes(CAB)
    RRN = int(input("Informe o número do RRN: "))

    if RRN >= TOTAL_REG:
        print("ERRO!")

    byteOffset = RRN * 64 + 4
    ARQ.seek(byteOffset, 0)
    REG = ARQ.read(64).decode()

    print("REGISTRO N", RRN, ":")
    cont = 1
    for campo in REG.split(sep= "|"):
        if cont != 7: 
            print(" "*4, "CAMPO ", cont, ": ", campo )
            cont += 1

    ARQ.close()
