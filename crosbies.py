from sys import argv
from os import system

if len(argv) < 2:
	print("Use " + argv[0] + " <process count>")
	exit(1)

process_count = int(argv[1])

start = 10000000
end = 99999999

delta_per_process = int((end-start)/process_count)

threads = []
for i in range(process_count):
	print("Starting process " + str(i))
	pstart = start+delta_per_process*i
	pend = start+delta_per_process*(1+i)
	system("python3 crosby.py " + str(pstart) + " " + str(pend) + "&")