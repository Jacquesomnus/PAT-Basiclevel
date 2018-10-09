n = int(input())
min, max = 101, -1
minname, minid, maxname, maxid = '', '', '', ''
for i in range(n):
    name, id, score = input().split()
    if int(score) < min:
        min = int(score)
        minname = name
        minid = id
    if int(score) > max:
        max = int(score)
        maxname = name
        maxid = id
print(maxname, maxid)
print(minname, minid)