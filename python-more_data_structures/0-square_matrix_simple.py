#!/usr/bin/python3
#!/usr/bin/python3 
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_array = []
        for x in i:
            new_array.append(x ** 2)
        new_matrix.append(new_array)
    return new_matrix
