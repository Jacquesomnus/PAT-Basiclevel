N = int(input())
w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
d = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
case = 0
for i in range(N):
    id = input()
    count = 0
    for j in range(17):
        if id[j].isdigit():
            count += int(id[j])*w[j]
        else:
            count = -1
            break
    if count == -1 or id[17] != d[count % 11]:
        print(id)
    else:
        case += 1
if case == N:
    print("All passed")
