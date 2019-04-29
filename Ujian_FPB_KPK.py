num1 = int(input('Ketik angka pertama : '))
num2 = int(input('Ketik angka kedua : '))

def FPB(num1, num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            fpb = i
    return fpb

def KPK(num1, num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            fpb = i
    kpk = int((num1 * num2) / fpb)
    return kpk

print('FPB dari angka', num1, 'dan', num2, 'adalah', FPB(num1, num2))
print('KPK dari angka', num1, 'dan', num2, 'adalah', KPK(num1, num2))