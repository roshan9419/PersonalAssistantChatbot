from time import sleep
import re
import playsound
from tkinter import *
from threading import Thread

def startTimer(query):
	nums = re.findall(r'[0-9]+', query)
	time = 0
	if "minute" in query and "second" in query:
		time = int(nums[0])*60 + int(nums[1])
	elif "minute" in query:
		time = int(nums[0])*60
	elif "second" in query:
		time = int(nums[0])
	else: return

	print("Timer Started")
	sleep(time)
	Thread(target=timer).start()
	playsound.playsound("extrafiles/audios/Timer.mp3")

def timer():
	root = Tk()
	root.title("Timer")
	root.iconbitmap("extrafiles/images/timer.ico")
	w_width, w_height = 300, 150
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
	root['bg'] = 'white'

	Label(root, text="Time's Up", font=("Arial Bold", 20), bg='white').pack(pady=20)
	Button(root, text="  OK  ", font=("Arial", 15), relief=FLAT, bg='#14A769', fg='white', command=lambda:quit()).pack()
	
	root.mainloop()
