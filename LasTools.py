import struct

type_sizes = {'char' : 1, 'unsigned char' : 1, 'unsigned short' : 2, 'unsigned long' : 4, 'unsigned long long' : 8, 'double' : 8}
# unsigned long = 'L', but 'L' requires 8 bytes, unsigned integer = 'I', requires 4 bytes
type_struct_codes = {'char' : 'c', 'unsigned char' : 'B', 'unsigned short' : 'H', 'unsigned long' : 'L', 'unsigned long long' : 'Q', 'double' : 'd'}

class LasHeader():
	# Las format 1.0, and above, features here onwards
	file_signature = {'type_format' : 'char', 'count' : 4, 'value' : None}
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
		self.las_12_header_variable_list.append(self.min_x)
		self.las_12_header_variable_list.append(self.max_y)
		self.las_12_header_variable_list.append(self.min_y)
		self.las_12_header_variable_list.append(self.max_z)
		self.las_12_header_variable_list.append(self.min_z)
		
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
		if for_version_minor >= 0:
			for item in self.las_12_header_variable_list:
				result = list()
				for i in range(item['count']):
					result.append(type_struct_codes[item['type_format']])
				yield "".join(result), type_sizes[item['type_format']] * item['count']
		
		if for_version_minor >= 3:
			for item in self.las_13_header_variable_list:
				result = list()
				for i in range(item['count']):
					result.append(type_struct_codes[item['type_format']])
				yield "".join(result), type_sizes[item['type_format']] * item['count']
		
		if for_version_minor == 4:
			for item in self.las_14_header_variable_list:
				result = list()
				for i in range(item['count']):
					result.append(type_struct_codes[item['type_format']])
				yield "".join(result), type_sizes[item['type_format']] * item['count']
		
	def store_header_data(self, data):
		#1.2 header check
		if len(data) >= 107:
			self.file_signature['value'] = data[0].decode("ascii") + data[1].decode("ascii") + data[2].decode("ascii") + data[3].decode("ascii")
			self.file_source_id['value'] = data[4]
			self.global_encoding['value'] = data[5]
			self.project_id_guid_data_1['value'] = data[6]
			self.project_id_guid_data_2['value'] = data[7]
			self.project_id_guid_data_3['value'] = data[8]
			self.project_id_guid_data_4['value'] = list(data[9:16])
			self.version_major['value'] = data[17]
			self.version_minor['value'] = data[18]
			self.system_identifier['value'] = data[19].decode("ascii") + data[20].decode("ascii") + data[21].decode("ascii") + data[22].decode("ascii") + data[23].decode("ascii") + data[24].decode("ascii") + data[25].decode("ascii") + data[26].decode("ascii") + data[27].decode("ascii") + data[28].decode("ascii") + data[29].decode("ascii") + data[30].decode("ascii") + data[31].decode("ascii") + data[32].decode("ascii") + data[33].decode("ascii") + data[34].decode("ascii") + data[35].decode("ascii") + data[36].decode("ascii") + data[37].decode("ascii") + data[38].decode("ascii") + data[39].decode("ascii") + data[40].decode("ascii") + data[41].decode("ascii") + data[42].decode("ascii") + data[43].decode("ascii") + data[44].decode("ascii") + data[45].decode("ascii") + data[46].decode("ascii") + data[47].decode("ascii") + data[48].decode("ascii") + data[49].decode("ascii") + data[50].decode("ascii")
			self.generating_software['value'] = data[51].decode("ascii") + data[52].decode("ascii") + data[53].decode("ascii") + data[54].decode("ascii") + data[55].decode("ascii") + data[56].decode("ascii") + data[57].decode("ascii") + data[58].decode("ascii") + data[59].decode("ascii") + data[60].decode("ascii") + data[61].decode("ascii") + data[62].decode("ascii") + data[63].decode("ascii") + data[64].decode("ascii") + data[65].decode("ascii") + data[66].decode("ascii") + data[67].decode("ascii") + data[68].decode("ascii") + data[69].decode("ascii") + data[70].decode("ascii") + data[71].decode("ascii") + data[72].decode("ascii") + data[73].decode("ascii") + data[74].decode("ascii") + data[75].decode("ascii") + data[76].decode("ascii") + data[77].decode("ascii") + data[78].decode("ascii") + data[79].decode("ascii") + data[80].decode("ascii") + data[81].decode("ascii") + data[82].decode("ascii")
			self.file_creation_day_of_year['value'] = data[83]
			self.file_creation_year['value'] = data[84]
			self.header_size['value'] = data[85]
			self.offset_to_point_data['value'] = data[86]
			self.number_of_variable_length_records['value'] = data[87]
			self.point_data_record_format['value'] = data[88]
			self.point_data_record_length['value'] = data[89]
			self.legacy_number_of_point_records['value'] = data[90]
			self.legacy_number_of_point_by_return['value'] = data[91] + data[92] + data[93] + data[94] + data[95]
			self.x_scale_factor['value'] = data[96]
			self.y_scale_factor['value'] = data[97]
			self.z_scale_factor['value'] = data[98]
			self.x_offset['value'] = data[99]
			self.y_offset['value'] = data[100]
			self.z_offset['value'] = data[101]
			self.max_x['value'] = data[102]
			self.min_x['value'] = data[103]
			self.max_y['value'] = data[104]
			self.min_y['value'] = data[105]
			self.max_z['value'] = data[106]
			self.min_z['value'] = data[107]
			
	def unkown_version_exception(self):
		raise Exception("Version not supported! Version: " + str(self.version_major) + "." + str(self.version_minor))

class Las():
	las_header = None
	
	def __init__(self):
		self.las_header = LasHeader()

	def read(self, file_path):
		generator = self.las_header.struct_unpack_parameter_generator(2)
		with open (file_path, 'rb') as f:
			parsed_data = list()
			current_offset = 0
			data_in_file = f.read(self.las_header.las_12_header_size)
			for unpack_str, chunksize in generator:
				parsed_data += struct.unpack('<' + unpack_str, data_in_file[current_offset: current_offset + chunksize])
				current_offset += chunksize
			self.las_header.store_header_data(parsed_data)

				
a = Las()
a.read('data_N4324F2.laz')
