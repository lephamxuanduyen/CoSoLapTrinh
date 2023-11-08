# import math
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# if a==0:
#     if b==0:
#         if c==0:
#             print('Phuong trinh co vo so nghiem.')
#         else:
#             print('Phuong trinh vo nghiem.')
#     else:
#         print('Phuong trinh co nghiem duy nhat: x=',-c/b)
# else:
#     denta=b**2-4*a*c
#     if denta<0:
#         print('Phuong trinh vo nghiem.')
#     if denta==0:
#         print('Phuong trinh co nghiem so kep: x1=x2=',-b/(2*a))
#     if denta>0:
#         print('Phuong trinh co 2 nghiem phan biet, x1=',(-b+math.sqrt(denta))/(2*a),'x2=',(-b+math.sqrt(denta))/(2*a))
# tieuthu=int(input('Tieu thu='))
# if tieuthu>=1 and tieuthu<=100:
#     dongia=tieuthu*550
#     phaitra=dongia*(1+0.1)
# if tieuthu>=101 and tieuthu<=150:
#     dongia=100*550+(tieuthu-100)*750
#     phaitra=dongia*(1+0.1)
# if tieuthu>=151 and tieuthu<=200:
#     dongia=100*550+50*750+(tieuthu-150)*950
#     phaitra=dongia*(1+0.1)
# if tieuthu>=201:
#     dongia=100*550+50*750+750*50+(tieuthu-200)*1350
#     phaitra=dongia*(1+0.1)
#     phaitra=tieuthu*dongia+tieuthu*dongia*0.01
# print('Phai tra='+str(float(phaitra)))