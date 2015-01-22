import struct

class FileType():
	"""docstring for FileType"""
	@staticmethod
	def is_file_name_bin(fileName):
		if fileName[-4:].lower() == '.bin':
			return True
		return False

	@staticmethod
	def is_file_name_txt(fileName):
		if fileName[-4:].lower() == '.txt':
			return True
		return False
		
	@staticmethod
	def is_file_name_las(fileName):
		if fileName[-4:].lower() == '.las':
			return True
		return False


class FileReader():
	encoding = 'ascii'
	las_chunk_size = 37
	"""docstring for FileReader"""
	def read(self, filePath):
		if FileType.is_file_name_bin(filePath):
			return self.__read_binary(filePath)
		elif FileType.is_file_name_txt(filePath):
			return self.__read_ascii(filePath)
		elif FileType.is_file_name_las(filePath):
			return self.__read_las(filePath)
		else:
			raise Exception('Unknown file type. File name has to end either as ".txt", ".las" or ".bin"')

	def read(self, filePath, fileType):
		if fileType.lower() == 'bin':
			return self.__read_binary(filePath)
		elif fileType.lower() == 'txt':
			return self.__read_ascii(filePath)
		elif fileType.lower() == 'las':
			return self.__read_las(filePath)
		else:
			raise Exception('Unknown file type. Supported types are: "txt", "las" and "bin"')
		
	def set_encoding(self, coding):
		self.encoding = coding
		
	def __read_ascii(self, path):
		data = list()
		with open(path) as f:
		    for line in f:
		        data.append(line)
		return data

	def __read_binary(self, path):
		data = list()
		with open(path, 'rb') as f:
			data = f.read().decode(self.encoding)
		return data
					
	def __read_las(self, path):
		data = list()
		for b in self.__read_las_binary_chunk(path):
			data.append(b)
		return data

	def __read_las_binary_chunk(self, path):
		with open(path, 'rb') as f:
			while True:
				chunk = f.read(self.las_chunk_size)
				if chunk:
					value = struct.unpack('fff', data[:12])
					value += struct.unpack('H', data[12:14])
					value += struct.unpack('II', data[14:22])
					value += struct.unpack('BBBBB', data[22:27])
					value += struct.unpack('H', data[27:29])
					value += struct.unpack('d', data[29:37])
					yield value
				else:
					break

class FileWriter():
	encoding = 'ascii'
	"""docstring for FileWriter"""
	def write(self, filePath, data, formatChar = 'B'):
		if FileType.is_file_name_bin(filePath):
			self.__write_binary(filePath, data, formatChar)
		elif FileType.is_file_name_txt(filePath):
			self.__write_ascii(filePath, data)
		elif FileType.is_file_name_las(filePath):
			self.__write_las(filePath, data)
		else:
			raise Exception('Unkown file type. File name has to end either as ".txt", ".las" or ".bin"')

	def write(self, filePath, fileType):
		if fileType.lower() == 'bin':
			return self.__write_binary(filePath)
		elif fileType.lower() == 'txt':
			return self.__write_ascii(filePath)
		elif fileType.lower() == 'las':
			return self.__write_las(filePath)
		else:
			raise Exception('Unknown file type. Supported types are: "txt", "las" and "bin"')
		
	def set_encoding(self, coding):
		self.encoding = coding
		
	def __write_ascii(self, path, data):
		with open(path, 'w') as f:
			for line in (data):
				f.write(line)

	def __write_binary(self, path, data, fmt):
		with open(path, 'wb') as f:
			# B = unsigned char
			for line in data:
				for ch in line:
					b = int.from_bytes(ch.encode(self.encoding), 'little')#https://docs.python.org/3/library/stdtypes.html 				
					f.write(struct.pack(fmt, b)) # https://docs.python.org/3.4/library/struct.html
					
	def __write_las(self, path, data):
		with open (path, 'wb') as f:
			st = struct.pack('fff', data[0], data[1], data[2])
			st += struct.pack('H', data[3])
			st += struct.pack('II', data[4], data[5])
			st += struct.pack('BBBBB', data[6], data[7], data[8], data[9], data[10])
			st += struct.pack('H', data[11])
			st += struct.pack('d', data[12])	
			f.write(st)