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
	las_chunk_size = 31
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
				parts = list()
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
					try:
						value = struct.unpack('fff', chunk[:12])
						value += struct.unpack('H', chunk[12:14])
						value += struct.unpack('BB', chunk[14:16])
						value += struct.unpack('BB', chunk[16:18])	#boolean flags
						value += struct.unpack('BBB', chunk[18:21])
						value += struct.unpack('H', chunk[21:23])
						value += struct.unpack('d', chunk[23:31])
						yield value
					except:
						raise Exception('Unable to las read file.')
				else:
					break

class FileWriter():
	"""docstring for FileWriter"""
	def write(self, file_path, data):
		if FileType.is_file_name_txt(file_path):
			self.__write_ascii(file_path, data)
		elif FileType.is_file_name_las(file_path):
			self.__write_las(file_path, data)
		else:
			raise Exception('Unkown file type. File name has to end either as ".txt" or ".las".')

	def write_as_type(self, file_path, data, fileType):
		if (fileType.lower() == 'txt'):
			return self.__write_ascii(file_path, data)
		elif (fileType.lower() == 'las'):
			return self.__write_las(file_path, data)
		else:
			raise Exception('Unknown file type. Supported types are: "txt" and "las".')
			
	def write_safe(self, file_path, data):
		if FileType.is_file_name_txt(file_path):
			self.__write_ascii(file_path, data)
		elif FileType.is_file_name_las(file_path):
			self.__write_las(file_path, data)
		else:
			raise Exception('Unkown file type. File name has to end either as ".txt" or ".las".')

	def write_as_type_safe(self, file_path, data, fileType):
		if (fileType.lower() == 'txt'):
			return self.__write_ascii(file_path, data)
		elif (fileType.lower() == 'las'):
			return self.__write_las(file_path, data)
		else:
			raise Exception('Unknown file type. Supported types are: "txt" and "las".')
			
	def __write_ascii(self, path, data):
		with open(path, 'w') as f:
			for line in (data):
				line = str(line).replace(',','').replace("'", "")
				line = line[1:-1] + '\n'
				f.write(line)
					
	def __write_las(self, path, data):
		with open (path, 'wb') as f:
			for line in data:
				st = self.__las_line_binary_builder(line)
				f.write(st)
				
	def __write_las_safe(self, path, data):
		with open (path, 'wb') as f:
			for line in data:
				self.__check_if_las_line_is_safe(line)
				st = self.__las_line_binary_builder(line)
				f.write(st)
					
	def __las_line_binary_builder(self, line):
		try:
			st = struct.pack('fff', float(line[0]), float(line[1]), float(line[2]))
			st += struct.pack('H', int(line[3]))
			st += struct.pack('BB', int(line[4]), int(line[5]))		# only 3 bits each allowed
			st += struct.pack('??', int(line[6]), int(line[7]))
			st += struct.pack('BBB', int(line[8]), int(line[9]), int(line[10]))
			st += struct.pack('H', int(line[11]))
			st += struct.pack('d', float(line[12]))
			return st
		except:
			raise Exception("Unable to write las file, line: " + ''.join(line))
			
	def __check_if_las_line_is_safe(self, line):
		if line[4] > 4 or line[4] < 0:
			raise Exception("'Return Number' doesn't have 3 bit value. Value: " + str(line[4]))
		if line[5] > 4 or line[5] < 0:
			raise Exception("'Scan Direction Flag' doesn't have 3 bit value. Value: " + str(line[5]))