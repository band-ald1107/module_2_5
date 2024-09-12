def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result = get_matrix(3, 4, 5)
for row in result:
    print(row)