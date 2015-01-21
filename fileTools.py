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


class FileReader():
	encoding = 'ascii'
	"""docstring for FileReader"""
	def read(self, filePath):
		if FileType.is_file_name_bin(filePath):
			return self.__read_binary(filePath)
		elif FileType.is_file_name_txt(filePath):
			return self.__read_ascii(filePath)
		else:
			raise Exception('Unknown file type. File name has to end either as ".txt" or ".bin"')

	def __read_ascii(self, path):
		data = list()
		with open(path) as f:
		    for line in f:
		        data.append(line)
		return data

	def set_encoding(self, coding):
		self.encoding = coding

	def __read_binary(self, path):
		data = list()
		with open(path, 'rb') as f:
			data = f.read().decode(self.encoding)
		return data

class FileWriter():
	encoding = 'ascii'
	"""docstring for FileWriter"""
	def write(self, filePath, data, formatChar = 'B'):
		if FileType.is_file_name_bin(filePath):
			self.__write_binary(filePath, data, formatChar)
		elif FileType.is_file_name_txt(filePath):
			self.__write_ascii(filePath, data)
		else:
			raise Exception('Unkown file type. File name has to end either as ".txt" or ".bin"')

	def __write_ascii(self, path, data):
		with open(path, 'w') as f:
			for line in (data):
				f.write(line)

	def set_encoding(self, coding):
		self.encoding = coding

	def __write_binary(self, path, data, fmt):
		#bin(int.from_bytes(fileData.encode(), 'big')) #http://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa-python
		with open(path, 'wb') as f:
			# B = unsigned char
			for line in data:
				for ch in line:
					b = int.from_bytes(ch.encode(self.encoding), 'little')#https://docs.python.org/3/library/stdtypes.html 				
					f.write(struct.pack(fmt, b)) # https://docs.python.org/3.4/library/struct.html
		
