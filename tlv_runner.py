from subprocess import Popen, PIPE, STDOUT

repeats = 100
def repeater(params):
	print("Starting repeater with params: " + params)
	for i in range(repeats):
		print(i)
		p = Popen("time python3 tlv.py " + params, shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		
		stderr = str(stderr)
		data = stderr.split("user")

		user = data[0].replace(" ", "").replace("b'", "")
		data = "".join(data[1]).split("system")

		system = data[0].replace(" ", "")
		data = "".join(data[1]).split("elapsed")

		elapsed = data[0].replace(" 0:", "")		
		with open ('results.csv', 'a') as f:
			f.write(params + "," + user + "," + system + "," + elapsed + "," + "\n")
		
			
with open ('results.csv', 'w') as f:
	f.write("parameter, user, system, elpased, timeit diff")
repeater("wl")
repeater("rl")
repeater("wa")
repeater("ra")
"""	
with Popen("time python3 tlv.py", shell=True, stderr=PIPE) as proc:
	result = str(proc.stdout.read())
	result_list = list(result)
	print(result_list)
"""