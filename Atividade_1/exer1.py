sugestao_arquivo = input('Nome do novo arquivo: ')
arq = open(sugestao_arquivo, 'w')
SOBRENOME = input('Sobrenome: ')

while SOBRENOME != '':
    arq.write(SOBRENOME + '|')

    NOME = input('Nome: ')
    arq.write(NOME + '|')

    ENDEREÇO = input('Endereço: ')
    arq.write(ENDEREÇO + '|')

    CIDADE = input('Cidade: ')
    arq.write(CIDADE + '|')

    ESTADO = input('Estado: ')
    arq.write(ESTADO + '|')

    CEP = input('CEP: ')
    arq.write(CEP + '|')

    SOBRENOME = input('Sobrenome: ')

arq.close()
















