prices = [100, 105, 103, 110, 108, 115, 112]
k = 3

max_sum = sum(prices[:k])
current_sum = max_sum
start = 0

for i in range(k, len(prices)):
    current_sum = current_sum - prices[i - k] + prices[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = i - k + 1

window = prices[start:start + k]

print("Найкращі ціни за", k, "дні:", window)
print("Сума цін:", max_sum)
print("Середня ціна:", max_sum / k)