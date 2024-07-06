def registro(ARQ, total_REG: int, option: int) -> None:

    while option < 3:
            Dados = ["Sobrenome", "Nome", "Endereço", "Cidade", "Estado", "CEP"]
            if option == 1:
                REG = ""
                print("Digite os dados para o novo registro: ")
                for campo in Dados:
                    CAMPOS = input(f'{"  " * 3}{campo} : ')
                    REG += CAMPOS + '|'

                REG = REG.encode().ljust(64, b'\0')
                offset = total_REG * 64 + 4
                ARQ.seek(offset, 0)
                ARQ.write(REG)
                total_REG += 1

            elif option == 2:
                RRN = int(input("Digite o número do RRN: "))
                print('\r')
                if RRN >= total_REG:
                    print("Registro não encontrado!")

                else:
                    offset = RRN * 64 + 4
                    ARQ.seek(offset, 0)
                    print("Informações do registro: ")

                    for campo in REG.decode().split(sep='|'):
                        print("  " * 3, campo)

                    print('\n')
                    print("Você quer modificar esse registro? ")
                    resposta = input("Responda S ou N, seguido de <ENTER> ==> ")
                    print("\n")

                    if resposta.lower() == "S":
                        print("Digite os novos dados do novo registro: ")
                        print("\r")
                        for campo in Dados:
                            CAMPOS = input("  " * 3, campo, ": ")
                            REG += CAMPOS

                        REG = REG.encode().ljust(64, b'\0')
                        offset = total_REG * 64 + 4
                        ARQ.seek(offset, 0)
                        ARQ.write(REG)

            option = interface()

    ARQ.seek(0)
    ARQ.write(total_REG.to_bytes(4))
    ARQ.close()



def interface() -> int:
    print("  " * 3, "PROGRAMA PARA INSERÇÃO E ALTERAÇÃO DE REGISTROS")
    print("\r")
    print("Suas opções são: ")
    print("\r")
    print(" " * 2, "1. Inserir novo registro")
    print(" " * 2, "2. Buscar um registro por RRN para alterações")
    print(" " * 2, "3. Terminar o programa")
    print("\r")

    option = int(input("Digite o número de suas escolha: "))

    return option



def main () -> None:
    option = -1

    nomeArq = input("Nome do arquivo: ")
    try:
        ARQ = open(nomeArq, "r+b")
        total_REG = ARQ.read(4)

    except FileNotFoundError:
        ARQ = open(nomeArq, "w+b")
        total_REG = 0
        ARQ.write(total_REG.to_bytes(4))

    option = interface()
    print("")
    registro(ARQ, total_REG, option)
   

if __name__ == '__main__':
    main()

