# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# max=a
# if max<b:
#     max=b
# if max<c:
#     max=c
# min=a
# if min>b:
#     min=b
# if min>c:
#     min=c
# print('SLN='+str(float(max)))
# print('SBN='+str(float(min)))
# somay=float(input('so may='))
# if somay>=5:
#     print('so tien='+str(float(somay)*450))
# else:
#     print('so tien='+str(float(somay)*500))
tieuthu=int(input('Tieu thu='))
if tieuthu>=1 and tieuthu<=100:
    dongia=tieuthu*550
    phaitra=dongia*(1+0.1)
if tieuthu>=101 and tieuthu<=150:
    dongia=100*550+(tieuthu-100)*750
    phaitra=dongia*(1+0.1)
if tieuthu>=151 and tieuthu<=200:
    dongia=100*550+50*750+(tieuthu-150)*950
    phaitra=dongia*(1+0.1)
if tieuthu>=201:
    dongia=100*550+50*750+750*50+(tieuthu-200)*1350
    phaitra=dongia*(1+0.1)
print('Phai tra='+str(round(phaitra)))