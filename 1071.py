T = [int(x) for x in input().split()]
for i in range(T[1]):
    a = [int(x) for x in input().split()]
    if a[2] > T[0]:
        print("Not enough tokens.  Total = " + str(T[0]) + ".")
    elif (a[0] > a[3] and a[1] == 0) or (a[0] < a[3] and a[1] == 1):
        T[0] += a[2]
        print("Win " + str(a[2]) + "!  Total = " + str(T[0]) + ".")
    elif T[0] > a[2]:
        T[0] -= a[2]
        print("Lose " + str(a[2]) + ".  Total = " + str(T[0]) + ".")
    elif T[0] == a[2]:
        print("Lose " + str(a[2]) + ".  Total = 0.")
        print("Game Over.")
        break
