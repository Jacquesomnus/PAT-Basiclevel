T = int(input())
for i in range(1, T+1):
    num = input().split()
    if int(num[0])+int(num[1])>int(num[2]):
        print("Case #"+str(i)+": true")
    else:
        print("Case #"+str(i)+": false")