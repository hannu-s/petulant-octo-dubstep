from fileTools import FileReader, FileWriter
import sys

def main(read_path, write_path):
	reader = FileReader()
	writer = FileWriter()
	
	data = reader.read(read_path)
	writer.write(write_path, data)

def print_error_message(msg):
	print("Error. Invalid startup arguments.")
	print("Error message: " + msg)
	print("Use '--help' for more information.")	

def print_help_message():
	print("\nExample parameters: ascii_data.txt binary_data.las")
	print("- Reads from file 'ascii_data.txt' in ascii format and converts it to 'binary_data.las' in las format.")
	print("- Also can read from las to ascii, las to las and ascii to ascii")
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print_error_message("Not enough arguments") 
	elif len(sys.argv) == 2:
		if str(sys.argv[1]).lower() == '--help':
			print_help_message()
		else:
			print_error_message("Not enough arguments") 
	elif len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	else:
		print_error_message("Too many arguments")
	exit()