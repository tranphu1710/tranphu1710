x=int(input("Nhập số cần tính giai thừa: "))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
