a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mul = 0
sum = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        sum += a[i] + i
    else:
        mul += a[i] * i

if mul > sum:
    print(mul - sum)
else:
    print(sum - mul)