n=int(input('So tien ban dau: '))
k=int(input('So thang gui: '))
T=float(input('Lai suat/ thang: '))
print('Voi so tien ban dau '+str(n)+', sau',k,'thang gui, lai suat '+str(T)+'/ thang')
print('Thi so tien nhan duoc cuoi ky la:',int(n*(1+k*T)))