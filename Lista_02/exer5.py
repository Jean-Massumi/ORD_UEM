def converter(Entrada, Saida, conversao) -> None:
    '''
        Faz a conversão do arquivo de "Entrada" para a conversão que o usuario informou em 
        "conversao". 

        Se o arquivo de entrada for == conversao entao retorne "Arquivo de entrada já está no seu formato 'conversao'" 
        Senão o resultado da conversao do arquivo será gravado em um novo arquivo
    
    '''
    if conversao.upper() == "WINDOWS":
        char = Entrada.read(1)

        while char:
            if (char == b'\n'):
                Saida.write(b'\r')

            Saida.write(char)
            char = Entrada.read(1)

    elif conversao.upper() == "LINUX":
        char = Entrada.read(1)

        while char:
            if (char == b'\r'):
                char = Entrada.read(1)

            Saida.write(char)
            char = Entrada.read(1)



def main() -> None:
    nomeArq = input("Informe o nome do arquivo: ")

    try:
        arq = open(nomeArq, "rb")
        print("ARQUIVO ENCONTRADO!")

    except: 
        print("ARQUIVO INEXISTENTE!")

    else:
        conversao = input("Você quer converter o arquivo para [Windows/Linux]? ")
        nomeNovoArq = 'ConvertidoPara' + conversao.upper()
        novoArq = open(nomeNovoArq, "wb")
        converter(arq, novoArq, conversao)

        arq.close()
        novoArq.close()


if __name__ == "__main__":
    main()
