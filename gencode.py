
def gencode (sequencia, cap='mai'):
    from random import randint, choice
    import string

    '''
    lang = pt-br
    Gera uma sequência personalizável de números e letras aleatórias.

    Possui 2 parâmetros, sendo o primeiro obrigatório e o segundo, se não declarado, gera letras maiúsculas por padrão. Recebem strings como argumentos, sendo eles:

    --> sequencia:
        Recebe 3 tipos de argumentos, sendo eles:
        * ('n0/l0/n0...'):
            Escreva o padrão e a quantidade de letras e/ou números que deseja gerar, sendo que 'l' para letras e 'n' para números e em seguida, sem espaços, digite a quantiade de caractere da respectiva letra ou número que deseja gerar separando cada conjunto com o sinal de '/'.
            Ex 1: ('l2/n4') Gera uma sequência de 6 caracteres, sendo 2 letras e 4 números = WR0933
            Ex 2: ('n2/l4/n1') Gera uma sequência de 7 caracteres, sendo 2 letras, 4 números e 1 letra = 51PGRT9
        * ('aleat'):
            Gera uma sequência de letras e números totalmente aleatória com tamanho que varia entre mínimo de 4 caracteres e máximo de 9 caracteres.
        * ('aleat/0):
            Gera uma sequência totalmente aleatória mas seu tamanho pode ser definido após a '/'.
            Ex: ('aleat/3') Gera uma sequência aleatória de 3 caracteres = A12

    --> cap:
        Captaliza as sequências de letras. Recebe 3 argumentos, sendo eles:
            * (cap ='mai'):
                Para tornar todas as letras maiúsculas (padrão).
            * (cap ='min'):
                Para tornar todas letras minúsculas.
            * (cap ='aleat')
                Para tornar algumas letras maisúsculas e minúsculas aleatoriamente.

    Exemplos:
        gencode ('l3/n2/l1','aleat'): = rAt38x
        gencode ('aleat/6', 'min'): = 2fn71b
        gencode ('aleat'): = ASV80M2
    '''

    resultado = str() # Recebe a lista de conjuntos de sequências unidos em uma única string.
    conjuntos = list() # Recebe uma lista dos conjuntos de sequências de letras e/ou números.
    argumentos_list = sequencia.split('/')

    ####### Sequencia Personalizada (l0/n0...)
    if 'aleat' not in argumentos_list: # Se o argumento 'aleat' não for declarado...
        for arg in argumentos_list:
            quantidade = int(arg[1:])  # Remove a letra (l ou n) do conjunto, deixando apenas os números. Será usado para definir a quantidade de letras ou números que será gerado mais a frente.

            # Gerando as letras conforme a quantidade passada no conjunto 'l'
            if 'l' in arg:
                l_list = list()
                l_sequencia = str()
                
                for _ in range(quantidade):
                    letra = choice(string.ascii_letters)

                    # Configuração do argumento 'aleat' do parâmetro cap.
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

        resultado = resultado.join(conjuntos) # Juntando os conjuntos l e n para formar uma única string de código.

    ####### Sequências Aleatórias (aleat e aleat/0)
    elif 'aleat' in argumentos_list:
        aleat_sequencia = str()
        aleat_list = list()

        # Gerando a sequência totalmente aleatória (aleat)
        if argumentos_list[0] == 'aleat' and len(argumentos_list) == 1:
            tamanho_minmax = randint(4, 9) # O tamanho do código gerado de forma totalmente aleatória terá, por padrão, o tamanho min de 4 caracteres e o tamanho máx de 9 caracteres. Os tamanhos serão escolhido aqui.
            for _ in range(tamanho_minmax):
                escolha = choice([choice(string.ascii_letters), str(randint(0, 9))])

                # Configuração do argumento 'aleat' do parâmetro cap.
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

                # Configuração do argumento 'aleat' do parâmetro cap.
                if cap == 'aleat' and escolha2 == escolha2[0]:
                        cap_aleat3 = randint(0, 1)
                        if cap_aleat3 <= 0:
                            escolha2 = escolha2.lower()
                        else:
                            escolha2 = escolha2.upper()

                aleat_list.append(escolha2)
            aleat_sequencia = aleat_sequencia.join(aleat_list)
        resultado = aleat_sequencia

    ##### Configuração dos argumentos 'mai' e 'min' do parâmetro cap.
    if cap == 'mai':
        resultado = resultado.upper()
    elif cap == 'min':
        resultado = resultado.lower()

    return resultado

#
#
##### TESTANDO A FUNÇÃO
print('Sequencia com padrão personalizado. Letras minúsculas')
print(gencode('n2/l4','min'))
print('Sequencia com padrão personalizado. Letras miúsculas padrão')
print(gencode('n2/l1/n1/l2'))
print('Sequencia com padrão personalizado. Letras aleatórias')
print(gencode('l5','aleat'))
print('Sequencia com padrão aleatório. Letras maiúsculas padrão')
print(gencode('aleat'))
print('Sequencia com padrão aleatório e tamanho definido. Letras aleatórias')
print(gencode('aleat/5', 'aleat'))
print('Obrigado ;-) ')