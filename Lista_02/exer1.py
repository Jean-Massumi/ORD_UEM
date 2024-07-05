nomeArq = input("Digite o nome do arquivo: ")
try:
    arq = open(nomeArq, "w")
except:
    print("Arquivo não encontrado!")

else:
    Dados = input("Informe alguns dados : ")
    while Dados != "":
        arq.write(Dados)
        Dados = input("Informe alguns dados : ")

finally:
    arq.close()

















