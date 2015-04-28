import struct

class Las():
	def __init__(self):
		self.header = None
		self.variable_length_records = list()
		self.point_data_records = list()
		self.extended_variable_lenght_records = list()
		
	def load(self, file_name):
		converted_data = list()
		with open (file_name, 'rb') as f:
			binary_data = f.read(227)
			# the '<' character stands for 'little-endian'
			converted_data += struct.unpack('<cccc', binary_data[:4])
			converted_data += struct.unpack('<HH', binary_data[4:8])
			
			# ... Rest of the header ...
			
			converted_data += struct.unpack('<ddd', binary_data[203:227])
			self.header = Header(converted_data)
			
			# ... Rest of the method ...
			
		
		
			
l = Las()
l.load("data_N4324F2.laz")