#*******Cau lenh While********

# 3.1
# n=int(input('n='))
# while n<1 or n>50:
#     print('Vui long nhap lai so khac')
#     n=int(input('n='))

#3.2
# n=int(input('n='))
# i=1
# if 1<=n<=50:
#     while i<=n:
#         print(i, end=' ')
#         i=i+1
#         if i%10==1:
#             print('\n')

# 3.3
# i=1
# j=1
# while j<=9:
#     while i<=9:
#         print(i*j, end='/t')
#         i=i+1
#     print('\n')
#     j=j+1
#     i=1

# 3.4

# hinh b
# i=1
# j=int(input(''))
# while i<=j:
#     print((j-i)*' '+(2*i-1)*'*')
#     i=i+1
    

# hinh a
# i=9
# while 1<=i<=9:
#     j=1
#     while j<=i:
#         print('$', end='')
#         j=j+1
#     print('')
#     i=i-1

# ******Cau lenh for*******

# Vidu 3.2-14

# total=0
# for num in range(101):
#     total=total+num
# print(total)

# vidu 3.2-15

# for i in range(12,16):
#     print(i)

# vidu 3.2-16

# for i in range(0,10,2):
#     print(i)

# Vidu 3.2-19va20

# *for

# n=int(input('n='))
# S=0
# t=1
# if n<=3:
#     print('Khong du so de nhan')
#     for i in range(1,n+1):
#         if i%2==1:
#             S=S+i
# else:
#     for i in range(1,n+1):
#         if i%2==1:
#             S=S+i
#         else:
#             t=t*i
# print('Tong so le:',S)
# print('tich so chan',t)


# n=int(input('n='))
# s=0
# i=1
# while i<=n:
#     s=s+i
#     i=i+1
# print(s)

# Vidu 3.2-21

# for i in range(1,7):
#     for j in range(1,i+1):
#         print('*',end='')
#     print('')

# ***For***

# Cau 3.2:
# n=int(input('n='))
# for i in range(1,n+1):
#     print(i,end='\t')
#     if i%10==0:
#         print('\n')

# Cau 3.3:
# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j,end='\t')
#     print('\n')

# Cau 3.4:

# Hinh a
# n=int(input('n='))
# for i in range(n,0,-1):
#     print('$'*i)

# Hinh b

# for j in range(0,n+1):
#     print((n-j)*' '+(2*j-1)*'*')

# Bai 1:
# n=int(input('n='))
# gt=1
# for i in range(n,0,-1):
#     gt=gt*i
# print('n!=',gt,sep='')

# Bai 2:
# n=int(input('n='))
# if n==1:
#     print(n,'khong la SNT')
# elif n==2:
#     print(n,'la SNT')
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,'khong la SNT')
#             break
#         else:
#             print(n,'la SNT')

# Bai 3:
# n=int(input('n='))
# dem=1
# while n>=10:
#     n=n/10
#     dem=dem+1
# print(round(n*10**(dem-1)),'co',dem,'chu so')

# Bai 4:
# while 1==1:
#     a=float(input('a='))
#     b=float(input('b='))
#     ch=input('Toan tu:')
#     if ch=='+':print(str(a),ch,str(b),'=',a+b,sep='')
#     elif ch=='-':print(str(a),ch,str(b),'=',a-b,sep='')
#     elif ch=='*':print(str(a),ch,str(b),'=',a*b,sep='')
#     elif ch=='/':
#         if b==0:
#             print('Khong hop le')
#             continue
#         else:print(str(a),ch,str(b),'=',a/b,sep='')
#     tt=input('Tiep tuc:')
#     if tt=='T' or tt=='t':break

# Vidu 2
# i=n=x=s=0
# n=int(input('n='))
# for i in range(1, n+1):
#     print('So thu ',i,':',sep='')
#     x=int(input('x='))
#     if x<0:continue
#     elif x==0:break
#     elif x%2==1 and x>0:
#         s=s+x
# print(s)


# *****Tính tổ hợp*****

# n, k = (int(x) for x in input().split())
# # tính n!
# N=1
# for i in range(1,n+1):
#     N=N*i
# # tính k!
# K=1
# for i in range(1,k+1):
#     K=K*i
# # tinh(n-k)!
# T=1
# for i in range(1,(n-k)+1):
#     T=T*i
# # tính tổ hợp
# if n>k:
#     print(N/(K*T))
# else:
#     print('INF')

# 3.7a
# gt=1
# i=1
# n=int(input('n='))
# if n==0:
#     print('0!=1')
# else:
#     while i<=n:
#         gt=gt*i
#         i=i+1
#     print(str(n)+str('!=')+str(int(gt)))