import struct

class FileType():
	"""docstring for FileType"""
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
	las_chunk_size = 37
	"""docstring for FileReader"""
	def read(self, filePath):
		if FileType.is_file_name_txt(filePath):
			return self.__read_ascii(filePath)
		elif FileType.is_file_name_las(filePath):
			return self.__read_las(filePath)
		else:
			raise Exception('Unknown file type. File name has to end either as ".txt" or ".las".')

	def read_as_type(self, filePath, fileType):
		if (fileType.lower() == 'txt'):
			return self.__read_ascii(filePath)
		elif (fileType.lower() == 'las'):
			return self.__read_las(filePath)
		else:
			raise Exception('Unknown file type. Supported types are: "txt" and "las".')
		
	def set_las_chunk_size(size):
		self.las_chunk_size = int(size)
		
	def __read_ascii(self, path):
		data = list()
		with open(path) as f:
			for line in f:
				line = line.replace('\n','')
				parts = line.split(' ')
				data.append(parts)
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
					value = struct.unpack('fff', chunk[:12])
					value += struct.unpack('H', chunk[12:14])
					value += struct.unpack('II', chunk[14:22])
					value += struct.unpack('BBBBB', chunk[22:27])
					value += struct.unpack('H', chunk[27:29])
					value += struct.unpack('d', chunk[29:37])
					yield value
				else:
					break

class FileWriter():
	"""docstring for FileWriter"""
	def write(self, filePath, data):
		if FileType.is_file_name_txt(filePath):
			self.__write_ascii(filePath, data)
		elif FileType.is_file_name_las(filePath):
			self.__write_las(filePath, data)
		else:
			raise Exception('Unkown file type. File name has to end either as ".txt" or ".las".')

	def write_as_type(self, filePath, data, fileType):
		if (fileType.lower() == 'txt'):
			return self.__write_ascii(filePath, data)
		elif (fileType.lower() == 'las'):
			return self.__write_las(filePath, data)
		else:
			raise Exception('Unknown file type. Supported types are: "txt" and "las".')
			
	def __write_ascii(self, path, data):
		with open(path, 'w') as f:
			print(data)
			for line in (data):
				line = str(line).replace(',','')
				line = line[1:-1] + '\n'
				f.write(line)
					
	def __write_las(self, path, data):
		with open (path, 'wb') as f:
			for line in data:
				st = struct.pack('fff', float(line[0]), float(line[1]), float(line[2]))
				st += struct.pack('H', int(line[3]))
				st += struct.pack('II', int(line[4]), int(line[5]))
				st += struct.pack('BBBBB', int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10]))
				st += struct.pack('H', int(line[11]))
				st += struct.pack('d', float(line[12]))
				f.write(st)