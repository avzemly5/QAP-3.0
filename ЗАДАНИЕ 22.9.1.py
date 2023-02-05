chisla_list = input("Введите список чисел, разделенных пробелом: ").split()
element = int(input("Введите элемент: "))


# Проверка
for value in chisla_list:
    if value.isdigit():
        True
        test_str = " ".join(chisla_list)
        if " " not in test_str:
            print("\nВы ввели числа без пробелов, повторите ввод\n")
            chisla_list = input("Введите список чисел, разделенных пробелом: ").split()
    else:
        False
        print('\nВ вводе содержатся буквы, повторите ввод\n')
        chisla_list = input("Введите список чисел, разделенных пробелом: ").split()

# Строки в числа
num_list = [int(item) for item in chisla_list]

# Сортируем список
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result
num_list = merge_sort(num_list)

# Установка позиции элемента
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# запускаем алгоритм на левой и правой границе
print(f'Индекс введенного элемента: {binary_search(num_list, element, 0, len(num_list))}')


