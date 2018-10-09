N = int(input())
dict = {'A': '1', 'B': '2', 'C': '3', 'D': '4'}
ans = ''
for i in range(N):
    str = input().split()
    for j in range(4):
        if str[j][2] == 'T':
            ans += dict[str[j][0]]
print(ans)
