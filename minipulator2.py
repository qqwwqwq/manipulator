import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import tkinter
import  math
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import cv2
global l1,l2,l3
l0=l1=l2=l3=1
global x,y,z,d1,d2,zeta
x=0
y=l3
z=l1+l0+l2
d1=d2=0
zeta=0
Zero=np.array([[x,y,z]])
def ini():
    global l1,l2,l3,x,y,z
    l1 = float(e1.get())
    l2 = float(e2.get())
    l3 = float(e3.get())
    e1.pack_forget()
    e2.pack_forget()
    e3.pack_forget()
    ll1.pack_forget()
    ll2.pack_forget()
    ll3.pack_forget()
    btn1.pack_forget()
    btnx.pack()
    btnx2.pack()
    btny.pack()
    btny2.pack()
    btnz.pack()
    btnz2.pack()
    x = 0
    y = l3
    z = l1 + l0 + l2
    getnewlocation(x,y,z)
def xup():
    global x
    x += 0.1
    calculate(x, y, z)
def xdown():
    global x
    x -= 0.1
    calculate(x, y, z)
def yup():
    global y
    y += 0.1
    calculate(x, y, z)
def ydown():
    global y
    y -= 0.1
    calculate(x, y, z)
def zup():
    global z
    z += 0.1
    calculate(x, y, z)
def zdown():
    global z
    if z - 0.1 <= 0:
        z = 0
    else:
        z -= 0.1
    calculate(x, y, z)
def getnewlocation(x,y,z):
    X=[]
    Y=[]
    Z=[]
    Pos=[[0,0,0],[0,0,l0],[0,0,l1+l0],[0,0,l0+l1+l2+d1],[(l3+d2)*math.sin(zeta),(l3+d2)*math.cos(zeta),l0+l1+l2+d1]]
    for i in Pos:
        X.append(i[0])
        Y.append(i[1])
        Z.append(i[2])
    ax.cla()
    #ax.view_init(10, 11)
    ax.set_xlim3d(-3, 3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_ylim3d(-3, 3)
    ax.set_zlim3d(0, 6)
    ax.plot(X, Y, Z, 'bo--')
    canvs.draw()
    print(Pos)
def call(event):
    global x,y,z
    if event.char == "z":
        ax.view_init()
        calculate(x, y, z)
    if event.char == "x":
        ax.view_init(30, 11)
        calculate(x, y, z)
    if event.char == "q":
        x +=0.1
        calculate(x, y, z)
    if event.char == "w":
        x -=0.1
        calculate(x, y, z)
    if event.char == "e":
        y +=0.1
        calculate(x, y, z)
    if event.char == "a":
        y -= 0.1
        calculate(x, y, z)
    if event.char == "s":
        z +=0.1
        calculate(x, y, z)
    if event.char == "d":
        if z - 0.1 <= 2:
            z = 2
        else:
            z -=0.1
        calculate(x, y, z)
def calculate(x,y,z):
    global d1,d2,zeta
    if math.sqrt(math.pow(x, 2)+math.pow(y, 2))-l3>=0 and math.sqrt(math.pow(x, 2)+math.pow(y, 2))-l3<=5:
        d2 = math.sqrt(math.pow(x, 2)+math.pow(y, 2))-l3
    elif math.sqrt(math.pow(x, 2)+math.pow(y, 2))-l3>5:
        d2=5
    else:
        d2=0
    if z - l0-l1-l2>=0 and z - l0-l1-l2<=5:
        d1 = z - l0-l1-l2
    elif z - l0-l1-l2>5:
        d1=5
    else :
        d1=0
    if y<0:
        zeta = np.pi -math.asin(x/(math.sqrt(math.pow(x, 2)+math.pow(y, 2))))
    else:
        zeta = math.asin(x / (math.sqrt(math.pow(x, 2) + math.pow(y, 2))))
    print(np.array([[d1,d2,zeta]]))
    getnewlocation(x, y, z)
fig = plt.figure()
ax = Axes3D(fig)
win = tkinter.Tk()
frame = tkinter.Frame(win, width=200, height=200)
ll1=tkinter.Label(frame,text="l1") #标签
ll1.pack()
e1=tkinter.Entry(frame) #创建文本框
e1.pack()
ll2=tkinter.Label(frame,text="l2") #标签
ll2.pack()
e2=tkinter.Entry(frame) #创建文本框
e2.pack()
ll3=tkinter.Label(frame,text="l3") #标签
ll3.pack()
e3=tkinter.Entry(frame) #创建文本框
e3.pack()
btn1 = tkinter.Button(frame,text = 'start',command =ini )
btn1.pack()
btnx = tkinter.Button(frame,text = 'x-up',command = xup)
btnx2 = tkinter.Button(frame,text = 'x-down',command = xdown)
btny = tkinter.Button(frame,text = 'y-up',command = yup)
btny2 = tkinter.Button(frame,text = 'y-down',command = ydown)
btnz = tkinter.Button(frame,text = 'z-up',command = zup)
btnz2 = tkinter.Button(frame,text = 'z-down',command = zdown)
canvs = FigureCanvasTkAgg(fig, win)
canvs.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#frame.bind("<Key>", call)  # 触发的函数
frame.focus_set()  # 必须获取焦点
frame.pack()
#getnewlocation(x, y, z)
win.mainloop()

