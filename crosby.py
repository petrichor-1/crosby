import math

def check_input(input, target):
	encoded = "/"
	for idx in range(8):
		if idx%2 == 0:
			check_alg_1 = math.floor(float(input[(idx-1+len(input))%len(input)])*1.27*float(input[(idx+1+len(input))%len(input)]))%9
			check_alg_2 = math.floor((math.sin(math.radians(float(input[(idx-2+len(input))%len(input)])))+math.cos(math.radians(float(input[(idx+2+len(input))%len(input)]))))*100)%99/100
			check_alg_3 = math.floor(float(input[idx])*(check_alg_1+check_alg_2+float(input[idx])))
			encoded += str(check_alg_3)
		else:
			check_alg_1 = math.ceil(float(input[(idx+1+len(input))%len(input)])*2.71*float(input[(idx-1+len(input))%len(input)]))%9
			check_alg_2 = math.floor((math.sin(math.radians(float(input[(idx+2+len(input))%len(input)])))+math.cos(math.radians(float(input[(idx-2+len(input))%len(input)]))))*100)%99/100
			check_alg_3 = math.ceil(float(input[idx])*(check_alg_1+check_alg_2+float(input[len(input)-idx])))
			encoded += str(check_alg_3)
		if not target.startswith(encoded):
			return False
	return True

for i in range(10000000,99999999):
	if check_input(str(i), "/153718425026999"):
		print(str(i) + " is valid!")
	if i % 10000000 == 0:
		print("Reached " + str(i))
print("Done!")