
class LasHeader():
	# Las format 1.0, and above, features here onwards
	file_signature = {'type_format' : 'char', 'count' : 4, 'value' : {'type_format' : 'double', 'count' : 1, 'value' : None}}
	file_source_id = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	global_encoding = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	project_id_guid_data_1 = {'type_format' : 'unsigned long', 'count' : 1, 'value' : None}
	project_id_guid_data_2 = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	project_id_guid_data_3 = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	project_id_guid_data_4 = {'type_format' : 'unsigned char', 'count' : 8, 'value' : None}
	version_major = {'type_format' : 'unsigned char', 'count' : 1, 'value' : None}
	version_minor = {'type_format' : 'unsigned char', 'count' : 1, 'value' : None}
	system_identifier = {'type_format' : 'char', 'count' : 32, 'value' : None}
	generating_software = {'type_format' : 'char', 'count' : 32, 'value' : None}
	file_creation_day_of_year = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	file_creation_year = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	header_size = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	offset_to_point_data = {'type_format' : 'unsigned long', 'count' : 1, 'value' : None}
	number_of_variable_length_records = {'type_format' : 'unsigned long', 'count' : 1, 'value' : None}
	point_data_record_format = {'type_format' : 'unsigned char', 'count' : 1, 'value' : None}
	point_data_record_length = {'type_format' : 'unsigned short', 'count' : 1, 'value' : None}
	legacy_number_of_point_records = {'type_format' : 'unsigned long', 'count' : 1, 'value' : None}
	legacy_number_of_point_by_return = {'type_format' : 'unsigned long', 'count' : 5, 'value' : None}
	x_scale_factor = {'type_format' : 'double', 'count' : 1, 'value' : None}
	y_scale_factor = {'type_format' : 'double', 'count' : 1, 'value' : None}
	z_scale_factor = {'type_format' : 'double', 'count' : 1, 'value' : None}
	x_offset = {'type_format' : 'double', 'count' : 1, 'value' : None}
	y_offset = {'type_format' : 'double', 'count' : 1, 'value' : None}
	z_offset = {'type_format' : 'double', 'count' : 1, 'value' : None}
	max_x = {'type_format' : 'double', 'count' : 1, 'value' : None}
	min_x = {'type_format' : 'double', 'count' : 1, 'value' : None}
	max_y = {'type_format' : 'double', 'count' : 1, 'value' : None}
	min_y = {'type_format' : 'double', 'count' : 1, 'value' : None}
	max_z = {'type_format' : 'double', 'count' : 1, 'value' : None}
	min_z = {'type_format' : 'double', 'count' : 1, 'value' : None}
	# Las format 1.3, and above, features here onwards
	start_of_wareform_data_packet_records = {'type_format' : 'unsigned long long', 'count' : 1, 'value' : None}
	# Las format 1.4 features here onwards
	start_of_first_extended_variable_length_records = {'type_format' : 'unsigned long long', 'count' : 1, 'value' : None}
	number_of_extended_variable_length_records = {'type_format' : 'unsigned long', 'count' : 1, 'value' : None}
	number_of_point_records = {'type_format' : 'unsigned long long', 'count' : 1, 'value' : None}
	number_of_points_by_return = {'type_format' : 'unsigned long long', 'count' : 15, 'value' : None}
		
	# las specific variables
	las_12_header_size = 227
	las_13_header_size = 235
	las_14_header_size = 375
	
	# las parameters usable for generator
	las_12_header_variable_list = list()
	las_13_header_variable_list = list()
	las_14_header_variable_list = list()
	
	# other
	type_struct_codes = {'char' : 'c', 'unsigned char' : 'B', 'unsigned short' : 'H', 'unsigned long' : 'L', 'unsigned long long' : 'Q', 'double' : 'd'}
	type_sizes = {'char' : 1, 'unsigned char' : 1, 'unsigned short' : 2, 'unsigned long' : 4, 'unsigned long long' : 8, 'double' : 8}

		
	def __init__(self):
		self.las_12_header_variable_list.append(self.file_signature)
		self.las_12_header_variable_list.append(self.file_source_id)
		self.las_12_header_variable_list.append(self.global_encoding)
		self.las_12_header_variable_list.append(self.project_id_guid_data_1)
		self.las_12_header_variable_list.append(self.project_id_guid_data_2)
		self.las_12_header_variable_list.append(self.project_id_guid_data_3)
		self.las_12_header_variable_list.append(self.project_id_guid_data_4)
		self.las_12_header_variable_list.append(self.version_major)
		self.las_12_header_variable_list.append(self.version_minor)
		self.las_12_header_variable_list.append(self.system_identifier)
		self.las_12_header_variable_list.append(self.generating_software)
		self.las_12_header_variable_list.append(self.file_creation_day_of_year)
		self.las_12_header_variable_list.append(self.file_creation_year)
		self.las_12_header_variable_list.append(self.header_size)
		self.las_12_header_variable_list.append(self.offset_to_point_data)
		self.las_12_header_variable_list.append(self.number_of_variable_length_records)
		self.las_12_header_variable_list.append(self.point_data_record_format)
		self.las_12_header_variable_list.append(self.point_data_record_length)
		self.las_12_header_variable_list.append(self.legacy_number_of_point_records)
		self.las_12_header_variable_list.append(self.legacy_number_of_point_by_return)
		self.las_12_header_variable_list.append(self.x_scale_factor)
		self.las_12_header_variable_list.append(self.y_scale_factor)
		self.las_12_header_variable_list.append(self.z_scale_factor)
		self.las_12_header_variable_list.append(self.x_offset)
		self.las_12_header_variable_list.append(self.y_offset)
		self.las_12_header_variable_list.append(self.z_offset)
		self.las_12_header_variable_list.append(self.max_x)
		self.las_12_header_variable_list.append(self.max_y)
		self.las_12_header_variable_list.append(self.max_z)
		
		self.las_13_header_variable_list.append(self.start_of_wareform_data_packet_records)
		
		self.las_14_header_variable_list.append(self.start_of_first_extended_variable_length_records)
		self.las_14_header_variable_list.append(self.number_of_extended_variable_length_records)
		self.las_14_header_variable_list.append(self.number_of_point_records)
		self.las_14_header_variable_list.append(self.number_of_points_by_return)
		
	""" Stores read data to variables 
		data is expected in list form """
	
	def parse_data(self, data, bytes_read):
		pass
		
	""" Returns type name, count and version number in the header types"""
	def las_format_generator(self):
		for i in self.las_12_header_variable_list:
			yield i['type_format'], i['count'], "1.2"
				
		for i in self.las_13_header_variable_list:
			yield i['type_format'], i['count'], "1.3"
				
		for i in self.las_14_header_variable_list:
			yield i['type_format'], i['count'], "1.4"
			
	""" Returns unpack string and chunksize of next header part"""
	def struct_unpack_parameter_generator(self, for_version_minor):
		for item in self.las_12_header_variable_list:
			result = list()
			for i in range(item['count']):
				result.append(self.type_struct_codes[item['type_format']])
			yield "".join(result), self.type_sizes[item['type_format']] * item['count']
		
		if for_version_minor >= 3:
			for item in self.las_13_header_variable_list:
				result = list()
				for i in range(item['count']):
					result.append(self.type_struct_codes[item['type_format']])
				yield "".join(result), self.type_sizes[item['type_format']] * item['count']
		
		if for_version_minor == 4:
			for item in self.las_14_header_variable_list:
				result = list()
				for i in range(item['count']):
					result.append(self.type_struct_codes[item['type_format']])
				yield "".join(result), self.type_sizes[item['type_format']] * item['count']
		
	
	def unkown_version_exception(self):
		raise Exception("Version not supported! Version: " + str(self.version_major) + "." + str(self.version_minor))

class Las():
	type_sizes = {'char' : 1, 'unsigned char' : 1, 'unsigned short' : 2, 'unsigned long' : 4, 'unsigned long long' : 8, 'double' : 8}
	type_struct_codes = {'char' : 'c', 'unsigned char' : 'B', 'unsigned short' : 'H', 'unsigned long' : 'L', 'unsigned long long' : 'Q', 'double' : 'd'}
	las_header = None
	
	def __init__(self):
		self.las_header = LasHeader()
			
	def hue(self):
		generator = self.las_header.struct_unpack_parameter_generator(4)
		#for format, count, version in generator:
			#print (format + " " + str(count) + " " + version)
			
		for unpack_str, chunksize in generator:
				print (unpack_str + " " + str(chunksize))
			

	def read(self, file_path):
		generator = self.las_header.struct_unpack_parameter_generator()
		with open (file_path, 'rb') as f:
			parsed_data = list()
			data_in_file = f.read(las_header.las_12_header_size)
			for unpack_str, chunksize in generator:
				print (unpack_str + " " + chunksize)
			

				
a = Las()
a.hue()
