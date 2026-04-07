from typing import List


#  4. Lower bound — индекс первого элемента ≥ key
#
#  Аналог std::lower_bound из C++.
#  Тот же принцип деления пополам — O(log n).
def f04_lower_bound(a: List[int], key: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        m = lo + (hi - lo) // 2
        if a[m] < key:
            lo = m + 1
        else:
            hi = m
    return lo


#  8. Нахождение минимального элемента — O(n).
def f08_find_min(a: List[int]) -> int:
    mn = a[0]
    for i in range(1, len(a)):
        if a[i] < mn:
            mn = a[i]
    return mn


# 12. Проверка, отсортирован ли массив по неубыванию
#
#  Один проход с проверкой a[i] >= a[i-1].  O(n).
def f12_is_sorted(a: List[int]) -> bool:
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


# --- вспомогательная функция для heap sort ---
def _hs_sift(a: List[int], n: int, i: int) -> None:
    while True:
        big = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[big]:
            big = l
        if r < n and a[r] > a[big]:
            big = r
        if big == i:
            break
        a[i], a[big] = a[big], a[i]
        i = big


# 16. Пирамидальная сортировка (heap sort)
#
#  Строим max-heap за O(n), затем n раз извлекаем максимум
#  (каждый раз O(log n)).  Итого O(n log n) ГАРАНТИРОВАННО.
def f16_heap_sort(a: List[int]) -> None:
    n = len(a)
    # построение кучи
    for i in range(n // 2 - 1, -1, -1):
        _hs_sift(a, n, i)
    # извлечение максимумов
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _hs_sift(a, i, 0)


# 20. Сортировка вставками (insertion sort)
#
#  Каждый новый элемент «вставляется» в уже отсортированную
#  часть массива, сдвигая бОльшие элементы вправо.  O(n^2).
def f20_insertion_sort(a: List[int]) -> None:
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# 24. Поиск тройки с суммой target (с бинарным поиском)
#
#  Фиксируем пару (i, j), ищем третий элемент
#  need = target − a[i] − a[j] бинарным поиском
#  среди a[j+1 .. n−1].
#  Пар C(n,2), каждый поиск O(log n) ⇒ O(n² log n).
#  ВАЖНО: массив должен быть отсортирован!
def f24_three_sum_bsearch(a: List[int], target: int) -> bool:
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            need = target - a[i] - a[j]
            lo, hi = j + 1, n - 1
            while lo <= hi:
                m = lo + (hi - lo) // 2
                if a[m] == need:
                    return True
                elif a[m] < need:
                    lo = m + 1
                else:
                    hi = m - 1
    return False

