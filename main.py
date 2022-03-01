with open("toconvert.txt", "r") as file:
	data = file.read()

mode = input("type spaces to convert them to tabs\nand tabs to convert them to spaces\n").upper()
if mode == "TABS":
	amount = int(input("to how many spaces does it need to convert the tabs?\n"))
	spaces = ""
	for i in range(amount):
		spaces += " "
	converted_data = ""
	for ch in data:
		if ch == "	":
			converted_data += spaces
		else:
			converted_data += ch

if mode == "SPACES":
	amount = int(input("how many spaces does 1 tab replace?\n"))
	streak = 0
	converted_data = ""
	for ch in data:
		if ch != " ":
			for i in range(streak):
				converted_data += " "
			streak = 0
			converted_data += ch
		else:
			streak += 1
			if streak >= amount:
				streak = 0
				converted_data += "	"
			

with open("converted.txt", "w") as file:
	file.write(converted_data)