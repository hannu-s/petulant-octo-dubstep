class VariableLengthRecord():
	def __init__(self, parameter_list):
		self.reserved = parameter_list[0]
		self.user_id = parameter_list[1]
		self.record_id = parameter_list[2]
		self.record_length_after_header = parameter_list[3]
		self.description = parameter_list[4]
		
		
		

		
