# Открываем файл для чтения
with open('ФИО_группа_vvod.txt', 'r') as f:
    # Считываем матрицу из файла
    matrix = []
    for line in f:
        row = [int(x) for x in line.split()]
        matrix.append(row)

# Выполняем необходимые операции с матрицей
...

# Открываем файл для записи результатов
with open('ФИО_группа_vivod.txt', 'w') as f:
    # Записываем результаты в файл
    for row in matrix:
        f.write(' '.join([str(x) for x in row]) + '\n')
