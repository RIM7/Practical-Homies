import tkinter as tk; from tkinter import *; from tkinter import font; import numpy as np; import webbrowser; import time; 
from time import sleep; from datetime import datetime; from random import randint
from PIL import ImageTk, Image
from os import chdir, path, getcwd, system, startfile


from Vernier_Callipers import Vernier_Callipers
from Screw_Gauge import Screw_Gauge
#Utility functions=================================================================================
#==================================================================================================
class Tortional_Pendulum():
    setup_val = 3; L=0; r=0; M=0; R=0; ita = 8.9*10**11; theta = 10
    minutes=0; seconds=0; milliseconds=0; stopper = 0; animator = 0; drawing_osc = 0
    
    class StopWatch(Frame):  
        def __init__(self, root, canvas, parent=None, **kw):
            Frame.__init__(self,root,kw);self.startTime=0.0;self.nextTime=0.0;self.onRunning=0;self.timestr=StringVar();self.MakeWidget();self.canva=canvas
        def MakeWidget(self):
            timeText=Label(self,textvariable=self.timestr,font=("Courier",12),fg="pale turquoise",bg="black"); self.SetTime(self.nextTime); timeText.pack(fill=X,expand=NO,pady=2,padx=2) 
        def Updater(self):
            self.nextTime = time.time () - self.startTime; self.SetTime(self.nextTime); self.timer = self.after(50, self.Updater)
        def SetTime(self, nextElap):
            minutes = int(nextElap / 60); seconds = int(nextElap - minutes * 60.0); 
            miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100); 
            self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
        def Start(self):
            if not self.onRunning:
                self.startTime = time.time() - self.nextTime; self.Updater(); self.onRunning = 1;
                Tortional_Pendulum.draw_on_next_canvas(self.canva)
        def Stop(self):
            if self.onRunning:
                self.after_cancel(self.timer);    self.nextTime = time.time() - self.startTime; self.SetTime(self.nextTime);
                self.onRunning = 0
        def Exit(self):  exit() #self.root.destroy();
        def Reset(self): self.startTime = time.time(); self.nextTime = 0.0; self.SetTime(self.nextTime)


    #Button Click Methods.
    def tort_instr_window(self):
    	startfile('Modulus of rigidity dynamic method.pdf')
    	#webbrowser.open(r'Modulus of rigidity dynamic method.pdf')#webbrowser.open("https://www.youtube.com/watch?v=07d2dXHYb94", new=1)

    def commit(self):
        try:
            self.setup_val = int(self.setup.get()); self.ok_button['state']='normal'; #self.vern['state']='normal'; self.screw['state']='normal'
            self.now_open['text']='Now open\n1. Vernier Callipers to measure R\n2. Screw Gauge to measure r'
        except: pass 


    def measures(self, op):
        if op=='vern':
            #if self.setup_val==1: self.vern['state']='disabled';
            vern_cal = Vernier_Callipers(self.root, self.setup_val, self.R, 6.0)
        elif op=='screw':
            #if self.setup_val==1: self.screw['state']='disabled'
            screw_gauge_obj = Screw_Gauge(self.setup_val, self.r)


    def ok_clicked(self):
        try:    self.canvas.delete('all');
        except: pass
        
        if self.setup_val==1: self.ok_button['state']='disabled';
        try:
            if self.setup_val==int(self.setup.get()): pass
        except:
            popup = Tk(); popup.wm_title("Note"); popup.configure(background='lemon chiffon'); msg = '   You need to enter the number of times   \n   the setup is supposed to be constant.   '
            Label(popup, text=msg, justify='center', font=('Courier', 12, 'bold'), bg='lemon chiffon'); pack(side="top", fill="x", pady=10)
            B1 = Button(popup, text="Okay",font=('Courier',12,'bold'),bg='lemon chiffon',command=popup.destroy); B1.pack(); popup.mainloop()
        try:
            if self.setup_val==int(self.setup.get()):
                Tortional_Pendulum.L = [ 20,   30,   40,   50,   60,    70,   80,   90][randint(0,7)]; Tortional_Pendulum.r = [0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12][randint(0,7)]
                Tortional_Pendulum.M = [1500, 1900, 2300, 2700, 3100, 3500, 3900, 4300][randint(0,7)]; Tortional_Pendulum.R = [ 3.3,  3.4,  3.5,  3.6,  3.7,  3.8,  3.9,  4.0][randint(0,7)]
        except: pass

        if self.setup_val>0:
            self.setup_val -= 1
            if self.setup_val==0: self.setup_val = int(self.setup.get())

        #print('L, r, M, R', self.L, self.r, self.M, self.R)

        self.L_and_M_value.config(text=str(self.L)+' cm\n'+str(self.M)+' g')

        Tortional_Pendulum.drawing_osc = self.osc.get()

        self.stopWatch = self.StopWatch(self.root, self.canvas); self.stopWatch.pack(); self.stopWatch.place(x=30, y=340)
        self.Start=Button(self.canvas1,text='Start', command=self.stopWatch.Start, width=5); self.Start.pack(); self.Start.place(x=30, y=380)
        self.Stop =Button(self.canvas1,text='Stop',  command=self.stopWatch.Stop,  width=5); self.Stop.pack(); self.Stop.place(x=80, y=380)
        self.Reset=Button(self.canvas1,text='Reset', command=self.stopWatch.Reset, width=5); self.Reset.pack();self.Reset.place(x=130, y=380)
        self.Exit =Button(self.canvas1,text='Close', command=self.stopWatch.Exit,  width=5); self.Exit.pack(); self.Exit.place(x=180, y=380)
        



    def __init__(self,master):
        #self.root = Tk()
        self.root = Toplevel(master);
        self.root.geometry('1100x600');self.root.title("Modulus of rigidity - Dynamic Method"); 
        self.root.iconbitmap(getcwd() + '\\AEC_logo.ico'); self.root.resizable(0, 0)
        
        self.frame = Frame(self.root); self.frame.pack(fill='both', expand = True)

        #Creating the canvas1 to take inputs.
        self.canvas1 = Canvas(self.frame, bg = 'peach puff3', width=380); self.canvas1.pack(side='left', fill = 'both')
        def moved(event): self.canvas1.itemconfigure(tag1, text="(%r, %r)" % (event.x, event.y))
        self.canvas1.bind("<Motion>", moved); tag1 = self.canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

        #Creating the canvas for animation
        self.canvas = Canvas(self.frame, bg = 'lemon chiffon', width=400, height=700); self.canvas.pack(side='left', fill = 'both', expand = YES) 
        def moved(event): self.canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas.bind("<Motion>", moved); tag = self.canvas.create_text(10, 10, text="", anchor="nw")
        
        #Creating the canvas for the image.
        self.canvas2 = Canvas(self.frame, bg = 'white', width=300, height=700); self.canvas2.pack(side='left', fill = 'both', expand = YES) 
        def moved(event):  self.canvas2.itemconfigure(tag2, text="(%r, %r)" % (event.x, event.y))
        self.canvas2.bind("<Motion>", moved); tag2 = self.canvas2.create_text(10, 10, text="", anchor="nw")
        
        img = ImageTk.PhotoImage(Image.open(getcwd() + '\\Tortional_Pendulum_Diagram.jpg').resize((260, 500), Image.ANTIALIAS))
        self.panel=Label(self.canvas2,image=img,bd=0);self.panel.pack(side="bottom",fill="both",expand="yes");self.panel.pack();self.panel.place(x=20,y=50)

        #instruction window button.
        self.instr_tortional_butt = Button(self.canvas1, text="Instructions", bg='peach puff3', command=self.tort_instr_window)
        self.instr_tortional_butt.config(font=("Courier", 12, 'bold')); self.instr_tortional_butt.pack(); self.instr_tortional_butt.place(x=30, y=30)
        
        self.canvas1.create_line(0, 75, 400, 75, width=2)

        Label(self.canvas1,text='Enter the validity of the setup\n(in iterations):                ',justify=LEFT,bg='peach puff3', font=("Courier", 12, 'bold')).place(x=30, y=90)
        self.setup = Entry(self.canvas1, relief=tk.FLAT, width = 20, font=("Courier", 12, 'bold')); self.setup.place(x=30, y=140);
        self.commit = Button(self.canvas1, text="Commit", bg='peach puff3', font=("Courier", 12, 'bold'), command=self.commit); self.commit.place(x=270, y=135)
        Label(self.canvas1,text='Enter the no. of oscillations:',justify=LEFT, bg='peach puff3',fg='black', font=("Courier", 12, 'bold')).place(x=30, y=190)

        self.osc=Entry(self.canvas1,relief=tk.FLAT,width=20);self.osc.place(x=30, y=220); self.osc.config(font=("Courier",12,'bold'))

        self.ok_button = Button(self.canvas1,width=5,text="ok",bg='peach puff3',anchor=CENTER,command=self.ok_clicked)
        self.ok_button.pack(padx=20, pady=20);self.ok_button.place(x=270, y=215);
        self.ok_button.config(font=("Courier", 12, 'bold'))
        self.ok_button['state']='disabled'

        Label(self.canvas1,text='After clicking the ok button,',justify='left',font=('Courier',12,'bold'),bg='peach puff3').place(x=30,y=260)
        self.vern = Button(self.canvas1, width=13, text="1.Calculate R", bg='peach puff3', anchor=CENTER, command=lambda : self.measures('vern'))
        self.vern.pack(padx=20,pady=20);self.vern.place(x=30, y=290); self.vern.config(font=("Courier",12,'bold')); #self.vern['state']='disabled'
        self.screw = Button(self.canvas1,width=13,text="2.Calculate r",bg='peach puff3',anchor=CENTER,command=lambda:self.measures('screw'))
        self.screw.pack(padx=20,pady=20);self.screw.place(x=200, y=290); self.screw.config(font=("Courier", 12, 'bold')); #self.screw['state']='disabled'

        self.l=Label(self.canvas1,text='Other parameters to be assumed\n(All parameters are in CGS):',font=('Courier',12,'bold'),bg='peach puff3',justify='left')
        self.l.place(x=30,y=430); f = font.Font(self.l, self.l.cget("font")); f.configure(underline=True); self.l.configure(font=f)

        Label(self.canvas1,text='L =\nM =',justify='left',font=('Courier',12),bg='peach puff3').place(x=30,y=490)
        self.L_and_M_value=Label(self.canvas1,text='',justify='left',font=('Courier',12),bg='peach puff3'); self.L_and_M_value.place(x=80,y=490)


        self.root.mainloop() 


    @staticmethod
    def circle_of_the_arc(*args):
        start_of_string_x, start_of_string_y, radius_of_bob = args
        t = np.linspace(-10, 10, 200); x = start_of_string_x + radius_of_bob * np.cos(t); 
        y = start_of_string_y+radius_of_bob*np.sin(t); return x, y
    @staticmethod
    def filter_arc_points(*args):
        li, start_of_string_y = args; se = set(); x = []; y = []
        for i in li:
            if i[0] in se or i[1] in se  : continue
            elif i[1] < start_of_string_y: continue
            else: se.add(i[0]); x.append(i[0]); y.append(i[1])
        del(se); return x, y
    @staticmethod
    def select_arc_points(*args): 
        x, y, start_of_string_x, start_of_string_y, end_of_string_x, end_of_string_y, length, theta = args
        li = sorted( [[i, j] for i, j in zip(x, y)], key = lambda x : [x[0], x[1]])  
        left_limit_x  = start_of_string_x-length*np.sin(theta/64); left_limit_y=start_of_string_y+length*np.cos(theta/8)
        right_limit_x = start_of_string_x+length*np.sin(theta/64); right_limit_y=start_of_string_y + length*np.cos(theta/8)
        left_index  = 0; right_index = 0; min_dist_for_left_coord = 10000; min_dist_for_right_coord = 10000
        for curr_index, i in enumerate(li):    #linear search being done on sorted array. Should implement binary search.
            dist_left = np.sqrt(  (i[0] - left_limit_x)**2 + (i[1] - left_limit_y)**2  )
            if dist_left < min_dist_for_left_coord: min_dist_for_left_coord = dist_left; left_index = curr_index
            dist_right = np.sqrt(  (i[0] - right_limit_x)**2 + (i[1] - right_limit_y)**2  )
            if dist_right < min_dist_for_right_coord: min_dist_for_right_coord = dist_right; right_index = curr_index
        if left_index > right_index: left_index, right_index = right_index, left_index 
        li= li[left_index : right_index + 1]; return Tortional_Pendulum.filter_arc_points(li, start_of_string_y)

    #Function for animation=====================================================================
    #===========================================================================================
    @classmethod
    def draw_on_next_canvas(cls,canvas): # global setup_val;global L,r,M,R,ita,theta;L=float(entries[0].get());r=float(entries[1].get());
        try:                             # R=float(entries[2].get())#M=float(entries[3].get());ita=8.9*10**11;theta=10;
            start_of_string_x = 200; start_of_string_y = 330; end_of_string_x =  200;   end_of_string_y = start_of_string_y + Tortional_Pendulum.R
            x, y = Tortional_Pendulum.circle_of_the_arc(start_of_string_x, start_of_string_y, Tortional_Pendulum.R*25)
            x, y = Tortional_Pendulum.select_arc_points(x,y,start_of_string_x,start_of_string_y,end_of_string_x,end_of_string_y,Tortional_Pendulum.R*25,Tortional_Pendulum.theta)
 
            T = ( (4*np.pi*Tortional_Pendulum.L*Tortional_Pendulum.M*Tortional_Pendulum.R**2) / (Tortional_Pendulum.ita*Tortional_Pendulum.r**4) )**0.5; len_x = len(x);
            factor = 0
            if T>=0.0 and T<0.1:   factor = 8
            elif T>=0.1 and T<0.2: factor = 5.5
            elif T>=0.2 and T<0.4: factor = 3
            elif T>=0.4 and T<1.1: factor = 2.3
            elif T>=1.1 and T<1.3: factor = 2.2
            elif T>=1.3 and T<2.7: factor = 2.1
            elif T>=2.7 and T<4.0: factor = 2.05

            time_gap = T / (len_x * factor)
            rad = Tortional_Pendulum.R * 25; loop = int( Tortional_Pendulum.drawing_osc )
            rem_loop = Label(canvas, text='Remaining oscilations: '+str(loop), font=("Courier", 12, 'bold'), bg='lemon chiffon'); rem_loop.place(x=30, y=40);
            while loop>0:
                rem_loop.config(text = 'Remaining oscilations: '+str(loop))
                for i in range(len_x):
                    try:
                        Tortional_Pendulum.top_view = canvas.create_oval((start_of_string_x-rad), (start_of_string_y-rad), (start_of_string_x+rad), (start_of_string_y+rad), fill = 'dark slate gray') 
                        Tortional_Pendulum.indicator = canvas.create_line(start_of_string_x,start_of_string_y,x[i],y[i],fill='snow',width=3) 
                        canvas.update(); time.sleep(time_gap); canvas.delete('all') 
                    except: continue
                for i in range(len_x):
                    try:
                        Tortional_Pendulum.top_view=canvas.create_oval( (start_of_string_x-rad), (start_of_string_y-rad), (start_of_string_x+rad), (start_of_string_y+rad), fill = 'dark slate gray')
                        Tortional_Pendulum.indicator = canvas.create_line(start_of_string_x,start_of_string_y,x[len_x-i],y[len_x-i],fill='snow',width=3)
                        canvas.update(); time.sleep(time_gap); canvas.delete('all')
                    except: continue
                #rem_loop.config(text = 'Remaining oscilations: '+str(loop))
                loop-=1
            rem_loop.config(text = '')
        except: pass

#tort_pend = Tortional_Pendulum(None)