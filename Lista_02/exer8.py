def main() -> None: 
    dados = ["Nome: ", "Cidade: ", "Sexo: "]
    Arq = open("ArquivoTeste.txt", "wb")

    for campo in dados:
        CAMPOS = input(f'{campo}')
        tamCampo = len(CAMPOS)
        Arq.write(tamCampo.to_bytes(2))
        Arq.write(CAMPOS.encode())


if __name__ == '__main__':
    main()
