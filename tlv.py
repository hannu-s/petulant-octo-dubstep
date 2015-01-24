import struct

x = int(398218.8700000)
y = int(6787626.83100000)
z = int(132.6600000)
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

''' LAS Writing '''

with open ('2.las', 'wb') as f:
	for asd in range(1000000):
		st = struct.pack('iii', x,y,z)
		st += struct.pack('H', i)
		st += struct.pack('BB', r,n)
		st += struct.pack('??', d, e) 
		st += struct.pack('BBB', c, a, u)
		st += struct.pack('H', p)
		st += struct.pack('d', t)	
		f.write(st)


''' LAS REAGIN '''

with open ('2.las', 'rb') as f:
	li = list()
	for i in range(1000000):
		data = f.read(31)
		value = struct.unpack('iii', data[:12])
		value += struct.unpack('H', data[12:14])
		value += struct.unpack('BB', data[14:16])
		value += struct.unpack('??', data[16:18])
		value += struct.unpack('BBB', data[18:21])
		value += struct.unpack('H', data[21:23])
		value += struct.unpack('d', data[23:31])
		li.append(value)


with open ('1.txt', 'w') as f:
	for loop in range(1000000):
		line = str(x) + " " + str(y) + " " + str(z) + " " + str(i) + " " + str(r) + " " + str(n) + " " + str(d) + " " + str(e) + " " + str(c) + " " + str(a) + " " + str(u) + " " + str(p) + " " + str(t) + "\n"
		f.write(line)



with open ('1.txt', 'r') as f:
	data = list()
	for loop in range(1000000):
		line = f.readline().replace("\n", "").split(" ")
		data.append(line)
