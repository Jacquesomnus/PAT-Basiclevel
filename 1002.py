str1 = list(input())
str2 = str(sum(int(i) for i in str1))
dict = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
list = []
for j in str2:
    list.append(dict[j])
print(' '.join(list))