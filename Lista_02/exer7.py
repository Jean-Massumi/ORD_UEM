def main() -> None:
    '''
        Complemento do exercicio 6.
        Converte o arquivo de bytes para inteiro.
    
    '''
    nomeArq = input("Informe o nome do arquivo: ")
    Arq = open(nomeArq, "rb")
    intByte = Arq.read(4)

    while intByte:
        convert = int.from_bytes(intByte)
        print(convert)
        intByte = Arq.read(1)
        intByte = Arq.read(4)


if __name__ == "__main__":
    main()