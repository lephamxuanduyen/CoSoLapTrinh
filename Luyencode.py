n=int(input('n='))
m=n
dem=1
while n>=10:
    n=n/10
    dem=dem+1
print(dem)
# =============================================================================================================================================
n=int(input())
dem=0
while n>1:
    n=n/10
    dem=dem+1
print(dem)
# =============================================================================================================================================
a=int(input())
n=int(input())
Lt=1
for i in range(1,n+1):
    Lt=Lt*a
print(Lt)
# =============================================================================================================================================
a, n = (int(x) for x in input().split())
lt=1
for i in range(1,n+1):
	lt=lt*a
# print(lt)
s=lt%(10**9+7)
print(s)
# =============================================================================================================================================
a, b = (int(x) for x in input().split())
max=a
if b>a:
	max=b
print(max)
# =============================================================================================================================================
n=int(input())
s=0
for i in range(2,n+1):
    s=s+i
print(s+2*n)
# =============================================================================================================================================
n=int(input())
s=0
if n>=2:
    for i in range(2,n+1):
        s=s+1/i
print(round(s,4))
# =============================================================================================================================================
import math
L=int(input())
R=int(input())
d=0
for i in range(L,R+1):
    if (math.sqrt(i)).is_integer:
        d=d+1
print(d)
# =============================================================================================================================================

n=int(input())
dem=0
if n>0:
    while n>1:
        n=n/10
        dem=dem+1
else:
    m=-n
    while m>1:
        m=m/10
        dem=dem+1
print(dem)
# =============================================================================================================================================

r=float(input())
pi=3.14
p=2*r*pi
s=pi*(r**2)
print(round(p,3),end=' ')
print(round(s,3))
# =============================================================================================================================================

a, b=(int(x) for x in input().split())
print(a,'+',b,'=',a+b)
# =============================================================================================================================================

a, b, c=(int(x) for x in input().split())
max=a
if max<b:
   max=b
elif max<c:
   max=c
print(max)
# =============================================================================================================================================

a,b=(int(x) for x in input().split())
c=a-b
if c<0:
   c=-c
print(c)
# =============================================================================================================================================
# LÀM TRÒN

n=float(input())
if n>=0:
   le=n-int(n)
   if le>=0.5:
      them=1
   else:
      them=0
   moi=int(n)+them
if n<0:
   n=-n
   le=n-int(n)
   if le>=0.5:
      them=1
   else:
      them=0
   moi=-(int(n)+them)
print(moi)
# =============================================================================================================================================
# TÌM SỐ CHÍNH PHƯƠNG

import math
n=float(input())
if n>0:
   cb2=int(math.sqrt(n))
   if n==(cb2**2):
      print('YES')
   else:
      print('NO')
elif n==0:
   print('YES')
else:
   print('NO')
# =============================================================================================================================================
# GIẢI PHƯƠNG TRÌNH BẬC NHẤT

a,b=(int(x) for x in input().split())
if a==0:
   if b==0:
      print('INF')
   else:
      print('NO')
else:
   print(round(-b/a,2))
# =============================================================================================================================================
# GIẢI PHƯƠNG TRÌNH BẬC HAI

import math
a,b,c=(int(x) for x in input().split())
if a==0:
   if b==0:
      if c==0:
         print('INF')
      else:
         print('NO')
   else:
      print(round(-c/b,2))
else:
   dental=b*b-4*a*c
   if dental<0:
      print('NO')
   elif dental==0:
      print(round(-b/(2*a),2))
   else:
      m=round((-b+math.sqrt(dental))/(2*a),2)
      n=round((-b-math.sqrt(dental))/(2*a),2)
      if m<n:
         min=m
         max=n
      elif m>n:
         max=m
         min=n
      print(min,end=' ')
      print(max)
# =============================================================================================================================================
# MÁY TÍNH BỎ TÚI ĐƠN GIẢN

a,dau,b=(x for x in input().split())
a=float(a)
b=float(b)
if dau=='+':
   if -10000<=a+b<=10000:
      print('{:.2f}'.format(a+b))
   else:
      print('Math Error')
elif dau=='-':
   if -10000<=a-b<=10000:
      print('{:.2f}'.format(a-b))
   else:
      print('Math Error')
elif dau=='*':
   if -10000<=a-b<=10000:
      print('{:.2f}'.format(a*b))
   else:
      print('Math Error')
elif dau=='/':
   if b==0:
      print('Math Error')
   else:
      if -10000<=a/b<=10000:
         print('{:.2f}'.format(a/b))
      else:
         print('Math Error')
# =============================================================================================================================================
# ĐẾM SỐ CHÍNH PHƯƠNG(partial accept)

import math
l,r=(int(x) for x in input().split())
dem=0
for i in range(l,r+1):
   if i>0:
      cb2=int(math.sqrt(i))
      if i==(cb2**2):
         dem=dem+1
      else:
         dem=dem
   elif i==0:
      dem=dem+1
   else:
      dem=dem
print(dem)
# =============================================================================================================================================
# XÁC ĐỊNH NĂM NHUẬN

n=int(input())
if 0<n<=100000:
   if n%400==0 or (n%4==0 and n%100!=0):
      print('YES')
   else:
      print('NO')
else:
   print('INVALID')
# =============================================================================================================================================
# TÌM SỐ NGÀY CỦA THÁNG
  
month,year=(int(x) for x in input().split())
if 1<=month<=12 and 0<year<=100000:
   if year%400==0 or (year%4==0 and year%100!=0):
      if month==2:
         print('29')
      elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
         print('31')
      else:
         print('30')
   else:
      if month==2:
         print('28')
      elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
         print('31')
      else:
         print('30')
else:
   print('INVALID')
# =============================================================================================================================================
# IN RA CÁC SỐ TỪ A ĐẾN B

a,b=(int(x) for x in input().split())
for i in range(a,b+1):
   print(i,end=' ')
# =============================================================================================================================================
# TÍNH TỔNG PHIÊN BẢN 1: S=1+2+3+...+N

n=int(input())
s=0
for i in range(1,n+1):
   s=s+i
print(s)
# =============================================================================================================================================
# TÍNH TỔNG S=1/2+1/3+...+1/N

n=float(input())
s=0
for i in range(1,n+1):
    s=s+(1/i)
print(s)
# =============================================================================================================================================
# TÍNH GIÁ TRỊ S=1-2+3-....+(3N+1)

n=int(input())
s=0
for i in range(1,3*n+2):
    if i%2==1:
        s=s+i
    elif i%2==0:
        s=s-i
print(s)
# =============================================================================================================================================
# TÍNH GIAI THỪA

n=int(input())
gt=1
for i in range(1,n+1):
    gt=gt*i
print(gt)
# =============================================================================================================================================
# TÍNH CÁC SỐ CHẴN TRONG [a,b]

a,b=(int(x) for x in input().split())
s=0
for i in range(a,b+1):
    if i%2==0:
        s=s+i
print(s)
# =============================================================================================================================================
TÍNH S=X+X^2/2!+...+X^N/N!

x,n=(int(x) for x in input().split())
s=x
for j in range(2,n+1):
    gt=1
    for i in range(2,j+1):
        gt=gt*i
        s=s+((x**i)/gt)
print(round(s,2))
# =============================================================================================================================================
# KIỂM TRA SỐ NGUYÊN TỐ

import math
n=int(input())
if n<2:
    print('NO')
elif n==2:
    print('YES')
elif 2<n<=10**12:
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            print('NO')
            break
    else:
        print('YES')
# =============================================================================================================================================
# LIỆT KÊ CÁC ƯỚC SỐ

n=int(input())
if n==0:
    print('INF')
elif n<0:
    n=-n
    for i in range(n,0,-1):
        if n%i==0:
            print(i,end=' ')
else:
    for i in range(n,0,-1):
        if n%i==0:
            print(i,end=' ')
# =============================================================================================================================================
# TÌM SỐ HOÀN HẢO

def nhap():
    n=int(input())
    return n
