#!/usr/bin/python3
import tkinter as tk
import turtle
turtle.bgcolor("black")
from tkinter.filedialog import askopenfilename
import ast


t = None
wn = None
def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance):
    t.color("#03fcdf", "green")
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def draw(iterations, axiom, rules, angle, length=8, size=3, y_offset=0,
        x_offset=0, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)
    global t
    global wn
    if t == None:
        
        t = turtle.Turtle()
        
        wn = turtle.Screen()
        #wn.setup(width, height)
        
    
    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    
    


axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 4 # TOP: 7
angle = 60





class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.axiom = None
        self.rules = None
        self.iterations = None
        self.angle = None
        self.length = None

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Provide the L-system"
        self.hi_there.grid(row = 1, column = 0)
        
        
        self.FN = tk.Button(self, text="....")
        self.FN.grid(row = 1, column = 2)
        
        tk.Label(self, text="Axiom").grid(row=2)
        tk.Label(self, text="Rules").grid(row=3)
        tk.Label(self, text="Iterations").grid(row=4)
        tk.Label(self, text="Angle").grid(row=5)
        tk.Label(self, text="Side Length").grid(row=6)
        
        self.Axiom= tk.Text(self,height=1,width = 20,)
        self.Axiom.grid(row = 2, column = 1)
        self.Axiom.insert('1.0', 'F--F--F')
        self.Rules = tk.Text(self,height=1, width = 50)
        self.Rules.grid(row = 3, column = 1 )
        self.Rules.insert('1.0', '{"F":"F+F--F+F"}')
        self.Iterations= tk.Text(self,height=1,width = 10)
        self.Iterations.grid(row = 4, column = 1)
        self.Iterations.insert('1.0', '3')
        self.Angle = tk.Text(self,height=1, width = 10)
        self.Angle.grid(row = 5, column = 1 )
        self.Angle.insert('1.0', '60')

        self.Len = tk.Text(self,height=1, width = 10)
        self.Len.grid(row = 6, column = 1 )
        self.Len.insert('1.0', '3')

        
        self.Draw = tk.Button(self, text="Draw", fg="Green",
                              command=self.draw)
        
        self.Draw.grid(row = 6, column = 2)
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.Quit)
        
        self.quit.grid(row = 7, column = 1)
        tk.Label(self,text="").grid(row=8)
        tk.Label(self,text="").grid(row=9)
        #tk.Label(self,text="").grid(row=10)
        #tk.Label(self,text="").grid(row=11)
        #tk.Label(self,text="").grid(row=12)
        #tk.Label(self,text="").grid(row=13)
        Rules = tk.Label(self, text=" A simple tool to draw fractal from it's L-system description. \
 \n Axiom: The initial string for the generation. \n Rules: A set of \
production rules. Input is taken in form of Python Dictionaries.\n Angle: Required Angle of rotation for the fractals. \n \
 Side Length: Length of each side of the Fractals.\
\n Sample inputs for Koch-Snowflake are given in the Input box.\n \
 Sample input for Piano-Gosper-Curve is: \n \
                Axiom = FX\n \
                Rules = {\"X\":\"X+YF++YF-FX--FXFX-YF+\", \"Y\":\"-FX+YFYF++YF+FX--FX-Y\"} \n \
                Iterations = 4 \n \
                Angle = 60 \n \
                Side Length = 3" )
        Rules.grid(row=14,columnspan = 6)
        Rules.config(bg="gray", fg='white', font=("Courier",10))
        

        
        
    def Quit(self):
        global t
        turtle.bye()
        self.master.destroy()
        
        
    def getRules(self):
        self.axiom = self.Axiom.get("1.0","end")
        self.rules = ast.literal_eval(self.Rules.get("1.0","end"))
        self.iterations = int(self.Iterations.get("1.0","end"))
        self.angle = float(self.Angle.get("1.0","end"))
        self.length = int(self.Len.get("1.0","end"))
    
    def draw(self):
        global t
        self.getRules()
        if t != None:
            t.clear()
        if self.axiom == None or self.rules == None or self.iterations == None or self.angle == None or self.length == None:
            self.msg.config(text="select all values")
        else:
           draw(self.iterations, self.axiom, self.rules, self.angle, length= self.length , size=2, y_offset=0,x_offset=0, offset_angle=0, width=800, height=800)
            
    def decompress(self,):
        if  self.fileName == None:
            self.msg.config(text="select a File")
        else:
            decompress(self.fileName, 'f')
            self.msg.config(text="decompressing "+ self.fileName)
            
            
        
        

root = tk.Tk()
app = Application(master=root)

root.geometry("750x500")
root.title("Happy L Fractals")
app.mainloop()



