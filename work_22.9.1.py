try:
    subsequence = list(int(i) for i in input("Введите последотельность целых чисел через пробел: ").split())
    number = int(input("Введите целое число для сравнения: "))
except ValueError:
    print("Введены некоректные символы или дробное число!")
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array
sort_subsequence = qsort(subsequence, 0, len(subsequence)-1)
max_index = len(sort_subsequence) - 1
if max(sort_subsequence) < number or number < min(sort_subsequence):
    print("Введенное число не входит в указанную последовательность!")
    exit()
position_number = 0
for i in sort_subsequence:
    if i < number:
        position_number = int(i)
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
x = binary_search(sort_subsequence, position_number, sort_subsequence[0], sort_subsequence[max_index])
print(f'Индекс меньшего значения {x}, индекс большего или равного значения {x+1}')