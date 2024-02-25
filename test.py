
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


rowm = int(input("Кол-во линейных уравнений:\n"))
nm = int(input("Кол-во неизвестных членов:\n"))
A = minput(rowm, nm)
nm += 1

endp = 0
for j in range(nm-2):  # цикл по столбцам с последнего
    for i in range(rowm-1, endp, -1):  # с конечной строки, с каждым новым столбцом начальная ниже

        zer = A[i][j]  # элемент для зануления
        strg = A[j][j]  # элемент главной диаг

        modz = 1
        mods = 1
        if zer > 0 and strg > 0:  # получение разных знаков
            modz *= -1
        if zer < 0 and strg < 0:
            mods *= -1

        if zer != 0:  # замена элементов строк после операций
            for k in range(j, nm, 1):
                A[i][k] = (A[j][k] * abs(zer) * modz) + (A[i][k] * abs(strg) * mods)
    endp += 1

print(A)

pres = 1
for i in range(rowm - 1, -1, -1):
    left = 0
    jshka = rowm - 1

    for j in range(nm - 2, -1, -1):
        if i != rowm - 1:
            pres = A[jshka][nm - 1]

        if j != i:
            left += (A[i][j] * pres)
        jshka -= 1

    res = ((-1) * A[i][nm - 1]) + left
    A[i][nm - 1] = res / ((-1) * A[i][i])
    pres = A[rowm - 1][nm - 1]

code = ord('z')

for i in range(rowm - 1, -1, -1):
    symb = chr(code)
    print(f" {symb} = {A[i][nm - 1]}")
    code -= 1
