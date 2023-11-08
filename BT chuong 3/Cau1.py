#3.1
# import math
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# p=(a+b+c)/2
# S=math.sqrt(p*(p-a)*(p-b)*(p-c))
# if (a+b)>c and (a+c)>b and (b+c)>a:
#     print('Dien tich='+str(round(S,3)))
# else:
#     print('Khong hop le')

#3.2
# M1=int(input('M1='))
# M2=int(input('M2='))
# M3=int(input('M3='))
# S=int(input('S='))
# if S<=100:
#     print('Phai tra='+str(int(M1*S)))
# elif S>=101 and S<=150:
#     print('Phai tra='+str(int(M1*100+(S-100)*M2)))
# else:
#     print('Phai tra='+str(int(100*M1+50*M2+(S-150)*M3)))

#3.3
x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+':
    print(str(float(x))+'+'+str(float(y))+'='+str(round(x+y,1)))
elif ch=='-':
    print(str(float(x))+'-'+str(float(y))+'='+str(round(x-y,1)))
elif ch=='*':
    print(str(float(x))+'*'+str(float(y))+'='+str(round(x*y,1)))
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        print(str(float(x))+'/'+str(float(y))+'='+str(round(x/y,1)))
else:
    print('Khong hop le')

#3.4
# toan=float(input(''))
# ly=float(input(''))
# hoa=float(input(''))
# DTB=(toan*2+ly*3+hoa)/6
# if toan>=0 and ly>=0 and hoa>=0:
#     if DTB<3:
#         print('Kem')
#     elif 3<=DTB<5:
#         print('Yeu')
#     elif 5<=DTB<6:
#         print('Trung binh')
#     elif 6<=DTB<7:
#         print('Trung binh Kha')
#     elif 7<=DTB<8:
#         print('Kha')
#     elif 8<=DTB<9:
#         print('Gioi')
#     elif 9<=DTB<=10:
#         print('Xuat sac')

# 3.5
# nghi=int(input(''))
# if nghi==0:
#     print('Xep loai A')
# elif nghi<2:
#     print('Xep loai B')
# elif nghi>=2 and nghi<4:
#     print('Xep loai C')
# else:
#     print('Xep loai D')

#3.6
a=float(input(''))
b=float(input(''))
c=float(input(''))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('Tam giac vuong')
    elif a==b and b==c and a==c:
        print('Tam giac deu')
    else:
        print('Tam giac loai khac')
else:
    print('Khong hop le')