from tkinter import *; from tkinter import font
from time import sleep
from random import randint
from PIL import ImageTk, Image
from os import startfile

class Resistance_by_Four_Probe():
    milliAmp = 0.0; Volt = 0.0; diff = 0.0; diff_of_diff = 0.0; i_temp = 25; Temperature=0.0; run_flag=0; wait_clicked=0

    def instr(self):
        startfile('..\\pdfs\\Four Probe.pdf')

    def setup(self): 
        #global milliAmp, Temperature, Volt, diff, i_temp, run_flag
        self.milliAmp = self.mA.get(); 
        self.Temperature = self.temp.get(); 
        self.i_temp = 25; 
        self.Volt = 0.0291 * self.milliAmp; 
        self.diff = 0.0007 * self.milliAmp
        
        if len(str(float(self.milliAmp)))==3: self.show_mA.config(text='0'+str(float(self.milliAmp))+'0')
        else: self.show_mA.config(text=str(float(self.milliAmp)))
        
        self.show_mV['text']='0.0000'; 
        self.show_oven['text']='00.0';
        self.run_flag = 0
        self.run['state']='normal'
        self.wait['state']='normal'

    def runner(self):
        #global milliAmp, Volt, Temperature, diff, i_temp, run_flag, wait_clicked, show_mV, show_oven
        if self.wait_clicked==0: self.run_flag=1
        else: self.wait_clicked=0
        
        if self.run_flag==1 and self.i_temp<=self.Temperature:
            if self.i_temp==31: 
                self.diff += 0.00012 * self.milliAmp
            elif self.i_temp >= 36 and self.i_temp%5==1:
                if self.milliAmp < 10: 
                    self.diff -= randint(1, 3) / 10000
                else: 
                    self.diff -= randint(3, 6) / 10000

            if self.i_temp<=30:
                if self.i_temp==25 or self.i_temp==26:
                    self.show_mV.configure(text=str(round(self.Volt,4))) 
                    self.show_oven.configure(text=str(float(self.i_temp)))
                else:
                    self.Volt = self.Volt - self.diff / 4;
                    self.show_mV.configure(text=str(round(self.Volt,4))) 
                    self.show_oven.configure(text=str(float(self.i_temp)))
            else:
                self.Volt = self.Volt - self.diff / 5;
                self.show_mV.configure(text=str(round(self.Volt,4))) 
                self.show_oven.configure(text=str(float(self.i_temp)))
            
            self.i_temp+=1   
            
            self.root.after(2000, self.runner)
            
        if self.i_temp>self.Temperature: 
            self.run['state']='disabled' 
            self.wait['state']='disabled' 

    def wait(self): 
        #global run_flag, wait_clicked; 
        self.run_flag=0
        self.wait_clicked=1

    def __init__(self,master):
        self.root = Toplevel(master); self.root.geometry("1000x600"); self.root.title("Resistance by Four Probe Method"); self.root.resizable(0,0); 
        self.root.iconbitmap('..\\img\\logos-and-icons\\AEC_logo.ico')

        self.canvas1 = Canvas(self.root, width=200, bg="peach puff3"); self.canvas1.pack(side='left', fill = 'both', expand=1); 
        def moved(event): self.canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas1.bind("<Motion>", moved); tag = self.canvas1.create_text(10, 10, text="", anchor="nw")

        self.canvas2 = Canvas(self.root, width=500, bg="white"); self.canvas2.pack(side='left', fill = 'both', expand=1); 
        def moved(event): self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")

        self.img1 = ImageTk.PhotoImage(Image.open('..\\img\\res-by-four-probe\\resistivity_by_four_probe.jpg')); 
        self.panel=Label(self.canvas2,image=self.img1); 
        self.panel.place(x=2,y=0)

        #canvas1
        self.instr = Button(self.canvas1, text='Instruction', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.instr)
        self.instr.place(x=25, y=40)

        Label(self.canvas1,text='Select the current range(in mA)',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=25,y=90)
        self.mA = Scale(self.canvas1, from_=1, to=20,bg='lemon chiffon',orient=HORIZONTAL,length=300,tickinterval=1)
        self.mA.place(x=25,y=130); self.mA.set(5)

        Label(self.canvas1,text='Select the temperature range\n(in C)',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=25,y=230)
        self.temp = Scale(self.canvas1, from_=25, to=95, bg='lemon chiffon', orient=HORIZONTAL, length=300, tickinterval=5)
        self.temp.place(x=25,y=280); self.temp.set(5)

        self.set = Button(self.canvas1, text='Set', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.setup)
        self.set.place(x=150, y=360) 

        self.run = Button(self.canvas1, text='Next', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.runner)
        self.run.place(x=200, y=360); self.run['state']='disabled'

        self.wait = Button(self.canvas1, text='Wait', font=('Courier',12,'bold'), bg='peach puff3',justify='left', command=self.wait)
        self.wait.place(x=270, y=360); self.wait['state']='disabled'

        self.l=Label(self.canvas1,text='Other parameters to be assumed:',font=('Courier',12,'bold'),bg='peach puff3',justify='left')
        self.l.place(x=25,y=410); f = font.Font(self.l, self.l.cget("font")); f.configure(underline=True); self.l.configure(font=f)

        self.l=Label(self.canvas1,text='Selected material: Germanium\nRange of oven: x1\nRange of voltmeter: 1V',bg='peach puff3',justify='left')
        self.l.config(font=('Courier',12)); self.l.place(x=25, y=440)

        #canvas2
        self.show_mA=Label(self.canvas2,text='00.00',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left')
        Label(self.canvas2,text='0.0000',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left').place(x=522,y=193)

        self.show_mV=Label(self.canvas2,text='0.0000',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left')
        Label(self.canvas2,text='00.00',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left').place(x=197,y=438)

        self.show_oven=Label(self.canvas2,text='00.0',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left')
        self.show_mA.place(x=57,y=196); self.show_mV.place(x=520,y=193); self.show_oven.place(x=195,y=438)

        Label(self.canvas2,text='Constant Current Source',font=('Courier',10,'bold'),bg='white',justify='left').place(x=60,y=80)
        Label(self.canvas2,text='Digital Microvoltmeter',font=('Courier',10,'bold'),bg='white',justify='left').place(x=410,y=80)
        Label(self.canvas2,text='PID Controlled Oven',font=('Courier',10,'bold'),bg='white',justify='left').place(x=250,y=550)
        Label(self.canvas2,text='X1',font=('Courier',10,'bold'),bg='white',justify='left').place(x=170,y=490)
        Label(self.canvas2,text='X10',font=('Courier',10,'bold'),bg='white',justify='left').place(x=220,y=490)
        Label(self.canvas2,text='ON',font=('Courier',8,'bold'),bg='white',justify='left').place(x=445,y=430)
        Label(self.canvas2,text='Set',font=('Courier',8,'bold'),bg='white',justify='left').place(x=345,y=490)
        Label(self.canvas2,text='Measure',font=('Courier',8,'bold'),bg='white',justify='left').place(x=390,y=475)
        Label(self.canvas2,text='1mV',font=('Courier',6,'bold'),bg='white',justify='left').place(x=478,y=175)
        Label(self.canvas2,text='10mV',font=('Courier',6,'bold'),bg='white',justify='left').place(x=478,y=187)
        Label(self.canvas2,text='100mV',font=('Courier',6,'bold'),bg='white',justify='left').place(x=478,y=198)
        Label(self.canvas2,text='1V',font=('Courier',6,'bold'),bg='white',justify='left').place(x=480,y=209)
        Label(self.canvas2,text='10V',font=('Courier',6,'bold'),bg='white',justify='left').place(x=480,y=220)
        Label(self.canvas2,text='ON',font=('Courier',8,'bold'),bg='white',justify='left').place(x=585,y=230)
        Label(self.canvas2,text='ON',font=('Courier',8,'bold'),bg='white',justify='left').place(x=190,y=220)
        Label(self.canvas2,text='Temperature',font=('Courier',10,'bold'),bg='white',justify='left').place(x=170,y=410)

        self.root.mainloop()

#res_by_four_probe = Resistance_by_Four_Probe(None)