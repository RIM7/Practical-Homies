from tkinter import *
from tkinter import font
from time import sleep
import numpy as np
from random import randint
from PIL import ImageTk, Image
from os import startfile


class Hall_Effect():
	milliAmp = 0.0; Volt = 0.0; diff = 0.0; diff_of_diff = 0.0; i_temp = 25; Temperature=0.0; run_flag=0; wait_clicked=0

	def instr(self):
		# ********************************************************
		startfile('..\\pdfs\\Hall Effect.pdf')

	def draw_circular_scale(self):
		# image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_magnetic_field, anchor = NW)
		#center at 200, 550
		for i in range(len(self.x1)):
			if i%10==0:    self.canvas2.create_line(self.x1[i], self.y1[i], self.x2[i], self.y2[i]); 
			elif i%5 == 0: self.canvas2.create_line(self.x1[i], self.y1[i], self.x3[i], self.y3[i]); 
			else:          self.canvas2.create_line(self.x1[i], self.y1[i], self.x4[i], self.y4[i])



	# ================================================================================================================================================
	# Reset
	def total_reset_method(self): 
		self.insert_remove_probe['text'] = 'Insert/Remove'
		self.insert_remove_probe['state'] = 'disabled'
		
		self.reset_method()


	def reset_method(self):
		self.Amp['state'] = 'disabled'
		self.thickness['state'] = 'disabled'
		self.hall_current['state'] = 'disabled'

		self.show_curr_or_volt['state'] = 'disabled'
		self.current_voltage['text'] = '00.00'

		self.canvas2.delete('all')
		if self.var1.get()==1:
			image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_magnetic_field, anchor = NW)
		else:
			image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_hall_effect, anchor = NW)

		self.draw_circular_scale()
		self.canvas2.create_line(self.current_reading_coordinates[0.0][0], self.current_reading_coordinates[0.0][1], 170, 460)


	# ================================================================================================================================================
	# Select Procedure
	def procedure_setup(self): 
		self.reset_method()
		self.insert_remove_probe['state'] = 'normal'
		
		if self.var1.get()==1:
			image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_magnetic_field, anchor = NW)
			self.insert_remove_probe['text'] = 'Insert Probe'
		elif self.var1.get()==2:
			image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_hall_effect, anchor = NW)
			self.insert_remove_probe['text'] = 'Insert Hall Probe'

		self.draw_circular_scale()
		self.canvas2.create_line(self.current_reading_coordinates[0.0][0], self.current_reading_coordinates[0.0][1], 170, 460)

	# ================================================================================================================================================
	# Insert Probe / Remove Probe / Insert Hall Probe / Remove Hall Probe
	def insert_remove_probe_method(self):
		self.reset_method()

		flag = 0
		if self.insert_remove_probe['text']=='Insert Probe':
			self.insert_remove_probe['text']='Remove Probe'
			self.Amp['state'] = 'normal'
			self.current_voltage['text'] = self.amp_dict[self.Amp.get()]
			image = self.canvas2.create_image(0, -5, image = self.bg_image_inserted_magnetic_field, anchor = NW)
			flag = 1

		elif self.insert_remove_probe['text']=='Remove Probe': 
			self.insert_remove_probe['text']='Insert Probe'
			self.Amp['state'] = 'disabled'
			image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_magnetic_field, anchor = NW)
			flag = 0

		elif self.insert_remove_probe['text']=='Insert Hall Probe': 
			self.show_curr_or_volt['text'] = 'Show Current'
			self.insert_remove_probe['text']='Remove Hall Probe'

			self.Amp['state'] = 'normal'
			self.thickness['state'] = 'normal'
			self.hall_current['state'] = 'normal'
			self.show_curr_or_volt['state'] = 'normal'

			image = self.canvas2.create_image(0, -5, image = self.bg_image_inserted_hall_effect_mV, anchor = NW)
			flag = 1

		elif self.insert_remove_probe['text']=='Remove Hall Probe':
			self.insert_remove_probe['text']='Insert Hall Probe'
			image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_hall_effect, anchor = NW)
			flag = 0

		# self.show_current_or_voltage_boilerplate()
		if flag == 1:
			self.draw_circular_scale()
			self.canvas2.create_line(self.current_reading_coordinates[self.Amp.get()][0], self.current_reading_coordinates[self.Amp.get()][1], 170, 460)
		else:
			self.draw_circular_scale()
			self.canvas2.create_line(self.current_reading_coordinates[0.0][0], self.current_reading_coordinates[0.0][1], 170, 460)


	# ================================================================================================================================================
	# Boilerplate for setting value of current_or_voltage label when "Hall Effect Setup is selected."
	def show_current_or_voltage_boilerplate(self):
		self.canvas2.delete('all')
		image = self.canvas2.create_image(0, -5, image = self.bg_image_inserted_hall_effect_mA, anchor = NW)
		self.draw_circular_scale()
		self.canvas2.create_line(self.current_reading_coordinates[self.Amp.get()][0], self.current_reading_coordinates[self.Amp.get()][1], 170, 460)

		if self.show_curr_or_volt['text'] == 'Show Current':
			image = self.canvas2.create_image(0, -5, image = self.bg_image_inserted_hall_effect_mV, anchor = NW)
			self.draw_circular_scale()
			self.canvas2.create_line(self.current_reading_coordinates[self.Amp.get()][0], self.current_reading_coordinates[self.Amp.get()][1], 170, 460)
			
			self.current_voltage['text'] = round(self.hall_voltage_dict[self.hall_current.get()] * self.Amp.get() / (self.thickness.get() * 10), 3)
		elif self.show_curr_or_volt['text'] == 'Show Voltage':
			image = self.canvas2.create_image(0, -5, image = self.bg_image_inserted_hall_effect_mA, anchor = NW)
			self.draw_circular_scale()
			self.canvas2.create_line(self.current_reading_coordinates[self.Amp.get()][0], self.current_reading_coordinates[self.Amp.get()][1], 170, 460)

			self.current_voltage['text'] = round(self.hall_current.get(), 3)

	# ================================================================================================================================================
	def show_current_or_voltage_method(self, value):
		# print(value)
		if self.var1.get()==1:
			self.current_voltage['text'] = self.amp_dict[self.Amp.get()]
			
			self.canvas2.delete('all')
			image = self.canvas2.create_image(0, -5, image = self.bg_image_inserted_magnetic_field, anchor = NW)
			self.draw_circular_scale()
			self.canvas2.create_line(self.current_reading_coordinates[self.Amp.get()][0], self.current_reading_coordinates[self.Amp.get()][1], 170, 460)

		elif self.var1.get()==2: self.show_current_or_voltage_boilerplate()


	# ================================================================================================================================================
	def curr_or_volt_selector(self):
		if self.show_curr_or_volt['text'] == 'Show Current':	self.show_curr_or_volt['text'] = 'Show Voltage'
		elif self.show_curr_or_volt['text'] == 'Show Voltage':	self.show_curr_or_volt['text'] = 'Show Current'

		self.show_current_or_voltage_boilerplate()



	# ================================================================================================================================================
	def __init__(self,master):
		self.amp_dict = {1.0: 0.1482, 1.5: 0.2223, 2.0: 0.2964, 2.5: 0.3706, 3.0: 0.4447, 3.5: 0.5188, 4.0: 0.5929, 4.5: 0.6670, 5.0: 0.7411}

		self.hall_voltage_dict = {1.0:28.756, 1.5:43.133, 2.0:57.511, 2.5:71.889, 3.0:86.267, 3.5:100.645, 4.0:115.023, 4.5:129.400, 5.0:143.778}

		self.current_reading_coordinates = {0.0: [100.0588219759603, 462.86907940105993], 0.5: [100.5544553882931, 451.2070293083948],
											1.0: [102.98108686406984, 439.7894759573472], 1.5: [107.27124165445503, 428.9338950554431],
											2.0: [113.30562800879105, 418.9421361427263], 2.5: [120.91645419285712, 410.0920293840943],
											3.0: [129.8920940943546, 402.6296602427361],  3.5: [139.98297168411042, 396.7625268445751],
											4.0: [150.90850071007293, 392.6537702995727], 4.5: [162.36488665944532, 390.41763841118296],
											5.0: [174.0335740481285, 390.1163089097445]
											}
		# ===========================================================================================================================================
		# root
		# self.root = Tk(); 
		self.root = Toplevel(master); 
		self.root.geometry("1050x600"); self.root.title("Resistance by Four Probe Method"); 
		self.root.resizable(0,0); self.root.iconbitmap('..\\img\\logos-and-icons\\AEC_logo.ico')

		# canvas1 (left side)
		self.canvas1 = Canvas(self.root, width=200, bg="peach puff3"); self.canvas1.pack(side='left', fill = 'both', expand=1); 
		def moved(event): self.canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.canvas1.bind("<Motion>", moved); tag = self.canvas1.create_text(10, 10, text="", anchor="nw")

		# canvas2 (right side)
		self.canvas2 = Canvas(self.root, width=500, bg="white"); self.canvas2.pack(side='left', fill = 'both', expand=1); 
		def moved(event): self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")

		# Background images for canvas2
		self.bg_image_inserted_magnetic_field = ImageTk.PhotoImage(Image.open('..\\img\\hall-effect\\hall_effect_insert_magnetic_field.jpg').resize((670, 630), Image.ANTIALIAS))
		self.bg_image_removed_magnetic_field  = ImageTk.PhotoImage(Image.open('..\\img\\hall-effect\\hall_effect_remove_magnetic_field.jpg').resize((670, 630), Image.ANTIALIAS))
		
		self.bg_image_removed_hall_effect     = ImageTk.PhotoImage(Image.open('..\\img\\hall-effect\\hall_effect_remove_hall_probe.jpg').resize((670, 630), Image.ANTIALIAS))
		self.bg_image_inserted_hall_effect_mA = ImageTk.PhotoImage(Image.open('..\\img\\hall-effect\\hall_effect_insert_hall_probe_mA.jpg').resize((670, 630), Image.ANTIALIAS))
		self.bg_image_inserted_hall_effect_mV = ImageTk.PhotoImage(Image.open('..\\img\\hall-effect\\hall_effect_insert_hall_probe_mV.jpg').resize((670, 630), Image.ANTIALIAS))




		# ===========================================================================================================================================
		#canvas1
		# Instruction button===================
		self.instr = Button(self.canvas1, text='Instruction', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.instr)
		self.instr.place(x=30, y=30)

		Label(self.canvas1,text='Select Procedure : ',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=70)

		# Radio buttons========================
		self.var1 = IntVar()
		self.mgntc_fld_vs_crrnt=Radiobutton(self.canvas1,text='Magnetic Field vs Current',font=('Courier',12,'bold'),variable=self.var1,value=1,bg='peach puff3',command=self.procedure_setup)
		self.mgntc_fld_vs_crrnt.place(x=30,y=90)

		self.hall_effct = Radiobutton(self.canvas1,text='Hall Effect', font=('Courier',12,'bold'), variable=self.var1,value=2, bg='peach puff3', command=self.procedure_setup) 
		self.hall_effct.place(x=30,y=120)



		# Insert probe / Insert hall probe===============================================
		self.insert_remove_probe = Button(self.canvas1, text='Insert/Remove', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.insert_remove_probe_method)
		self.insert_remove_probe.place(x=30, y=150) 
		self.insert_remove_probe['state'] = 'disabled'



		# Current in ampere (Used while measuring magnetic field vs current)=============
		Label(self.canvas1,text='Current (in ampere): ',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=190)
		self.Amp = Scale(self.canvas1, from_=1, to=5,bg='lemon chiffon',orient=HORIZONTAL,length=300, tickinterval=0.5, resolution = 0.5, command=self.show_current_or_voltage_method)
		self.Amp.place(x=25,y=210); self.Amp.set(1)
		self.Amp['state'] = 'disabled'

		# Thickness & hall current (Used while using Hall Effect Setup)
		Label(self.canvas1,text='Thickness (in mm): ',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=290)
		self.thickness = Scale(self.canvas1, from_=0.1, to=0.9,bg='lemon chiffon',orient=HORIZONTAL,length=300, tickinterval=0.1, resolution = 0.1, command=self.show_current_or_voltage_method)
		self.thickness.place(x=25,y=320); self.thickness.set(0.1)
		self.thickness['state'] = 'disabled'

		Label(self.canvas1,text='Hall Current (in mAmp): ',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=390)
		self.hall_current = Scale(self.canvas1, from_=1, to=5, bg='lemon chiffon',orient=HORIZONTAL,length=300,tickinterval=0.5, resolution = 0.5, command=self.show_current_or_voltage_method)
		self.hall_current.place(x=25,y=420); self.hall_current.set(1)
		self.hall_current['state'] = 'disabled'



		# Buttons on lower section of Canvas1===========================================
		self.show_curr_or_volt = Button(self.canvas1, text='Show Current', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.curr_or_volt_selector)
		self.show_curr_or_volt.place(x=30, y=500); self.show_curr_or_volt['state']='disabled'

		self.reset = Button(self.canvas1, text='Reset', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.total_reset_method)
		self.reset.place(x=170, y=500)


		# ===========================================================================================================================================
		#canvas2

		# Use the image as background in canvas2.
		# image = self.canvas2.create_image(0, -5, image = self.bg_image, anchor = NW)
		image = self.canvas2.create_image(0, -5, image = self.bg_image_removed_magnetic_field, anchor = NW)

		self.current_voltage = Label(self.canvas2,text='00.00',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left')
		self.current_voltage.place(x=468, y=385)

		self.t = np.linspace(-10, 10, 600)
		self.x1 = 170 + 100 * np.cos(self.t); self.y1 = 460 + 100 * np.sin(self.t); self.x1 = self.x1[16:68]; self.y1 = self.y1[16:68]
		self.x2 = 170 +  70 * np.cos(self.t); self.y2 = 460 +  70 * np.sin(self.t); self.x2 = self.x2[16:68]; self.y2 = self.y2[16:68]
		self.x3 = 170 +  80 * np.cos(self.t); self.y3 = 460 +  80 * np.sin(self.t); self.x3 = self.x3[16:68]; self.y3 = self.y3[16:68]
		self.x4 = 170 +  90 * np.cos(self.t); self.y4 = 460 +  90 * np.sin(self.t); self.x4 = self.x4[16:68]; self.y4 = self.y4[16:68]
		# self.t1= np.linspace(-10, 10, 1800)
		# self.x_dense=200+160*np.cos(self.t1);self.y_dense=550+160*np.sin(self.t1);self.x_dense=self.x_dense[95:285];self.y_dense=self.y_dense[95:285]
		
		self.draw_circular_scale()
		self.canvas2.create_line(self.current_reading_coordinates[0.0][0], self.current_reading_coordinates[0.0][1], 170, 460)

		self.root.mainloop()


# Hall_Effect(None)