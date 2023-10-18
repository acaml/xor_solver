def solve_f2(M, Y):
    n = len(M)
    m = len(M[0])
    MY = [M[i] + [Y[i]] for i in range(n)]
    for j in range(m):
        pivot_row = None
        for i in range(j, n):
            if MY[i][j] == 1:
                pivot_row = i
                break
        if pivot_row is None:
            continue
        MY[j], MY[pivot_row] = MY[pivot_row], MY[j]
        for i in range(j+1, n):
            if MY[i][j] == 1:
                MY[i] = [a ^ b for a, b in zip(MY[i], MY[j])]
    
    X = [0] * m
    for j in range(m-1, -1, -1):
        if MY[j][j] == 1:
            X[j] = MY[j][-1]
            for i in range(j):
                if MY[i][j] == 1:
                    MY[i][-1] = MY[i][-1] ^ X[j]
    return X

def array_to_binary_matrix(input_array):
    max_length = max(len(bin(element)[2:]) for element in input_array)
    binary_matrix = [int_to_binary_array(element, max_length) for element in input_array]
    binary_matrix_transposed = list(map(list, zip(*binary_matrix)))
    return binary_matrix_transposed

def binary_matrix_to_array(binary_matrix):
    transposed_matrix = list(map(list, zip(*binary_matrix)))
    result_array = [int(''.join(map(str, row)), 2) for row in transposed_matrix]
    return result_array

def solver(matrix, Y):
    B = array_to_binary_matrix(Y)
    R = [solve_f2(matrix, y) for y in B]
    N = binary_matrix_to_array(R)
    return N

def int_to_binary_array(n, m):
    binary_representation = bin(n)[2:]
    binary_array = [int(bit) for bit in binary_representation]
    while len(binary_array) < m:
        binary_array.insert(0, 0)
    return binary_array

M = [[0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0],
        [1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0], 
        [1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,1], 
        [0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1], 
        [1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0], 
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1], 
        [1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1],
        [0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1], 
        [1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0], 
        [1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0], 
        [0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1], 
        [1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0], 
        [0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1], 
        [0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,1], 
        [1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0], 
        [1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0],
        [0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,0,0], 
        [0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1],
        [0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,0],
        [1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1],
        [1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0], 
        [0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1], 
        [1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0],
        [1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1], 
        [1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,1], 
        [1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1], 
        [0,1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,1], 
        [0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1]]

constraints = [28, 120, 40, 52, 72, 99, 118, 31, 54, 18, 23, 100, 103, 14, 34, 111, 7, 57, 106, 40, 34, 89, 100, 84, 102, 116, 100, 82]

sol = solver(M,constraints)
print(sol)
