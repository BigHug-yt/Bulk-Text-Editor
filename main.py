import os

with open("toconvert.txt", "r") as file:
	data = file.read()
converted_data = ""

class option:
	def __init__(self,q,opts):
		self.q = q
		self.opts = opts

		if type(self.opts) == list:
			valid_ans = False
			while not valid_ans:
				self.ans = self.askopts()
				try:
					self.ans = int(self.ans)
				except:
					self.ans = self.ans
				if type(self.ans) == int and self.ans >= 0 and self.ans < len(self.opts):
					valid_ans = True
			self.ans = self.opts[self.ans]

		if self.opts == "int":
			self.ans = self.askint()
		if self.opts == "str":
			self.ans = self.askstr()

	def askstr(self):
		os.system("clear")
		return input(self.q+"\n")
	def askint(self):
		os.system("clear")
		return int(input(self.q+"\n"))
	def askopts(self):
		os.system("clear")
		str = self.q + "\n"
		for i, opt in enumerate(self.opts):
			str += f"\t[{i}] " + opt + "\n"
		return input(str)




def spaces_and_tabs(data):
	converted_data = ""
	mode = option(
		"choose a mode:",
		["tabs to spaces",
		"spaces to tabs"]
	).ans
	
	if mode == "tabs to spaces":
		amount = option(
			"how many spaces does it need to convert one tab?",
			"int"
		).ans
		spaces = ""
		for i in range(amount):
			spaces += " "
		tabs_found = 0
		for ch in data:
			if ch == "	":
				converted_data += spaces
				tabs_found += 1
			else:
				converted_data += ch
		print("tabs found:",tabs_found)
	
	if mode == "spaces to tabs":
		amount = option(
			"how many spaces does one tab replace?",
			"int"
		).ans
		streak = 0
		tabs_placed = 0
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
					tabs_placed += 1
		print("tabs placed:",tabs_placed)
	return converted_data

def find_and_replace(data):
	converted_data = ""
	to_find = option(
		"what do you want to replace?",
		"str"
	).ans
	amount = data.count(to_find)
	to_replace = option(
		f"found {to_find} {amount} times\nwhat do you want to replace '{to_find}' with?",
		"str"
	).ans
	converted_data = data.replace(to_find,to_replace)
	return converted_data


# main menu
program = option(
	"select a program:",
	["spaces and tabs",
	"find and replace"]
).ans

if program == "spaces and tabs":
	converted_data = spaces_and_tabs(data)
if program == "find and replace":
	converted_data = find_and_replace(data)


# saves the converted data in converted.txt
with open("converted.txt", "w") as file:
	file.write(converted_data)