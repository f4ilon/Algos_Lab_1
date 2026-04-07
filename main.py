import random
import time
from fileinput import close
from bench import Bench
from functions import *


def x2_gen(i: int, n: int) -> list[int]:
    return [i *(2**x)  for x in range(n)]

def x1d5_gen(i: int, n: int) -> list[int]:
    return [int(i *(1.5**x))  for x in range(n)]

def plusx_gen(i: int, n: int) -> list[int]:
    return [i * x  for x in range(1, n+1)]



# Обёртка с фиксированным ключом
def f04(arr: List[int]) -> int:
    key = arr[len(arr) // 2]  # ищем элемент в середине
    return f04_lower_bound(arr, key)


# Обёртка: Тройка НЕ существует
def f24_three_sum_not_found(arr: List[int]) -> bool:
    # Для отсортированного массива [0,1,2,...,n-1]
    # максимальная сумма трёх = (n-3) + (n-2) + (n-1) = 3n - 6
    # Ищем сумму больше максимальной — гарантированно не найдём
    target = sum(arr[-3:]) + 1 if len(arr) >= 3 else 1000000
    return f24_three_sum_bsearch(arr, target)


# Обёртка:
def subset_sum(arr: List[int]) -> bool:
    target = 190
    return f28_subset_sum(arr, target)


if __name__ == "__main__":    
    # f04_lower_bound
    sorted_data = list(range(1_000_003))
    random_data = [random.randint(1, 1_000_000) for _ in range(1_000_000)]
    print("f04_lower_bound: O(log n)")
    # Создаём отсортированный массив
    
    results_f04 = Bench.this(
        func=f04,
        data=sorted_data,
        repeats=100,
        #scale_sizes=x2_gen(100, 10),
        scale_sizes=plusx_gen(1000, 20),
    )
    print("\n")

    # f08_find_min
    print("f08_find_min: O(n)")
    results_f08 = Bench.this(
        func=f08_find_min,
        data=random_data,
        repeats=100,
        scale_sizes=plusx_gen(1000, 20),
    )
    print("\n")

    # f12_is_sorted
    print("f12_is_sorted: O(n)")
    results_f12 = Bench.this(
        func=f12_is_sorted,
        data=sorted_data,
        repeats=100,
        scale_sizes=plusx_gen(1000, 20),
    )
    print("\n")

    # f16_heap_sort
    print("f16_heap_sort: O(n*log(n))")
    results_f16 = Bench.this(
        func=f16_heap_sort,
        data=random_data,
        repeats=20,
        scale_sizes=plusx_gen(1000, 20),
    )
    print("\n")

    # f20_insertion_sort
    print("f20_insertion_sort: O(n^2)")
    results_f20 = Bench.this(
        func=f20_insertion_sort,
        data=random_data,
        repeats=10,
        scale_sizes=plusx_gen(100, 20),
    )
    print("\n")

    # f24_three_sum_bsearch
    print("f24_three_sum_bsearch: O(n²*log(n))")
    results_f24 = Bench.this(
        func=f24_three_sum_not_found,
        data=sorted_data,
        repeats=3,
        scale_sizes=plusx_gen(100, 20),
    )
    print("\n")



