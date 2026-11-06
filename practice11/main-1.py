import time

N = 500_000

numbers_list = list(range(N))
numbers_set = set(numbers_list)

target = N - 1

start = time.perf_counter()

target in numbers_list

list_time = time.perf_counter() - start

start = time.perf_counter()

target in numbers_set

set_time = time.perf_counter() - start

print(f"List search time: {list_time:.8f} seconds")
print(f"Set search time: {set_time:.8f} seconds")

print(f"List complexity: O(N)")
print(f"Set complexity: O(1)")