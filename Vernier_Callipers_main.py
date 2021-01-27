from tkinter import *
import tkinter as tk
import webbrowser;
import sys
from os import startfile

#print('Numberofarguments:',len(sys.argv),'arguments.')#print('ArgumentList:',str(sys.argv))#print('ArguList:',type(sys.argv))

class Vernier_Callipers_Main():

	def instr_window(self):
		startfile('Vernier Callipers.pdf')
		#webbrowser.open("https://www.youtube.com/watch?v=07d2dXHYb94", new=1)

	def direction_button(self,direction):
		self.vern_canvas.delete('all')
		def moved(event): self.vern_canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.vern_canvas.bind("<Motion>", moved); tag = self.vern_canvas.create_text(10, 10, text="", anchor="nw")
        
        #global gx, x_stop_left, x_stop_right #global arc_x0, arc_y0, arc_x1, arc_y1; #global px1, py1, px2, py2, px3, py3, px4, py5, px6, py7, px8, py8, px9, py9;    
        #global ax,ay, bx,by, cx,cy, dx,dy, ex,ey, fx,fy, gy, hx,hy, ix,iy, jx,jy; #global x1_vern, x2_vern, x_vern_inc;
        #global useless_ax, useless_ay, useless_bx, useless_by, useless_cx, useless_cy, useless_dx, useless_dy
        
		if self.which_opt == 'width':
			self.vern_canvas.create_oval(145, 245, 145+self.dia, 275);
			self.vern_canvas.create_line(145, 260, 145, 360); self.vern_canvas.create_line(145+self.dia, 260, 145+self.dia, 360);
			self.vern_canvas.create_oval(145, 345, 145+self.dia, 375)
			self.x_stop_left = 145+ self.dia
		elif self.which_opt == 'height':
			self.vern_canvas.create_oval(145-15, 310-40, 145+15, 310+40)
			self.vern_canvas.create_line(145, 270, 145+self.hig, 270); self.vern_canvas.create_line(145, 350, 145+self.hig, 350); 
			self.vern_canvas.create_oval(145+self.hig-15, 310-40, 145+self.hig+15, 310+40)
			self.x_stop_left = 145+ self.hig
        #except: pass
        #============================================================================
        
		if direction=='left':
			if self.x_stop_right >= self.gx:  self.right['state'] = 'normal'
			if self.x_stop_left+1 >= self.gx: self.left['state']  = 'disabled'
			self.arc_x0-=1; self.arc_x1-=1
			self.ax-=1; self.bx-=1; self.cx-=1; self.dx-=1; self.ex-=1; self.fx-=1; self.gx-=1; self.hx-=1; self.ix-=1; self.jx-=1;
			self.x1_vern-=1; self.x2_vern-=1; self.x_vern_inc = 0;
			self.useless_ax-=1; self.useless_bx-=1; self.useless_cx-=1; self.useless_dx-=1; 
		elif direction=='right':
			if self.x_stop_left <= self.gx+1: self.left['state'] = 'normal'
			if self.x_stop_right<= self.gx:   self.right['state'] = 'disabled'
			self.arc_x0+=1; self.arc_x1+=1
			self.ax+=1; self.bx+=1; self.cx+=1; self.dx+=1; self.ex+=1; self.fx+=1; self.gx+=1; self.hx+=1; self.ix+=1; self.jx+=1;
			self.x1_vern+=1; self.x2_vern+=1; self.x_vern_inc = 0;
			self.useless_ax+=1; self.useless_bx+=1; self.useless_cx+=1; self.useless_dx+=1; 
	        
	    #static part
		self.vern_canvas.create_arc(70, 50, 140, 190, start = 0)
		self.vern_canvas.create_line(self.px1,self.py1, self.px2,self.py2,self.px3,self.py3,self.px4,self.py4,self.px5,self.py5,self.px6,self.py6,self.px7,self.py7,self.px8,self.py8,self.px4,self.py4,self.px9,self.py9,self.px1,self.py1,width=1.4)
		self.x_cm_inc = 0
		for i in range(60):
			if i%10==0:             self.vern_canvas.create_line(200 + self.x_cm_inc, 140, 200 + self.x_cm_inc, 120); self.x_cm_inc += 12.7
			elif i%10 in (2,4,6,8): self.vern_canvas.create_line(200 + self.x_cm_inc, 130, 200 + self.x_cm_inc, 120); self.x_cm_inc += 12.7
			else:                   self.vern_canvas.create_line(200 + self.x_cm_inc, 125, 200 + self.x_cm_inc, 120); self.x_cm_inc += 12.7
		self.x_cm_inc = 0
		for i in range(151):
			if i%10==0:   self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 185); self.x_cm_inc += 5
			elif i%10==5: self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 190); self.x_cm_inc += 5
			else:         self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 195); self.x_cm_inc += 5

		#dynamic part-arc
		self.vern_canvas.create_arc(self.arc_x0, self.arc_y0, self.arc_x1, self.arc_y1, start = 90)
		#dynamic part-lines
		self.vern_canvas.create_line(self.ax,self.ay,self.bx,self.by,self.cx,self.cy,self.dx,self.dy,self.ax,self.ay,self.ex,self.ey,self.fx,self.fy,self.gx,self.gy,self.hx,self.hy,self.ix,self.iy,self.ex,self.ey,self.jx,self.jy,self.cx,self.cy, width=1.4)
		#dynamic part-scale body
		self.vern_canvas.create_line(self.useless_ax,self.useless_ay,self.useless_cx,self.useless_cy,self.useless_dx,self.useless_dy,self.useless_bx,self.useless_by,width=1.4)
		#dynamic part-scale body
		for i in range(11): self.vern_canvas.create_line(self.x1_vern + self.x_vern_inc, 230, self.x2_vern + self.x_vern_inc, 210); self.x_vern_inc+=4.5

	#=====================================================================================================================  


	def apply(self):
		#global arc_x0, arc_y0, arc_x1, arc_y1; #global x_stop_left, x_stop_right; global px1, py1, px2, py2, px3, py3, px4, py5, px6, py7, px8, py8, px9, py9;    
	    #global ax,ay, bx,by, cx,cy, dx,dy, ex,ey, fx,fy, gx, gy, hx,hy, ix,iy, jx,jy; global x1_vern, x2_vern, x_vern_inc;  
	    #global dia, hig #global useless_ax, useless_ay, useless_bx, useless_by, useless_cx, useless_cy, useless_dx, useless_dy
	    
		self.vern_canvas.delete('all')
		def moved(event): self.vern_canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.vern_canvas.bind("<Motion>", moved); tag = self.vern_canvas.create_text(10, 10, text="", anchor="nw")

		#drawing the cylinder
		#try: self.dia = float(self.Rad)*2*50;  self.hig = float(self.H)*50
		try: self.dia = float(self.ent.get())*50;  self.hig = float(self.ent.get())*50
		except: self.dia = 2*2*50; self.hig = 4*2*50

		if self.which_opt == 'width':
			self.vern_canvas.create_oval(145, 245, 145+self.dia, 275); self.vern_canvas.create_line(145, 260, 145, 360)
			self.vern_canvas.create_line(145+self.dia, 260, 145+self.dia, 360); self.vern_canvas.create_oval(145, 345, 145+self.dia, 375)
			self.x_stop_left = 145+ self.dia
		elif self.which_opt == 'height':
			self.vern_canvas.create_oval(145-15, 310-40, 145+15, 310+40)
			self.vern_canvas.create_line(145, 270, 145+self.hig, 270)
			self.vern_canvas.create_line(145, 350, 145+self.hig, 350); 
			self.vern_canvas.create_oval(145+self.hig-15, 310-40, 145+self.hig+15, 310+40)
			self.x_stop_left = 145+ self.hig

		self.left['state']='normal'; self.right['state']='normal'

		self.gx = self.x_stop_left

		self.vern_canvas.create_arc(70, 50, 140, 190, start = 0)

		self.px1= 60; self.py1=120;  self.px2=970; self.py2=120;    self.px3=970; py3=210;  px4=145; py4=210
		self.px5=145; self.py5=310;  self.px6=130; self.py6=310;    self.px7=100; py7=245;  px8=100; py8=210;    px9= 60; py9=210;
		self.vern_canvas.create_line(self.px1,self.py1, self.px2,self.py2,self.px3,self.py3,self.px4,self.py4,self.px5,self.py5,self.px6,self.py6,self.px7,self.py7,self.px8,self.py8,self.px4,self.py4,self.px9,self.py9,self.px1,self.py1,width=1.4)
		self.x_cm_inc = 0
		for i in range(60):
			if i%10==0:             self.vern_canvas.create_line(200 + self.x_cm_inc, 140, 200 + self.x_cm_inc, 120); self.x_cm_inc += 12.7
			elif i%10 in (2,4,6,8): self.vern_canvas.create_line(200 + self.x_cm_inc, 130, 200 + self.x_cm_inc, 120); self.x_cm_inc += 12.7
			else:                   self.vern_canvas.create_line(200 + self.x_cm_inc, 125, 200 + self.x_cm_inc, 120); self.x_cm_inc += 12.7
		self.x_cm_inc = 0
		for i in range(151):
			if i%10==0:   self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 185); self.x_cm_inc += 5
			elif i%10==5: self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 190); self.x_cm_inc += 5
			else:         self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 195); self.x_cm_inc += 5

		self.sit=-30
		try:
			if self.which_opt=='width':    self.sit=self.dia
			elif self.which_opt=='height': self.sit=self.hig
		except: pass

		self.ax=160+self.sit+30;self.ay=210;  self.bx=300+self.sit+30;self.by=210;   self.cx=300+self.sit+30;self.cy=230;   self.dx=160+self.sit+30;self.dy=230;  
		self.ex=160+self.sit+30;self.ey=245;  self.fx=145+self.sit+30;self.fy=245;   self.gx=145+self.sit+30;self.gy=310;   self.hx=160+self.sit+30;self.hy=310; 
		self.ix=190+self.sit+30;self.iy=245;  self.jx=300+self.sit+30;self.jy=245
		self.useless_ax=160+self.sit+30; self.useless_bx=300+self.sit+30; self.useless_cx=160+self.sit+30; self.useless_dx=300+self.sit+30;

		#dynamic part-arc
		self.arc_x0=70+self.sit+30; self.arc_x1=140+self.sit+30
		self.vern_canvas.create_arc(self.arc_x0, self.arc_y0, self.arc_x1, self.arc_y1, start = 90)
		#dynamic part-lines
		self.vern_canvas.create_line(self.ax,self.ay,self.bx,self.by,self.cx,self.cy,self.dx,self.dy,self.ax,self.ay, self.ex,self.ey,self.fx,self.fy,self.gx,self.gy,self.hx,self.hy,self.ix,self.iy, self.ex,self.ey, self.jx,self.jy,self.cx,self.cy,width=1.4)
		#dynamic part-scale upper body
		self.vern_canvas.create_line(self.useless_ax,self.useless_ay,self.useless_cx,self.useless_cy,self.useless_dx,self.useless_dy,self.useless_bx,self.useless_by,width=1.4)
		#dynamic part-scale lower body
		self.x1_vern = 160+self.sit+30+40; self.x2_vern = 160+self.sit+30+40; self.x_vern_inc = 0
		for i in range(11): self.vern_canvas.create_line(self.x1_vern + self.x_vern_inc, 230, self.x2_vern + self.x_vern_inc, 210);  self.x_vern_inc += 4.5  
		#except: pass

	def m(self): 
		if self.var.get()==1:   self.which_opt='width'
		elif self.var.get()==2: self.which_opt='height'

	#def __init__(self, master, setup_val, R, h):
	#def __init__(self, master):
	def __init__(self, master):
		self.arc_x0 = 70;       self.arc_y0 = 50;               self.arc_x1 = 140; self.arc_y1 = 190
		self.x_stop_left = 145; self.x_stop_right = 850
		self.dia=0;             self.hig=0;                     self.which_opt=''
		#self.Rad = R #self.Hei = h


		self.vern_root = Toplevel(master);
		#self.vern_root = Tk();
		self.vern_root.geometry('1000x600'); self.vern_root.resizable(0,0); self.vern_root.iconbitmap('AEC_logo.ico')
		try: self.vern_root.title('Vernier Callipers: Measurement number: ' + str(setup_val))
		except: self.vern_root.title('Vernier Callipers')

		self.vern_canvas1 = Canvas(self.vern_root, bg='peach puff3', height=100); self.vern_canvas1.pack(side='top', fill = 'both')
		def moved(event): self.vern_canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.vern_canvas1.bind("<Motion>", moved); tag = self.vern_canvas1.create_text(10, 10, text="", anchor="nw")

		self.vern_canvas = Canvas(self.vern_root, bg='white', height=500); self.vern_canvas.pack(side='bottom', fill = 'both', expand=1)
		def moved(event): self.vern_canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
		self.vern_canvas.bind("<Motion>", moved); tag = self.vern_canvas.create_text(10, 10, text="", anchor="nw")


		#====================================================================================================
		self.vern_canvas.create_arc(70, 50, 140, 190, start = 0)
		self.vern_canvas.create_arc(70, 50, 140, 190, start = 90)

		self.px1= 60; self.py1=120;  self.px2=970; self.py2=120;    self.px3=970; self.py3=210;  self.px4=145; self.py4=210
		self.px5=145; self.py5=310;  self.px6=130; self.py6=310;    self.px7=100; self.py7=245;  self.px8=100; self.py8=210;    self.px9= 60; self.py9=210;
		self.vern_canvas.create_line(self.px1,self.py1, self.px2,self.py2,self.px3,self.py3,self.px4,self.py4,self.px5,self.py5,self.px6,self.py6,self.px7,self.py7,self.px8,self.py8,self.px4,self.py4,self.px9,self.py9,self.px1,self.py1,width=1.4)

		self.x_cm_inc = 0
		for i in range(60):
			if i%10==0:             self.vern_canvas.create_line(200 + self.x_cm_inc, 140, 200 + self.x_cm_inc, 120);  self.x_cm_inc += 12.7
			elif i%10 in (2,4,6,8): self.vern_canvas.create_line(200 + self.x_cm_inc, 130, 200 + self.x_cm_inc, 120);  self.x_cm_inc += 12.7
			else:                   self.vern_canvas.create_line(200 + self.x_cm_inc, 125, 200 + self.x_cm_inc, 120);  self.x_cm_inc += 12.7
	            
		self.x_cm_inc = 0  #x1_cm = 200; x2_cm = 200; 
		for i in range(151):
			if i%10==0:
				self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 185);
				self.label = Label(self.vern_canvas, text=str(i//10), font=("Courier", 10, 'bold'), bg='white'); 
				self.label.pack(); self.label.place(x=200+self.x_cm_inc-5, y=165)
				self.x_cm_inc += 5
			elif i%10==5: self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 190);  self.x_cm_inc += 5
			else:         self.vern_canvas.create_line(200 + self.x_cm_inc, 210, 200 + self.x_cm_inc, 195);  self.x_cm_inc += 5

		self.useless_ax=160; self.useless_ay=120; self.useless_bx=300; self.useless_by=120; self.useless_cx=160; self.useless_cy=100; self.useless_dx=300; self.useless_dy=100
		self.vern_canvas.create_line(self.useless_ax, self.useless_ay, self.useless_cx, self.useless_cy, self.useless_dx, self.useless_dy, self.useless_bx, self.useless_by, width=1.4)

		self.ax = 160; self.ay = 210;    self.bx = 300; self.by = 210;    self.cx = 300; self.cy = 230;    self.dx = 160; self.dy = 230;    self.ex = 160; self.ey = 245;  
		self.fx = 145; self.fy = 245;    self.gx = 145; self.gy = 310;    self.hx = 160; self.hy = 310;    self.ix = 190; self.iy = 245;    self.jx = 300; self.jy = 245
		self.vern_canvas.create_line(self.ax,self.ay,self.bx,self.by,self.cx,self.cy,self.dx,self.dy,self.ax,self.ay,self.ex,self.ey,self.fx,self.fy,self.gx,self.gy,self.hx,self.hy,self.ix,self.iy,self.ex,self.ey,self.jx,self.jy,self.cx,self.cy,width=1.4)
		self.x1_vern = 200; self.x2_vern = 200; self.x_vern_inc = 0
		for i in range(11): self.vern_canvas.create_line(self.x1_vern + self.x_vern_inc, 230, self.x2_vern + self.x_vern_inc, 210);  self.x_vern_inc += 4.5
	        
	    #====================================================================================================
	        
		self.left=Button(self.vern_canvas,width=5,text="Left",anchor=CENTER,command=lambda:self.direction_button('left'))
		self.left.pack(); self.left.place(x=800, y= 400); self.left.config(font=("Courier", 12, 'bold')); self.left['state'] = 'disabled'

		self.right=Button(self.vern_canvas,width=5,text="Right",anchor=CENTER,command=lambda:self.direction_button('right'))
		self.right.pack(); self.right.place(x=900, y= 400); self.right.config(font=("Courier", 12, 'bold'))


	    #=====================================================================================================================
		Label(self.vern_canvas1, text='Enter the value to check:', font=("Courier", 12, 'bold'), bg='peach puff3').place(x=240, y=20)
		self.ent = Entry(self.vern_canvas1, relief=tk.FLAT, width = 10); self.ent.pack(); self.ent.place(x=500, y=20); self.ent.config(font=("Courier", 12, 'bold'))

		self.var=IntVar()
		self.measure1=Radiobutton(self.vern_canvas1,text='Measure by width',width=18,bg='peach puff3',variable=self.var,value=1,command=self.m)
		self.measure1.config(font=("Courier", 12, 'bold')); self.measure1.pack(padx=20, pady=20); self.measure1.place(x=630, y=20);
		self.measure2=Radiobutton(self.vern_canvas1,text='Measure by height',width=18,bg='peach puff3',variable=self.var,value=2,command=self.m);
		self.measure2.config(font=("Courier", 12, 'bold')); self.measure2.pack(padx=20, pady=20); self.measure2.place(x=634, y=60);


		self.apply=Button(self.vern_canvas1,text="Use shape",anchor=CENTER,bg='peach puff3',command=self.apply)
		self.apply.pack(); self.apply.place(x=850, y=60); self.apply.config(font=("Courier", 12, 'bold'))

		self.instr_butt = Button(self.vern_canvas1, text="Instructions", bg='peach puff3', command=self.instr_window)
		self.instr_butt.config(font=("Courier", 12, 'bold')); self.instr_butt.pack(); self.instr_butt.place(x=70, y=20)

		#self.vern_root.mainloop()
		mainloop()

#vernier_callipers = Vernier_Callipers(master)
#vernier_callipers = Vernier_Callipers()
#vernier_callipers = Vernier_Callipers(master, sys.argv[1], sys.argv[2], sys.argv[2])