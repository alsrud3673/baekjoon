num1, num2 = input('숫자 두 개 입력 : ').split()


a = int(''.join(reversed(num1)))
b = int(''.join(reversed(num2)))

if a > b:
    print(a)
else:
    print(b)