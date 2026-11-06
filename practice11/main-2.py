import time

def intersection_slow(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)

    return result

def intersection_fast(list1, list2):
    set2 = set(list2)
    result = []

    for item in list1:
        if item in set2 and item not in result:
            result.append(item)

    return result


list1 = list(range(5000))
list2 = list(range(2500, 7500))

start = time.perf_counter()

result1 = intersection_slow(list1, list2)

slow_time = time.perf_counter() - start

start = time.perf_counter()

result2 = intersection_fast(list1, list2)

fast_time = time.perf_counter() - start

print("Slow algorithm:", slow_time)
print("Fast algorithm:", fast_time)

print("Results are equal:", result1 == result2)

print("Slow complexity: O(N * M)")
print("Fast complexity: O(N + M)")