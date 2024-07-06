def removeComentarios(Entrada, Saida) -> None:
    char = Entrada.read(1)

    while char:
        if (char == "#"):
            while (char != "\n"):
                char = Entrada.read(1)
                if (char == "\n"):
                    Saida.write(char)

        else:
            Saida.write(char)

        char = Entrada.read(1)


def main() -> None:
    print("Copia um codigo python sem os comentarios")
    NomeArq = input("Informe o nome do arquivo Python: ")

    try:
        arq = open(NomeArq, "r")
        print("ARQUIVO ENCONTRADO!")

    except:
        print("ARQUIVO INEXISTENTE!")

    else:
        novoArq = open("CopiaExer4.py", "w")

        removeComentarios(arq, novoArq)

        arq.close()
        novoArq.close()


if __name__ == "__main__":
    main()
