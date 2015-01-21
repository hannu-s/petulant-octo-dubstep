from fileTools import FileReader, FileWriter
import sys

def main(read_path, write_path, coding = "utf-8", format = "B"):
	read_path = str(read_path)
	write_path = str(write_path)
	coding = str(coding)
	format = str(format)

	reader = FileReader()
	reader.set_encoding(coding)

	data = reader.read(read_path)

	writer = FileWriter()
	writer.set_encoding(coding)
	writer.write(write_path, data, format)

def print_error_message(msg):
	print("Error. Invalid startup arguments")
	print("Example: Main.py ansii_file_to_be_read.txt converted_bin_file.bin")
	print(msg)

if __name__ == "__main__":
	if len(sys.argv) <= 2:
		print_error_message("Not enough arguments") 
		exit()
	elif len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	elif len(sys.argv) == 4:
		main(sys.argv[1], sys.argv[2], sys.argv[3])
	elif len(sys.argv) == 5:
		main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	else:
		print_error_message("Too many arguments")
		exit()
