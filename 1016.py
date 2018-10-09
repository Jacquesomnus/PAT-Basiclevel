a, b, c, d = input().split(' ')
num1 = 0 if a.count(b) == 0 else int(''.join(b for i in range(a.count(b))))
num2 = 0 if c.count(d) == 0 else int(''.join(d for i in range(c.count(d))))
print(num1 + num2)