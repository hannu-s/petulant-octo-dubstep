from fileTools import FileReader, FileWriter
import sys

def main(read_path, write_path):
	reader = FileReader()
	writer = FileWriter()
	
	data = reader.read(read_path)
	writer.write(write_path, data)

def print_error_message(msg):
	print("Error. Invalid startup arguments")
	print("Example: Main.py ansii_file_to_be_read.txt converted_bin_file.las")
	print(msg)

if __name__ == "__main__":
	if len(sys.argv) <= 2:
		print_error_message("Not enough arguments") 
	elif len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	else:
		print_error_message("Too many arguments")
	exit()
