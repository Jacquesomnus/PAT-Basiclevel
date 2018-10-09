N, M = input().split()
dict1 = {}
for i in range(int(N)):
    a, b = input().split()
    dict1[a] = dict1.get(a, [])+[b]
    dict1[b] = dict1.get(b, [])+[a]
for i in range(int(M)):
    dict2 = {}
    test = input().split()
    ans = 'Yes'
    for j in range(1, len(test)):
        if test[j] in dict2:
            ans = 'No'
        elif test[j] in dict1:
            for k in dict1[test[j]]:
                dict2[k] = True
    print(ans)