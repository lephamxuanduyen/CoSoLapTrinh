# 3.7a
# while 1==1:
#     gt=1
#     m=n=int(input('n='))
#     if n>0:
#         while n>0:
#             gt=gt*n
#             n=n-1
#         print('n!='+str(int(gt)))
#     elif n==0:
#         print('n!=1')
#     else:
#         break

# 3.7b
# while True:
#     gt=1
#     m=n=int(input('n='))
#     if n>0:
#         for j in range(1,n+1):
#             gt=gt*j
#         print('n!='+str(int(gt)))
#     elif n==0:
#         print('n!=1')
#     else:
#         break

# =================================================================================================================================================
# 3.8
# dau=input()
# n=int(input())
# for i in range(1,n+1):
#     print('* '*i,end=('\n'))

# =================================================================================================================================================
# 3.9
# a)
# n=int(input())
# i=1
# while i<=10:
#     if i%2==0:
#         print(i,end=' ')
#     i=i+1

# b)
# n=int(input())
# for i in range(2,n+1):
#     if i%2==0:
#         print(i,end=' ')

# =================================================================================================================================================
# 3.10
# a)
# n=int(input('n='))
# for i in range(1,n+1):
#     print(i,end='\n')

# b)
# n=int(input('n='))
# for i in range(1,n+1):
#     print(i,end=' ')
#     if i%5==0:
#         print(sep='')

# c)
# n=int(input('n='))
# for j in range(1,n+1):
#     for i in range(1,n+1):
#         print(i,end=' ')
#     print(sep='')

# =================================================================================================================================================
# 3.11
# duong=0
# am=0
# while 1==1:
#     n=int(input())
#     if n>0:
#         duong+=1
#     elif n<0:
#         am+=1
#     else:break
# print(duong,'so duong')
# print(am,'so am')

# =================================================================================================================================================
# 3.12
# n=int(input())
# p=len(str(n))
# while n>=0 and p>0:
#     p=p-1
#     m=n//(10**p)
#     if m==0:
#         print('A')
#     elif m==1:
#         print('B')
#     elif m==2:
#         print('C')
#     elif m==3:
#         print('D')
#     elif m==4:
#         print('E')
#     elif m==5:
#         print('F')
#     elif m==6:
#         print('G')
#     elif m==7:
#         print('H')
#     elif m==8:
#         print('K')
#     elif m==9:
#         print('L')
#     n=n-m*(10**p)

# =================================================================================================================================================
# n=int(input())
# p=len(str(n))
# while n>=0 and p>0:
#     p=p-1
#     m=n//(10**p)
#     if m==0:
#         print('A',end='')
#     elif m==1:
#         print('B',end='')
#     elif m==2:
#         print('C',end='')
#     elif m==3:
#         print('D',end='')
#     elif m==4:
#         print('E',end='')
#     elif m==5:
#         print('F',end='')
#     elif m==6:
#         print('G',end='')
#     elif m==7:
#         print('H',end='')
#     elif m==8:
#         print('K',end='')
#     elif m==9:
#         print('L',end='')
#     n=n-m*(10**p)

# n=int(input())
# for i in range(1,n+1):
#     if i%2==0 and i<=10:
#         print(i,end=' ')

# =================================================================================================================================================
                                                #   BÀI TẬP CÁ NHÂN CHƯƠNG 4
# =================================================================================================================================================
# Bài 2

# def nhap():
#     n=int(input('Nhap mot so nguyen duong n='))
#     return n

# def inkq(n):
#     print('Cac so nguyen chan trong',n,'so tu nhien dau tien la:')
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i,end=' ')
#     print(sep='')
# while True:
#     n=nhap()
#     inkq(n)
#     tt=input('Ban co muon tiep tuc hay khong ?')
#     if tt=='T':
#         break
# =================================================================================================================================================
                                                #   BÀI TẬP CÁ NHÂN CHƯƠNG 5
# =================================================================================================================================================
#  Bài 1:

# def FisrtAndLast(L):
#     DS=[]
#     DS=DS+[L[0]]
#     DS=DS+[L[n-1]]
#     print(DS)
#     return
# def Search(L,x):
#     if x in L:
#         print('True')
#     else:
#         print('False')
#     return

# n=int(input('n='))
# L=[] 
# for i in range(1,n+1):
#     so=int(input())
#     L=L+[so]
# x=int(input('x='))
# FisrtAndLast(L)
# Search(L,x)
# ================================================================================================================================================
# Bài 2:

