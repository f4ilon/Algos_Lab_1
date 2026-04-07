import copy
import statistics
import time
from statistics import median
from typing import Callable, Iterable, Optional
import xlsx



class Bench:
    @staticmethod
    def this(
            func: Callable[[Iterable], None],
            data: Iterable,
            *,
            repeats: int = 3,
            scale_sizes: list[int],
            verbose: bool = False,
    ) -> None:
        
        results: list[tuple[int, float]] = []

        for size in scale_sizes:
            src = list(data)
            
            base = src[:size]

            times: list[float] = []
            for _ in range(repeats):
                arr = copy.deepcopy(base)
                t0 = time.perf_counter()
                func(arr)
                t1 = time.perf_counter()
                times.append((t1 - t0)*1000)

            median_time = statistics.median(times)
            mean_time = statistics.mean(times)
            results.append((size, median_time))

        if verbose:
            print(f"{'size':>10} | {'time (ms)':>12}")
            print("-"*25)
            for size, t in results:
                print(f"{size:10d} | {t:12.10f}")
                
        xlsx.save_results(results, func.__name__[:3])
