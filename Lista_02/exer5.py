def converter(Entrada, Saida) -> None:
    ...












def main() -> None:
    nomeArq = input("Informe o nome do arquivo: ")

    try:
        arq = open(nomeArq, "rb")
        print("ARQUIVO ENCONTRADO!")

    except: 
        print("ARQUIVO INEXISTENTE!")

    else:
        conversao = input("Você quer converter o arquivo para [Windows/Linux]? ")
        novoArq = open(conversao, "wb")








if __name__ == "__main__":
    main()
