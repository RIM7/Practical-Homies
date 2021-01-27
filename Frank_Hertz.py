from tkinter import *
from tkinter import font; from time import sleep;
from random import randint; from PIL import ImageTk, Image
from os import getcwd, startfile

class Frank_Hertz():
    def shower(self,number):
        number = str(round(number,3))
        i = number.index('.'); l = len(number)
        if i == 2: pass
        if i == 1: number = '0'+number
        if l-1==i:     number = number + '000'
        elif l-1-i==1: number = number + '00'
        elif l-1-i==2: number = number + '0'
        return number

    def instr(self):
        startfile('Frank-Hertz.pdf')

    def on(self):
        self.filament_knob.configure(image = self.filament_on)
        self.left['state']='normal'
        self.right['state']='normal'
        self.reset['state']='normal'
        try:
        	self.reset_func()
        except:
        	pass

    def off(self):
        self.filament_knob.configure(image = self.filament_off)
        self.left['state']='disabled'
        self.right['state']='disabled'
        self.reset['state']='disabled'
        try:
        	self.reset_func()
        except:
        	pass

    def left_right(self,direction):
        #global g1k_val, g2a_val, g2k_val, temperature, index, index_check, text
        if round(self.g1k_val,1)!=1.5 or round(self.g2a_val,1)!=7.5 or round(self.g2k_val,1)<=9: self.t.config(text='00.000')
        if self.var.get()==1:
            if direction==1: self.g1k_val -= 0.1; self.v.config(text=self.shower(self.g1k_val))
            else:            self.g1k_val += 0.1; self.v.config(text=self.shower(self.g1k_val))
        elif self.var.get()==2:
            if direction==1: self.g2a_val -= 0.1; self.v.config(text=self.shower(self.g2a_val))
            else:            self.g2a_val += 0.1; self.v.config(text=self.shower(self.g2a_val))

        elif self.var.get()==3:
            if round(self.g2k_val,1)>=79:  self.right['state']='disabled'
            elif round(self.g2k_val,1)<=1: self.left['state']='disabled'

            if direction==1 and self.index>=0:
                if self.g2k_val>=10 and self.g2k_val%2==0: self.index-=1
                self.g2k_val -= 1; self.v.config(text=self.shower(self.g2k_val))

                self.index_check -= 1
                if round(self.g2k_val,1)>=10 and round(self.g2k_val,1)%2==0:   self.text=round(self.temperature[self.index],3); self.sel1()
                elif round(self.g2k_val,1)>=10 and round(self.g2k_val%2,1)!=0: self.text=round((self.temperature[self.index]+self.temperature[self.index+1])/2,3); self.sel1()
                elif round(self.g2k_val,1)<=9: self.t.config(text='00.000')
                if self.index+1<len(self.temperature): self.right['state']='normal'

            elif direction==2 and self.index+1<len(self.temperature):
                self.g2k_val += 1; self.v.config(text=self.shower(self.g2k_val))
                if self.g2k_val>=10 and self.g2k_val%2==0: self.index += 1

                self.index_check += 1
                if self.g2k_val>=10 and self.g2k_val%2==0:   self.text=round(self.temperature[self.index],3); self.sel1()
                elif self.g2k_val>=10 and self.g2k_val%2!=0: self.text=round((self.temperature[self.index]+self.temperature[self.index+1])/2,3); self.sel1()
                if self.index>0:                             self.right['state']='normal'    #print(index_check)

    def reset_func(self):
        #global g1k_val, g2a_val, g2k_val, index; 
        self.g1k_val = 1.4; self.g2a_val = 7.3; self.g2k_val = 9.0; self.index=-1; self.index_check = 9
        self.v.config(text='00.000'); self.t.config(text='00.000')

    def sel(self):
        #global g1k_val, g2a_val, g2k_val
        if self.var.get()==1:   self.l.config(text='G1K');self.v.config(text=self.shower(self.g1k_val));self.left['state']='normal';self.right['state']='normal'
        elif self.var.get()==2: self.l.config(text='G2A');self.v.config(text=self.shower(self.g2a_val)); self.left['state']='normal';self.right['state']='normal'
        elif self.var.get()==3: 
            self.l.config(text='G2K');self.v.config(text=self.shower(self.g2k_val))
            if self.g1k_val==1.5 and self.g2a_val==7.5:  self.left['state']='normal'; self.right['state']='normal'
            elif round(self.g1k_val,1)!=1.5 or round(self.g2a_val,1)!=7.5: self.left['state']='disabled'; self.right['state']='disabled'

    def sel1(self):
        #global index_check, temperature, change_of_scale1, change_of_scale2, text
        if self.var1.get()==-9:   self.panel.configure(image=self.img9);
        elif self.var1.get()==-8: self.panel.configure(image=self.img7);
        elif self.var1.get()==-7: self.panel.configure(image=self.img8);
            
        if self.var1.get()==-9 and self.index_check >= 10 and self.index_check <= self.change_of_scale1:                     self.t.config(text=self.shower(self.text*100))
        elif self.var1.get()==-8 and self.index_check > self.change_of_scale1 and self.index_check <= self.change_of_scale2: self.t.config(text=self.shower(self.text*10))
        elif self.var1.get()==-7 and self.index_check > self.change_of_scale2:                                               self.t.config(text=self.shower(self.text))
        else: self.t.config(text='00.000')          


    def __init__(self, master):
        self.g1k_val = randint(0,3) + randint(0,9)*0.1; self.g2a_val=randint(4,8)+randint(0,9)*0.1; self.g2k_val=float(randint(5,9)); self.text = ''
        self.change_of_scale1 = randint(13, 15); self.change_of_scale2 = randint(39, 42)

        self.temperature = [[0.02, 0.14, 0.210, 0.280, 0.298, 0.327, 0.327, 0.305, 0.375, 0.570, 0.730, 0.830, 0.753, 0.750, 1.370, 2.01, 2.55, 2.69, 2.20, 2.46, 4.08, 
                            5.50, 5.99, 5.43, 3.99, 4.79, 6.57, 7.91, 8.07, 7.10, 5.38, 6.47, 9.03, 10.76 , 10.79, 9.53],
                            [0.05, 0.184, 0.262, 0.317, 0.350, 0.362, 0.343, 0.328, 0.403, 0.582, 0.708, 0.759, 0.758, 0.782, 2.130, 3.210, 3.99, 4.36, 3.49, 3.75,6.72, 
                            9.00, 10.11, 9.36, 6.89, 8.14, 12.24, 15.15, 15.85, 14.19, 10.37, 12.20, 17.32, 16.79, 18.72, 16.48],
                            [0.04, 0.25, 0.42, 0.51, 0.57, 0.60, 0.56, 0.50, 0.55, 0.68, 0.78, 0.80, 0.68, 0.57, 0.79, 1.22, 1.43, 1.39, 
                            1.07, 1.04, 1.88, 2.66, 3.09, 2.95, 2.32, 2.73, 4.82, 6.77, 7.55, 7.04, 5.36, 6.22, 9.76, 13.16, 13.99, 12.53]][randint(0, 2)]
        self.index=-1; self.index_check = 9


        #self.root = Tk()
        self.root = Toplevel(master);self.root.geometry("1000x600");
        self.root.title("Frank Hertz");self.root.resizable(0,0);self.root.iconbitmap(getcwd()+'\\AEC_logo.ico')

        self.canvas1 = Canvas(self.root, width=200, bg="peach puff3"); self.canvas1.pack(side='left', fill = 'both', expand=1); 
        def moved(event): self.canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas1.bind("<Motion>", moved); tag = self.canvas1.create_text(10, 10, text="", anchor="nw")

        self.canvas2 = Canvas(self.root, width=500, bg="white"); self.canvas2.pack(side='left', fill = 'both', expand=1); 
        def moved(event): self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")


        #canvas1===========================================================================================================
        self.instr=Button(self.canvas1,text='Instruction',font=('Courier',12,'bold'),bg='peach puff3',justify='left',command=self.instr);self.instr.place(x=25,y=40)

        self.canvas1.create_line(0, 85, 350, 85)

        Label(self.canvas1,text='Adjust V   :',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=270)
        self.l=Label(self.canvas1,text='__',font=('Courier',10,'bold'),bg='peach puff3',justify='left'); self.l.place(x=115,y=280)

        self.left=Button(self.canvas1,text='Left',font=('Courier',12,'bold'),bg='peach puff3',justify='left',command=lambda:self.left_right(1)); self.left.place(x=170, y=270)
        self.right=Button(self.canvas1,text='Right',font=('Courier',12,'bold'),bg='peach puff3',justify='left',command=lambda:self.left_right(2)); self.right.place(x=240, y=270)
        self.reset=Button(self.canvas1,text='Reset',font=('Courier',12,'bold'),bg='peach puff3',justify='left',command=self.reset_func); self.reset.place(x=240, y=320)


        Label(self.canvas1,text='Switching the filament: ',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=100)
        self.On=Button(self.canvas1,text='On',font=('Courier',12,'bold'),bg='peach puff3',justify='left',command=self.on);self.On.place(x=275, y=105)
        self.Off=Button(self.canvas1,text='Off',font=('Courier',12,'bold'),bg='peach puff3',justify='left',command=self.off);self.Off.place(x=275, y=140)


        Label(self.canvas1,text='Select the range of current:',font=('Courier',12,'bold'),bg='peach puff3',justify='left').place(x=30,y=190)

        self.var1 = IntVar()
        self._9=Radiobutton(self.canvas1,text='10^-9',font=('Courier',12,'bold'),variable=self.var1,value=-9,bg='peach puff3',command=self.sel1); self._9.place(x=230,y=220)
        self._8=Radiobutton(self.canvas1,text='10^-8',font=('Courier',12,'bold'),variable=self.var1,value=-8,bg='peach puff3',command=self.sel1); self._8.place(x=130,y=220)
        self._7=Radiobutton(self.canvas1,text='10^-7',font=('Courier',12,'bold'),variable=self.var1,value=-7,bg='peach puff3',command=self.sel1); self._7.place(x=30,y=220)



        #canvas2===========================================================================================================

        self.img0 = ImageTk.PhotoImage(Image.open('Frank_Hertz_0.jpg')); self.panel=Label(self.canvas2,image=self.img0,bd=0); self.panel.place(x=5,y=-50)

        self.filament_off = ImageTk.PhotoImage(Image.open(getcwd() + '\\filament_off.jpg').resize((74, 74), Image.ANTIALIAS))
        self.filament_on  = ImageTk.PhotoImage(Image.open(getcwd() + '\\filament_on.jpg').resize((74, 74), Image.ANTIALIAS))
        self.filament_knob = Label(self.canvas2,image=self.filament_off,bd=0); self.filament_knob.place(x=224,y=259)

        self.off()


        self.t=Label(self.canvas2,text='00.000',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left'); self.t.place(x=95,y=205)
        self.v=Label(self.canvas2,text='00.000',font=('Courier',12,'bold'),bg='black',fg='cyan',justify='left'); self.v.place(x=480,y=205)

        self.var = IntVar()
        self.v_g1k=Radiobutton(self.canvas2,text='',font=('Courier',1,'bold'),variable=self.var,value=1,bg='gainsboro',command=self.sel); self.v_g1k.place(x=469,y=305)
        self.v_g2a=Radiobutton(self.canvas2,text='',font=('Courier',1,'bold'),variable=self.var,value=2,bg='gainsboro',command=self.sel); self.v_g2a.place(x=514,y=305)
        self.v_g2k=Radiobutton(self.canvas2,text='',font=('Courier',1,'bold'),variable=self.var,value=3,bg='gainsboro',command=self.sel); self.v_g2k.place(x=554,y=305)

        #print(self.change_of_scale1, self.change_of_scale2)

        self.img9 = ImageTk.PhotoImage(Image.open('Frank_Hertz_9.jpg'))
        self.img8 = ImageTk.PhotoImage(Image.open('Frank_Hertz_8.jpg'))
        self.img7 = ImageTk.PhotoImage(Image.open('Frank_Hertz_7.jpg'))
  
        self.root.mainloop()


#frank_hertz = Frank_Hertz(None)