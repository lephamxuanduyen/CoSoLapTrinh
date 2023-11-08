                                                # cHƯƠNG4

# Bài 84: TÍNH TRUNG VỊ CỦA BA GIÁ TRỊ
def min(a,b,c):
    min=a
    if min>b:
        min=b
    if min>c:
        min=c
    return min

def max(a,b,c):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    return max

def TrungVi(a,b,c):
    t=(a+b+c)-min(a,b,c)-max(a,b,c)
    return t

def chinh():
    a=int(input('Nhap so thu nhat:'))
    b=int(input('Nhap so thu hai:'))
    c=int(input('Nhap so thu ba:'))
    print('Gia tri trung vi cua ba so la:',TrungVi(a,b,c))

chinh()
# =========================================================================================================================================
# Bài 85:

# def nhap():
#     n=int(input('Moi nhap so: '))
#     return n
# def giai(n):
#     if n==1:
#         print('First')
#     elif n==2:
#         print('Second')
#     elif n==3:
#         print('Third')
#     elif n==4:
#         print('Fourth')
#     elif n==5:
#         print('Fifth')
#     elif n==6:
#         print('Sixth')
#     elif n==7:
#         print('Seventh')
#     elif n==8:
#         print('Eighth')
#     elif n==9:
#         print('Ninth')
#     elif n==10:
#         print('Tenth')
#     elif n==11:
#         print('Eleventh')
#     elif n==12:
#         print('Twelfth')
#     return
# def main():
#     n=nhap()
#     if 1<=n<=12:
#         giai(n)
#     else:
#         print('')
#     return

# main()
# =========================================================================================================================================
                                                    # CHƯƠNG 5
# =========================================================================================================================================
# Bài 107:

# L=[]
# l=[]
# while True:
#     n=input('Moi nhap: ')
#     l=l+[n]
#     for i in l:
#         if i not in L and i!='':
#             L.append(i)
#     if n=='':
#         break
# print(L)
# =========================================================================================================================================
# Bài 108:

# A=[]
# Z=[]
# D=[]
# while True:
#     n=input('Moi nhap: ')
#     if n=='':
#         break
#     else:
#         if int(n)<0:
#             A=A+[n]
#         elif int(n)==0:
#             Z=Z+[n]
#         elif int(n)>0:
#             D=D+[n]
# for x in A:
#     print(x)
# for y in Z:
#     print(y)
# for z in D:
#     print(z)
# =================================================================================================================================================
# BÀI 82:

# def nhap():
 
#     n=float(input('Nhap quang duong da di(km): '))
#     return n
# def tinhgia(n):
#     giacoban=4
#     giamoi140m=float(input('Nhap gia cho moi 140 met: '))
#     tinhgia=giacoban+giamoi140m*(n/0.14)
#     return tinhgia
# def inkq(n,tinhgia):
#     print('Gia cuoc taxi cho '+str(n)+'km la '+str(tinhgia))
# n=nhap()
# tinhgia=tinhgia(n)
# inkq(n,tinhgia)
# =================================================================================================================================================
# BÀI 83:

# def nhap():
#     m=int(input('Nhap so mat hang da mua: '))
#     return m
# def tinhphivanchuyen(m):
#     mathangdautien=10.95
#     mathangtieptheo=2.95
#     if m==1:
#         phivanchuyen=10.95
#     elif m>1:
#         phivanchuyen=(mathangdautien*m)+((mathangtieptheo)*(m-1))
#     return phivanchuyen
# def inkq(m,phivanchuyen):
#     print('Phi van chuyen cua',m,'mat hang la:',phivanchuyen)
#     return
# m=nhap()
# phivanchuyen=tinhphivanchuyen(m)
# inkq(m,phivanchuyen)
# =================================================================================================================================================
# BÀI 106:
# --------

# while True:
#     giatri=[int(x) for x in input().split()]
#     n=int(input('n='))
#     if len(giatri)>=(2*n):
#         break
#     else:
#         print('Loi!! Khong du gia tri. Vui long nhap lai.')
# bansao=giatri.copy()
# print(bansao)
# for a in range(n):
#     min=bansao[0]
#     max=bansao[0]
#     for b in bansao:
#         if b>max:
#             max=b
#         if b<min:
#             min=b
#     bansao.remove(min)
#     bansao.remove(max)
# print('Danh sach da loai bo ngoai te:',bansao)
# print('Danh sach ban dau:',giatri)
# ================================================================================================================================================
# BÀI 104:
# --------

L=[]
while True:
    n=int(input())
    if n==0:
        break
    L=L+[n]
print('Gia tri da sap xep:')
while len(L)>0:
    min=L[0]
    for i in L:
        if i<min:
            min=i
    print(min)
    L.remove(min)
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================