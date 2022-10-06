n=int(input("Nhập n="))

flag=True # Giả sử n là số nguyên tố
x=2 # khởi tạo biến lặp

while x <= int(n/2):

    if n%x==0: # lúc này x là ước

        flag=False

        break

    x +=1 # Tăng biến lặp

if flag==True:

    print(n, "là số nguyên tố!")

else:

    print(n, "không là số nguyên tố")
