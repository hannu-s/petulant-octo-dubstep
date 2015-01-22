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
	st = struct.pack('fff', x,y,z)
	st += struct.pack('H', i)
	st += struct.pack('II', r,n)
	st += struct.pack('BBBBB', d, e, c, a, u)
	st += struct.pack('H', p)
	st += struct.pack('d', t)	
	f.write(st)

with open ('data.bin', 'rb') as f:
	data = f.read(37)
	value = struct.unpack('fff', data[:12])
	value += struct.unpack('H', data[12:14])
	value += struct.unpack('II', data[14:22])
	value += struct.unpack('BBBBB', data[22:27])
	value += struct.unpack('H', data[27:29])
	value += struct.unpack('d', data[29:37])
	
	print(value)
