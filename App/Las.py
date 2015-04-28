import struct

#static helper class
class Converter():
	def convert(type, count):
		if (type == "char"):
			return Converter._loop("c", count)
		elif (type == "uchar"):
			return Converter._loop("B", count)
		elif (type == "ushort"):
			return Converter._loop("H", count)
		elif (type == "long"):
			return Converter._loop("l",count)
		elif (type == "ulong"):
			return Converter._loop("L", count)
		elif (type == "ulong long"):
			return Converter._loop("Q", count)
		elif (type == "double"):
			return Converter._loop("d", count)
		else:
			raise Exception("Invalid argument: " + type)
			
	def _loop(letter, count):
		result = ""
		for i in range(count):
			result += letter
		return result
	
#static helper class
class HeaderVariables():
	def get_default_struct_parameters():
		result = "<"
		result += Converter.convert("char", 4)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ulong", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("uchar", 8)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("char", 32)
		result += Converter.convert("char", 32)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ulong", 1)
		result += Converter.convert("ulong", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ulong", 1)
		result += Converter.convert("ulong", 5)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		result += Converter.convert("double", 1)
		return result
		
	def get_extended_format_3_struct_parameters():
		result = Converter.convert("ulong long", 1)
		return result
		
	def get_extended_format_4_struct_parameters():
		result = Converter.convert("ulong long", 1)
		result += Converter.convert("ulong", 1)
		result += Converter.convert("ulong long", 1)
		result += Converter.convert("ulong long", 15)
		return result
		
	def get_default_header_length():
		return 227
		
	def get_extended_format_3_length():
		return 8
		
	def get_extended_format_4_length():
		return 148

#static helper class
class VariableLengthRecordVariables():
	def get_length():
		return 54
	
#static helper class	
class PointDataRecordVariables():
	def get_format_1_struct_parameters():
		result = "<"
		result += Converter.convert("long", 1)
		result += Converter.convert("long", 1)
		result += Converter.convert("long", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("char", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("double", 1)
		return result
		
	def get_format_2_struct_parameters():
		result = "<"
		result += Converter.convert("long", 1)
		result += Converter.convert("long", 1)
		result += Converter.convert("long", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("char", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("uchar", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		result += Converter.convert("ushort", 1)
		return result
		
	def get_format_1_length():
		return 28
		
	def get_format_2_length():
		return 26
	
class Header():
	def __init__(self, converted_data_list):
		self.file_signature = ""
		for char in converted_data_list[0:4]:
			self.file_signature += char.decode('utf-8')
			
		self.file_source_id = converted_data_list[4]
		self.global_encoding = converted_data_list[5]
		self.project_id_guid_data_1 = converted_data_list[6]
		self.project_id_guid_data_2 = converted_data_list[7]
		self.project_id_guid_data_3 = converted_data_list[8]
		self.project_id_guid_data_4 = converted_data_list[9:17]
		self.version_major = converted_data_list[17]
		self.version_minor = converted_data_list[18]
		
		self.system_identifier = ""
		for char in converted_data_list[19:51]:
			self.system_identifier += char.decode('utf-8')
			
		self.system_generating_software = ""
		for char in converted_data_list[51:83]:
			self.system_generating_software += char.decode('utf-8')
		
		self.file_creation_day_of_the_year = converted_data_list[83]
		self.file_creation_year = converted_data_list[84]
		self.header_size = converted_data_list[85]
		self.offset_to_point_data = converted_data_list[86]
		self.number_of_variable_length_records = converted_data_list[87]
		self.point_data_record_format = converted_data_list[88]				#129 default arvo, 1 decodattuna
		self.point_data_record_length = converted_data_list[89]
		self.legacy_number_of_point_records = converted_data_list[90]
		self.legacy_number_of_point_by_return = converted_data_list[91:96]
		self.x_scale_factor = converted_data_list[96]
		self.y_scale_factor = converted_data_list[97]
		self.z_scale_factor = converted_data_list[98]
		self.x_offset = converted_data_list[99]
		self.y_offset = converted_data_list[100]
		self.z_offset = converted_data_list[101]
		self.max_x = converted_data_list[102]
		self.min_x = converted_data_list[103]
		self.max_y = converted_data_list[104]
		self.min_y = converted_data_list[105]
		self.max_z = converted_data_list[106]
		self.min_z = converted_data_list[107]
		
	def get_las_format(self):
		return self.version_minor
		
class PointDataRecord():
	def format1(self, converted_data_list, header):
		self.x = converted_data_list[0]
		self.y = converted_data_list[1]
		self.z = converted_data_list[2]	
		self.intensity = converted_data_list[3]
		
		self.return_number, self.number_of_returns, self.scan_direction_flag, self.edge_of_flight_line = self.get_single_byte_parameters(converted_data_list[4])
		
		self.classification = converted_data_list[5]
		self.scan_angle_rank = converted_data_list[6]
		self.user_data = converted_data_list[7]
		self.point_source_id = converted_data_list[8]
		self.gps_time = converted_data_list[9]
		
		
	'''
	Return Number: The Return Number is the pulse return number for a given output pulse. A
	given output laser pulse can have many returns, and they must be marked in sequence of return.
	The first return will have a Return Number of one, the second a Return Number of two, and so
	on up to five returns.
	
	Number of Returns (for this emitted pulse): The Number of Returns is the total number of
	returns for a given pulse. For example, a laser data point may be return two (Return Number)
	within a total number of five returns.
	
	Scan Direction Flag: The Scan Direction Flag denotes the direction at which the scanner mirror
	was traveling at the time of the output pulse. A bit value of 1 is a positive scan direction, and a
	bit value of 0 is a negative scan direction (where positive scan direction is a scan moving
	from the left side of the in-track direction to the right side and negative the opposite).
	
	Edge of Flight Line: The Edge of Flight Line data bit has a value of 1 only when the point is at
	the end of a scan. It is the last point on a given scan line before it changes direction.
	'''	
	def get_single_byte_parameters(self, data_byte):
		return 0, 0, False, False
	
class Las():
	def __init__(self):
		self.header = None
		self.point_data_records = list()
	
	def is_pdr_format_valid(self, format):
		if (type(format) != int):
			return False
		return format > 0 and format < 10
	
	def load(self, file_name):
		converted_data = list()
		with open (file_name, 'rb') as f:
			#header reading
			binary_data = f.read(HeaderVariables.get_default_header_length())
			self.header_binary = binary_data	# quick fix
			converted_data = struct.unpack(HeaderVariables.get_default_struct_parameters(), binary_data)			
			self.header = Header(converted_data)
			
			las_format = self.header.get_las_format()
			#do nothing with this data
			if (las_format == 3):
				f.read(HeaderVariables.get_extended_format_3_length())
			elif (las_format == 4):
				f.read(HeaderVariables.get_extended_format_4_length())
			
			# read and discard vlr
			for i in range(self.header.number_of_variable_length_records):
				f.read(VariableLengthRecordVariables.get_length())
				
			# read pdr
			pdr_format = self.header.point_data_record_format
						
			if not self.is_pdr_format_valid(pdr_format):
				print("PDR format not recognized. Format was: "+str(pdr_format))
				pdr_format = int(input("Set pdr format manually: "))
			
			if (pdr_format == 1):
				for i in range (self.header.legacy_number_of_point_records):
					f.read(self.header.point_data_record_length)
					binary_data = f.read(PointDataRecordVariables.get_format_1_length())
					converted_data = struct.unpack(PointDataRecordVariables.get_format_1_struct_parameters(), binary_data)
					pdr = PointDataRecord()
					pdr.format1(converted_data, self.header)
					self.point_data_records.append(pdr)
					if i % 50000 == 0:
						print(str(i) + "/" + str(self.header.legacy_number_of_point_records))
			else:
				raise Exception("PDR format unsupported: " + pdr_format)
		
	def write(self, file_name):
		with open(file_name, 'wb') as f:
			#write header
			f.write(self.header_binary[0:85])	# quick fix
			offset_to_point_data = self.header.header_size
			point_data_record_format = 1
			number_of_variable_length_records = 0
			number_of_point_records = len(self.point_data_records)
			f.write(struct.pack("<llBHl", offset_to_point_data, number_of_variable_length_records, point_data_record_format, self.header.point_data_record_length, number_of_point_records))
			f.write(self.header_binary[91:])
			
			#write PDRs			
			for pdr in self.point_data_records:
				f.write(struct.pack(PointDataRecordVariables.get_format_1_struct_parameters(), pdr.x, pdr.y, pdr.z, pdr.intensity, str.encode('a'), pdr.classification, pdr.scan_angle_rank, pdr.user_data, pdr.point_source_id, pdr.gps_time))
		
l = Las()
l.load("../data_zN4324F2.las")
l.write("../data_zN4324F2_a.las")