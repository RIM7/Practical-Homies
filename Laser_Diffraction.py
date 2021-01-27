from tkinter import *; import tkinter as tk; from tkinter import font;
from PIL import ImageTk, Image
from os import chdir, path, getcwd, system, startfile
#import math
#from threading import Thread


class Laser_Diffraction():
    def las_dif_instr_func(self):
        startfile('Laser Diffraction.pdf')
    def on(self):
        self.panel.configure(image=self.img2);
        pass
    def off(self):
        self.panel.configure(image=self.img1);
        self.canvas2.delete('all')
        self.canvas2.create_line(20, 220, 980, 220)
        x_inc=0
        for i in range(-200, 201):
            if i%10==0:  self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 190)
            elif i%5==0: self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 205)
            else:        self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 210)
            x_inc += 2.4

    def ok_clicked(self):
        if self.x_entry.get()!='':
            self.canvas2.delete("all")
            self.on()

            def moved(event):  self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
            self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")
            
            self.canvas2.create_line(20, 220, 980, 220)
            x_inc=0
            for i in range(-200, 201):
                if i%10==0:  self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 190)
                elif i%5==0: self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 205)
                else:        self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 210)
                x_inc += 2.4

            #x = 50
            #lambda(wavelength of red light) = 7/10**5 cm [range(6.3, 7.0)] #n = (1, 2)
            #d(grating_spec) = 1/N = 1/300
            #sin_theta = 1 * 300/0.1 * 7/10**5; theta = math.asin(sin_theta); d1 = x * math.tan(theta)
            #sin_theta = 1 * 300/0.1 * 7/10**5; cos_theta = (1-sin_theta**2)**0.5; d1 = x * sin_theta / cos_theta
            #sin_theta = (1 * 300/0.1 * 7/10**5)

            sin_theta = (1 * 300/0.1 * (700/100)/10**5)

            d1 = float(self.x_entry.get()) * sin_theta / (1-sin_theta**2)**0.5
            d2 = float(self.x_entry.get()) * 2 * sin_theta / (1-4 * sin_theta**2)**0.5
            d3 = float(self.x_entry.get()) * 3 * sin_theta / (1-4 * sin_theta**2)**0.5


            self.canvas2.create_oval(490, 90, 510, 110, outline='red3')
            self.canvas2.create_oval(495, 95, 505, 105, fill='red3', outline='red3'); #canvas2.create_oval(498, 98, 502, 102, fill='red3', outline='red3')
            
            d1*=24
            self.canvas2.create_oval(492-d1, 92, 508-d1, 108, outline='red2'); self.canvas2.create_oval(495-d1, 95, 505-d1, 105, fill='red2', outline='red2')
            self.canvas2.create_oval(492+d1, 92, 508+d1, 108, outline='red2'); self.canvas2.create_oval(495+d1, 95, 505+d1, 105, fill='red2', outline='red2')
            
            d2*=24
            self.canvas2.create_oval(494-d2, 94, 506-d2, 106, outline='OrangeRed2'); self.canvas2.create_oval(497-d2, 97, 503-d2, 103, fill='OrangeRed2', outline='OrangeRed2') 
            self.canvas2.create_oval(494+d2, 94, 506+d2, 106, outline='OrangeRed2'); self.canvas2.create_oval(497+d2, 97, 503+d2, 103, fill='OrangeRed2', outline='OrangeRed2')
            
            d3*=24
            self.canvas2.create_oval(497-d3, 97, 503-d3, 103, fill='IndianRed1', outline='red') 
            self.canvas2.create_oval(497+d3, 97, 503+d3, 103, fill='IndianRed1', outline='red')
            
            self.label_erase.config(text='x = ' + str(round(float(self.x_entry.get()), 2)) + 'cm')

    def __init__(self,master):
        self.root = Toplevel(master); 
        self.root.geometry("1000x600"); 
        self.root.title("Determination of Wavelength of Laser Light Using Plane Transmission Diffraction Grating"); 
        self.root.iconbitmap('AEC_logo.ico')
        self.root.resizable(0, 0)
        self.frame = Frame(self.root); self.frame.pack(fill='both', expand = True)

        #canvas1 for image.
        self.canvas1 = Canvas(self.frame, bg = 'peach puff3', height=250) ; self.canvas1.pack(side='top', fill = 'both')
        def moved(event): self.canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas1.bind("<Motion>", moved); tag = self.canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

        self.img1=ImageTk.PhotoImage(Image.open('g_Laser_Diffraction_Grating_off.jpg').resize((550, 200), Image.ANTIALIAS))
        self.img2=ImageTk.PhotoImage(Image.open('g_Laser_Diffraction_Grating_on.jpg').resize((550, 200), Image.ANTIALIAS))
        self.panel=Label(self.canvas1,image=self.img1);self.panel.pack(side="bottom",fill="both",expand="yes");self.panel.place(x=430,y=40)

        self.label_erase = Label(self.canvas1, text='x =  ', font=('Courier', 10, 'bold'), bg='white');
        self.label_erase.pack(); self.label_erase.place(x=740, y=80)


        #canvas2 for actual work.
        self.canvas2 = Canvas(self.frame, bg = 'white'); self.canvas2.pack(side='bottom', fill = 'both', expand = YES) 
        def moved(event):  self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")


        
        self.laser_diff_instr=Button(self.canvas1, bg='peach puff3', text="Instruction",font=("Courier",12,'bold'),anchor=CENTER,command=self.las_dif_instr_func)
        self.laser_diff_instr.pack(); self.laser_diff_instr.place(x=40, y= 10);

        Label(self.canvas1, text='Enter the value of x(in cm):', font=('Courier', 12, 'bold'), bg='peach puff3').place(x=40, y=60)
        self.x_entry=Entry(self.canvas1, bd=4, width=6, relief=tk.FLAT, font=('Courier',12,'bold')); self.x_entry.place(x=330, y=60)

        #Label(self.canvas1, text='Enter the value of lambda:  ', font=('Courier', 12, 'bold'), bg='lemon chiffon').place(x=30, y=100)
        #self.e=Entry(self.canvas1, bd=4 , width=6, relief=tk.FLAT, font=('Courier', 12, 'bold')); self.e.pack(); self.e.place(x=320 , y=100)
        #self.e.insert(0,'700')

        self.l=Label(self.canvas1,text='Other parameters to be assumed:\n',font=('Courier',12,'bold'),bg='peach puff3',justify='left')
        self.l.place(x=30,y=140); f = font.Font(self.l, self.l.cget("font")); f.configure(underline=True); self.l.configure(font=f)
        Label(self.canvas1,text='1.10cm <= x <= 45cm (suggested)\n2.650nm <= Wavelength <= 720nm.',font=('Courier',12),bg='peach puff3',justify='left').place(x=30, y=165)

        self.canvas2.create_line(20, 220, 980, 220)
        x_inc=0
        for i in range(-200, 201):
            if i%10==0:
                label = Label(self.canvas2, text=str(abs(i//10)), font=('Courier', 6, 'bold'), bg='white')
                label.pack(); label.place(x=15+x_inc, y=180)
                self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 190)
            elif i%5==0: self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 205)
            else:        self.canvas2.create_line(20+x_inc, 220, 20+x_inc, 210)
            x_inc += 2.4    
        
        self.use_x=Button(self.canvas1,bg='peach puff3',text="On",font=("Courier",12,'bold'),anchor=CENTER,command=self.ok_clicked); self.use_x.pack(); self.use_x.place(x=365, y= 100); 
        self.Off=Button(self.canvas1,bg='peach puff3',text="Off",font=("Courier",12,'bold'),anchor=CENTER,command=self.off); self.Off.pack();self.Off.place(x=310, y=100);
        self.root.mainloop()

#laser_diff_obj = Laser_Diffraction(None)
#laser_diff_obj = Laser_Diffraction()
