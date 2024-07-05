def main() -> None:
    print("REMOÇÃO DE ESPAÇOS REPETIDOS")
    nomeArq = input("Informe o nome do arquivo a ser lido: ")

    try:
        arq = open(nomeArq, "r")
        print("ARQUIVO ENCONTRADO!")

    except:
        print("ARQUIVO INEXISTENTE!")

    else:
        atual = arq.read(1)
        antes = ""

        novoArq = open("semEspacoRep", "w")
        while atual:
            if (atual != antes) or ((antes != " ") and (atual != " ")):
                novoArq.write(atual)
                antes = atual

            atual = arq.read(1)
        
        novoArq.close()
        arq.close()



if __name__ == '__main__':
    main()
