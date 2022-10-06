a= int(input('nhap a: '))

kt=1   #mac dinh la so nguyen to

if ( a==0)|(a==1):
    kt=0
elif (a==2):
    kt=1
else :
    for i in range(2,a) :
        if (a%i==0):
            kt=0   #khong la so nguyen to
if (kt==1):
    print("a la so nguyen to")
else:
    print("a khong la so nguyen to ")
