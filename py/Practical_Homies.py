from tkinter import *
from os import getcwd
from PIL import ImageTk, Image
from time import sleep
import win32gui, win32con

from Mod_of_Rigidity_Static_Method import Modulus_of_Rigidity_Static
from Tortional_Pendulum_Simulation import Tortional_Pendulum
from Vernier_Callipers_main import Vernier_Callipers_Main
from Screw_Gauge_main import Screw_Gauge_Main
from Laser_Diffraction import Laser_Diffraction
from Resistivity_by_Four_Probe import Resistance_by_Four_Probe
from Frank_Hertz import Frank_Hertz
from Hall_Effect import Hall_Effect
from Credits import Credits

class HomePage():
	def exp_exec(self, exp):
	    if exp=='Static Method':     Modulus_of_Rigidity_Static(self.root)
	    if exp=='Dynamic Method':    Tortional_Pendulum(self.root)
	    if exp=='Laser Diffraction': Laser_Diffraction(self.root)
	    if exp=='Four Probe':        Resistance_by_Four_Probe(self.root)
	    if exp=='Frank-Hertz':       Frank_Hertz(self.root)
	    if exp=='Hall_Effect':		 Hall_Effect(self.root)
	    if exp=='Vernier Callipers': Vernier_Callipers_Main(self.root)
	    if exp=='Screw Gauge':		 Screw_Gauge_Main(self.root)
	    if exp=='Credits':			 Credits(self.root)
	    
	def __init__(self):
		self.root = Tk()
		app_width  = 1000
		app_height = 600
		screen_width  = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		self.root.geometry(f'{app_width}x{app_height}+{int((screen_width/2)-(app_width/2))}+{int((screen_height/2)-(app_height/2))}')
		self.root.title("Practical Homies"); self.root.resizable(0, 0); self.root.iconbitmap('..\\img\\logos-and-icons\\AEC_logo.ico')

		self.canvas = Canvas(self.root, bg='white', height=700); self.canvas.pack(side='left', fill = 'both', expand = YES)
		def moved(event):  self.canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.canvas.bind("<Motion>", moved); tag = self.canvas.create_text(10, 10, text="", anchor="nw")

		self.img1 = ImageTk.PhotoImage(Image.open('..\\img\\main-page\\main_page_image1.jpg').resize((180, 180), Image.ANTIALIAS))
		panel = Label(master=self.canvas,image=self.img1,bd=0);panel.pack(side="bottom",fill="both",expand="yes");panel.place(x=-12,y=420)

		self.img2 = ImageTk.PhotoImage(Image.open('..\\img\\main-page\\main_page_image2.jpg').resize((250, 250), Image.ANTIALIAS))
		panel = Label(master=self.canvas,image=self.img2,bd=0);panel.pack(side="bottom",fill="both",expand="yes");panel.place(x=800,y=320)

		self.img3 = ImageTk.PhotoImage(Image.open('..\\img\\main-page\\main_page_image3.jpg').resize((140, 290), Image.ANTIALIAS))
		panel = Label(master=self.canvas, image=self.img3,bd=0);panel.pack(side="bottom", fill="both", expand="yes"); panel.place(x=825,y=-12)

		self.img4 = ImageTk.PhotoImage(Image.open('..\\img\\main-page\\main_page_image4.jpg').resize((80, 190), Image.ANTIALIAS))
		panel = Label(master=self.canvas,image=self.img4,bd=0);panel.pack(side ="bottom",fill="both",expand="yes"); panel.place(x=10, y=-40)


		self.a=Button(self.canvas,text="Determination of\nwavelength of light by\nLaser Diffraction method",width=32,height=12,justify='center',bg='white',
			command=lambda:self.exp_exec('Laser Diffraction'))
		self.a.config(font=("Courier", 12, 'bold'));self.a.pack();self.a.place(x=110, y=50)

		self.b=Button(self.canvas,text="Modulus of rigidity-Static Method",width=39,height=6,justify='center',bg='white',
			command=lambda:self.exp_exec('Static Method'))
		self.b.config(font=("Courier", 12, 'bold'));self.b.pack();self.b.place(x=460,y=50)

		self.c=Button(self.canvas,text="Frank-Hertz",width=18,height=3,justify='center',bg='white',command=lambda:self.exp_exec('Frank-Hertz'))
		self.c.config(font=("Courier",12,'bold'));self.c.pack();self.c.place(x=460,y=180)

		#self.d=Button(self.canvas,text="Determination of\nspecific charge \n(e/m) by\nJ.J. Thomson’s\nmethod\n(coming soon)",width=19,height=12,justify='center',bg='white',
		#	command=lambda:self.exp_exec('Thomson’s (e/m)'))
		#self.d.config(font=("Courier",12,'bold'));self.d.pack();self.d.place(x=658,y=180) #self.d['state']='disabled'

		self.d1=Button(self.canvas,text="Vernier Callipers",width=19,height=5,justify='center',bg='white', command=lambda:self.exp_exec('Vernier Callipers'))
		self.d1.config(font=("Courier",12,'bold'));self.d1.pack();self.d1.place(x=658,y=180)
		
		self.d2=Button(self.canvas,text="Screw Gauge",width=19,height=5,justify='center',bg='white', command=lambda:self.exp_exec('Screw Gauge'))
		self.d2.config(font=("Courier",12,'bold'));self.d2.pack();self.d2.place(x=658,y=290)

		self.e=Button(self.canvas,text="Determination of \ncharge carrier \ndensity-\nHall Effect \nexperiment\n(coming soon)",width=18,height=12, justify='center',
			bg='white',command=lambda:self.exp_exec('Hall_Effect'))
		self.e.config(font=("Courier",12,'bold'));self.e.pack();self.e.place(x=460,y=252)
		# self.e['state']='disabled'

		self.f=Button(self.canvas,text="Resistivity by\nFour Probe",width=18,height=2,justify='center',bg='white',command=lambda:self.exp_exec('Four Probe'))
		self.f.config(font=("Courier",12,'bold'));self.f.pack();self.f.place(x=250,y=291)

		self.g=Button(self.canvas,text="Modulus of \nrigidity–\nDynamic\nmethod",width=12,height=10,justify='center',bg='white',
			command=lambda:self.exp_exec('Dynamic Method'))
		self.g.config(font=("Courier",12,'bold'));self.g.pack();self.g.place(x=110, y=290)


		credits_img = ImageTk.PhotoImage(Image.open('..\\img\\logos-and-icons\\credits_button.jpg').resize((180, 130), Image.ANTIALIAS))
		self.credits_button = Button(self.canvas, image=credits_img,borderwidth=0,command=lambda:self.exp_exec('Credits'))
		self.credits_button.pack(); self.credits_button.place(x=660, y=420)


		self.root.mainloop()


def home():
	splash_root.destroy()
	home_page = HomePage()

# Hiding the cmd
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)

splash_root = Tk(); splash_root.configure(bg='white'); splash_root.title("Practical Homies"); splash_root.resizable(0, 0)
app_width  = 350
app_height = 350
screen_width  = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
splash_root.geometry(f'{app_width}x{app_height}+{int((screen_width/2)-(app_width/2))}+{int((screen_height/2)-(app_height/2))}')

#img = ImageTk.PhotoImage(Image.open(getcwd() + '\\img\\splash_screen_image.jpg').resize((250, 200), Image.ANTIALIAS))
img = ImageTk.PhotoImage(Image.open(getcwd() + '\\..\\img\\logos-and-icons\\AEC_logo_splash.png').resize((350, 350), Image.ANTIALIAS))
panel = Label(master = splash_root, image = img,bd=0); panel.pack(side = "bottom", fill = "both", expand = "yes"); panel.pack(); panel.place(x=-15,y=0)

#Hide the title bar.
splash_root.overrideredirect(True)
splash_root.after(4000,home)


mainloop()