nome_arquivo = input('Digite o nome do arquivo: ')
arq = open(nome_arquivo, 'w')
SOBRENOME = input('Sobrenome: ')

while SOBRENOME != '':
    arq.write(SOBRENOME + '|')

    NOME = input('Nome: ')
    arq.write(NOME + '|')

    ENDERECO = input('Endereço: ')
    arq.write(ENDERECO + '|')

    CIDADE = input('Cidade: ')
    arq.write(CIDADE + '|')

    ESTADO = input('Estado: ')
    arq.write(ESTADO + '|')

    CEP = input('CEP: ')
    arq.write(CEP + '|')

    SOBRENOME = input('Sobrenome: ')

arq.close()
















