
def gencode (sequencia, cap='mai'):
    from random import randint, choice
    import string

    '''
    Gera uma sequência personalizável de números e letras aleatória.

    Params:
        sequencia - introduza, entre aspas, a quantidade de letras e/ou números que deseja gerar, sendo que 'l' para letras e 'n' para números e em seguida, sem espaços, digite a quantiade de caractere da respectiva letra ou número que deseja gerar separando cada conjunto com o sinal de '/'.
        Ex 1: 'l2/n4'
        Gera uma sequência de 6 dígitos, sendo 2 letras e 4 números - WR0933
        Ex 2: 'n2/l4/n1' = 51PGRT9
        Para gerar aleatoriamente use 'aleat' como argumento deste param.

        cap - captaliza as sequências de letras, sendo:
            cap ='mai' para tornar todas as letras maiúsculas (padrão).
            cap ='min' para tornar todas letras minúsculas.
            cap ='aleat' para tornar algumas letras maisúsculas e minúsculas aleatoriamente.
    '''

    resultado = str() # Recebe a lista de conjuntos de sequências unidos em uma única string.
    conjuntos = list() # Recebe uma lista dos conjuntos de sequências de letras e/ou números.
    argumentos_list = sequencia.split('/')

    ####### Sequencia Personalizada (l0/n0...)
    if 'aleat' not in argumentos_list: # Se o argumento 'aleat' não for declarado...
        for arg in argumentos_list:
            quantidade = int(arg[1:])  # Remove a letra (l ou n) do conjunto, deixando apenas os números. Será usado para definir a quantidade de letras ou números que será gerado.

            # Gerando as letras conforme a quantidade passada no conjunto 'l'
            if 'l' in arg:
                l_list = list()
                l_sequencia = str()
                
                for _ in range(quantidade):
                    letra = choice(string.ascii_letters)

                    # Configuração do argumento 'aleat' do parâmetro 'cap'.
                    if cap == 'aleat':
                        cap_aleat1 = randint(0, 1)
                        if cap_aleat1 <= 0:
                            letra = letra.lower()
                        else:
                            letra = letra.upper()

                    l_list.append(letra[:])
                l_sequencia = l_sequencia.join(l_list)
                conjuntos.append(l_sequencia[:])
                    
            # Gerando os números conforme a quantidade passada no conjunto 'n'
            if 'n' in arg:
                n_list = list()
                n_sequencia = str()

                for _ in range(quantidade):
                    numero = randint(0,9)
                    n_list.append(str(numero))

                n_sequencia = n_sequencia.join(n_list)
                conjuntos.append(n_sequencia[:])
                n_list.clear()

        resultado = resultado.join(conjuntos)

    ####### Sequencias Aleatórias (aleat e aleat/0)
    elif 'aleat' in argumentos_list:
        aleat_sequencia = str()
        aleat_list = list()

        # Gerando sequencia totalmente aleatória (aleat)
        if argumentos_list[0] == 'aleat' and len(argumentos_list) == 1:
            tamanho_minmax = randint(4, 9) # O tamanho do código gerado de forma totalmente aleatória terá, por padrão, o tamanho min de 4 caracteres e o tamanho máx de 9 caracteres. Os tamanhos serão escolhido aqui.
            for _ in range(tamanho_minmax):
                escolha = choice([choice(string.ascii_letters), str(randint(0, 9))])

                if cap == 'aleat' and escolha == escolha[0]:
                        cap_aleat2 = randint(0, 1)
                        if cap_aleat2 <= 0:
                            escolha = escolha.lower()
                        else:
                            escolha = escolha.upper()

                aleat_list.append(escolha)
            aleat_sequencia = aleat_sequencia.join(aleat_list)
        resultado = aleat_sequencia

        # Gerando sequência aleatória mas com tamanho personalizável (aleat/0)
        if argumentos_list[0] == 'aleat' and len(argumentos_list) ==2:
            for _ in range(int(argumentos_list[1])):
                escolha2 = choice([choice(string.ascii_letters.upper()), str(randint(0, 9))])

                if cap == 'aleat' and escolha2 == escolha2[0]:
                        cap_aleat3 = randint(0, 1)
                        if cap_aleat3 <= 0:
                            escolha2 = escolha2.lower()
                        else:
                            escolha2 = escolha2.upper()

                aleat_list.append(escolha2)
            aleat_sequencia = aleat_sequencia.join(aleat_list)
        resultado = aleat_sequencia

    ##### Configuração dos argumentos do parâmetro 'cap'.
    if cap == 'mai':
        resultado = resultado.upper()
    elif cap == 'min':
        resultado = resultado.lower()


    return resultado





print(gencode('n2/l4','min'))
print(gencode('n2/l4'))
print(gencode('l9','min'))
print(gencode('aleat','aleat'))
print(gencode('aleat'))
print(gencode('aleat/5', 'aleat'))

x = 'l3/n1'

print(gencode(x))
