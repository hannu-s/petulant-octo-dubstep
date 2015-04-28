class PointDataRecords():
	def __init__(self, x,y,z, intensity, return_number, number_of_returns, scan_direction_flag, edge_of_flight_line, classification, scan_angle_rank, user_data, point_source_id, gps_time):
		self.x = x
		self.y = y
		self.z = z
		self.intensity = intensity
		self.return_number = return_number
		self.scan_direction_flag = scan_direction_flag
		self.edge_of_flight_line = edge_flight_line
		self.classification = classification
		self.scan_angle_rank = scan_angle_rank
		self.user_data = user_data
		self.point_source_id = point_source_id
		self.gps_time = gps_time