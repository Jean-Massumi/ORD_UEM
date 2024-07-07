def main() -> None:
    '''
        Complemento do exercicio 8.
    
    '''
    Arq = open('ArquivoTeste.txt', "rb")
    tam = Arq.read(2)

    while tam:
        tam = int.from_bytes(tam)
        tam = Arq.read(tam).decode()
        print(tam)

        tam = Arq.read(2)


if __name__ == '__main__':
    main()
