N = int(input())
if N<4:
    print(0)
else:
    check = [0]*(N+1)
    check[4] = 1
    prime = [2]
    count = 0
    for i in range(3, N+1):
        if check[i] == 0:
            if i-prime[-1] == 2:
                count+=1
            prime.append(i)
        for j in prime:
            if i*j>N:
                break
            check[i*j]=1
            if i%j==0:
                break
    print(count)