# def Input():
#     n=int(input('n='))
#     L=[]
#     for i in range(1,n+1):
#         L=L+[int(input())]
#     return n,L
# def Search(n,L):
#     min=L[0]
#     max=L[0]
#     for j in range(1,n):
#         if min>L[j]:
#             min=L[j]
#         if max<L[j]:
#             max=L[j]
#     return min,max
# def Output(min,max):
#     print(max,min)
# n,L=Input()
# min,max=Search(n,L)
# Output(min,max)
# ================================================================================================================================================
# Bài 3:

# n=int(input('n='))
# L=[]
# SND=[]
# SC=[]
# s=0
# for i in range(1,n+1):
#     L=L+[int(input())]
# for j in L:
#     if j>=0:
#         SND=SND+[j]
#     if j%2==0:
#         SC=SC+[j]
#         s=s+j
# SND=len(SND)
# TBC=s/len(SC)
# print('SND='+str(SND))
# print('TBC='+str(TBC))
# ================================================================================================================================================
# Bài 4:
# n=int(input('n='))
# A=[]
# B=[]
# for i in range(1,n+1):
#     A=A+[int(input())]
# for i in range(n-1,-1,-1):
#     B=B+[A[i]]
# for x in B:
#     print(x,end=' ')
# print(sep='')
# for i in range(0,len(A)-1):
#     for j in range(i + 1,len(A)):
#         if (A[i] > A[j]):
#             tmp = A[i]
#             A[i] = A[j]
#             A[j] = tmp
# for y in A:
#     print(y,end=' ')
# =================================================================================================================================================
# Bài 5:
# n=int(input('n='))
# L=[]
# for i in range(1,n+1):
#     L=L+[int(input())]
# s=0
# for x in range(0,n):
#     if x%2==1:
#         s=s+L[x]
# print('Tong='+str(s))
# =================================================================================================================================================
# Bài 6:

# A=[]
# B=[]
# for i in range(1,11):
#     A=A+[int(input())]
# for j in range(0,9,2):
#     B=B+[A[j+1]]
#     B=B+[A[j]]
# for x in B:
#     print(x,end=' ')
# =================================================================================================================================================
# Bài 7:

# n=int(input('n='))
# L=[]
# for i in range(1,n+1):
#     L=L+[int(input())]
# M=set(L)
# for x in M:
#     print(x,end=' ')
# ================================================================================================================================================
# Bài 8:

# m=int(input('m='))
# n=int(input('n='))
# print('A:')
# A=[]
# for i in range(1,m*n+1):
#     A=A+[int(input())]
# print('B:')
# B=[]
# for j in range(1,m*n+1):
#     B=B+[int(input())]
# C=[]
# for x in range(0,m*n):
#     C=C+[A[x]+B[x]]
# print('C:')
# for y in range(0,m*n):
#     print(C[y],end=' ')
#     if y%n==m:
#         print(sep='')
# ================================================================================================================================================
# Bài 9:

# n=int(input('n='))
# m=int(input('m='))
# print('L1:')
# L1=[]
# for i in range(1,n+1):
#     L1=L1+[int(input())]
# print('L2:')
# L2=[]
# for j in range(1,m+1):
#     L2=L2+[int(input())]
# L3=[]
# for x in L1:
#     if x in L2:
#         L3.append(x)
# for a in L3:
#     while L3.count(a)>1:
#         L3.remove(a)
# if len(L3)!=0:
#     print('L3:',end=' ')
#     for y in L3:
#         print(y,end=' ')
# elif len(L3)==0:
#     print('L3:')
# ================================================================================================================================================
# Bai 3 Chương 4:

# import math

# def nhap():
#     print('Moi nhap 3 so nguyen:')
#     a=int(input('-a = '))
#     b=int(input('-b = '))
#     c=int(input('-c = '))
#     return a,b,c
# def giaipt(a,b,c):
#     if a==0:
#         if b==0:
#             if c==0:
#                 x1=x2='Phuong trinh vo so nghiem'
#             else:
#                 x1=x2='Phuong trinh vo nghiem'
#         else:
#             x1=-c/b
#             x2=None
#     else:
#         dental=b*b-4*a*c
#         if dental<0:
#             x1=x2='Phuong trinh vo nghiem'
#         elif dental==0:
#             x1=None
#             x2=-b/(2*a)
#         else:
#             x1=(-b+math.sqrt(dental))/(2*a)
#             x2=(-b-math.sqrt(dental))/(2*a)
#     return x1,x2
# def inkq(x1,x2):
#     if x1==x2=='Phuong trinh vo so nghiem':
#         print(x1)
#     elif x1==x2=='Phuong trinh vo nghiem':
#         print(x1)
#     elif x1==None and x2!=None:
#         print('Phuong trinh co mot nghiem kep')
#         print('x1 = x2 =',x2)
#     elif x1!=None and x2==None:
#         print('Phuong trinh co 1 nghiem')
#         print('x =',x1)
#     elif x1!=None and x2!=None:
#         print('Phuong trinh co hai nghiem')
#         print('x1 =',x1)
#         print('x2 =',x2)
# a,b,c=nhap()
# x1,x2=giaipt(a,b,c)
# inkq(x1,x2)
# ================================================================================================================================================
# BÀI 5.9:
# --------

