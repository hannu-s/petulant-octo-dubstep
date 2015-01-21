import struct

x = 398218.87 
y = 6787626.831 
z = 132.66 
i = 16
r = 2 
n = 4 
d = 0 
e = 0
c = 1 
a = 3 
u = 1 
p = 23 
t = 20933176.629502

with open ('data.bin', 'wb') as f:
	st = struct.pack('III', int(x),int(y),int(z))
	st += struct.pack('HII', i,r,n)
	st += struct.pack('BBBBB', d, e, c, a, u)
	st += struct.pack('Hd', p,t)
	f.write(st)

with open ('data.bin', 'rb') as f:
	data = f.read(40)
	value = struct.unpack('IIIHIIBBBBBHd', data)
	print(value)
