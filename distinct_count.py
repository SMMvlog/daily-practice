l = [1, 5, 4, 2, 9, 9, 9]
k = 3

print(len(l))
print(len(l) - k + 1)
max_sum = 0
for i in range(len(l)):
    window = l[i:i+k]
    print(window)
    if len(set(window)) == k:  # all distinct
        max_sum = max(max_sum, sum(window))

print(max_sum)
