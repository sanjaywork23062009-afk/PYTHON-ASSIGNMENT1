import time
from decimal import Decimal

def benchmark_totals():
    payments_float = [33.40] * 150000
    payments_decimal = ["33.40"] * 150000

    start_time = time.perf_counter()
    total_f = sum(payments_float)
    end_time = time.perf_counter()
    float_time = end_time - start_time

    start_time = time.perf_counter()
    total_d = sum(Decimal(p) for p in payments_decimal)
    end_time = time.perf_counter()
    decimal_time = end_time - start_time

    print(f"Float Total: {total_f}, Time: {float_time:.6f} seconds")
    print(f"Decimal Total: {total_d}, Time: {decimal_time:.6f} seconds")

if __name__ == "__main__":
    benchmark_totals()
```[cite: 13, 14]
