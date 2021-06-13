from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from pynput.keyboard import Key, Controller
import userHandler
from userHandler import UserData

u = UserData()
u.extractData()
avatarChoosen = u.getUserPhoto()

def closeWindow():
	keyboard = Controller()
	keyboard.press(Key.alt_l)
	keyboard.press(Key.f4)
	keyboard.release(Key.f4)
	keyboard.release(Key.alt_l)

def SavePhoto():
	userHandler.UpdateUserPhoto(avatarChoosen)
	closeWindow()

def selectAVATAR(avt=0):
	global avatarChoosen
	avatarChoosen = avt

	i=1
	for avtr in (avtb1,avtb2,avtb3,avtb4,avtb5,avtb6,avtb7,avtb8,avtb9,avtb10,avtb11,avtb12,avtb13,avtb14,avtb15):
		if i==avt:
			avtr['state'] = 'disabled'
		else:
			avtr['state'] = 'normal'
		i+=1

if __name__ == "__main__":

	background = '#F6FAFB'
	avtrRoot = Tk()
	avtrRoot.title("Choose Avatar")
	avtrRoot.configure(bg=background)
	w_width, w_height = 500, 450
	s_width, s_height = avtrRoot.winfo_screenwidth(), avtrRoot.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	avtrRoot.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))

	Label(avtrRoot, text="Choose Your Avatar", font=('arial bold', 15), bg=background, fg='#303E54').pack(pady=10)

	avatarContainer = Frame(avtrRoot, bg=background)
	avatarContainer.pack(pady=10, ipadx=50, ipady=20)
	size = 100

	#create a main frame
	main_frame = Frame(avatarContainer)
	main_frame.pack(fill=BOTH, expand=1)

	#create a canvas
	my_canvas = Canvas(main_frame, bg=background)
	my_canvas.pack(side=LEFT, expand=1, fill=BOTH)

	#add a scrollbar to the canvas
	my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
	my_scrollbar.pack(side=RIGHT, fill=Y)

	#configure the canvas
	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

	#create another frame inside the canvas
	second_frame = Frame(my_canvas)
	
	#add that new frame to a window in the canvas
	my_canvas.create_window((0,0), window=second_frame, anchor='nw')

	avtr1 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a1.png').resize((size, size)), Image.ANTIALIAS)
	avtr2 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a2.png').resize((size, size)), Image.ANTIALIAS)
	avtr3 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a3.png').resize((size, size)), Image.ANTIALIAS)
	avtr4 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a4.png').resize((size, size)), Image.ANTIALIAS)
	avtr5 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a5.png').resize((size, size)), Image.ANTIALIAS)
	avtr6 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a6.png').resize((size, size)), Image.ANTIALIAS)
	avtr7 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a7.png').resize((size, size)), Image.ANTIALIAS)
	avtr8 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a8.png').resize((size, size)), Image.ANTIALIAS)
	avtr9 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a9.png').resize((size, size)), Image.ANTIALIAS)
	avtr10 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a10.png').resize((size, size)), Image.ANTIALIAS)
	avtr11 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a11.png').resize((size, size)), Image.ANTIALIAS)
	avtr12 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a12.png').resize((size, size)), Image.ANTIALIAS)
	avtr13 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a13.png').resize((size, size)), Image.ANTIALIAS)
	avtr14 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a14.png').resize((size, size)), Image.ANTIALIAS)
	avtr15 = ImageTk.PhotoImage(Image.open('extrafiles/images/avatars/a15.png').resize((size, size)), Image.ANTIALIAS)

	
	avtb1 = Button(second_frame, image=avtr1, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(1))
	avtb2 = Button(second_frame, image=avtr2, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(2))
	avtb3 = Button(second_frame, image=avtr3, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(3))
	avtb4 = Button(second_frame, image=avtr4, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(4))
	avtb5 = Button(second_frame, image=avtr5, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(5))
	avtb6 = Button(second_frame, image=avtr6, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(6))
	avtb7 = Button(second_frame, image=avtr7, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(7))
	avtb8 = Button(second_frame, image=avtr8, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(8))
	avtb9 = Button(second_frame, image=avtr9, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(9))
	avtb10 = Button(second_frame, image=avtr10, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(10))
	avtb11 = Button(second_frame, image=avtr11, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(11))
	avtb12 = Button(second_frame, image=avtr12, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(12))
	avtb13 = Button(second_frame, image=avtr13, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(13))
	avtb14 = Button(second_frame, image=avtr14, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(14))
	avtb15 = Button(second_frame, image=avtr15, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(15))

	avtb1.grid( row=0, column=0, ipadx=25, ipady=10)
	avtb2.grid( row=0, column=1, ipadx=25, ipady=10)
	avtb3.grid( row=0, column=2, ipadx=25, ipady=10)
	avtb4.grid( row=1, column=0, ipadx=25, ipady=10)
	avtb5.grid( row=1, column=1, ipadx=25, ipady=10)
	avtb6.grid( row=1, column=2, ipadx=25, ipady=10)
	avtb7.grid( row=2, column=0, ipadx=25, ipady=10)
	avtb8.grid( row=2, column=1, ipadx=25, ipady=10)
	avtb9.grid( row=2, column=2, ipadx=25, ipady=10)
	avtb10.grid(row=3, column=0, ipadx=25, ipady=10)
	avtb11.grid(row=3, column=1, ipadx=25, ipady=10)
	avtb12.grid(row=3, column=2, ipadx=25, ipady=10)
	avtb13.grid(row=4, column=0, ipadx=25, ipady=10)
	avtb14.grid(row=4, column=1, ipadx=25, ipady=10)
	avtb15.grid(row=4, column=2, ipadx=25, ipady=10)

	BottomFrame = Frame(avtrRoot, bg=background)
	BottomFrame.pack(pady=10)
	Button(BottomFrame, text='         Update         ', font=('Montserrat Bold', 15), bg='#01933B', fg='white', bd=0, relief=FLAT, command=SavePhoto).grid(row=0, column=0, padx=10)
	Button(BottomFrame, text='         Cancel         ', font=('Montserrat Bold', 15), bg='#EDEDED', fg='#3A3834', bd=0, relief=FLAT, command=closeWindow).grid(row=0, column=1, padx=10)

	avtrRoot.iconbitmap("extrafiles/images/changeProfile.ico")
	avtrRoot.mainloop()
