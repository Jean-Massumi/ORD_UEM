def main() -> None:
    lista = []

    print("Informe 10 números inteiros: ")
    for i in range(1,11):
        num = int(input(f'{i} número: '))
        lista.append(num)

    numeros = open("tenNumber", "wb")
    for num in lista:
        numeros.write(num.to_bytes(4) + b"|")

    numeros.close()


if __name__ == "__main__":
    main()

