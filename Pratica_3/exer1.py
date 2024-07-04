import io

VALOR_BAIXO = ''
VALOR_ALTO = '~'

def inicialize() -> tuple[str, str, io.TextIOWrapper, io.TextIOWrapper, io.TextIOWrapper, bool]:

    ant1 = VALOR_BAIXO
    ant2 = VALOR_BAIXO

    lista1 = open('lista1.txt', 'tr')
    lista2 = open('lista2.txt', 'tr')

    saida = open('arq.txt', 'w')
    existem_mais_nomes = True

    return ant1, ant2, lista1, lista2, saida, existem_mais_nomes


def leia_nome(lista: io.TextIOWrapper, nome_ant: str, nome_outra_lista: str, existem_mais_nomes: bool) -> tuple[str, str, bool]:

    nome = lista.read()
    if nome == ' ':
        if nome_outra_lista == VALOR_ALTO:
            existem_mais_nomes = False
        else:
            nome = VALOR_ALTO
    else:
        if nome <= nome_ant:
            raise 'Erro na checagem de sequencia'

    nome_ant = nome

    return nome, nome_ant, existem_mais_nomes


def merge () -> None:
    nome1, nome2, lista1, lista2, saida, existem_mais_nomes = inicialize()

    print(lista2)


    # leia_nome(lista1, nome1, nome2, existem_mais_nomes)
    # leia_nome(lista2, nome2, nome1, existem_mais_nomes)

    # while existem_mais_nomes:
    #     if nome1 < nome2:
    #         saida = nome1
    #         leia_nome(lista1, nome1, nome2, existem_mais_nomes)
    #     elif nome1 > nome2:
    #         saida = nome2
    #         leia_nome(lista2, nome2, nome1, existem_mais_nomes)
    #     else:
    #         saida = nome1
    #         leia_nome(lista1, nome1, nome2, existem_mais_nomes)
    #         leia_nome(lista2, nome2, nome1, existem_mais_nomes)

    # lista2.close()
    # lista1.close()
    # saida.close()




if __name__ == '__main__':
    merge()
