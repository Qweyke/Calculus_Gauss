def minput(row, n):
    matr = []
    n += 1
    for inp in range(1, row + 1):
        elem_inp = input(f"Введите {n - 1} коэфф. {inp}-го уравнения через пробелы, последнее, {n} значение -"
                         f" свободный член: \n")
        row = [float(elem) for elem in elem_inp.split()[:n]]
        print(row)
        matr.append(row)
    return matr


def straight(mtrx):
    endp = 0  # служебный ограничитель хода

    for j in range(nm-1):  # цикл по столбцам с последнего
        for i in range(rowm-1, endp, -1):  # с конечной строки, с каждым новым столбцом начальная ниже

            zer = mtrx[i][j]  # элемент для зануления
            strg = mtrx[j][j]  # элемент главной диаг

            modz = 1
            mods = 1
            if zer > 0 and strg > 0:  # получение разных знаков
                modz *= -1
            if zer < 0 and strg < 0:
                mods *= -1

            if zer != 0:  # замена элементов строк после операций
                for k in range(j, nm + 1, 1):
                    mtrx[i][k] = (mtrx[j][k] * abs(zer) * modz) + (mtrx[i][k] * abs(strg) * mods)  # домножаем верхнюю и
                    # нижнюю на соотв эл друг друга
        endp += 1

    return mtrx


def reverse(mtrx):
    pres = 1

    for i in range(rowm - 1, -1, -1):
        left = 0
        jshka = rowm - 1  # индекс для pres эла

        for j in range(nm - 1, -1, -1):  # ход от lst coef
            if i != rowm - 1:  # исключение для lst str
                pres = A[jshka][nm]

            if j != i:  # исключаем суммирование текущего неизвестного
                left += (A[i][j] * pres)
            jshka -= 1

        res = ((-1) * A[i][nm]) + left  # переброс свб члн влево
        A[i][nm] = res / ((-1) * A[i][i])  # рез знч неизв вместо свб члена
        pres = A[rowm - 1][nm]  # обновление первого неизв

    return mtrx


rowm = int(input("Кол-во линейных уравнений:\n"))
nm = int(input("Кол-во неизвестных членов:\n"))
A = minput(rowm, nm)
A = straight(A)
print(A)
A = reverse(A)

code = ord('z')  # получение юникода
for o in range(rowm - 1, -1, -1):  # вывод неизвестных
    symb = chr(code)
    print(f" {symb} = {A[o][nm]}")
    code -= 1
