from datetime import datetime
import os
file = "userData/toDoList.txt"

def createList():
	f = open(file,"w")
	present = datetime.now()
	dt_format = present.strftime("Date: " + "%d/%m/%Y"+ " Time: " + "%H:%M:%S" + "\n")
	f.write(dt_format)
	f.close()

def toDoList(text):
	if os.path.isfile(file) == False:
		createList()

	f = open(file,"r")
	x = f.read(8)
	f.close()
	y = x[6:]
	yesterday = int(y)
	present = datetime.now()
	today = int(present.strftime("%d"))
	if (today-yesterday) >= 1:
		createList()
	f = open(file,"a")
	dt_format = present.strftime("%H:%M")
	print(dt_format)
	f.write(f"[{dt_format}] : {text}\n")
	f.close()

def showtoDoList():
	if os.path.isfile(file)==False:
		return ["It looks like that list is empty"]
	
	f = open(file, 'r')
	
	items = []
	for line in f.readlines():
		items.append(line.strip())

	speakList = [f"You have {len(items)-1} items in your list:\n"]
	for i in items[1:]:
		speakList.append(i.capitalize())
	return speakList
