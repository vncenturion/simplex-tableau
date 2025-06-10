#EXEMPLO 01

func_objetivo = [3, 5, 0, 0, 0]  # x1, x2, x3, x4, x5

matriz_restricoes = np.array([
    [1, 0, 1, 0, 0],
    [0, 2, 0, 1, 0],
    [3, 2, 0, 0, 1]
], dtype=float)

vetor_restricoes = np.array([4, 12, 18], dtype=float)

# exemplo 01
resultado1=simplex(func_objetivo, matriz_restricoes, vetor_restricoes, tipo='max')

#EXEMPLO 02

func_objetivo = [2, 3, 4, 0, 0, 0]  # x1, x2, x3, s1, s2, s3
matriz_restricoes = np.array([
    [1, 1, 1, 1, 0, 0],
    [2, 2, 3, 0, 1, 0],
    [1, 4, 2, 0, 0, 1],
], dtype=float)
vetor_restricoes = np.array([5, 12, 10], dtype=float)

# rodar exemplo 02
resultado2=simplex(func_objetivo, matriz_restricoes, vetor_restricoes, tipo='max')

#EXEMPLO 03

func_objetivo = [6, 4, 5, 3, 0, 0, 0, 0]  # x1 to x4 + s1 to s4
matriz_restricoes = np.array([
    [1, 1, 1, 1, 1, 0, 0, 0],
    [2, 1, 0, 3, 0, 1, 0, 0],
    [0, 1, 2, 0, 0, 0, 1, 0],
    [1, 0, 0, 2, 0, 0, 0, 1],
], dtype=float)
vetor_restricoes = np.array([10, 15, 8, 7], dtype=float)

# rodar exemplo 03
resultado3=simplex(func_objetivo, matriz_restricoes, vetor_restricoes, tipo='max')
