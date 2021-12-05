from tkinter import *
from tkinter import font;
import numpy as np
from PIL import ImageTk, Image
from os import startfile



class Modulus_of_Rigidity_Static():
    def instr(self):
        startfile('..\\pdfs\\Modulus of rigidity static method.pdf')

    def clicked(self):
        if self.length.get()!='':
            self.canvas2.delete('all');

        def moved(event): self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")  #nw = north-west
        
        #canvas2 contents==========
        #dynamic part of canvas2===
        #Modify  label2 according to the ratio you have onsidered previously for say 10 cm = 50 px. (5x)
        try:
            if int(self.length.get())>45:
                self.panel2.destroy(); self.panel2=Label(self.canvas2, bd=0, image=self.img2); self.panel2.place(x=340-90, y=30)
            elif int(self.length.get())>=10 and int(self.length.get())<=45:
                self.panel2.destroy(); self.panel2=Label(self.canvas2, bd=0, image=self.img2); self.panel2.place(x=340-int(self.length.get())*2, y=30)
                #self.shift = -int(self.length.get()) * 2
            elif int(self.length.get())< 10: 
                self.panel2.destroy(); self.panel2=Label(self.canvas2, bd=0, image=self.img2); self.panel2.place(x=320, y=30)
                #self.shift=0

            #center at 200, 550
            for i in range(len(self.x1)):
                if i%10==0:    self.canvas2.create_line(self.x1[i], self.y1[i], self.x2[i], self.y2[i])
                elif i%5 == 0: self.canvas2.create_line(self.x1[i], self.y1[i], self.x3[i], self.y3[i])
                else:          self.canvas2.create_line(self.x1[i], self.y1[i], self.x4[i], self.y4[i])
            #center at 630, 550
            for i in range(len(self.x1)):
                if i%10==0:    self.canvas2.create_line(self.x1[i]+430, self.y1[i], self.x2[i]+430, self.y2[i])
                elif i%5 == 0: self.canvas2.create_line(self.x1[i]+430, self.y1[i], self.x3[i]+430, self.y3[i])
                else:          self.canvas2.create_line(self.x1[i]+430, self.y1[i], self.x4[i]+430, self.y4[i])
            #the pointer line.=======================================  
            self.phi=int(np.ceil(180*float(self.length.get())*13.21*980 / (np.pi**2 * 0.2345**4)*(float(self.var.get())*500/(8.9 * 10**11))))
            for i in range(len(self.x_dense)): self.canvas2.create_line(self.x_dense[i], self.y_dense[i], self.x_dense[i]+1, self.y_dense[i]+1, width=2)
            for i in range(len(self.x_dense)): self.canvas2.create_line(self.x_dense[i]+430,self.y_dense[i],self.x_dense[i]+431,self.y_dense[i]+1, width=2)

            self.index = 30 + int(self.var.get()); self.canvas2.create_line(self.x2[self.index], self.y2[self.index]+10, 200, 550, width=2)
            self.index = 90 + int(self.var.get()) + self.phi*3 + int(np.random.randint(0, 2)); self.canvas2.create_line(self.x_dense[self.index]+430,self.y_dense[self.index]+10, 630, 550,width=2)
            #print(phi)

        except: pass


    def sel(self):
        if self.var.get()==0:
            self.weight1.configure(image=self.img4); self.weight2.configure(image=self.img4); self.weight3.configure(image=self.img4)
            self.weight4.configure(image=self.img4); self.weight5.configure(image=self.img4); self.weight6.configure(image=self.img4)
        if self.var.get()==1:
            self.weight1.configure(image=self.img3); self.weight2.configure(image=self.img4); self.weight3.configure(image=self.img4)
            self.weight4.configure(image=self.img4); self.weight5.configure(image=self.img4); self.weight6.configure(image=self.img4)
        elif self.var.get()==2:
            self.weight1.configure(image=self.img3); self.weight2.configure(image=self.img3); self.weight3.configure(image=self.img4)
            self.weight4.configure(image=self.img4); self.weight5.configure(image=self.img4); self.weight6.configure(image=self.img4)
        elif self.var.get()==3:
            self.weight1.configure(image=self.img3); self.weight2.configure(image=self.img3); self.weight3.configure(image=self.img3)
            self.weight4.configure(image=self.img4); self.weight5.configure(image=self.img4); self.weight6.configure(image=self.img4)
        elif self.var.get()==4:
            self.weight1.configure(image=self.img3); self.weight2.configure(image=self.img3); self.weight3.configure(image=self.img3)
            self.weight4.configure(image=self.img3); self.weight5.configure(image=self.img4); self.weight6.configure(image=self.img4)
        elif self.var.get()==5:
            self.weight1.configure(image=self.img3); self.weight2.configure(image=self.img3); self.weight3.configure(image=self.img3)
            self.weight4.configure(image=self.img3); self.weight5.configure(image=self.img3); self.weight6.configure(image=self.img4)
        elif self.var.get()==6:
            self.weight1.configure(image=self.img3); self.weight2.configure(image=self.img3); self.weight3.configure(image=self.img3)
            self.weight4.configure(image=self.img3); self.weight5.configure(image=self.img3); self.weight6.configure(image=self.img3)



    def __init__(self,master):
        self.t = np.linspace(-10, 10, 600)
        self.x1 = 200 + 200 * np.cos(self.t); self.y1 = 550 + 200 * np.sin(self.t); self.x1 = self.x1[35:96]; self.y1 = self.y1[35:96]
        self.x2 = 200 + 160 * np.cos(self.t); self.y2 = 550 + 160 * np.sin(self.t); self.x2 = self.x2[35:96]; self.y2 = self.y2[35:96]
        self.x3 = 200 + 175 * np.cos(self.t); self.y3 = 550 + 175 * np.sin(self.t); self.x3 = self.x3[35:96]; self.y3 = self.y3[35:96]
        self.x4 = 200 + 190 * np.cos(self.t); self.y4 = 550 + 190 * np.sin(self.t); self.x4 = self.x4[35:96]; self.y4 = self.y4[35:96]
        self.t1= np.linspace(-10, 10, 1800)
        self.x_dense=200+160*np.cos(self.t1);self.y_dense=550+160*np.sin(self.t1);self.x_dense=self.x_dense[105:285];self.y_dense=self.y_dense[105:285]

        #self.root = Tk();
        self.root = Toplevel(master); self.root.geometry('1100x600'); self.root.resizable(0, 0); self.root.iconbitmap('..\\img\\logos-and-icons\\AEC_logo.ico')
        self.root.title('Determination of modulus of rigidity using static method')
        #root.iconbitmap()
        #self.frame = Frame(root); frame.pack(fill='both', expand = True)
        #Creating the canvas1 to take inputs.
        self.canvas1 = Canvas(self.root, bg = 'peach puff3', width=250) ; self.canvas1.pack(side='left', fill = 'both')
        def moved(event): self.canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas1.bind("<Motion>", moved); tag = self.canvas1.create_text(10, 10, text="", anchor="nw")

        self.canvas2 = Canvas(self.root, bg = 'white', width = 700) ; self.canvas2.pack(side='left', fill = 'both', expand=1)
        def moved(event): self.canvas2.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas2.bind("<Motion>", moved); tag = self.canvas2.create_text(10, 10, text="", anchor="nw")


        #canvas1 contents==========================================================================================================
        self.instr_butt=Button(self.canvas1,text='Instruction',font=('Courier',12,'bold'),bg='peach puff3',command=self.instr);self.instr_butt.place(x=22,y=15)

        Label(self.canvas1,text='Select the weight to\nput in:',font=('Courier',12,'bold'),bg='peach puff3', justify='left').place(x=20,y=50)
        self.var = IntVar()
        self.zero=Radiobutton(self.canvas1,text='   0g',bg='peach puff3',variable=self.var,value=0,font=('Courier',12,'bold'),command=self.sel);self.zero.place(x=130,y=70)
        self.five=Radiobutton(self.canvas1,text=' 500g',bg='peach puff3',variable=self.var,value=1,font=('Courier',12,'bold'),command=self.sel);self.five.place(x=20,y=100)
        self.ten =Radiobutton(self.canvas1,text='1000g',bg='peach puff3',variable=self.var,value=2,font=('Courier',12,'bold'),command=self.sel);self.ten.place(x=130,y=100)
        self.one5=Radiobutton(self.canvas1,text='1500g',bg='peach puff3',variable=self.var,value=3,font=('Courier',12,'bold'),command=self.sel);self.one5.place(x=20,y=130)
        self.two0=Radiobutton(self.canvas1,text='2000g',bg='peach puff3',variable=self.var,value=4,font=('Courier',12,'bold'),command=self.sel);self.two0.place(x=130,y=130)
        self.two5=Radiobutton(self.canvas1,text='2500g',bg='peach puff3',variable=self.var,value=5,font=('Courier',12,'bold'),command=self.sel);self.two5.place(x=20,y=160)
        self.thr0=Radiobutton(self.canvas1,text='3000g',bg='peach puff3',variable=self.var,value=6,font=('Courier',12,'bold'),command=self.sel);self.thr0.place(x=130,y=160)

        self.label = Label(self.canvas1,text='Select the length\nbetween the scales:',font=('Courier',12,'bold'),bg='peach puff3',justify='left'); self.label.place(x=20,y=220)
        self.length = Entry(self.canvas1, font=('Courier', 12, 'bold')); self.length.place(x=20, y=270)
        
        self.ok = Button(self.canvas1, text='ok', font=('Courier',12,'bold'), bg='peach puff3', command=self.clicked); self.ok.place(x=190, y=306)

        self.l=Label(self.canvas1,text='Other parameters to be\nassumed:',font=('Courier',12,'bold'),bg='peach puff3',justify='left')
        self.l.place(x=20,y=380); f = font.Font(self.l, self.l.cget("font")); f.configure(underline=True); self.l.configure(font=f)
        Label(self.canvas1,text='Enter a length between\n10 and 45 for better\nvisuals.',font=('Courier',12),bg='peach puff3',justify='left').place(x=20, y=425)


        #==========================================================================================================================
        #==========================================================================================================================
        #canvas2 contents==========================================================================================================
        #canvas2.create_line(50,40, 800,40, 800,270, 50,270, 50, 40)  #*********to be removed**************
        #Add the labels here. label1, movable -> add the given images.
        #img = ImageTk.PhotoImage(Image.open(getcwd() + '\\Mod_of_Rig_Stat_Method.png'))
        
        self.img1 = ImageTk.PhotoImage(Image.open('..\\img\\modulus-of-rigidity\\Mod_of_Rig_Stat_Method.jpg').resize((640, 310), Image.ANTIALIAS));
        self.panel=Label(self.canvas2,image=self.img1,bd=0); self.panel.place(x=110,y=5)
        self.img2 = ImageTk.PhotoImage(Image.open('..\\img\\modulus-of-rigidity\\Movable_2nd_ptr.jpg').resize((105, 169), Image.ANTIALIAS));
        self.panel2=Label(self.canvas2,image=self.img2,bd=0); self.panel2.place(x=320,y=30)

        self.img3 = ImageTk.PhotoImage(Image.open('..\\img\\modulus-of-rigidity\\unit_weight.jpg').resize((50, 12), Image.ANTIALIAS));
        self.img4 = ImageTk.PhotoImage(Image.open('..\\img\\modulus-of-rigidity\\unit_weight_dummy.jpg').resize((1, 1), Image.ANTIALIAS));

        self.weight1=Label(self.canvas2,image=self.img4,bd=0); self.weight1.place(x=700,y=286)
        self.weight2=Label(self.canvas2,image=self.img4,bd=0); self.weight2.place(x=700,y=274)
        self.weight3=Label(self.canvas2,image=self.img4,bd=0); self.weight3.place(x=700,y=262)
        self.weight4=Label(self.canvas2,image=self.img4,bd=0); self.weight4.place(x=700,y=250)
        self.weight5=Label(self.canvas2,image=self.img4,bd=0); self.weight5.place(x=700,y=238)
        self.weight6=Label(self.canvas2,image=self.img4,bd=0); self.weight6.place(x=700,y=226)


        Label(self.canvas2,text='θ',font=('Courier',18,'bold'),bg='white',justify='left').place(x=30,y=300)
        Label(self.canvas2,text='1',font=('Courier',10,'bold'),bg='white',justify='left').place(x=45,y=320)

        Label(self.canvas2,text='θ',font=('Courier',18,'bold'),bg='white',justify='left').place(x=450,y=300)
        Label(self.canvas2,text='2',font=('Courier',10,'bold'),bg='white',justify='left').place(x=465,y=320)
        #dynamic part of canvas2==============================================================================
        #center at 200, 550
        for i in range(len(self.x1)):
            if i%10==0:    self.canvas2.create_line(self.x1[i], self.y1[i], self.x2[i], self.y2[i])
            elif i%5 == 0: self.canvas2.create_line(self.x1[i], self.y1[i], self.x3[i], self.y3[i])
            else:          self.canvas2.create_line(self.x1[i], self.y1[i], self.x4[i], self.y4[i])
        #center at 630, 550
        for i in range(len(self.x1)):
            if i%10==0:    self.canvas2.create_line(self.x1[i]+430, self.y1[i], self.x2[i]+430, self.y2[i])
            elif i%5 == 0: self.canvas2.create_line(self.x1[i]+430, self.y1[i], self.x3[i]+430, self.y3[i])
            else:          self.canvas2.create_line(self.x1[i]+430, self.y1[i], self.x4[i]+430, self.y4[i])
        #the initial pointer lines at 0.
        self.x = 200 + 150 * np.cos(self.t); self.y = 550 + 150 * np.sin(self.t); self.x = self.x[35:96]; self.y = self.y[35:96]
        self.canvas2.create_line(self.x[30], self.y[30], 200, 550, width=2); self.canvas2.create_line(self.x[30]+430, self.y[30], 630, 550, width=2)

        for i in range(len(self.x_dense)): self.canvas2.create_line(self.x_dense[i], self.y_dense[i], self.x_dense[i]+1, self.y_dense[i]+1, width=2)
        for i in range(len(self.x_dense)): self.canvas2.create_line(self.x_dense[i]+430, self.y_dense[i], self.x_dense[i]+431, self.y_dense[i]+1, width=2)
        #static part of canvas2============================================================================
        self.x = [ 10,  58, 120, 200, 272, 333, 376]
        self.y = [425, 368, 338, 326, 341, 379, 429]
        self.scale=[30, 20, 10, 0, 10, 20, 30]
        for i in range(len(self.x)):
            Label(self.canvas2,text=str(self.scale[i]),font=('Courier',10,'bold'),bg='white',justify='left').place(x=self.x[i],y=self.y[i])
            Label(self.canvas2,text=str(self.scale[i]),font=('Courier',10,'bold'),bg='white',justify='left').place(x=self.x[i]+430,y=self.y[i])
            
            
        self.root.mainloop()