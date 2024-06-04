
def straight(mtrx):
    equat_strings = (len(mtrx))  # число уравнений(строк)
    column_x = (len(mtrx[0]) - 1)  # число неизвестных (столбцы - 1, так как последний столбец это своб. члены)

    current_last_string = 0  # конечная строка на текущий момент
    for j in range(column_x - 1):  # цикл по каждому столбцу
        for i in range(equat_strings-1, current_last_string, -1):  # с последней, с каждым новым столбцом нулевая ниже

            zeroed = mtrx[i][j]  # элемент, который будет занулен для приведения к треугольному виду
            main_diag_el = mtrx[j][j]  # элемент главной диагонали

            modz = 1
            mods = 1
            if zeroed > 0 and main_diag_el > 0:  # получение разных знаков
                modz *= -1
            if zeroed < 0 and main_diag_el < 0:
                mods *= -1

            if zeroed != 0:  # если zeroed уже не равен нулю, выполняем преобразования
                for k in range(j, column_x + 1, 1):
                    # домножаем верхнюю и нижнюю на соотв эл друг друга
                    mtrx[i][k] = (mtrx[j][k] * abs(zeroed) * modz) + (mtrx[i][k] * abs(main_diag_el) * mods)
        current_last_string += 1
    return mtrx


def reverse(mtrx):
    equat_strings = (len(mtrx))
    column_x = len(mtrx[0]) - 1

    prev_coef = 1
    for i in range(equat_strings - 1, -1, -1):  # с последней строки вверх
        left_side_sum = 0
        j_index = equat_strings - 1  # индекс для prev_coef эла

        for j in range(column_x - 1, -1, -1):  # ход от последнего коэфа к первому
            if i != equat_strings - 1:  # исключение для последней строки
                prev_coef = mtrx[j_index][column_x]

            if j != i:  # исключаем суммирование текущего неизвестного
                left_side_sum += (mtrx[i][j] * prev_coef)
            j_index -= 1

        res = ((-1) * mtrx[i][column_x]) + left_side_sum  # переброс свб члн влево
        mtrx[i][column_x] = res / ((-1) * mtrx[i][i])  # рез знч неизв вместо свб члена
        prev_coef = mtrx[equat_strings - 1][column_x]  # обновление первого неизв

    return mtrx


A = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]
A = straight(A)
A = reverse(A)
print(A)

code = ord('z')  # получение юникода
for o in range(len(A) - 1, -1, -1):  # вывод неизвестных
    symb = chr(code)
    print(f" {symb} = {A[o][len(A[0]) - 1]}")
    code -= 1
