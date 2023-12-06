
def read_matrix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.strip().split())) for line in lines]
    return matrix


def write_matrix(file_name, matrix):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + 'n')


input_file_name = 'C:/Пользователи/yakov/OneDrives/Яковишин Антон Максимович ПР10_УБ_31_vvod.txt'
output_file_name = 'C:/Пользователи/yakov/OneDrives/Яковишин Антон Максимович ПР10_УБ_31_vivod.txt'


matrix = read_matrix(input_file_name)


result_matrix = [[sum(row)] for row in matrix]


write_matrix(output_file_name, result_matrix)
