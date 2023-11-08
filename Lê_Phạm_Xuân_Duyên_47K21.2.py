# while True:
#     n=int(input())
#     if n<=0:
#         n=int(input())
#     if n>0:
#         s=0
#         dem=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 s=s+i
#                 dem=dem+1
#                 tb=s/dem
#         print(round(tb,2))
#         break

# s=0
# l=[]
# while True:
#     n=input()
#     if n=='T':
#         break
#     else:
#         l=l+[float(n)]
# for i in l:
#     if i!=int(i):
#         s=s+i
# print(s)

# A=[]
# dai=0
# n=int(input())
# for so in range(n):
#     A=A+[int(input())]
# for i in range(len(A)-1):
#     if A[i]*A[i+1]<0:
#         dai=dai+1
#         if A[i+1]*A[i+2]>0:
#             break
# if dai!=0:
#     print(dai+1)
# else:
#     print(dai)

# l=[]
# st=input()
# for i in st:
#     if i.isnumeric():
#         l=l+[int(i)]
# if len(l)==0:
#     print('')
# else:
#     p=1
#     for j in l:
#         p=p*j
#     print(p)
