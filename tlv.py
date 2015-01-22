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
	st += struct.pack('BB', r,n)
	st += struct.pack('??', d, e) 
	st += struct.pack('BBB', c, a, u)
	st += struct.pack('H', p)
	st += struct.pack('d', t)	
	f.write(st)

with open ('data.bin', 'rb') as f:
	data = f.read(31)
	value = struct.unpack('fff', data[:12])
	value += struct.unpack('H', data[12:14])
	value += struct.unpack('BB', data[14:16])
	value += struct.unpack('??', data[16:18])
	value += struct.unpack('BBB', data[18:21])
	value += struct.unpack('H', data[21:23])
	value += struct.unpack('d', data[23:31])
	
	print(value)