# n=int(input('n='))
# m=int(input('m='))
# print('L1:')
# L1=[]
# for i in range(n):
#     L1=L1+[int(input())]
# print('L2:')
# L2=[]
# for j in range(m):
#     L2=L2+[int(input())]
# print('L3:',end=' ')
# L1.reverse()
# for kt in L1:
#     if L1.count(kt)>1:
#         while L1.count(kt)>1:
#             L1.remove(kt)
# L1.reverse()
# for k in L1:
#     if k in L2:
#         print(k,end=' ')
# ================================================================================================================================================
# BÀI 7.1
# -------

# str=input()
# hoa=0
# thuong=0
# so=0
# khac=0
# for i in str:
#     if i.isupper():
#         hoa=hoa+1
#     if i.islower():
#         thuong=thuong+1
#     if i.isdecimal():
#         so=so+1
#     if i.isalnum():
#         khac=khac+1
# print('In hoa:',hoa)
# print('In thuong:',thuong)
# print('Chu so:',so)
# print('Khac:',len(str)-khac)
# ================================================================================================================================================
# BÀI 7.2
# -------

# str=input()
# str=str.split()
# str=' '.join(str)
# str=str.strip()
# for i in range(len(str)):
#     if 0<i<len(str) and str[i]==' ':
#         if str[i+1]==',' or str[i+1]=='.' or str[i+1]==';' or str[i+1]==':':
#             str=str[:i]+str[(i+1):]
# for j in range(len(str)):
#     if 0<j<len(str) and (str[j]==',' or str[j]=='.' or str[j]==';' or str[j]==':'):
#         if str[j+1]!=' ':
#             str=str[:(j+1)]+' '+str[(j+1):]
# str=str.lower()
# str=str[0].upper()+str[1:]
# print(str)
# ================================================================================================================================================
# BÀI 7.3
# -------

# import re

# str=input()
# str.strip()
# if re.search("[a-z]",str) and re.search("[0-9]",str) and re.search("[A-Z]",str) and re.search("[$#@]",str) and 6<=len(str)<=17:
#     print('TRUE')
# else:
#     print('FALSE')
# ================================================================================================================================================
# BÀI 7.4
# --------

# str=input()
# str=str.split(',')
# for i in str:
#     while str.count(i)>1:
#         str.remove(i)
# str.sort()
# print(','.join(str))
# ================================================================================================================================================
# BÀI 7.5
# --------

# str=input()
# kt=int(input())
# str=str.split()
# str=[int(i) for i in str]
# if kt in str:
#     dem=0
#     while kt in str:
#         idx=str.index(kt)+dem+1
#         print(idx)
#         str.remove(kt)
#         dem=dem+1
# else:
#     print(0)
# ================================================================================================================================================
# BÀI 7.6
# -------

# str=input()
# str=str.split(',')
# he2=str.copy()
# str=[int(i,2) for i in str]
# kq=[]
# for x in str:
#     if x%3==0:
#         kq.append(x)
# inkq=[]
# for a in he2:
#     if int(a,2) in kq:
#         inkq.append(a)
# print(','.join(inkq))
# ================================================================================================================================================
# BÀI 7.7
# --------

# str=input()
# str=str.split()
# for i in str:
#     if 'gmail' in i:
#         print(i)
# ================================================================================================================================================
# def nhap():
#     n=int(input('Nhap mot so nguyen duong n= '))
#     return n
# def giaithua(n):
#     gt=1
#     for i in range(1,n+1):
#         gt=gt*i
#     return gt
# def inkq(n,gt):
#     print(str(n)+'!'+'='+str(gt))
#     return
# n=nhap()
# gt=giaithua(n)
# inkq(n,gt)
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================