T = (10, 40, 30, 50, 70)
print("Tuple in reverse order:", T[::-1])
sum_T = sum(T)
print("Sum of values in T:", sum_T)
min_T = min(T)
max_T = max(T)
print("Minimum value in T:", min_T)
print("Maximum value in T:", max_T)

adjacent_sums = [T[i] + T[i + 1] for i in range(len(T) - 1)]
print("Sum of each adjacent pair of values:", adjacent_sums)

pairs_matching_sum = []
for i in range(len(T)):
    for j in range(i + 1, len(T)):
        pair_sum = T[i] + T[j]
        if pair_sum in T:
            pairs_matching_sum.append(((T[i], T[j]), pair_sum))

print("Pairs whose sum is equal to one of the values in T:")
for pair, pair_sum in pairs_matching_sum:
    print(f"Pair {pair} has a sum of {pair_sum} which is in T")
