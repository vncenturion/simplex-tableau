#EXEMPLO 01 MIN
#O codigo não trata os problemas de minimização de forma automática.

func_objetivo = [3, 2, 0, 0]  # x1, x2, s1, s2
matriz_restricoes = np.array([
    [1, 2, 1, 0],
    [2, 1, 0, 1]
], dtype=float)
vetor_restricoes = np.array([4, 5], dtype=float)

# Rodar o simplex com tipo 'min'
resultado=simplex(func_objetivo, matriz_restricoes, vetor_restricoes, tipo='max')
