N = int(input())
for i in range(N):
    str = input()
    if len(str) < 6:
        print('Your password is tai duan le.')
    elif str.replace('.', '').isdigit():
        print('Your password needs zi mu.')
    elif str.replace('.', '').isalpha():
        print('Your password needs shu zi.')
    elif str.replace('.', '').isalnum():
        print('Your password is wan mei.')
    else:
        print('Your password is tai luan le.')