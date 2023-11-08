# import math
# a=int(input('a= '))
# b=int(input('b= '))
# c=int(input('c= '))
# s=(a+b+c)/2
# print('Dien tich = ',math.sqrt(s*(s-a)*(s-b)*(s-c)))
# s=int(input('Nhap so giay: '))
# h=s//(60*60)
# m=(s%(60**2))//60
# giay=(s%(60**2))%60
# print('Gio: ',h,' , phut: ',m,', giay"',giay)
import math
a=float(input('a='))
b=float(input('b='))
goc=int(input('goc='))
print('c= ',math.sqrt(a**2+b**2-2*a*b*math.cos((goc*math.pi)/180)))
# print(math.cos(math.pi))