nomeArq = input("Informe o nome do arquivo a ser lido: ")

try:
    arq = open(nomeArq, "r")
    print("Arquivo encontrado!")

except:
    print("Arquivo não encontrado!")

else:
    tamanhoDoArquivo = 0
    quantidadeDeLinhas = 1
    char = arq.read(1)

    while char:
        tamanhoDoArquivo += 1

        if char == "\n":
            quantidadeDeLinhas += 1

        char = arq.read(1)
        
    int_to_byte = tamanhoDoArquivo.to_bytes()

    print("Tamanho do arquivo em inteiro: ", tamanhoDoArquivo)
    print("Tamanho do arquivo em bytes: ", int_to_byte)
    print("Quantidade de linhas no arquivo: ", quantidadeDeLinhas)

    arq.close()

