import struct, sys
import timeit

range_value = 1000000
start = 0
stop = 0
x = int(398218)
y = int(678762)
z = int(132)
i = 16
r = 2 
c = 1 
a = 3 
u = 1 
p = 23 
t = 20933176.6295

''' LAS Writing '''

def write_las():
	with open ('2.las', 'wb') as f:
		start = timeit.default_timer()
		for asd in range(range_value):
			st = struct.pack('iii', x,y,z)
			st += struct.pack('H', i)
			st += struct.pack('B', r)
			st += struct.pack('BbB', c, a, u)
			st += struct.pack('H', p)
			st += struct.pack('d', t)
			f.write(st)
		stop = timeit.default_timer()
	with open ('wl.csv', 'a') as f:
		f.write(str(stop-start)+"\n")


''' LAS REAGIN '''
def read_las():
	with open ('2.las', 'rb') as f:
		start = timeit.default_timer()
		li = list()
		for i in range(1):
			data = f.read(28)
			
			value = struct.unpack('iii', data[:12])
			"""
			value += struct.unpack('H', data[12:14])
			value += struct.unpack('B', data[14:15])
			value += struct.unpack('BbB', data[15:18])
			value += struct.unpack('H', data[18:20])
			"""
			value += struct.unpack('HBBbBHd', data[12:28])
			
			#value += struct.unpack('d', data[20:28])
			
			
			
			li.append(value)
			print(li)
		stop = timeit.default_timer()
	#with open ('rl.csv', 'a') as f:
		#f.write(str(stop-start)+"\n")

def write_ascii():
	with open ('1.txt', 'w') as f:
		start = timeit.default_timer()
		for loop in range(range_value):
			line = str(x) + " " + str(y) + " " + str(z) + " " + str(i) + " " + str(r) + " " + str(c) + " " + str(a) + " " + str(u) + " " + str(p) + " " + str(t) + "\n"
			f.write(line)
		stop = timeit.default_timer()
	with open ('wa.csv', 'a') as f:
		f.write(str(stop-start)+"\n")


def read_ascii():
	with open ('1.txt', 'r') as f:
		start = timeit.default_timer()
		data = list()
		for loop in range(range_value):
			line = f.readline().replace("\n", "").split(" ")
			convert_line = list()
			for li in line:
				try:
					convert_line.append(int(li))
				except:
					convert_line.append(float(li))
			data.append(convert_line)
		stop = timeit.default_timer()
	with open ('ra.csv', 'a') as f:
		f.write(str(stop-start)+"\n")

if sys.argv[1] == "wl":
	write_las()
	
if sys.argv[1] == "rl":
	read_las()
	
if sys.argv[1] == "wa":
	write_ascii()
	
if sys.argv[1] == "ra":
	read_ascii()