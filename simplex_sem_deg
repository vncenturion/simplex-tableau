import numpy as np

np.set_printoptions(precision=2, suppress=True)

def imprimir_tableau(tableau, iteracao):
    print(f"\nTableau - Iteração {iteracao}")
    print(tableau)

def imprimir_tableau_rotulado(tableau, rotulos_tableau, num_variaveis):
    rotulos_colunas = [" "] + [rotulos_tableau.get(int(idv), f"x?") for idv in tableau[0, 1:-1]] + ["LD"]
    rotulos_linhas = [rotulos_tableau.get(int(idv), f"x?") for idv in tableau[1:, 0]]

    print("\n" + "\t".join(rotulos_colunas))
    for i, linha in enumerate(tableau[1:]):
        print(f"{rotulos_linhas[i]}	" + "\t".join(f"{val:.2f}" for val in linha[1:]))

def gerar_rotulos(n):
    return ["Z"] + [f"x{i+1}" for i in range(n)] + ["LD"]

def simplex(func_objetivo, matriz_restricoes, vetor_restricoes, tipo='max'):
    lista_tableaus = []
    num_restricoes, num_variaveis = matriz_restricoes.shape

    id_variaveis = np.arange(11001, 11001 + num_variaveis, dtype=int)
    rotulos_tableau = {11000: 'Z'}
    for i, idv in enumerate(id_variaveis):
        rotulos_tableau[idv] = f"x{i+1}"

    id_base = np.arange(11001 + num_variaveis - num_restricoes, 11001 + num_variaveis, dtype=int)

    tableau = np.zeros((num_restricoes + 2, num_variaveis + 2))
    tableau[2:, 1:-1] = matriz_restricoes
    tableau[2:, -1] = vetor_restricoes

    if tipo == 'min':
        func_objetivo = [-coef for coef in func_objetivo]

    tableau[1, 1:-1] = -np.array(func_objetivo)
    tableau[0, 1:-1] = id_variaveis
    tableau[0, -1] = 0.
    tableau[1, 0] = 11000.
    tableau[2:, 0] = id_base

    lista_tableaus.append(tableau.copy())

    iteracao = 0

    while np.any(tableau[1, 1:-1] < 0):

        imprimir_tableau(tableau, iteracao)

        iteracao += 1

        indice_entrada = np.argmin(tableau[1, 1:-1]) + 1
        rotulo_entrada = rotulos_tableau.get(int(tableau[0, indice_entrada]), f"x?")
        print(f"\nVariável que entra na base: {rotulo_entrada}")

        termos_lado_direito = tableau[2:, -1]
        coluna_entrada = tableau[2:, indice_entrada]
        with np.errstate(divide='ignore', invalid='ignore'):
            razoes = np.where(coluna_entrada > 0, termos_lado_direito / coluna_entrada, np.inf)
        indice_saida = np.argmin(razoes) + 2

        rotulo_saida = rotulos_tableau.get(int(tableau[indice_saida, 0]), f"x?")
        print(f"Variável que sai da base: {rotulo_saida}")

        print(f"Elemento pivô: {tableau[indice_saida, indice_entrada]:.2f}")
        pivo = tableau[indice_saida, indice_entrada]
        tableau[indice_saida, 1:] /= pivo

        for i in range(1, len(tableau)):
            if i != indice_saida:
                tableau[i, 1:] -= tableau[i, indice_entrada] * tableau[indice_saida, 1:]

        tableau[indice_saida, 0] = tableau[0, indice_entrada]

        lista_tableaus.append(tableau.copy())

    imprimir_tableau(tableau, iteracao)
    print(f"\nSolução ótima encontrada após {iteracao} iterações")
    print("Z =", tableau[1, -1])

    print("\nTableau a cada iteração:")
    for t in lista_tableaus:
        imprimir_tableau_rotulado(t, rotulos_tableau, num_variaveis)
        print()

    return lista_tableaus
