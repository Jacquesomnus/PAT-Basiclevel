c1, c2 = input().split()
sec = int((int(c2) - int(c1)) / 100 + 0.5)
print('%02d:%02d:%02d' % (sec // 3600, sec % 3600 // 60, sec % 60))