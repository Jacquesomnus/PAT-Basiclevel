N, c = input().split()
num = int(((int(N)+1)/2)**0.5)
for i in range(num):
    print(' '*i + c*((num-i)*2-1))
for i in range(num-1):
    print(' '*(num-2-i)+c*(i*2+3))
print(int(N)-2*num**2+1)