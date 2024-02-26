import random


# classic multiply
def multiply(X, Y):
    result = [[0] * len(Y) for i in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result


# 8 recursive multiply
def add(X, Y):
    n = len(X)
    result = [[0] * len(Y) for i in range(len(X))]

    for i in range(0, n):
        for j in range(0, n):
            result[i][j] = X[i][j] + Y[i][j]

    return result


def subtract(X, Y):
    n = len(X)
    result = [[0] * len(Y) for i in range(len(X))]

    for i in range(0, n):
        for j in range(0, n):
            result[i][j] = X[i][j] - Y[i][j]

    return result


def add_zeros(matrix):
    matrix.append([0] * len(matrix))
    for sublist in matrix:
        sublist.append(0)


def recursiveMultipyImplementation(X, Y):
    if len(X) <= 16:
        return multiply(X, Y)

    middle = len(X) // 2

    A = [[X[i][j] for j in range(0, middle)] for i in range(0, middle)]
    B = [[X[i][j] for j in range(middle, len(X))] for i in range(0, middle)]
    C = [[X[i][j] for j in range(0, middle)] for i in range(middle, len(X))]
    D = [[X[i][j] for j in range(middle, len(X))] for i in range(middle, len(X))]
    E = [[Y[i][j] for j in range(0, middle)] for i in range(0, middle)]
    F = [[Y[i][j] for j in range(middle, len(X))] for i in range(0, middle)]
    G = [[Y[i][j] for j in range(0, middle)] for i in range(middle, len(X))]
    H = [[Y[i][j] for j in range(middle, len(X))] for i in range(middle, len(X))]

    AE_BG = add(recursiveMultipyImplementation(A, E), recursiveMultipyImplementation(B, G))
    AF_BH = add(recursiveMultipyImplementation(A, F), recursiveMultipyImplementation(B, H))
    CE_DG = add(recursiveMultipyImplementation(C, E), recursiveMultipyImplementation(D, G))
    CF_DH = add(recursiveMultipyImplementation(C, F), recursiveMultipyImplementation(D, H))

    result = [[0] * len(Y) for i in range(len(X))]

    for i in range(0, middle):
        for j in range(0, middle):
            result[i][j] = AE_BG[i][j]
            result[i][j + middle] = AF_BH[i][j]
            result[i + middle][j] = CE_DG[i][j]
            result[i + middle][j + middle] = CF_DH[i][j]

    return result


def recursiveMultipy(X, Y):
    n = len(X)
    preparation_matrix(X, Y)
    ans_matrix = recursiveMultipyImplementation(X, Y)
    return [[ans_matrix[i][j] for j in range(n)] for i in range(n)]


# Strassen algorithm
def strassenImplementation(X, Y):
    if len(X) <= 16:
        return multiply(X, Y)

    middle = len(X) // 2

    A = [[X[i][j] for j in range(0, middle)] for i in range(0, middle)]
    B = [[X[i][j] for j in range(middle, len(X))] for i in range(0, middle)]
    C = [[X[i][j] for j in range(0, middle)] for i in range(middle, len(X))]
    D = [[X[i][j] for j in range(middle, len(X))] for i in range(middle, len(X))]
    E = [[Y[i][j] for j in range(0, middle)] for i in range(0, middle)]
    F = [[Y[i][j] for j in range(middle, len(X))] for i in range(0, middle)]
    G = [[Y[i][j] for j in range(0, middle)] for i in range(middle, len(X))]
    H = [[Y[i][j] for j in range(middle, len(X))] for i in range(middle, len(X))]

    P1 = strassenImplementation(A, subtract(F, H))
    P2 = strassenImplementation(add(A, B), H)
    P3 = strassenImplementation(add(C, D), E)
    P4 = strassenImplementation(D, subtract(G, E))
    P5 = strassenImplementation(add(A, D), add(E, H))
    P6 = strassenImplementation(subtract(B, D), add(G, H))
    P7 = strassenImplementation(subtract(A, C), add(E, F))

    Q1 = add(subtract(add(P5, P4), P2), P6)
    Q2 = add(P1, P2)
    Q3 = add(P3, P4)
    Q4 = subtract(subtract(add(P1, P5), P3), P7)

    result = [[0] * len(Y) for i in range(len(X))]

    for i in range(0, middle):
        for j in range(0, middle):
            result[i][j] = Q1[i][j]
            result[i][j + middle] = Q2[i][j]
            result[i + middle][j] = Q3[i][j]
            result[i + middle][j + middle] = Q4[i][j]

    return result


def strassenAlgorithm(X, Y):
    flag = 0
    if len(X) % 2 != 0:
        add_zeros(X)
        flag = 1

    if len(Y) % 2 != 0:
        add_zeros(Y)
        flag = 1

    result = strassenImplementation(X, Y)
    if flag == 1:
        n = len(X) - 1
    else:
        n = len(X)
    return [[result[i][j] for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    N = random.randint(1, 100)

    first_arr = [[random.randint(1, 100) for i in range(N)] for j in range(N)]
    second_arr = [[random.randint(1, 100) for i in range(N)] for j in range(N)]

    print(multiply(first_arr, second_arr))
    print()
    print(recursiveMultipy(first_arr, second_arr))
    print()
    print(strassenAlgorithm(first_arr, second_arr))

    print(strassenAlgorithm(first_arr, second_arr) == recursiveMultipy(first_arr, second_arr) == multiply(first_arr,
                                                                                                            second_arr))
