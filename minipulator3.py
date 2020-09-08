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
l0=1
global l2,l3,l1
l1=l2=1
l3=1.5
global x,y,z,d1,zeta1,zeta2
x=0
y=0
z=l1+l2+l3+l0
d1=0
zeta1=0
zeta2=0
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
    y = 0
    z = l1 + l2 + l3 + l0
    getnewlocation(x,y,z)
def getnewlocation(x,y,z): 
    X=[]
    Y=[]
    Z=[]
    Pos=[[0,0,0],[0,0,l0],[0,0,l1+l0],[l2*math.sin(zeta1)*math.sin(zeta2),l2*math.cos(zeta1)*math.sin(zeta2),l1+l0+l2*math.cos(zeta2)],[(l2+l3+d1)*math.sin(zeta1)*math.sin(zeta2),(l2+l3+d1)*math.cos(zeta1)*math.sin(zeta2),(l2+l3+d1)*math.cos(zeta2)+l1+l0]]
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
def calculate(x,y,z):
    global d1,zeta1,zeta2
    if math.sqrt(math.pow(x, 2)+math.pow(y, 2)+math.pow(z-l1-l0,2))-l2-l3>=0 and math.sqrt(math.pow(x, 2)+math.pow(y, 2)+math.pow(z-l1-l0,2))-l2-l3 <=3:
        d1 = math.sqrt(math.pow(x, 2)+math.pow(y, 2)+math.pow(z-l1-l0,2))-l2-l3
    elif math.sqrt(math.pow(x, 2)+math.pow(y, 2)+math.pow(z-l1-l0,2))-l2-l3>3:
        d1=3
    else:
        d1=0
    if z>l0+l1:
        zeta2 = math.acos((z -l1-l0) / (d1 +l3+l2))
    else:
        zeta2 = np.pi-math.acos(abs((z -l1-l0) / (d1+l3+l2)))
    if y==0:
        if x==0:
            zeta1=0
        elif x>0:
            zeta1=np.pi/2
        else:
            zeta1 = -np.pi / 2
    elif y<0:
        zeta1 = math.atan(x / y)-np.pi
    else:
        zeta1 = math.atan(x / y)
    print(np.array([[d1,zeta1,zeta2]]))
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
canvs.get_tk_widget().pack(fill=tkinter.BOTH, expand=1)
#frame.bind("<Key>", call)  # 触发的函数
frame.focus_set()  # 必须获取焦点
frame.pack()
#getnewlocation(x, y, z)
win.mainloop()
