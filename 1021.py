N = input()
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in N:
    l[int(i)] += 1
count = 0
for i in l:
    if i:
        print(str(count)+":"+str(i))
    count += 1
