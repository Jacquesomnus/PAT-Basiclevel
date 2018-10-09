n = int(input())
count = 0
while n != 1:
    n = (3 * n + 1) / 2 if n % 2 == 1 else n / 2
    count += 1
print(count)