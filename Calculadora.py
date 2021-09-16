# Criado por: Elcio Furtili
# Data: 15 Set 2021
# Calculador com Histório e Validação de Resultado Divisivel por 10

# Varíavel Global para Gravação do Histórico
history_data = ''

# Função Inicial
# Chamada das Funções de Histórico e Cálculo
def welcome():
    wel = input('''
    **********************************
    *     Bem vindo a Calculadora!   *
    *                                *
    *   1 - Calculadora              * 
    *   2 - Histórico                *
    *   3 - Sair                     *
    **********************************

            Escolha a Opção:
    ''')

    if wel == '1': 
        calculate()

    elif wel == '2':
        history()
    
    elif wel == '3':
        exit()
    
    else:
        print ('### Opção inserida inválido! ###')
        welcome()

# Função de Cálculo
# Aqui é Feita as Operações e Também é Gravado o Log na Váriavel Global 'history_data'
def calculate():
    operation = input('''
    ******************************************************
    * Selecioneo o Tipo de Operação que Deseja Realizar: *
    *    + Adição                                        *
    *    - Subtração                                     *
    *    * Multiplicação                                 *
    *    / Divisão                                       *
    *    % Percentual                                    *
    ******************************************************

                    Escolha a Operação:
    ''')

    number_1 = int(input('\nInsira o Primeiro Número: '))
    number_2 = int(input('Insira o Segundo Número: '))

    calculo = ''
    result  = ''

    if operation == '+':
        calculo = ('{} + {} = '.format(number_1, number_2))
        result  = number_1 + number_2

    elif operation == '-':
        calculo = ('{} - {} = '.format(number_1, number_2))
        result  = number_1 - number_2

    elif operation == '*':
        calculo = ('{} * {} = '.format(number_1, number_2))
        result  = number_1 * number_2

    elif operation == '/':
        calculo = ('{} / {} = '.format(number_1, number_2))
        result  = number_1 / number_2

    elif operation == '%':
        calculo = ('{} % {} = '.format(number_1, number_2))
        result  = number_1 % number_2

    else:
        print('### Foram inserido informações de Calculo Invalidas, Tente novamente! ###')
    
    print(str(calculo) + str(result))

    # Instancia da Variável Global 'history_data'
    global history_data 
    history_data = history_data + (str(calculo) + str(result)) + '\n'

    # Validação se é Divisível por 10
    if result % 10 == 0:
        print('*** Valor é Divisível por 10! ***')

    again()

# Função do Histórico
# Aqui valida se existem registros na variável global, caso não exisa ele informa.
def history():
    if history_data == '':
        print ('''\n
        ### Histórico Vazio! ###
        ''')

    else:
        print('''
        ******************************
        *   Histórico de Cálculos:   *
        ******************************
        ''')

    print(history_data)
    welcome()

# Função de Repetição para Lançamento de Múltiplos Calculos
def again():
    calc_again = input('''
    ***********************************
    * Deseja Calcular Novamente?      *
    * Digite S para SIM e N para NÃO. *
    ***********************************

            Escolha a Opção:
    ''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        welcome()
    else:
        print('Valor digitado invalido!')
        again()

welcome()