def solve(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
def inkq(s,n):
    if n==s:
        print('YES')
    else:
        print('NO')
n=nhap()
kq=solve(n)
inkq(kq,n)

# =============================================================================================================================================
# TÌM ƯỚC CHUNG LỚN NHẤT

a,b=(int(x) for x in input().split())
if a>0 and b>0:
    if a==b:
        print(a)
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
elif a>0 and b<0:
    b=-b
    if a==b:
        print(a)
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
elif a<0 and b>0:
    a=-a
    if a==b:
        print(a)
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
elif a<0 and b<0:
    a=-a
    b=-b
    if a==b:
        print(a)
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
elif a*b==0 and (a>0 or b>0):
    print(a+b)
elif a*b==0 and (a<0 or b<0):
    print(-(a+b))
elif a==0 and b==0:
    print('INF')
# =============================================================================================================================================
# RÚT GỌN PHÂN SỐ

a,b=(int(x) for x in input().split())
if -1000<=a<=1000 and -1000<=b<=1000:
    if b==0:
        print('INVALID')
    elif a%b==0:
        print(int(a/b))
    elif b!=0:
        if a>0 and b>0:
            if a>b:
                for i in range(b,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(a,end=' ')
                print(b)
            else:
                for i in range(a,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(int(a),end=' ')
                print(int(b))
        elif a>0 and b<0:
            b=-b
            if a>b:
                for i in range(b,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(-int(a),end=' ')
                print(int(b))
            else:
                for i in range(a,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(-int(a),end=' ')
                print(int(b))
        elif a<0 and b>0:
            a=-a
            if a>b:
                for i in range(b,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(-int(a),end=' ')
                print(int(b))
            else:
                for i in range(a,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(-int(a),end=' ')
                print(int(b))
        elif a<0 and b<0:
            a=-a
            b=-b
            if a>b:
                for i in range(b,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(int(a),end=' ')
                print(int(b))
            else:
                for i in range(a,0,-1):
                    if a%i==0 and b%i==0:
                        a=a/i
                        b=b/i
                print(int(a),end=' ')
                print(int(b))
        elif a==0:
            print('0')
else:
    print('INF')
# =============================================================================================================================================
# TÌM BỘI CHUNG NHỎ NHẤT CỦA HAI SỐ

a,b=(int(x) for x in input().split())
if a>0 and b>0:
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
elif a>0 and b<0:
    b=-b
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
elif a<0 and b>0:
    a=-a
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
elif a<0 and b<0:
    a=-a
    b=-b
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
print(int((a*b)/ucln))
# =============================================================================================================================================
#  ĐẾM SỐ LƯỢNG ƯỚC SỐ

n=int(input())
dem=0
if n>0:
    for i in range(1,n+1):
        if n%i==0:
            dem=dem+1
elif n<0:
    for i in range(n,0):
        if n%i==0:
            dem=dem+1
print(int(dem))
# =============================================================================================================================================
# IN RA CÁC SỐ CHIA HẾT CHO 3 TRONG KHOẢNG (A,B)

a,b=(int(x) for x in input().split())
L=[]
if a<b:
    for i in range(a+1,b):
        if i%3==0 and i>=0:
            L.append(i)
    if len(L):
        L.reverse()
        for j in L:
            print(j,end=' ')
    else:
        print('NOT FOUND')
else:
    print('NOT FOUND')
# =============================================================================================================================================
# SỐ GẤP ĐÔI

n=int(input())
print(2*n)
# =============================================================================================================================================
# PHÉP TOÁN LỚP 3

a,b,c=(int(x) for x in input().split())
print((a-b)*c)
# =============================================================================================================================================
# PROD - PRODUCT

a,b=(int(x) for x in input().split())
if a*b>0:
    print('1')
elif a*b<0:
    print('-1')
else:
    print('0')
# =============================================================================================================================================
# CHUẨN BỊ CHO NĂM HỌC MỚI

a,b,x,y=(int(i) for i in input().split())
print(a*x+b*y)
# =============================================================================================================================================
# SỐ CHIA HẾT HAY KHÔNG?

n=int(input())
a,b=(int(x) for x in input().split())
if a==0 and b==0:
    print('Khong chia het cho so nao ca.')
elif a==0 and b!=0:
    if n%b==0:
        print('Chi chia het cho '+str(b)+'.')
    else:
        print('Khong chia het cho so nao ca.')
elif a!=0 and b==0:
    if n%a==0:
        print('Chi chia het cho '+str(a)+',')
    else:
        print('Khong chia het cho so nao ca.')
elif a!=0 and b!=0:
    if n%a==0 and n%b==0:
        print('Co, tat ca!')
    elif n%a==0 and n%b!=0:
        print('chi chia het cho '+str(a)+',')
    elif n%a!=0 and n%b==0:
        print('Chi chia het cho '+str(b)+'.')
    elif n%a!=0 and n%b!=0:
        print('Khong chia het cho so nao ca.')
# =============================================================================================================================================
# LÀM TRÒN

n=float(input())
if n>=0:
    print(int(n),end=' ')
    print(int(n)+1)
else:
    print(-(-int(n)+1),end=' ')
    print(int(n))
# =============================================================================================================================================
# TÍNH GIÁ TRỊ HÀM BẬC 2

a,b,c,x=(int(x) for x in input().split())
print(a*x*x+b*x+c)
# =============================================================================================================================================
# TRUNG BÌNH CỘNG CỦA BA SỐ

a,b,x=(int(i) for i in input().split())
print(x*3-(a+b))
# =============================================================================================================================================
# CGAME - Pokémon Trading Card Game

a,b=(int(x) for x in input().split())
if a>b:
    print('1')
elif a<b:
    print('0')
# =============================================================================================================================================
# VL02 - Tính tổng S = 1 + 2 + 3 + ... + n

n=int(input())
if 1<=n<=10**9:
    s=0
    for i in range(1,n+1):
        s=s+i
print(s)
# =============================================================================================================================================
# KIỂM TRA TAM GIÁC HỢP LỆ

import math
a,b,c=(int(x) for x in input().split())
if a+b>c and a+c>b and b+c>a:
    p=a+b+c
    print(p,end=' ')
    p=p/2
    s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
    print(s)
else:
    print('NO')
# =============================================================================================================================================
# TÌM SỐ ĐẢO NGƯỢC

n=int(input())
nguoc=0
while n>0:
    cuoi=n%10
    nguoc=nguoc*10+cuoi
    n=n//10
print(nguoc)
# =============================================================================================================================================
# CHUYỂN HỆ THẬP PHÂN SANG NHỊ PHÂN
n=int(input())
L=[]
for i in range(1,n+1):
    L=L+[int(input())]
for j in L:
    K=[]
    while j>0:
        if j%2==0:
            K=K+[0]
        else:
            K=K+[1]
        n=n//2
    for k in range(len(L)-1,-1,-1):
        print(K[k],end='')
    print(sep='')

n=int(input())
for i in range(1,n+1):
    a=int(input())
    l=[]
    while a>0:
        if a%2==0:
            l=l+[0]
        else:
            l=l+[1]
        a=a//2
    l.reverse()
    for x in l:
        print(x,end='')
    print(sep='')

for i in range(int(input())): print(bin(int(input()))[2:])

n=int(input())
for i in range(1,n+1):
    a=int(input())
    kq=''
    while a>0:
        kq=str(a%2)+kq
        a=a//2
    print(kq)

n=int(input())
for i in range(1,n+1):
    a=int(input())
    he2=bin(a)
    print(he2[2:])

# =============================================================================================================================================
# TÌM SỐ LỚN NHẤT TRONG MẢNG

n=int(input())
l=[int(x) for x in input().split()]
print(max(l))
# =============================================================================================================================================
# TÌM SỐ LỚN THỨ HAI TRONG MẢNG

n=int(input())
L=[int(x) for x in input().split()]
L=list(sorted(set(L)))
if len(L)==1:
    print('NOT FOUND')
elif len(L)>1:
    print(L[-2])
# =============================================================================================================================================
# TỔNG THỂ TÍCH

v=0
for i in range(1,int(input())+1):
    v=v+i**3
print(v)
# =============================================================================================================================================
# ĐẾM SỐ NGUYÊN TỐ

for i in range(int(input())):
    a,b=(int(x) for x in input().split())
    so=0
    for y in range(a,b+1):
        if y==2:
            so=so+1
        elif y>2:
            dem=0
            for j in range(2,y):
                if y%j==0:
                    dem=dem+1
            if dem==0:
                so=so+1
    print(so)
# =============================================================================================================================================
# GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN

a1,b1,c1,a2,b2,c2=(int(x) for x in input().split())
D=a1*b2-a2*b1
Dx=c1*b2-c2*b1
Dy=a1*c2-a2*c1
if D==0:
    if Dx==0 and Dy==0:
        if a1==b1==a2==b2==c1==0 and c2!=0:
            print('VONGHIEM')
        elif a1==b1==a2==b2==c2==0 and c1!=0:
            print('VONGHIEM')
        else:
            print('VOSONGHIEM')
    elif Dy!=0:
        print('VONGHIEM')
    elif Dx!=0:
        print('VONGHIEM')
    elif Dx!=0 and Dy!=0:
        print('VONGHIEM')
else:
    x=round(Dx/D,2)
    y=round(Dy/D,2)
    if x==-0: x=-x
    elif y==-0: y=-y
    elif x==-0 and y==-0:
        x=-x
        y=-y
    print(x,y)
# =============================================================================================================================================
# PHÂN TÍCH RA THỪA SỐ NGUYÊN TỐ

def phanTichSoNguyen(n):
    i = 2
    L= []
    while (n > 1):
        if (n % i == 0):
            n = int(n / i)
            L.append(i)
        else:
            i = i + 1
    if (len(L) == 0):
        L.append(n)
    return L
 
n = int(input())
if n==1:
    print(0)
else:
    L = phanTichSoNguyen(n)
    l=list(set(L))
    print(len(l))
    for i in range(0,len(l)):
        print(l[i],end=' ')
        print(L.count(l[i]))
size = len(L)
sb = ""
for i in range(0, size - 1):
    sb = sb + str(L[i]) + " x "
sb = sb + str(L[size-1])
# in kết quả ra màn hình
print("Kết quả:", n, "=", sb)
# =============================================================================================================================================
# TÌM KIẾM TRONG MẢNG

n,a=(int(x) for x in input().split())
L=[int(y) for y in input().split()]
dem=0
if a in L:
    dem=dem+1
if dem==0:
    print('NO')
else:
    print('YES')
# =============================================================================================================================================
# TÌM CHỈ SỐ MẢNG CÓ GIÁ TRỊ LỚN NHẤT

n=int(input())
L=[int(x) for x in input().split()]
while L.count(max(L))>1:
    L[L.index(max(L))]=min(L)
print(L.index(max(L)))
# =============================================================================================================================================
# HỌC ĐẾM TRONG MẢNG

n,a=(int(y) for y in input().split())
L=[int(x) for x in input().split()]
print(L.count(a))
# =============================================================================================================================================
# TRUNG BÌNH CỘNG CỦA MẢNG

A=[int(x) for x in input().split()]
B=A[0:-1]
a=A[10]
s=0
if a in B:
    for x in B:
        s=s+1
        if x==a:
            print(s,end=' ')
else:
    print(-1)
# =============================================================================================================================================
# Vẫn là tìm kiếm trong mảng

A=[int(x) for x in input().split()]
B=A[0:-1]
s=0
for x in B:
    s=s+1
    if x==A[10]:
        print(s,end=' ')
if A[10] not in B:
    print(-1)
# =============================================================================================================================================
# Sắp xếp mảng giảm dần

n=int(input())
L=[int(x) for x in input().split()]
l=sorted(L,reverse=True)
for i in l:
    print(i,end=' ')
# =============================================================================================================================================
# Hãy viết chương trình sắp xếp mảng các số nguyên AA có nn phần tử tăng dần nhưng giữ nguyên vị trí phần tử đầu tiên và phần tử cuối cùng của mảng

n=int(input())
l=[int(x) for x in input().split()]
L=sorted(l[1:-1])
print(l[0],end=' ')
for i in L:
    print(i,end=' ')
print(l[-1])
# =============================================================================================================================================
# TÌM SỐ NGUYÊN TỐ TRONG MẢNG

import math

n=int(input())
L=[int(x) for x in input().split()]
snt=[]
for i in L:
    if i>1:
        if i==2:
            snt.append(i)
        else:
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    break
            else:
                if i not in snt:
                    snt.append(i)
SNT=sorted(snt)
for y in SNT:
    print(y,end=' ')
# =============================================================================================================================================
# LIỆT KÊ CÁC SỐ ÂM TRONG MẢNG

L=[int(x) for x in input().split()]
A=[]
dem=0
for i in L:
    if i<0:
        A.append(i)
        dem=dem+1
if dem==0:
    print('NOT FOUND')
else:
    for j in A:
        print(j,end=' ')
# =============================================================================================================================================
# VT08 - Biến đổi mảng 1 chiều

n=int(input())
L=[int(x) for x in input().split()]
inkq=[]
for i in L:
    if L.index(i)%2==0:
        inkq.append(i)
    else:
        if L.index(i)!=n-1:
            if L[L.index(i)+1]>=L[L.index(i)-1]:
                inkq.append(i+(L[L.index(i)+1]-L[L.index(i)-1]))
            else:
                inkq.append(i-(L[L.index(i)+1]>=L[L.index(i)-1]))
        else:
            inkq.append(i+L[n-])
for kq in inkq:
    print(kq,end=' ')
# =============================================================================================================================================
#   IN HOA CÁC CHỮ CÁI

thuong=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
hoa=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a,b=(str(x) for x in input().split())
str = "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z"
L = str.split(".")
i=L.index(a)
ii=L.index(b)
if i<ii:
    inkq=[]
    for chu in range(i,ii+1):
        inkq.append(L[chu].upper())
    if len(inkq)==1:
        print(inkq)
    else:
        for kq in inkq:
            print(kq,end=' ')

# -----------------------------------------------
a,b=[x.upper() for x in input().split()]

for i in range(ord(a),ord(b)+1):
    print(chr(i),end=' ')

# -----------------------------------------------
a, b = [str(x) for x in input().split()]
L=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
id1 = L.index(a)
id2 = L.index(b)
if id1 <= id2:
    A = []
    for x in range(id1, id2 + 1):
        A.append(L[x].upper())
    for y in A:
        if len(A) == 1:
            print(y)
        else:
            print(y, end=" ")
# =============================================================================================================================================
#  TÍNH DIỆN TÍCH HÌNH

pi=3.141592653589793238462643
a=int(input())
tam_giac=a*a
khuyet=((pi*a*a)/2)-a*a
s=tam_giac+khuyet
print(round(s,3))

a=int(input())
pi=3.141592653589793238462643
def tam_giac(a):
    s=(a*a)/2
    return s
def tron(a):
    s=pi*a*a
    return s
def goc(a):
    s=(tron(a))/4
    return s
def khuyet(a):
    s=(goc(a))-(tam_giac(a))
    return s
s=(2*(tam_giac(a)))+(2*(khuyet(a)))
print(round(s,3))
# =============================================================================================================================================
# SUM2

n=int(input())
s=0
for i in range(1,n+1):
    s=s+(i*i)
print(s)
# =============================================================================================================================================
# SUM3

n=int(input())
s=0
if 1<=n<=10**6:
    for i in range(1,n+1):
        s=s+1/(i*(i+1))
    print(round(s,5))
# =============================================================================================================================================
# TÌM CHÊNH LỆCH LỚN NHẤT TRONG MẢNG

n=int(input())
L=[int(x) for x in input().split()]
kq=sorted(L)
print(kq[-1]-kq[0])
# =============================================================================================================================================
# LẠI LÀ ĐI TÌM CẶP ĐÔI

import copy
n=int(input())
L=[int(x) for x in input().split()]
max=0
for i in L:
    xet=copy.copy(L)
    xet.remove(i)
    for j in range(0,n-1):
        s=i*xet[j]
        if s>max:
            max=s
print(max)
# =============================================================================================================================================
# ĐI TÌM ẨN SỐ

n=int(input())
l=[]
for i in range(1,n+1):
    n=n-i
    if n>=0:
        l.append(i)
    else:
        break
print(l[-1])
# =============================================================================================================================================
# ĐẾM KHOẢNG TRẮNG TRONG CHUỖI

n=int(input())
for i in range(n):
    str=input()
    L=list(str)
    dem=0
    if L[-1]==' ':
        dem=dem+1
    for j in range(len(L)-1):
        if L[j]==' ' and L[j+1]!=' ':
            dem=dem+1
    print(dem)

# =============================================================================================================================================
# CON SỐ DUYÊN NỢ

while True:
    try:
        n = input()
        if n[0]==n[-1]:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
# =============================================================================================================================================
# BÉ HỌC TIẾNG ANH

str=list(input())
dem=1
if str[0]==' ':
    dem=dem+0
for i in range(len(str)-1):
    if str[i]==' ' and str[i+1]!=' ':
        dem=dem+1
print(dem)
# =============================================================================================================================================
# TỔNG CÁC CHỮ SỐ

n=int(input())
for i in range(n):
    so=input()
    s=0
    L=list(so)
    for j in L:
        s=s+int(j)
    print(s)
# =============================================================================================================================================
# TỔNG CÁC ƯỚC SỐ

n=int(input())
for i in range(n):
    so=int(input())
    uoc=[]
    for j in range(1,so+1):
        if so%j==0:
            uoc.append(j)
    s=0
    for k in uoc:
        s=s+k
    print(s)
# =============================================================================================================================================
# SUM 4

n=int(input())
for i in range(n):
    so=int(input())
    s=2*(1-1/(so+1))
    print(round(s,8))
# =============================================================================================================================================
# THUẬT TOÁN SÀNG NGUYÊN TỐ

import math

n=int(input())
ngto=[]
for i in range(2,n+1):
    if i==2:
        ngto.append(i)
    else:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            ngto.append(i)
for k in ngto:
    print(k,end=' ')
# =============================================================================================================================================
# KÍ TỰ LIỀN SAU

chu=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str=input()
if str!='z':
    print(chu[chu.index(str)+1])
else:
    print('a')
# =============================================================================================================================================
# LŨY THỪA BẬC 3

n=int(input())
for i in range(n):
    so=int(input())
    for j in range(1,so):
        if j**3==so:
            print('YES')
            break
    else:
        print('NO')
# =============================================================================================================================================
# IROHA VÀ HAIKU

a,b,c=(int(x) for x in input().split())
L=[]
L.append(a)
L.append(b)
L.append(c)
if L.count(5)==2 and L.count(7)==1:
    print('YES')
else:
    print('NO')
# =============================================================================================================================================
# GIÁ TRỊ MANG TẦN SUẤT LẺ

import copy

n=int(input())
L=[int(x) for x in input().split()]
l=copy.copy(L)
l=list(set(l))
for i in l:
    if L.count(i)%2!=0:
        print(i)

# WRONG ANSWER
# =============================================================================================================================================
# SỐ ĐẸP

n=int(input())
l=list(str(n))
s=0
for i in l:
    s=s+int(i)
tong=list(str(s))
if int(tong[-1])==9:
    print('YES')
elif int(tong[-1])!=9:
    print('NO')
# =============================================================================================================================================
# ĐỔI THỜI GIAN

n=int(input())
h=n//3600
m=(n-(h*3600))//60
s=(n-(h*3600)-(m*60))//1
if len(str(h))==1:
    hh=str(0)+str(h)
else:
    hh=str(h)
if len(str(m))==1:
    mm=str(0)+str(m)
else:
    mm=str(m)
if len(str(s))==1:
    ss=str(0)+str(s)
else:
    ss=str(s)
print(hh+':'+mm+':'+ss)
# =============================================================================================================================================
# IN RA CHỮ SỐ HÀNG TRĂM, CHỤC, ĐƠN VỊ

n=int(input())
if n<=9:
    print('00'+str(n))
elif 10<=n<=99:
    print('0'+str(n))
elif 100<=n<=999:
    print(n)
else:
    l=list(str(n))
    print(str(l[-3])+str(l[-2])+str(l[-1]))
# =============================================================================================================================================
# PHÂN TÍCH RA THỪA SỐ NGUYÊN TỐ

import copy
def phan_tich_snt(n):
    i=2
    l=[]
    while n>1:
        if n%i==0:
            l.append(i)
            n=n//i
        else:
            i=i+1
    if len(l)==0:
        l.append(n)
    return l
n=int(input())
l=phan_tich_snt(n)
snt=list(set(copy.copy(l)))
for j in snt:
    print(j,l.count(j))
# =============================================================================================================================================
# HÌNH HỘP CHỮ NHẬT

import math

s1, s2, s3 =(int(x) for x in input().split())

a=math.sqrt(s1*s2*s3)/s1
b=math.sqrt(s1*s2*s3)/s2
c=math.sqrt(s1*s2*s3)/s3

kq=(4*(a+b+c))%(10**9+7)
print(kq)
# =============================================================================================================================================
# TRA CỨU NGÀY THÁNG

n, y = (int(x) for x in input().split())
if 1<=n<=365 and 1990<=y<=2050:
    if y%100!=0:
        if y%4==0:
            nam='nam nhuan'
        else:
            nam='nam thuong'
    else:
        if y%400==0:
            nam='nam nhuan'
        else:
            nam='nam thuong'
    
    thang=0
    thang_31=[1,3,5,7,8,10,12]
    thang_30=[4,6,9,11]
    while n>31:
        thang=thang+1
        if thang in thang_31:
            n=n-31
        elif thang in thang_30:
            n=n-30
        elif thang==2:
            if nam=='nam nhuan':
                n=n-29
            elif nam=='nam thuong':
                n=n-28
    print(n,thang+1)
        
else:
    print('INVALID')
# =============================================================================================================================================
# SỐ ĐẸP

while True:
    try:
        l, r = (int(x) for x in input().split())
        l=[]
        for i in range(55,r+1):
            so=list(str(i))
            for k in range(len(so)):
                if so[k]==so[-(1+k)]:
                    s=0
                    for j in so:
                        s=s+int(j)
                        if s%10==0:
                            l.append(i)
        print(len(list(set(l))))
    except EOFError:
        break
# =============================================================================================================================================
# TÍNH TỔNG ƯỚC CHUNG CỦA 2 SỐ

a,b=(int(x) for x in input().split())
s=0
if a<b:
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            s=s+i
else:
    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            s=s+i
print(s)
# =============================================================================================================================================
# ĐIỂM TRÊN MỘT CHUỖI

n=int(input())
chuoi=input()
print(chuoi.count('luyencode'))
# =============================================================================================================================================
# QUÀ TẶNG BẠN GÁI

a,b=(int(x) for x in input().split())
if a<b:
    print(0)
else:
    print(1)
# =============================================================================================================================================
# SO SÁNH BỘ 3 SỐ

a=[int(x) for x in input().split()]
b=[int(y) for y in input().split()]
HD=0
HP=0
for i in range(3):
    if a[i]<b[i]:
        HP=HP+1
    elif a[i]>b[i]:
        HD=HD+1
print(HD,HP)
# =============================================================================================================================================
# NGÀY HỢP LỆ

n=int(input())
for i in range(n):
    d,m,y=(int(x) for x in input().split())
    thang31=[1,3,5,7,8,10,12]
    thang30=[4,6,9,11]
    if 1<=d and m<1990<=y<=3000:
        if y%100!=0:
            if y%4==0:
                nam='nam nhuan'
            else:
                nam='nam thuong'
        else:
            if y%400==0:
                nam='nam nhuan'
            else:
                nam='nam thuong'
        if m in thang31:
            if 1<=d<=31:
                print('TRUE')
            else:
                print('FALSE')
        elif m in thang30:
            if 1<=d<=30:
                print('TRUE')
            else:
                print('FALSE')
        elif m==2:
            if nam=='nam nhuan':
                if 1<=d<=29:
                    print('TRUE')
                else:
                    print('FALSE')
            elif nam=='nam thuong':
                if 1<=d<=28:
                    print('TRUE')
                else:
                    print('FALSE')
        else:
            print('FALSE')
    else:
        print('FALSE')
# =============================================================================================================================================
# BỘI CHUNG NHỎ NHẤT CỦA 2 SỐ

a,b=(int(x) for x in input().split())
if a>0 and b>0:
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
elif a>0 and b<0:
    b=-b
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
elif a<0 and b>0:
    a=-a
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
elif a<0 and b<0:
    a=-a
    b=-b
    if a==b:
        ucln=a
    elif a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
    else:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                ucln=i
                break
print(int((a*b)/ucln))
# =============================================================================================================================================
# SO SÁNH 2 LŨY THỪA

n=int(input())
for i in range(n):
    a,b,c=(int(x) for x in input().split())
    if a**c>b**c:
        print('>')
    elif a**c<b**c:
        print('<')
    else:
        print('=')
# =============================================================================================================================================
# TỔNG CĂN BẬC HAI LỒNG NHAU

import math

N=int(input())
for i in range(N):
    n=int(input())
    s=math.sqrt(2)
    for j in range(2,n+1):
        s=math.sqrt(2+s)
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# LỚN HƠN

a,b=(int(x) for x in input().split())
nam=0
while a<=b:
    a=3*a
    b=2*b
    nam=nam+1
print(nam)
# =============================================================================================================================================
# VĂN NGHỆ CHÀO MỪNG

n=int(input())
thap=0
ruot=0
for i in range(0,n):
    thap=thap+(2*i+1)
for j in range(0,n-2):
    ruot=ruot+(2*j+1)
vo=thap-ruot
print(vo,ruot)
# =============================================================================================================================================
# GHÉP TAM GIÁC

a,b,c=(int(x) for x in input().split())
s=0
if a+b<=c:
    s=s+c+1-(a+b)
if a+c<=b:
    s=s+b+1-(a+c)
if b+c<=a:
    s=s+a+1-(b+c)
print(s)
# =============================================================================================================================================
# SỐ CHỮ SỐ 5

m,n=(int(x) for x in input().split())
dem=0
for i in range(m,n+1):
    kt=list(str(i))
    a='5'
    if a in kt:
        dem=dem+kt.count(a)
print(dem)
# =============================================================================================================================================
# TÍNH TỔNG NGHỊCH ĐẢO CÁC SỐ LẺ

lap=int(input())
for i in range(lap):
    n=int(input())
    s=0
    for j in range(1,n+1):
        s=s+(1/(2*j-1))
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# CHO 2 SỐ DƯƠNG A, B. TÍNH TỔNG CÁC SỐ NGUYÊN DƯƠNG LÀ ƯỚC CỦA A MÀ KHÔNG PHẢI LÀ ƯỚC CỦA B

a,b=(int(x) for x in input().split())
s=0
if a==b:
    print(0)
else:
    for i in range(2,a+1):
        if a%i==0 and b%i!=0:
            s=s+i
print(s)
# =============================================================================================================================================
# VẼ HÌNH CHỮ NHẬT ĐẶC

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end='')
    print(end='\n')
# =============================================================================================================================================
# GÀ VÀ CHÓ

m,n=(int(x) for x in input().split())
ga=(4*m-n)/2
cho=(n-2*m)/2
if ga<0 or cho<0 or ga!=int(ga) or cho!=int(cho):
    print(-1)
else:
    print(int(ga),int(cho))
# =============================================================================================================================================
# SỐ ĐƠN GIẢN

n=int(input())
if n<10:
    print(n)
else:
    while len(str(n))>1:
        l=list(str(n))
        n=0
        for i in l:
            n=n+int(i)
    print(n)
# =============================================================================================================================================
# SỐ ĐẶC BIỆT

n=int(input())
l=list(str(n))
s=0
for i in l:
    s=s+int(i)
if n%s==0:
    print('YES')
else:
    print('NO')
# =============================================================================================================================================
# ALICE VÀ TIỆM THUỐC LÁ

bao,k=(int(x) for x in input().split())
ngay=bao
while bao>=k:
    bao=bao-k+1
    ngay=ngay+1
print(ngay)
# =============================================================================================================================================
# SỐ MẠNH MẼ

def snt(l,r):
    L=[2]
    for i in range(l+1,r+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            L.append(i)
    return L
l,r=(int(x) for x in input().split())
L=snt(l,r)
dem=0
for j in range(l+1,r+1):
    if j in L:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# BẢNG CỬU CHƯƠNG

n=int(input())
for i in range(0,31):
    print(n,'x',i,'=',n*i)
# =============================================================================================================================================
# SỐ ĐẶC BIỆT

n=int(input())
if n==2:
    print('YES')
else:
    for i in range(2,n):
        if n%i==0:
            print('NO')
            break
    else:
        l=list(str(n))
        s=0
        for j in l:
            s=s+int(j)
        for k in range(2,s):
            if s%k==0:
                print('NO')
                break
        else:
            print('YES')
# =============================================================================================================================================
# SỐ VUI VẺ

l,r=(int(x) for x in input().split())
dem=0
for i in range(l+1,r):
    kt=0
    for j in range(1,i+1):
        if i%j==0:
            kt=kt+1
    if kt%2==1:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# CHUYỂN VỀ CHUỖI VIẾT THƯỜNG

str=input()
print(str.lower())
# =============================================================================================================================================
# CHUẨN HÓA TÊN RIÊNG

n=int(input())
for i in range(n):
    str=input()
    print(str.title())
# =============================================================================================================================================
# ĐẾM SỐ LƯỢNG KÍ TỰ

str=input()
n=int(input())
for i in range(n):
    str=str.lower()
    x=input().lower()
    print(str.count(x))
# =============================================================================================================================================
# TẦN SUẤT XUẤT HIỆN CÁC KÍ TỰ

str=input().lower()
chu=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l=sorted(str)
for i in l:
    if i in chu:
        print(l.count(i),i)
# =============================================================================================================================================
so=[0,1,2,3,4,5,6,7,8,9]
chu=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str=list(input().lower())
dem=0
for i in range(len(str)-1):
    if str[i] in chu:
        if str[i+1] in so:
            dem=dem+1
print(dem)
# =============================================================================================================================================
# THẾ NÀO LÀ TRÀN SỐ

a,b=(int(x) for x in input().split())
print(a+b,a-b,a*b)
# =============================================================================================================================================
# PHÉP XOR TRÊN DÃY NHỊ PHÂN

a,b=(int(x) for x in input().split())
kq=a-b
if kq<0:
    print(-kq)
else:
    print(kq)
# =============================================================================================================================================
# SỐ NGUYÊN TỐ ĐẶC BIỆT

n=int(input())
kt=0
for i in range(1,n+1):
    dem=0
    for i in range(1,i):
        dem=dem+1
    if dem==3:
        kt=kt+1
print(kt)
# =============================================================================================================================================
# SUM 7

import math

N=int(input())
for i in range(N):
    s=0
    n=int(input())
    for i in range(1,n+1):
        s=math.sqrt(s+i)
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# SUM 8

import math

N=int(input())
for i in range(N):
    s=0
    n=int(input())
    for i in range(n,0,-1):
        s=math.sqrt(s+i)
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# SUM 9 - LIÊN PHÂN SỐ

N=int(input())
for i in range(N):
    s=1
    n=int(input())
    for i in range(1,n+1):
        s=1/(1+s)
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# THIẾT KẾ LOGO

n=int(input())
print('*')
for i in range(0,n-2):
    print('*',end='')
    print(i*' ',end='')
    print('*',)
print((2*n-1)*'*')

cach=0
for j in range(n-1,1,-1):
    print((' '*n)+(cach*' '),end='')
    cach=cach+1
    print('*',end='')
    print(((j-2)*' ')+'*')
print((2*n-2)*' '+'*')
# =============================================================================================================================================
# TỔNG TỪ A ĐẾN B

T=int(input())
l=[int(x) for x in input().split()]
k=int(input())
for i in range(k):
    a,b=(int(c) for c in input().split())
    s=0
    for j in range(a,b+1):
        s=s+l[j-1]
    print(s)
# =============================================================================================================================================
# TỔNG CÁC SỐ LẺ

l,r=(int(x) for x in input().split())
s=0
for i in range(l,r+1):
    if i%2!=0:
        s=s+i
print(s)
# =============================================================================================================================================
# BẮT TAY

n=int(input())
if n==1:
    print(0)
else:
    s=1
    for i in range(1,n):
        s=s*i
    print(s)
# =============================================================================================================================================
# KÍ TỰ MỚI

str=input()
print(str.lower())
# =============================================================================================================================================
# HOÀN THÀNH CÂU LỆNH

d,m,y=(int(x) for x in input().split())
print("users setClock \%d\%d\%d" % (m,d,y))
# =============================================================================================================================================
# CHUẨN HÓA XẤU

str=input()
kq=''
kt=str.strip(' ')
for i in range(0,len(str)):
    if (str[i]!=' ') or (str[i]==' ' and str[i+1]!=' '):
        kq=kq+str[i]
print(kq)
# =============================================================================================================================================
# ROBOT NHẶT CHỮ

str=input()
kq=''
for i in str:
    if i not in kq:
        kq=kq+i
print(kq)
# =============================================================================================================================================
# BÉ HỌC TIẾNG ANH

str=input()
kq=''
kt=str.strip(' ')
for i in range(0,len(str)):
    if (str[i]!=' ') or (str[i]==' ' and str[i+1]!=' '):
        kq=kq+str[i]
dem=1
for j in kq:
    if j==' ':
        dem=dem+1
print(dem)
# =============================================================================================================================================
# MẬT KHẨU AN TOÀN

def min(a,b):
    min=a
    if min>b:
        min=b
    return min
def max(a,b):
    max=a
    if max<b:
        max=b
    return max
n=int(input())
for i in range(n):
    str=input()
    s=min(5,max(len(str)-5,0))
    thuong=0
    hoa=0
    so=0
    for j in str:
        if j.isupper():
            hoa=hoa+1
        elif j.islower():
            thuong=thuong+1
        elif j.isnumeric():
            so=so+1
    if (hoa!=0 and thuong==0 and so==0) or (hoa==0 and thuong!=0 and so==0) or (hoa==0 and thuong==0 and so!=0):
        s=s+1
    elif (hoa!=0 and thuong!=0 and so==0) or (hoa==0 and thuong!=0 and so!=0) or (hoa!=0 and thuong==0 and so!=0):
        s=s+2
    elif (hoa!=0 and thuong!=0 and so!=0):
        s=s+5
    print(s)
# =============================================================================================================================================
# ĐẾM TỪ VIẾT HOA

str=input()
dem=0
if str.isupper():
    print(1)
elif str.islower():
    print(0)
else:
    for i in range(len(str)):
        if str[i].isupper() and str[i+1].islower():
            dem=dem+1
    print(dem)
# =============================================================================================================================================
# ĐẾM SỐ

str=input()
dem=0
for i in range(len(str)):
    if str[i].isnumeric() and str[i+1].isalpha():
        dem=dem+1
print(dem)
# =============================================================================================================================================
# ĐỐ CHỮ

str=input()
snt=[]
for x in range(2,len(str)+1):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        snt.append(x)
for i in str:
    if str.index(i) in snt:
        str=str[:str.index(i)]+'*'+str[str.index(i)+1:]
print(str)
# =============================================================================================================================================
# ĐẾM SỐ ÂM DƯƠNG TRONG MẢNG

n=int(input())
L=[int(x) for x in input().split()]
A=[]
D=[]
for i in L:
    if i<0:
        A.append(i)
    elif i>0:
        D.append(i)
print(len(A),len(D))
# =============================================================================================================================================
# ĐẾM TỪ

str=input()
kt=str.strip('.')
dem=1
for i in kt:
    if i=='.':
        dem=dem+1
print(dem)
# =============================================================================================================================================
# GHÉP TÊN THUỐC

str=list(input())
print(len(set(str)))
# =============================================================================================================================================
# XIN CHÀO

str=input()
mau='hello'
dem=0
for i in str:
    if dem==5:
        break
    if i==mau[dem]:
        dem=dem+1
if dem==5:
    print('YES')
else:
    print('NO')    
# =============================================================================================================================================
# TÍNH ĐIỂM SỐ

str=input()
diem=0
tong=0
for i in str:
    if i=='C':
        diem=diem+1
        tong=tong+diem
    if i=='N':
        diem=0
print(tong)
# =============================================================================================================================================
# SO SÁNH CHUỖI

m,n=(int(x) for x in input().split())
a=int(m*str(n))
b=int(n*str(m))
if a>=b:
    print(a)
else:
    print(b)
# =============================================================================================================================================
# LŨY THỪA CỦA CHUỖI

mau=input()
kt=input()
n=int(input())
str=''
for i in range(n):
    str=str+mau
if str==kt:
    print('YES')
else:
    print('NO')
# =============================================================================================================================================
# THƠ HAIKU

str=input()
inkq=''
for i in str:
    if i!=',':
        inkq=inkq+i
    else:
        inkq=inkq+' '
print(inkq)
# =============================================================================================================================================
# TÌM SỐ LỚN NHẤT TRONG XÂU

import re
n = input()
kq = re.findall("\d+", n)
max=int(kq[0])
for i in range(len(kq)):
    if max<int(kq[i]):
        max=int(kq[i])
print(max)

# =============================================================================================================================================
# XUẤT KÍ TỰ (BẢN DỄ)

str=input()
kt=sorted(str)
so=''
trong=' '
for i in kt:
    if i.isnumeric():
        so=so+i
for j in kt:
    if j not in so:
        if j not in trong:
            print('%s:%d'%(j,str.count(j)))
# =============================================================================================================================================
# ĐỊA ĐIỂM HỌP MẶT

n,chu=input().split()
for i in range(int(n)):
    str=input()
    if chu not in str:
        print(str)
# =============================================================================================================================================
T=int(input())
for i in range(T):
    str=input()
    n=int(input())
    kt=list(str).reverse()
    nguoc=''
    for i in kt:
        nguoc=nguoc+i
    if str==nguoc:
        print('YES')
    else:
        print('NO')
# =============================================================================================================================================
# CHỮ SỐ TẬN CÙNG CỦA 2^n

n=int(input())
kq=2**n
str=str(kq)
print(str[-1])
# =============================================================================================================================================
# TRÙNG KHOẢNG

a,b,c,d=(int(x) for x in input().split())
M=[int(i)for i in range(a,b+1)]
N=[int(j) for j in range(c,d+1)]
for y in M:
    if y in N:
        print('YES')
else:
    print('NO')
# =============================================================================================================================================
# IN MẢNG 2 CHIỀU DẠNG BẢNG

a,b=(int(x) for x in input().split())
L=[int(y) for y in input().split()]
cot=0
for i in L:
    cot=cot+1
    print(i,end=' ')
    if cot%b==0:
        print(sep='')
# =============================================================================================================================================
# TÍNH TỔNG CÁC HÀNG CÓ CHỈ SỐ LẺ

a,b=(int(x) for x in input().split())
L=[int(y) for y in input().split()]
kt=[]
s=0
dem=0
for i in L:
    kt.append(i)
    dem=dem+1
    if dem%b==0 and (dem/b)%2==0:
        for j in range(1,b+1):
            s=s+kt[-j]
print(s)
# =============================================================================================================================================
# TÍNH TỔNG ĐƯỜNG CHÉO CHÍNH

n=int(input())
i=0
L=[int(x) for x in input().split()]
s=0
while i<n:
    idx=n*i+i
    i=i+1
    s=s+L[idx]
print(s)
# =============================================================================================================================================
# SẮP XẾP MA TRẬN 1

m,n,i=(int(x) for x in input().split())
L=[int(y) for y in input().split()]
kq=[]
sx=[]
if i==1:
    j=0
    while j<n:
        sx.append(L[j])
        j=j+1
    them=sorted(sx)
    for b in them:
        kq.append(b)
    for c in range(n*(i-1)+n,m*n):
        kq.append(L[c])
elif i==m:
    for a in range(0,n*(i-1)):
        kq.append(L[a])
    j=0
    while j<n:
        sx.append(L[n*(i-1)+j])
        j=j+1
    them=sorted(sx)
    for b in them:
        kq.append(b)
else:
    for a in range(0,n*(i-1)):
        kq.append(L[a])
    j=0
    while j<n:
        sx.append(L[n*(i-1)+j])
        j=j+1
    them=sorted(sx)
    for b in them:
        kq.append(b)
    for c in range(n*(i-1)+n,m*n):
        kq.append(L[c])
dem=0
for d in kq:
    print(d,end=' ')
    dem=dem+1
    if dem%n==0:
        print(sep='')
# =============================================================================================================================================
# SỐ CẶP BẰNG NHAU 1

n=int(input())
L=[int(x) for x in input().split()]
dem=0
for i in range(n-1):
    if L[i]==L[i+1]:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# TÌM SỐ CHÍNH PHƯƠNG TRONG MA TRẬN

import math

m,n=(int(x) for x in input().split())
L=[]
for i in range(m):
    L=L+[int(y) for y in input().split()]
kq=[]
for j in L:
    if (int(math.sqrt(j)))**2==j:
        if i not in kq:
            kq.append(j)
kt=sorted(kq)
if len(kt)==0:
    print('NOT FOUND')
else:
    for k in kt:
        print(k,end=' ')
# =============================================================================================================================================
# TÍNH GIAI THỪA 2

n=int(input())
L=[int(x) for x in input().split()]
for i in L:
    gt=1
    for j in range(1,i+1):
        gt=gt*j
    print(gt)
# =============================================================================================================================================
# SẮP XẾP MA TRẬN 2

m,n,i=(int(x) for x in input().split())
L=[int(y) for y in input().split()]
sx=[]
kq=[]
for a in range(m):
    sx.append(L[n*a+(i-1)])
them=sorted(sx)
if i==1:
    for b in range(m):
        kq.append(them[b])
        for c in range(1,n):
            kq.append(L[n*b+c])
elif i==n:
    for b in range(m):
        for c in range(n-1):
            kq.append(L[n*b+c])
        kq.append(them[b])
else:
    for b in range(m):
        for c in range(0,i-1):
            kq.append(L[n*b+c])
        kq.append(them[b])
        for d in range(i,n):
            kq.append(L[n*b+d])
dem=0
for inkq in kq:
    print(inkq,end=' ')
    dem=dem+1
    if dem%n==0:
        print(sep='')
# =============================================================================================================================================
# CẶP ĐÔI HOÀN HẢO

n=int(input())
L=[int(x) for x in input().split()]
kt=sorted(L)
ss=[]
for i in range(len(kt)-1):
    h=kt[i+1]-kt[i]
    ss.append(h)
kq=sorted(ss)
print(kq[0])
# =============================================================================================================================================
# ĐỘI TÌNH NGHUYỆN VIÊN

n=int(input())
L=[int(x) for x in input().split()]
ss=[]
for i in L:
    dem=L.count(i)
    ss.append(dem)
kq=sorted(ss)
print(kq[-1])
# =============================================================================================================================================
# HÌNH PHẠT

n=int(input())
L=[int(x) for x in input().split()]
s=0
for i in L:
    if i==1:
        s=s+1
    elif i==2:
        s=s-1
if s<0:
    s=-s
print(s)
# =============================================================================================================================================
# ĐẾM TẦN SUẤT MẢNG

n=int(input())
L=[int(x) for x in input().split()]
kt=list(dict.fromkeys(L))
print(len(kt))
for i in kt:
    print(i,end=' ')
    print(L.count(i))
# =============================================================================================================================================
# SỐ BÉ NHẤT VÀ SỐ LỚN NHẤT

n=int(input())
L=[int(x) for x in input().split()]
print(min(L),L.index(min(L))+1,end=' ')
print(max(L),L.index(max(L))+1)
# =============================================================================================================================================
# SỐ CẶP BẰNG NHAU 2

n=int(input())
L=[int(x) for x in input().split()]
kt=sorted(L)
dem=0
for i in range(len(kt)-1):
    if kt[i]==kt[i+1]:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# PHẦN TỬ XUẤT HIỆN NHIỀU NHẤT

n=int(input())
L=[int(x) for x in input().split()]
sx=sorted(L)
inkq=[]
max=0
for i in sx:
    dem=L.count(i)
    if max<dem:
        max=dem
        inkq.append(i)
print(inkq[-1],max)
# =============================================================================================================================================
# BÀI TẬP MẢNG 1 CHIỀU TỔNG HỢP

n=int(input())
L=[int(x) for x in input().split()]
chan=[]
duong=[]
s=0
for i in L:
    s=s+i
    if i%2==0:
        chan.append(i)
    if i>0:
        duong.append(i)
print(s,len(chan),end=' ')
if len(duong)==0:
    print(0)
else:
    print(duong[-1])
# =============================================================================================================================================
# TRAO GIẢI

n=int(input())
L=[int(x) for x in input().split()]
sx=sorted(L)
inkq=[]
dem=0
for i in range(int(n/2)):
    dem=dem+1
    inkq.append(sx[-1])
    sx.remove(sx[-1])
dem=dem+sx.count(inkq[-1])
print(dem)
# =============================================================================================================================================
# SỐ ĐỘC THÂN

n=int(input())
L=[int(x) for x in input().split()]
kt=sorted(L)
dem=0
for i in kt:
    if L.count(i)==1:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# LINH KIỆN ĐIỆN TỬ

n=int(input())
L=[int(x) for x in input().split()]
kt=sorted(L)
gh=[int(y) for y in range(kt[0],kt[-1]+1)]
dem=0
for i in gh:
    if i not in kt:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# HOÁN VỊ VÒNG TRÒN
# ------------------

a,b=(int(x) for x in input().split())
L=[int(y) for y in input().split()]
kq=[]
for i in L[b:]:
    kq.append(i)
for j in L[:b]:
    kq.append(j)
for k in kq:
    print(k,end=' ')
# =============================================================================================================================================
# SẮP XẾP MẢNG KIỂU MỚI
# ---------------------

n=int(input())
L=[int(x) for x in input().split()]
kq=[]
for i in L:
    so=list(str(i))
    so.sort()
    num=0
    mu=0
    for j in so:
        num=num+(int(j)*(10**mu))
        mu=mu+1
    kq.append(num)
kq.sort(reverse=True)
for k in kq:
    print(k,end=' ')
# =============================================================================================================================================
# SỐ LỚN THỨ 3
# ------------

T=int(input())
for i in range(T):
    n=int(input())
    L=[int(x) for x in input().split()]
    sx=list(set(L))
    if len(sx)<3:
        print('Khong the tim duoc!')
    else:
        print(L[2],L.index(L[2])+1)
# =============================================================================================================================================
# GỘP MẢNG
# --------

n=int(input())
A=[int(x) for x in input().split()]
B=[int(y) for y in input().split()]
C=list(set(A+B))
for i in C:
    print(i,end=' ')
# =============================================================================================================================================
# LỜI CHÚC TẾT
# ------------

n=int(input())
L=[]
for i in range(n):
    chuc=input().upper()
    if chuc not in L:
        L.append(chuc)
print(len(chuc))
# =============================================================================================================================================
# TỔNG VÀ HIỆU
# ------------

t,h=int(input())
a=(t+h)/2
b=(t-h)/2
print(a,b)
# =============================================================================================================================================
# GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT
# -----------------------------

a,b,c,d,e,f=map(int,input().split())
D = a*e - b*d
Dx = c*e - b*f
Dy = a*f - c*d
if D==0 and Dx==0:
    print("VOSONGHIEM")
elif D==0 and Dx!=0:
    print("VONGHIEM")
elif D!=0:
    x=Dx/D
    y=(c-a*x)/b
    print("{:.2f}".format(x),end=' ')
    print("{:.2f}".format(y))
# =============================================================================================================================================
# TÌM ƯỚC LẺ LỚN NHÂT
# -------------------

n=int(input())
for i in range(n):
    so=int(input())
    uoc=[]
    for j in range(2,so+1):
        if so%j==0:
            uoc.append(j)
    uocle=[]
    for k in uoc:
        if k!=so and k%2!=0:
            uocle.append(k)
    if len(uocle)==0:
        print(1)
    else:
        uocle.sort(reverse=True)
        print(uocle[0])
# =============================================================================================================================================
# TÍNH S=1+2+3+4+....+N
# ----------------------

n=int(input())
s=(n*(n+1))/2
print(s)
# =============================================================================================================================================
# MÁY TÍNH CẦM TAY (BẢN DỄ)
# -------------------------


# =============================================================================================================================================
# GIẢI PHƯƠNG TRÌNH
# ------------------

import math

a,b,c=(int(x) for x in input().split())
inkq=[]
if a==0:
    if b==0:
        if c==0:
            print('INF')
        else:
            print('NO')
    else:
        kq=round(-c/b,2)
        inkq.append(kq)
else:
    dental=b*b-4*a*c
    if dental<0:
        print('NO')
    elif dental==0:
        inkq.append(round(-b/(2*a),2))
    else:
        inkq.append(round((-b+math.sqrt(dental))/(2*a),2))
        inkq.append(round((-b-math.sqrt(dental))/(2*a),2))
inkq.sort()
if len(inkq)==0:
    for i in inkq:
        print(i,i)
else:
    for i in inkq:
        if i==-0:
            i=-i
        print("{:.2f}".format(i),end=' ')
# =============================================================================================================================================
# MÁY TÍNH BỎ TÚI
# ---------------

a,dau,b=(x for x in input().split())
a=float(a)
b=float(b)
if dau=='+':
    if -10000<=a+b<=10000:
        print("{:.2f}".format(a+b))
    else:
        print('Math Error')
elif dau=='-':
    if -10000<=a-b<=10000:
        print("{:.2f}".format(a-b))
    else:
        print('Math Error')
elif dau=='*':
    if -10000<=a-b<=10000:
        print("{:.2f}".format(a*b),end=' ')
    else:
        print('Math Error')
elif dau=='/':
    if b==0:
        print('Math Error')
    else:
        if -10000<=a/b<=10000:
            print("{:.2f}".format(a/b),end=' ')
        else:
            print('Math Error')
# =============================================================================================================================================
# TÍNH TỔNG 1/2+1/3+...+1/N
# --------------------------

n=int(input())
s=0
for i in range(2,n+1):
    s=s+(1/i)
print("{:.4f}".format(s))
# =============================================================================================================================================
# TÍNH TỔNG S=X+X^2/2!+X^3/3!+....+X^N/N!
# ---------------------------------------

x,n=(int(x) for x in input().split())
s=x
for j in range(2,n+1):
    gt=1
    for i in range(2,j+1):
        gt=gt*i
        s=s+((x**i)/gt)
print("{:.2f}".format(s))
# =============================================================================================================================================
# TÍNH TRUNG BÌNH CỘNG CỦA MẢNG
# ------------------------------

n=int(input())
L=[int(x) for x in input().split()]
s=0
dem=0
for i in L:
    if i%2!=0:
        s=s+i
        dem=dem+1
tbc=(s/dem)
print("{:.4f}".format(tbc))
# # =============================================================================================================================================
# SUM4
# -----

n=int(input())
for i in range(n):
    so=int(input())
    s=2*(1-1/(so+1))
    print("{:.8f}".format(s))
# =============================================================================================================================================
# SUM5 - TÍNH TỔNG NGHỊCH ĐẢO
# ----------------------------

T=int(input())
for i in range(T):
    n=int(input())
    s=0
    for j in range(1,n+1):
        s=s+(1/j)
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# MÁY TÍNH CẦM TAY (BẢN DỄ)
# -------------------------

import math

def can(a):
    return math.sqrt(a)
def giaithua(a):
    gt=1
    for i in range(1,a):
        gt=gt*i
    return gt

a=int(input())
dau=input()
b=int(input())
if dau=='+':
    print(a+b)
elif dau=='-':
    print(a-b)
elif dau=='*':
    print(a*b)
elif dau=='/':
    if b!=0:
        print(a/b)
elif dau=='!+':
    print(giaithua(a)+b)
elif dau=='!-':
    print(giaithua(a)-b)
elif dau=='!*':
    print(giaithua(a)*b)
elif dau=='!/':
    if b!=0:
        print(giaithua(a)/b)
elif dau=='sqrt+':
    print(can(a)+b)
elif dau=='sqrt-':
    print(can(a)-b)
elif dau=='sqrt*':
    print(can(a)*b)
elif dau=='sqrt/':
    if b!=0:
        print(can(a)/b)
# =============================================================================================================================================
# TÌM BỘ 3 HOÀN HẢO
# ---------

n=int(input())
L=[int(x) for x in input().split()]
L.sort()
kq=[L[0]*L[1]*L[n-1],L[n-1]*L[n-2]*L[n-3]]
print(max(kq))
# =============================================================================================================================================
# LẠI LÀ ĐI TÌM CẶP ĐÔI
# ---------------------

n=int(input())
L=[int(x) for x in input().split()]
L.sort()
kq=[L[0]*L[1],L[n-1]*L[n-2]]
print(max(kq))
# =============================================================================================================================================
# PHÉP TÍNH XOR TRÊN DÃY NHỊ PHÂN
# -------------------------------

A,B=input().split()
kq=''
for i in range(len(A)):
    if A[i]==B[i]:
        kq=kq+'0'
    else:
        kq=kq+'1'
print(kq.lstrip('0'))
# =============================================================================================================================================
# ĐI TÌM CẶP ĐÔI
# --------------

n=int(input())
L=[int(x) for x in input().split()]
max=0
for i in range(-1,n-1):
    sum=L[i]+L[i+1]
    if sum>=max:
        max=sum
        a=L[i]
        b=L[i+1]
print(a,b)
# =============================================================================================================================================
# TÌM SỐ NGUYÊN TỐ TRONG MẢNG
# ----------------------------

import math

n=int(input())
L=[int(x) for x in input().split()]
snt=[]
for i in L:
    if i>1:
        if i==2:
            snt.append(i)
        else:
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    break
            else:
                snt.append(i)
SNT=sorted(set(snt))
for y in SNT:
    print(y,end=' ')
# # =============================================================================================================================================
# BIẾN ĐỔI MẢNG MỘT CHIỀU
# -----------------------

n = int(input())
l = [int(x) for x in input().split(" ")]
for i in range(0, n):
    if i % 2 != 0:
        if i >= n - 1:
            l[i] = l[i] + l[i-1]
        else:
            l[i] = l[i] + abs(l[i+1] - l[i-1])
print(' '.join([str(y) for y in l]))
# =============================================================================================================================================
# VẪN LÀ TÌM KIẾM TRONG MẢNG
# ---------------------

L=[int(x) for x in input().split()]
kt=L[:10]
ch=L[10]
if ch in kt:
    for i in range(0,10):
        if kt[i]==ch:
            print(i+1,end=' ')
else:
    print(-1)
# =============================================================================================================================================
# TÌM CHỈ SỐ MẢNG LỚN NHẤT
# ------------------------

n=int(input())
L=[int(x) for x in input().split()]
kt=L[:n]
kq=max(L)
for i in range(n):
    if kq==kt[i]:
        so=i
print(so)
# =============================================================================================================================================
# VL19 - IN RA CÁC SỐ CHIA HẾT CHO 3 - CHƯA AC
# ---------------------------------

a,b=(int(x) for x in input().split())
if a<b:
    for i in range(b-1,a,-1):
        if i%3==0:
            print(i,end=' ')
# =============================================================================================================================================
# VL09
# ----

def gt(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    return gt
x,n=(int(x) for x in input().split())
s=x
for i in range(2,n+1):
    s=s+((x**i)/(gt(i)))
print('{:.2f}'.format(s))
# =============================================================================================================================================
# VL07 - TÍNH TỔ HỢP

def gt(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    return gt
n,k=(int(x) for x in input().split())
print(int((gt(n))/((gt(k))*gt(n-k))))
# =============================================================================================================================================
# GIẢI PHƯƠNG TRÌNH
# --------------------

import math
a,b,c=(int(x) for x in input().split())
if a==0:
    if b==0:
        if c==0:
            print('INF')
        else:
            print('NO')
    else:
        print('{:.2f}'.format(-c/b))
else:
    dental=(b*b)-(4*a*c)
    if dental<0:
        print('NO')
    elif dental==0:
        print('{:.2f}'.format(-b/(2*a)))
    else:
        kq=[]
        kq.append('{:.2f}'.format((-b+math.sqrt(dental))/(2*a)))
        kq.append('{:.2f}'.format((-b-math.sqrt(dental))/(2*a)))
        kq.sort()
        for i in kq:
            print(i,end=' ')
# =============================================================================================================================================
# TÍNH TỔNG ƯỚC 2 - AC 8/10
# ----------------

a,b=(int(x) for x in input().split())
s=0
if a<=b:
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            s=s+i
    print(s)
else:
    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            s=s+i
    print(s)
# =============================================================================================================================================
# TÍNH TỔNG ƯỚC 1
# ---------------

a,b=(int(x) for x in input().split())
s=0
for i in range(2,a+1):
    if a%i==0 and b%i!=0:
        s=s+i
print(s)
# =============================================================================================================================================
# TỔNG CÁC CHỮ SỐ
# ---------------

T=int(input())
for i in range(T):
    n=input()
    s=0
    for j in n:
        s=s+int(j)
    print(s)
# =============================================================================================================================================
# DEMTU - BÉ HỌC TIẾNG ANH
# ------------------------

s = input()
print(len(s.split()))
# =============================================================================================================================================
# TÍNH TỔNG CÁC ƯỚC - AC 2/3
# -----------------

T=int(input())
for i in range(T):
    n=int(input())
    s=1+n
    for i in range(2,n):
        if n%i==0:
            s=s+i
    print(s)
# =============================================================================================================================================
# TÍNH TỔNG NGHỊCH ĐẢO
# --------------------

T=int(input())
for j in range(T):
    n=int(input())
    s=0
    i=1
    while i<=n:
        s=s+(1/i)
        i=i+1
    print('{:.5f}'.format(s))
# =============================================================================================================================================
# SỐ LƯỢNG SỐ
# -----------

print(len([str(int(x)) for x in input().split()]))
# =============================================================================================================================================
# CHUẨN HÓA
# ---------

T=int(input())
for i in range(T):
    str=input()
    L=str.split(' ')
    while L.count('')>0:
        L.remove('')
    print(' '.join(L))
# =============================================================================================================================================
# SO SÁNH 2 LŨY THỪA
# ------------------

T=int(input())
for i in range(T):
    a,b,c=(int(x) for x in input().split())
    if c==0:
        print('=')
    else:
        if c%2==0:
            if a<0:
                a=-a
            if b<0:
                b=-b
        if a>b:
            print('>')
        elif a==b:
            print('=')
        else:
            print('<')
# =============================================================================================================================================
# TÍNH LŨY THỪA 1
# ---------------

a,n=(int(x) for x in input().split())
if n%2==0:
    lt=(a**(n/2))*(a**(n/2))
else:
    lt=(a**(n//2))*(a**(n//2))*a
print(int((lt)%(10**9+7)))
# =============================================================================================================================================
# TÌM SỐ CHÍNH PHƯƠNG TRONG MA TRẬN
# ---------------------------------

import math
m,n=(int(x) for x in input().split())
M=[]
kq=[]
for i in range(m):
    M=M+[int(y) for y in input().split()]
for j in M:
    if j==(int(math.sqrt(j)))**2:
        if j not in kq:
            kq.append(j)
kq.sort()
print(' '.join([str(k) for k in kq]))
# =============================================================================================================================================
# BÀI TOÁN HÌNH CHỮ NHẬT 1
# ------------------------

x1,y1,x2,y2,x,y=(int(i) for i in input().split())
if x1<x2 and y1<y2:
    if x1<x<x2 and y1<y<y2:
        print('YES')
    else:
        print('NO')
elif x1>x2 and y1>y2:
    if x2<x<x1 and y2<y<y1:
        print('YES')
    else:
        print('NO')
elif x1<x2 and y1>y2:
    if x1<x<x2 and y2<y<y1:
        print('YES')
    else:
        print('NO')
elif x1>x2 and y1<y2:
    if x2<x<x1 and y1<y<y2:
        print('YES')
    else:
        print('NO')
# ===============================================================================================================================
ax,ay,bx,by=(int(i) for i in input().split())
cx,cy,dx,dy=(int(j) for j in input().split())
def max4(a,b,c,d):
    return max(a,max(b,max(c,d)))
def min4(a,b,c,d):
    return min(a,min(b,min(c,d)))
D=abs(ax-bx)+abs(cx-dx)-(max4(ax,bx,cx,dx)+min4(ax,bx,cx,dx))
R=abs(ay-by)+abs(cy-dy)-(max4(ay,by,cy,dy)+min4(ay,by,cy,dy))
if D<0 or R<0:
    print(0)
elif D>0 and R>0:
    print(D*R)
# =============================================================================================================================================
# CHỒNG GẠCH

n=int(input())
a=[]
brick=0 # Đếm số gạch ban đầu, đặt là 0 vì chưa xếp
for i in range(n):
    a.append(int(input())) # Nhập độ cứng gạch vô
    a.sort() # Sắp xếp mảng gồm độ cứng gạch từ bé đến lớn
    b=a
    a=list(filter(lambda a:a!=0,a)) #Loại bỏ gạch có giá trị độ cứng là 0, giảm vòng lặp và sẽ xử lý sau
    n=len(a)
    if n-max(a)>0:
        last=n-max(a)-1
    else:
        last=0 # Đặt điểm kết thúc vòng lặp
for i in range(n-1,last-1,-1): # Vòng lặp sẽ chạy từ viên cuối lên trên do đã sắp xếp
    if a[i]>=i-last: # i - last là số lượng viên gạch ở trên viên đang xét
        brick+=1
    else:
        last=i-a[i] # Nếu số lượng gạch lớn hơn sức bền thì thay đổi last để số gạch bằng đúng sức bền
        brick+=1
    if i-last <= 0:
        break
if 0 in b and last == 0: # Quay lại xử lý trường hợp có độ cứng là 0, thêm vô để đúng test 5 nhưng sai bài toán
    print(brick+2)
else:
    print(brick)
# *******************************************************************************************************************

lap=int(input())
L=[]
dem=0
for i in range(lap):
    L.append(int(input()))
    L.sort()
b=L
L=list(filter(lambda a:a!=0,L)) 
n=len(L)
if n-max(L)>0:
    last=n-max(L)-1
else:
    last=0
for i in range(n-1,last-1,-1):
    if L[i]>=i-last:
        dem+=1
    else:
        last=i-L[i]
        dem+=1
    if i-last <= 0:
        break
if 0 in b and last == 0:
    print(dem+2)
else:
    print(dem)
# =============================================================================================================================================
# PTIT064 - GỘP MẢNG

n=int(input())
A=[int(x) for x in input().split()]
B=[int(y) for y in input().split()]
C=[]
for i in range(n):
    C.append(A[i])
    C.append(B[i])
C.sort()
for j in C:
    print(j,end=' ')
# =============================================================================================================================================
# PTIT063 - SỐ VUI VẺ

import math

dem=0
l,r=(int(x) for x in input().split())
for i in range(l+1,r):
    j=int(math.sqrt(i))
    if j*j==i:
        dem=dem+1
print(dem)
# =============================================================================================================================================
# SUM5

T=int(input())
tong=[]
for i in range(T):
    tong.append(int(input()))
kq=[1]
s=1
for j in range(2,(max(tong)+1)):
    s=s+(1/j)
    kq.append(s)
for k in tong:
    print('{:.5f}'.format(kq[k-1]))
# =============================================================================================================================================
# SUM7

import math

T=int(input())
tong=[]
for i in range(T):
    tong.append(int(input()))
kq=[1]
s=1
for j in range(2,(max(tong)+1)):
    s=math.sqrt(s+j)
    kq.append(s)
for k in tong:
    print('{:.5f}'.format(kq[k-1]))
# =============================================================================================================================================
# ANGRY - GIÁO SƯ NỔI GIÂN

T=int(input())
for a in range(T):
    n,k=(int(x) for x in input().split())
    t=[int(x) for x in input().split()]
    dung=0
    tre=0
    for i in t:
        if i<=0:
            dung=dung+1
        else:
            tre=tre+1
    if dung<k:
        print('YES')
    else:
        print('NO')
# =============================================================================================================================================
# PTIT062 - SỐ LỚN THỨ 3

T=int(input())
for i in range(T):
    n=int(input())
    l=[int(x) for x in input().split()]
    L=l.copy()
    l=set(l)
    if len(l)<3:
        print('Khong the tim duoc!')
    else:
        for a in range(2):
            L.remove(max(L))
        print(max(L),end=' ')
        L.reverse()
        print(n-(L.index(max(L))))
# =============================================================================================================================================
# TKDBC - BẮN CUNG

n,u=(int(x) for x in input().split())
print(n//(u+1))
# =============================================================================================================================================
n=int(input())
A=[int(x) for x in input().split()]
B=[int(y) for y in input().split()]
if A.count(0)>B.count(0):
    print(2)
elif A.count(0)<B.count(0):
    print(1)
else:
    a=0
    b=0
    for i in A:
        a=a+i
    for j in B:
        b=b+j
    if a>b:
        print(2)
    elif a<B:
        print(1)
    else:
        print('Double Win')
# =============================================================================================================================================
# PTIT024 - ĐỐ CHỮ

str=input()
snt=[]
for x in range(2,len(str)):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        snt.append(x)
for i in snt:
    str=str[:i]+'*'+str[(i+1):]
print(str)
# =============================================================================================================================================
# PTIT033 - Số chia hết hay không?

n=int(input())
a,b=(int(x) for x in input().split())
if n%a==0 and n%b==0:
    print('Co, tat ca!')
elif n%a==0 and n%b!=0:
    print('Chi chia het cho '+str(a)+',')
elif n%a!=0 and n%b==0:
    print('Chi chia het cho '+str(b)+'.')
elif n%a!=0 and n%b!=0:
    print('Khong chia het cho so nao ca.')
# =============================================================================================================================================
# PTIT053 - SỐ MẠNH MẼ

l,r=(int(x) for x in input().split())
dem=0
for i in range(l+1,r+1):
    L=list(str(i))
    s=0
    for j in L:
        s=s+int(j)
    if s==2:
        dem=dem+1
    elif s>2:
        for k in range(2,s):
            if s%k==0:
                break
        else:
            dem=dem+1
print(dem)
# =============================================================================================================================================
# PTIT002 - TÌM ĐỊNH THỨC CỦA MA TRẬN VUÔNG

a,b,c=(int(x) for x in input().split())
d,e,f=(int(x) for x in input().split())
g,h,i=(int(x) for x in input().split())
s=(a*(e*i-f*h))-(b*(d*i-f*g))+(c*(d*h-e*g))
print(s)
# =============================================================================================================================================
# PTIT011 - MẬT MÃ!

import math

n=int(input())
# x*2+x-2n=0
dental=1+8*n
if dental<=0:
    print('NO')
else:
    x1=(-1+math.sqrt(dental))/(2)
    x2=(-1-math.sqrt(dental))/(2)
    if (x1%(int(x1))==0 and x1>0) or (x2%(int(x2))==0 and x2>0):
        print('YES')
    else:
        print('NO')
# =============================================================================================================================================
# PTIT020 - ĐÁNH THỨC RỒNG VÀNG

n=int(input())
str=input()
for i in range(2):
    str=str+str[-1]+str[0:(len(str)-1)]
print(str[n+1])
# =============================================================================================================================================
# PTIT025 - CUỘC THI!

n=int(input())
name=[]
for i in range(n):
    name=name+[input()]
t=[int(x) for x in input().split()]
l=[int(y) for y in input().split()]
c=[int(z) for z in input().split()]
kq=[]
for j in range(n):
    s=t[j]+l[j]+c[j]
    kq.append(s)
kqcao=max(kq)
chi_so=[kq.index(kqcao)]
while kq.count(kqcao)>1:
    vi_tri=kq.index(kqcao)
    kq=kq[:vi_tri]+[min(kq)]+kq[(vi_tri+1):]
    chi_so.append(kq.index(kqcao))
for so in chi_so:
    print(name[so],t[so],l[so],c[so])
# =============================================================================================================================================
# TRAOGIAI - TRAO GIẢI

n=int(input())
L=[int(x) for x in input().split()]
L.sort()
L.reverse()
kt=L[:(n//2)]
kt.sort()
l=L[(n//2):]
them=0
for i in l:
    if i==kt[0]:
        them=them+1
print(len(kt)+them)
# =============================================================================================================================================
# DATE1 - TRA CỨU NGÀY THÁNG

n,y=(int(x) for x in input().split())
if y%400==0 or (y%4==0 and y%100!=0):
    if 1<=n<=31:
        m=1
        d=n
    elif 32<=n<=60:
        m=2
        d=n-31
    elif 61<=n<=91:
        m=3
        d=n-60
    elif 92<=n<=121:
        m=4
        d=n-91
    elif 122<=n<=152:
        m=5
        d=n-121
    elif 153<=n<=182:
        m=6
        d=n-152
    elif 183<=n<=213:
        m=7
        d=n-182
    elif 214<=n<=244:
        m=8
        d=n-213
    elif 245<=n<=274:
        m=9
        d=n-244
    elif 275<=n<=305:
        m=10
        d=n-274
    elif 306<=n<=335:
        m=11
        d=n-305
    elif 336<=n<=366:
        m=12
        d=n-335
else:
    if 1<=n<=31:
        m=1
        d=n
    elif 32<=n<=59:
        m=2
        d=n-31
    elif 60<=n<=90:
        m=3
        d=n-59
    elif 91<=n<=120:
        m=4
        d=n-90
    elif 121<=n<=151:
        m=5
        d=n-120
    elif 152<=n<=181:
        m=6
        d=n-151
    elif 182<=n<=212:
        m=7
        d=n-181
    elif 213<=n<=243:
        m=8
        d=n-212
    elif 244<=n<=273:
        m=9
        d=n-243
    elif 274<=n<=304:
        m=10
        d=n-273
    elif 305<=n<=334:
        m=11
        d=n-304
    elif 335<=n<=365:
        m=12
        d=n-334
print(d,m)
# =============================================================================================================================================
# DCTDN1 - DÃY CON TĂNG DÀI NHẤT (BẢN DỄ)

n=int(input())
a=[]
l=[]
for so in range(n):
    a=a+[int(input())]
    l=l+[1]
for i in range(0,n):
    for j in range(0,i):
        if a[i]>a[j]:
            l[i]=max(l[i],l[j]+1)
print(max(l))
# =============================================================================================================================================
# BINARY - LIỆT KÊ CHUỖI NHỊ PHÂN

n=int(input())
for i in range(2**n):
    he2=bin(i)
    kq=(he2[2:])
    while len(kq)<n:
        kq='0'+kq
    print(kq)
# =============================================================================================================================================
# PTIT006 - MA TRẬN XOẮN ỐC 1

n=int(input())
l=[]
for i in range(n*n):
    l.append('l')
dem=1
h1=0
h2=n-1
c1=0
c2=n-1
while h1<=h2 and c1<=c2:
    for a in range(h1,h2+1):
        l[n*h1+a]=dem
        dem=dem+1
    h1=h1+1
    for b in range(h1,h2+1):
        l[n*b+c2]=dem
        dem=dem+1
    c2=c2-1
    if c1<=c2:
        for c in range(c2,c1-1,-1):
            l[n*h2+c]=dem
            dem=dem+1
        h2=h2-1
    if h1<=h2:
        for d in range(h2,h1-1,-1):
            l[n*d+c1]=dem
            dem=dem+1
        c1=c1+1
for i in range(n):
    for j in range(n):
        print(l[n*i+j],end=' ')
    print(sep='')
# =============================================================================================================================================
# RSPRIAL - MA TRẬN XOẮN ỐC 2

# Ngược

n,m=(int(x) for x in input().split())
l=[]
for i in range(n*m):
    l.append('l')
dem=1
h1=0
h2=n-1
c1=0
c2=m-1
while h1<=h2 and c1<=c2:
    for a in range(c1,c2+1):
        l[m*h1+a]=dem
        dem=dem+1
    h1=h1+1
    for b in range(h1,h2+1):
        l[m*b+c2]=dem
        dem=dem+1
    c2=c2-1
    if c1<=c2:
        for c in range(c2,c1-1,-1):
            l[m*h2+c]=dem
            dem=dem+1
        h2=h2-1
    if h1<=h2:
        for d in range(h2,h1-1,-1):
            l[m*d+c1]=dem
            dem=dem+1
        c1=c1+1
for i in range(n):
    for j in range(m):
        print(l[m*i+j],end=' ')
    print(sep='')

# GIẢI
n,m=(int(x) for x in input().split())
l=[]
for i in range(n):
    l=l+[int(x) for x in input().split()]
h1=0
h2=n-1
c1=0
c2=m-1
while h1<=h2 and c1<=c2:
    for a in range(c1,c2+1):
        print(l[m*h1+a],end=' ')
    h1=h1+1
    for b in range(h1,h2+1):
        print(l[m*b+c2],end=' ')
    c2=c2-1
    if c1<=c2:
        for c in range(c2,c1-1,-1):
            print(l[m*h2+c],end=' ')
        h2=h2-1
    if h1<=h2:
        for d in range(h2,h1-1,-1):
            print(l[m*d+c1],end=' ')
        c1=c1+1
# =============================================================================================================================================
# CSC - CẤP SỐ CỘNG

l=[int(x) for x in input().split()]
l.sort()
hieu=[]
for i in range(1,3):
    hieu.append(l[i]-l[i-1])
hieu=list(set(hieu))
if len(hieu)==1:
    print(l[-1]+hieu[0])
elif len(hieu)>1:
    du=[int(y) for y in range(min(l),max(l)+1,hieu[0])]
    kq=[]
    for z in du:
        if z not in l:
            kq.append(z)
    print(max(kq))
# =============================================================================================================================================
# CUTTING - CẮT BÁNH SINH NHẬT

n,m=(int(x) for x in input().split())
nn=min(n,m) 
from math import gcd
rut=(int(gcd(n,m)))
print((int(n/rut)-1)+int(m/rut)-1)
# =============================================================================================================================================
# CNB2D - ĐỔI HỆ NHỊ PHÂN SANG THẬP PHÂN

T=int(input())
L=[]
kq=[]
for x in range(T):
    y=input()
    l=list(y)
    mu=len(l)-1
    s=0
    for i in l:
        s=s+(int(i)*(2**mu))
        mu=mu-1
    kq.append(s)
for z in kq:
    print(z)
# =============================================================================================================================================
# CVB2H - ĐỔI HỆ NHỊ PHÂN SANG HỆ CƠ SỐ 16

n = int(input())
a = []
for x in range(n):
    a.append(input())
for i in a:
    res = hex(int(i,2))
    res = res.upper()
    print(res.replace("0X",""))
# =============================================================================================================================================
# DANDAU - DÃY CON ĐAN DẤU DÀI NHẤT

n=int(input())
a=[]
dem=1
kt=1
for i in range(n):
    a.append(int(input()))
for j in range(1,n):
    if a[j]*a[j-1]<0:
        dem=dem+1
        kt=max(kt,dem)
    else:
        dem=1
if kt!=1:
    print(kt)
else:
    print(-1)
# =============================================================================================================================================
# DELARR - XÓA DÃY

n=int(input())
l=[int(x) for x in input().split()]
s=0
for so in l:
    s=s+so
l=sorted(l)
dau=0
cuoi=n-1
dem=0
while s!=0:
    if s>0:
        s=s-l[cuoi]
        cuoi=cuoi-1
    else:
        s=s-l[dau]
        dau=dau+1
    dem=dem+1
print(dem)
# =============================================================================================================================================
# DICHOI - CÔNG VIÊN 2049

n,u=(int(x) for x in input().split())
dem=0
while u>2*n:
    n=n*2
    dem=dem+1
print(u-n+dem)
# =============================================================================================================================================
l,r=(int(x) for x in input().split())

import math

print(math.floor(math.sqrt(r)-math.ceil(math.sqrt(l)))+1)
# =============================================================================================================================================
# ENCRYPT - MÃ HÓA MẬT KHẨU

n=input()
l=list(n)
tap_chu=[]
tap_so=[]
for i in l:
    if i.isalpha():
        tap_chu.append(i)
    else:
        tap_so.append(i)
s=0
for j in tap_so:
    s=s+int(j)
chuoi=''.join(tap_chu)+str(s)
print(chuoi)
# =============================================================================================================================================
# EVENSUM - TÍNH TỔNG CÁC SỐ Ở VỊ TRÍ CHẴN

n=int(input())
l=[int(x) for x in input().split()]
s=0
for i in range(1,len(l),2):
    s=s+l[i]
print(s)
# =============================================================================================================================================
# EZDICE - XÚC XẮC (BẢN DỄ)

n,m=(int(x) for x in input().split())
dich=int(input())
tuan=0
tu=0
while True:
    tuan=tuan+m
    tu=tu+n
    if tuan>dich:
        tuan=tuan-dich
    if tu>dich:
        tu=tu-dich
    if tuan==dich or tu==dich:
        break
if tuan==dich and tu!=dich:
    print(-1)
elif tu==dich and tuan!=dich:
    print(1)
elif tu==tuan==dich:
    print(0)
# =============================================================================================================================================
# FIBO1 - TÌM SỐ FIBONACCI THỨ N

T=int(input())
l=[int(x) for x in input().split()]
for i in l:
    if i==0 or i==1:
        print(1)
    else:
        kq=[1,1]
        for j in range(2,i+1):
            kq.append(kq[j-1]+kq[j-2])
        print(kq[i])
# =============================================================================================================================================
# BIGFINO - DÃY SỐ FIBONACCY

n=int(input())
if n==0 or n==1:
    print(1)
else:
    kq=[1,1]
    for j in range(2,n+1):
        kq.append((kq[j-1]+kq[j-2])%((10**9)+7))
    print(kq[n])
# =============================================================================================================================================
# FIBON - DÃY SỐ FIBONACCI

n=int(input())
kq=[1,1]
if n>1:
    for i in range(2,n):
        kq.append(kq[i-1]+kq[i-2])
for j in kq:
    print(j,end=' ')
# =============================================================================================================================================
# FIBO4 - FIBONACI

n=int(input())
if n==0 or n==1:
    print(1)
else:
    kq=[1,1]
    for j in range(2,n):
        kq.append((kq[j-1]+kq[j-2])%((10**6)+7))
    print(kq[n-1])
# =============================================================================================================================================
# HIPHA - HÌNH PHẠT

n=int(input())
l=[int(x) for x in input().split()]
d=0
for i in l:
    if i==1:
        d=d-1
    elif i==2:
        d=d+1
print(abs(d))
# =============================================================================================================================================
# KH_02 - LÀM TRÒN ĐIỂM

T=int(input())
for t in range(T):
    n=int(input())
    if n<38:
        print(n)
    else:
        if n%5<3:
            print(n)
        else:
            if n%10<5:
                print(((n//10)*10+5))
            else:
                print(((n//10)+1)*10)
# =============================================================================================================================================
# LC1 - BỘ B3 SỐ

n=int(input())
print(0,1,n-1)
# =============================================================================================================================================
# LDIGIT1 - CHỮ SỐ CUỐI CÙNG 1

n=int(input())
gt=1
for i in range(1,n+1):
    gt=gt*i
kq=str(gt)
kq=kq.strip('0')
print(kq[-1])
# =============================================================================================================================================
# LDIGIT2 - CHỮ SỐ CUỐI CÙNG 2

a,n=(int(x) for x in input().split())
lt=a
for i in range(1,n):
    lt=lt*a
kq=str(lt)
kq=kq.strip('0')
print(kq[-1])
# =============================================================================================================================================
# MARBLES - XẾP BI

n=int(input())
s=0
them=1
while s<n:
    s=s+them
    them=them+1
if s==n:
    print('Yes.')
else:
    print('No.')
# =============================================================================================================================================
# MOD - MOD

n=input()
n=n.strip('-')
while len(n)<3:
    n='0'+n
print(n[-3:])
# =============================================================================================================================================
# MSQUARE - CẮT HÌNH VUÔNG

a,b=(int(x) for x in input().split())
for i in range(a-b):
    print('* '*a)
for j in range(b):
    print('* '*(a-b))
# =============================================================================================================================================
# Chuoi 1

Str=input()
str=Str.lower()
STR=Str.upper()
print(str)
print(STR)
# =============================================================================================================================================
# # Chuoi 2

str=input()
chu=0
so=0
for i in str:
    if i.isalpha():
        chu=chu+1
    elif i.isnumeric():
        so=so+1
print('So chu cai:',chu)
print('So chu so:',so)
# =============================================================================================================================================

# =============================================================================================================================================

n=int(input())
if n>=2:
    i=2
    s=0
    while i<=n:
        s=s+i
        i=i+1
    print(s+2*n)
# =============================================================================================================================================
       
# =============================================================================================================================================
n=int(input())
s=0
for i in range(n+1):
    if i%2==0:
        s=s+(3*i+1)
    else:
        s=s-(3*i-1)
print(s)
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================
# =============================================================================================================================================