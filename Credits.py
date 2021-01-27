from tkinter import *
from os import getcwd
from PIL import ImageTk, Image

class Credits():
	def __init__(self, master):
		self.root = Toplevel(master)
		app_width  = 600
		app_height = 400
		screen_width  = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		self.root.geometry(f'{app_width}x{app_height}+{int((screen_width/2)-(app_width/2))}+{int((screen_height/2)-(app_height/2))}')
		self.root.configure(bg='white'); self.root.title("Practical Homies"); self.root.resizable(0, 0); self.root.iconbitmap(getcwd() + '\\AEC_logo.ico')
		#self.root.overrideredirect(True)

		credits_img = ImageTk.PhotoImage(Image.open('credits.jpg').resize((540, 300), Image.ANTIALIAS))
		self.credits_label = Label(self.root, image=credits_img,borderwidth=0); self.credits_label.place(x=30, y=40)

		self.close=Button(self.root,text="Close",justify='center',bg='white', command=self.root.destroy)
		self.close.config(font=("Courier", 12, 'bold')); self.close.place(x=260, y=360)

		self.root.mainloop()

#Credits(None)

