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
		for b in self.__read_binary_chunk(path, 256):
			data.append(b)
		return data

	def __read_binary_chunk(self, path, chunk_size):
		with open(path, 'rb') as f:
			while True:
				chunk = f.read(chunk_size)
				if chunk:
					for b in chunk:
						yield b
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
		else:
			raise Exception('Unkown file type. File name has to end either as ".txt" or ".bin"')

	def __write_ascii(self, path, data):
		with open(path, 'w') as f:
			for line in (data):
				f.write(line)

	def set_encoding(self, coding):
		self.encoding = coding

	def __write_binary(self, path, data, fmt):
		with open(path, 'wb') as f:
			# B = unsigned char
			for line in data:
				for ch in line:
					b = int.from_bytes(ch.encode(self.encoding), 'little')#https://docs.python.org/3/library/stdtypes.html 				
					f.write(struct.pack(fmt, b)) # https://docs.python.org/3.4/library/struct.html
		
class CustomEncoder():
	"""docstring for CustomEncoder"""
	def ascii_to_custom(self, data):
		result = list()
		for line in data:
			for ch in line:
				b = ord(ch)
				if (b == 32): # 'space'
					b = 58
				elif (b == 46): # '.'
					b = 59
				elif (b == 10): # 'new line'
					b = 60
				b = b - 47 # ASCII '0' is 48 decimal
				result.append(b)
		return result, "custom"

	def custom_to_ascii(self, data):
		result = list()	
		for i in data:
			value = ''
			if (i == 11):
				value = chr(32)
			elif (i == 12):
				value = chr(46)
			elif (i == 13):
				value = chr(10)
			else:
				value = chr(i + 47)
			result.append(value)
		return result, "ascii"
