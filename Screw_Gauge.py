from tkinter import *; from os import getcwd, startfile; import webbrowser; #from sys import argv

class Scale():
    def __init__(self, data):
        self.data = data; 
        self.next = None; 
        self.prev = None
       

class Screw_Gauge():
    def instruction_butt(self):
        startfile('Screw Gauge.pdf')
        #webbrowser.open("https://www.youtube.com/watch?v=07d2dXHYb94", new=1)

    def apply_func(self, instr):
        #global applied, x_left_lim, px, qx, rx, sx, tx, ux, grab_x
        if float(self.r)>0.3: pass
        else:
            if instr=='insert':
                self.applied = 1; self.x_left_lim = 449.1+float(self.r)*10*10*2
                self.grab_x = 345; self.px=720; self.qx=650; self.rx=650; self.sx=720; self.tx=980; self.ux=980;    #print(self.param[3])
                self.canvas.create_oval(144.1, 130, 144.1+float(self.r)*10*10*2, 140); self.canvas.create_line(144.1, 135, 144.1, 305)
                self.canvas.create_line(144.1+float(self.r)*10*10*2, 135, 144.1+float(self.r)*10*10*2, 305); 
                self.canvas.create_oval(144.1, 300, 144.1+float(self.r)*10*10*2, 310)
                
                self.direction_button('')
            elif instr=='remove': 
                if self.applied==1: self.left['state']='normal'
                self.applied = 0; self.direction_button(''); self.x_left_lim = 449.1
                self.faster_left['state'] = 'normal'

    def direction_button(self, direction):
        try: self.canvas.delete('all')
        except: pass
        
        def moved(event): self.canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas.bind("<Motion>", moved); tag = self.canvas.create_text(10, 10, text="", anchor="nw")
        
        #dynamic part.
        #movable part on the right side. #global px,py, qx,qy, rx,ry, sx,sy, tx,ty, ux,uy   #->global #global first_thick_line, second_thick_line, third_thick_line

        if self.applied==1: 
            self.canvas.create_oval(144.1, 130, 144.1+float(self.r)*10*10*2, 140); 
            self.canvas.create_line(144.1, 135, 144.1, 305)
            self.canvas.create_line(144.1+float(self.r)*10*10*2, 135, 144.1+float(self.r)*10*10*2, 305); 
            self.canvas.create_oval(144.1, 300, 144.1+float(self.r)*10*10*2, 310)
            
        self.label1.destroy(); self.label2.destroy(); self.label3.destroy()
        
        if direction=='up': 
            self.first_thick_line -= 1; self.second_thick_line -= 1; self.third_thick_line -= 1; 
            self.right['state']='normal'
            if self.rx <= self.x_left_lim+1:  self.left['state']='disabled'
            if self.rx <= self.x_left_lim + 15: self.faster_left['state'] = 'disabled'    #px-=1; qx-=1; rx-=1; sx-=1; tx-=1; ux-=1; grab_x-=1
            self.px-=0.05; self.qx-=0.05; self.rx-=0.05; self.sx-=0.05; self.tx-=0.05; self.ux-=0.05; self.grab_x-=0.05
            
            if self.first_thick_line==-10:
                self.first_thick_line = self.second_thick_line; self.second_thick_line = self.third_thick_line; self.third_thick_line = 20
                self.temp = self.temp.prev 
                #print(temp.data)       
        
        elif direction=='down':
            self.first_thick_line += 1; self.second_thick_line += 1; self.third_thick_line += 1; 
            self.left['state']='normal'
            if self.rx >= self.x_left_lim + 15: self.faster_left['state'] = 'normal'    #***************
            if self.rx >= self.x_right_lim: self.right['state']='disabled'

            self.px+=0.05; self.qx+=0.05; self.rx+=0.05; self.sx+=0.05; self.tx+=0.05; self.ux+=0.05; self.grab_x+=0.05

            if self.third_thick_line==30:
                self.third_thick_line = self.second_thick_line; self.second_thick_line = self.first_thick_line; self.first_thick_line  = 0
                self.temp = self.temp.next
                
        self.canvas.create_line(self.px,self.py, self.qx,self.qy, self.rx,self.ry, self.sx,self.sy, self.tx,self.ty, self.ux,self.uy, self.px,self.py,self.sx,self.sy)
        self.canvas.create_line(355,200, self.grab_x,200, self.grab_x,260, 355,260)
        
        #circular scale division.
        y_cir_inc = 0
        for i in range(21): 
            if i == self.first_thick_line:
                self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+20, 190+y_cir_inc, width=2)
                self.label1 = Label(self.canvas, text=str(self.temp.next.data), font=("Courier", 7, 'bold'), bg='lemon chiffon')
                self.label1.pack(); self.label1.place(x = self.qx+25, y=180+y_cir_inc)   
            elif i == self.second_thick_line:
                self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+20, 190+y_cir_inc, width=2)
                self.label2 = Label(self.canvas, text=str(self.temp.data), font=("Courier", 7, 'bold'), bg='lemon chiffon')
                self.label2.pack(); self.label2.place(x = self.qx+25, y=180+y_cir_inc)   
            elif i == self.third_thick_line:
                self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+20, 190+y_cir_inc, width=2)
                self.label3 = Label(self.canvas, text=str(self.temp.prev.data), font=("Courier", 7, 'bold'), bg='lemon chiffon')
                self.label3.pack(); self.label3.place(x=self.qx+25, y=180+y_cir_inc)   

            else: self.canvas.create_line(self.qx, 190+y_cir_inc,self.qx+10, 190+y_cir_inc)
            y_cir_inc+=4


        #static diagram.
        self.canvas.create_arc(120, 172, 360, 400, start=172, extent=186, style=ARC)
        self.canvas.create_arc( 70, 125, 430, 470, start=171, extent=191, style=ARC)
        #static box on the left side.
        self.canvas.create_line(130,200, 144.1,200, 144.1,260, 130,260, 130,270, 70,270, 70,190, 130,190, 130,260)
        #static diagram on right
        self.canvas.create_line(435,290, 355,290, 355,170, 435,170,435,180,self.rx,180,self.rx,280,435,280,435,180,435,290)
        #middle line that separates the 1mm and 0.5mm scale.
        self.canvas.create_line(435,230,self.rx,230)

        #linear mm scales
        x_mm_inc = 0
        for i in range(41):
            if 448+x_mm_inc<=self.rx:
                if i==0 or i==10 or i==20 or i==30 or i==40:
                    self.canvas.create_line(448+x_mm_inc, 230, 448+x_mm_inc, 210)
                    #label = Label(canvas, text=str(i/20), font=("Courier", 7, 'bold'), bg='lemon chiffon'); 
                    #label.pack(); label.place(x = 448+x_mm_inc-10, y=190);
                elif i%2==0: self.canvas.create_line(448+x_mm_inc, 230, 448+x_mm_inc, 220)
                else:        self.canvas.create_line(448+x_mm_inc, 230, 448+x_mm_inc, 240)
                x_mm_inc+=5    
            else: break;
          
    def faster_direction_button(self, direction):             #global rx, x_left_lim, temp #if rx >= x_right_lim: faster_right['state'] = 'disabled'
        if self.rx <= self.x_left_lim + 15: self.faster_left['state'] = 'disabled'
        for i in range(150):
            self.direction_button(direction)



    def __init__(self, setup_val, r):
        self.r = r
        self.root = Tk()
        self.root.geometry("1000x600"); 
        self.root.title("Screw Guage: Measurement number: " + str(setup_val) ); self.root.resizable(0,0)
        self.root.iconbitmap(getcwd() + '\\AEC_logo.ico')

        self.canvas = Canvas(self.root,bg="lemon chiffon"); self.canvas.pack(fill = 'both', expand=1); 
        def moved(event): self.canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
        self.canvas.bind("<Motion>", moved); tag = self.canvas.create_text(10, 10, text="", anchor="nw")
        
        self.x_left_lim  = 449.1; self.x_right_lim = 650
        self.label1 = None; self.label2 = None; self.label3 = None; self.applied = 0    # label1, label2, label3 may be needed as class variables.
        #dynamic part.
        #movableself. part on the right side.
        self.px=720;self.py=160;  self.qx=650;self.qy=180;  self.rx=650;self.ry=280;  self.sx=720;self.sy=300;  self.tx=980;self.ty=300;  self.ux=980;self.uy=160;   #->global
        self.canvas.create_line(self.px,self.py, self.qx,self.qy, self.rx,self.ry, self.sx,self.sy, self.tx,self.ty, self.ux,self.uy, self.px,self.py,self.sx,self.sy)
        self.grab_x = 345
        self.canvas.create_line(355,200, self.grab_x,200, self.grab_x,260, 355,260)

        self.head = Scale(0); self.head.next = Scale(10); self.head.next.next = Scale(20); self.head.next.next.next = Scale(30); self.head.next.next.next.next = Scale(40); 
        self.head.next.next.next.next.next = Scale(50); self.head.next.next.next.next.next.next = Scale(60); self.head.next.next.next.next.next.next.next = Scale(70)
        self.head.next.next.next.next.next.next.next.next = Scale(80); self.head.next.next.next.next.next.next.next.next.next = Scale(90)
        self.head.next.next.next.next.next.next.next.next.next.next = self.head
        tempo = self.head; count = 10
        while count: tempo.next.prev = tempo; tempo = tempo.next; count-=1
        self.temp = self.head

        #circular scale division 21
        self.first_thick_line  = 0; self.second_thick_line = 10; self.third_thick_line  = 20
        y_cir_inc = 0
        for i in range(21): 
            if i == self.first_thick_line:      
                self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+20, 190+y_cir_inc, width=2)
                self.label1 = Label(self.canvas, text=str(self.temp.next.data), font=("Courier", 7, 'bold'), bg='lemon chiffon')
                self.label1.pack(); self.label1.place(x =675, y=180+y_cir_inc)
            elif i == self.second_thick_line:      
                self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+20, 190+y_cir_inc, width=2)
                self.label2 = Label(self.canvas, text=str(self.temp.data), font=("Courier", 7, 'bold'), bg='lemon chiffon')
                self.label2.pack(); self.label2.place(x =675, y=180+y_cir_inc)
            elif i == self.third_thick_line:
                self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+20, 190+y_cir_inc, width=2)
                self.label3 = Label(self.canvas, text=str(self.temp.prev.data), font=("Courier", 7, 'bold'), bg='lemon chiffon')
                self.label3.pack(); self.label3.place(x =675, y=180+y_cir_inc)            
            else: self.canvas.create_line(self.qx, 190+y_cir_inc, self.qx+10, 190+y_cir_inc)
            y_cir_inc+=4
            

        #static diagram.
        self.canvas.create_arc(120, 172, 360, 400, start=172, extent=186, style=ARC)
        self.canvas.create_arc( 70, 125, 430, 470, start=171, extent=191, style=ARC)
        self.canvas.create_line(130,200, 144.1,200, 144.1,260, 130,260, 130,270, 70,270, 70,190, 130,190, 130,260) #static box on the left side.
        self.canvas.create_line(435,290, 355,290, 355,170, 435,170,435,180,self.rx,180,self.rx,280,435,280,435,180,435,290) #static diagram on right
        self.canvas.create_line(435,230,self.rx,230) #middle line that separates the 1mm and 0.5mm scale.

        #linear mm scales
        x_mm_inc = 0
        for i in range(41):
            if i==0 or i==10 or i==20 or i==30 or i==40: self.canvas.create_line(448+x_mm_inc, 230, 448+x_mm_inc, 210)
            elif i%2==0: self.canvas.create_line(448+x_mm_inc, 230, 448+x_mm_inc, 220)
            else:        self.canvas.create_line(448+x_mm_inc, 230, 448+x_mm_inc, 240)
            x_mm_inc+=5
            

        self.left = Button(self.canvas, width=5, text = "Left", bg='lemon chiffon', anchor = CENTER,command = lambda: self.direction_button('up'))
        self.left.pack(); self.left.place(x=800, y= 400); self.left.config(font=("Courier", 12, 'bold'))
        self.right = Button(self.canvas, width=5, text = "Right", bg='lemon chiffon', anchor = CENTER, command = lambda: self.direction_button('down'))
        self.right.pack(); self.right.place(x=900, y= 400); self.right.config(font=("Courier", 12, 'bold'))


        self.faster_left = Button(self.canvas, text = "Move left Faster", bg='lemon chiffon', anchor = CENTER, command = lambda: self.faster_direction_button('up'))
        self.faster_left.pack(); self.faster_left.place(x=800, y= 440); self.faster_left.config(font=("Courier", 12, 'bold'))

        self.apply=Button(self.canvas,width=12,text="Insert Wire",bg='lemon chiffon',anchor=CENTER,command=lambda:self.apply_func('insert'))
        self.apply.pack();self.apply.place(x=650, y= 400); self.apply.config(font=("Courier",12,'bold'))
        self.remove=Button(self.canvas,width=12,text="Remove Wire",bg='lemon chiffon',anchor=CENTER,command=lambda:self.apply_func('remove'))
        self.remove.pack();self.remove.place(x=650,y=440);self.remove.config(font=("Courier", 12,'bold'))

        self.instruction=Button(self.canvas,width=12,text="Instruction",anchor=CENTER,bg='lemon chiffon',command=self.instruction_butt)
        self.instruction.pack(); self.instruction.place(x=60,y=30); self.instruction.config(font=("Courier", 12, 'bold'))

        self.root.mainloop()


#param = open("Parameters.txt","r"); li = param.readline().split(); param.close()
#screw_gauge_obj = Screw_Gauge(li[0], li[2])