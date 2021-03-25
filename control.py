"""
This script shows few functions you can use with the TCP API
"""

# Imports
from tf import HomogeneousMatrix
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from FindX import findc
from forward import findf
from axxb import main3
import numpy as np
np.set_printoptions(suppress=True)
from niryo_one_tcp_client import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import pyk4a
from pyk4a import Config, PyK4A, ColorResolution
import tkinter
global tx,ty,tz,ox,oy,oz
matplotlib.use('TkAgg')
# Connecting to robot
k4a = PyK4A(Config(color_resolution=ColorResolution.RES_3072P,
                       depth_mode=pyk4a.DepthMode.WFOV_UNBINNED,
                       synchronized_images_only=True,
                       camera_fps=pyk4a.FPS.FPS_5, ))
k4a.connect()
k4a.exposure_mode_auto=True
k4a.whitebalance_mode_auto=True
k4a.sharpness=4
k4a.backlight_compensation=1
k4a.gain=100


niryo_one_client = NiryoOneClient()
ctoo=[]
forword=[]
niryo_one_client.connect("10.10.10.10")
niryo_one_client.change_tool(RobotTool.GRIPPER_1)# =< Replace by robot ip address
gripper_used = RobotTool.GRIPPER_1
# Trying to calibrate
status, data = niryo_one_client.calibrate(CalibrateMode.AUTO)
if status is False:
    print("Error: " + data)
# Getting pose
status, data = niryo_one_client.get_pose()
initial_pose = None
if status is True:
    initial_pose = data
    print("data",data)
    tx=data.x
    ty=data.y
    tz=data.z
    ox=data.roll
    oy=data.pitch
    oz=data.yaw
else:
    print("Error: " + data)
status, data = niryo_one_client.get_joints()
if status is True:
    print("data",data)
else:
    print("Error: " + data)
status, data = niryo_one_client.move_joints(0,0,0,0,0,0)
if status is True:
    print("data",data)
status, data = niryo_one_client.get_pose()
if status is True:
    print("data",data)
else:
    print("Error: " + data)
#forward kinematic
# # Move Joints
# status, data = niryo_one_client.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
# if status is False:
#     print("Error: " + data)
#
# # Shift pose
# status, data = niryo_one_client.shift_pose(RobotAxis.Y, 0.15)
# if status is False:
#     print("Error: " + data)
#
# # Going back to initial pose
# if initial_pose is not None:
#     status, data = niryo_one_client.move_pose(*niryo_one_client.pose_to_list(initial_pose))
#     if status is False:
#         print("Error: " + data)
def ini():
    btn1.pack_forget()
    btnx.pack()
    btnx2.pack()
    btny.pack()
    btny2.pack()
    btnz.pack()
    btnz2.pack()
    opent.pack()
    close.pack()
    out.pack()
def opent():
    niryo_one_client.open_gripper(RobotTool.GRIPPER_1,100)
def closet():
    niryo_one_client.close_gripper(RobotTool.GRIPPER_1, 100)
def out():
    win.destroy()
    niryo_one_client.quit()
def xup():
    global tx
    tx += 0.01
    status, data = niryo_one_client.move_pose(tx,ty,tz,ox,oy,oz)
    if status is False:
        print("Error: " + data)
def xdown():
    global tx
    tx -= 0.01
    status, data = niryo_one_client.move_pose(tx, ty, tz, ox, oy, oz)
    if status is False:
        print("Error: " + data)
def yup():
    global ty
    ty += 0.01
    status, data = niryo_one_client.move_pose(tx, ty, tz, ox, oy, oz)
    if status is False:
        print("Error: " + data)
def ydown():
    global ty
    ty -= 0.01
    status, data = niryo_one_client.move_pose(tx, ty, tz, ox, oy, oz)
    if status is False:
        print("Error: " + data)
def zup():
    global tz
    tz += 0.01
    status, data = niryo_one_client.move_pose(tx, ty, tz, ox, oy, oz)
    if status is False:
        print("Error: " + data)
def zdown():
    global tz
    tz -= 0.01
    status, data = niryo_one_client.move_pose(tx, ty, tz, ox, oy, oz)
    if status is False:
        print("Error: " + data)
def docali(c,f):
    a1=np.dot(np.linalg.inv(f[0]),f[1])
    a2=np.dot(np.linalg.inv(f[1]),f[2])
    b1=np.dot(c[0],np.linalg.inv(c[1]))
    b2=np.dot(c[1],np.linalg.inv(c[2]))
    A=np.concatenate([a1, a2], axis=1)
    B=np.concatenate([b1, b2], axis=1)
    return main3(A,B)
def handeye():
    if len(ctoo)==3:
        cmatric=docali(ctoo,forword)
        print(cmatric,'calibration matrix')
        return cmatric
    else:
        img_color, img_depth = k4a.get_capture()
        ctoo.append(findc(img_color))
        status, data = niryo_one_client.get_joints()
        if status is True:
            print("data", data)
            forword.append(findf(data))
        else:
            print("Error: " + data)
# Getting hardware information
# status, data = niryo_one_client.get_digital_io_state()
# if status is True:
#     digital_pin_array = data
#     for digital_pin in digital_pin_array:
#         print("Pin: " + digital_pin.pin_id
#               + ", name: " + digital_pin.name
#               + ", mode: " + str(digital_pin.mode)
#               + ", state: " + str(digital_pin.state))
#
# # Turning learning mode ON
# status, data = niryo_one_client.set_learning_mode(True)
# if status is False:
#     print("Error: " + data)
# fig = plt.figure()
# ax = Axes3D(fig)
win = tkinter.Tk()
frame = tkinter.Frame(win, width=200, height=200)
btn1 = tkinter.Button(frame,text = 'start',command =ini )
btn1.pack()
btnx = tkinter.Button(frame,text = 'x-up',command = xup)
btnx2 = tkinter.Button(frame,text = 'x-down',command = xdown)
btny = tkinter.Button(frame,text = 'y-up',command = yup)
btny2 = tkinter.Button(frame,text = 'y-down',command = ydown)
btnz = tkinter.Button(frame,text = 'z-up',command = zup)
btnz2 = tkinter.Button(frame,text = 'z-down',command = zdown)
opent=tkinter.Button(frame,text = 'open',command = opent)
close=tkinter.Button(frame,text = 'close',command = closet)
out= tkinter.Button(frame,text = 'out',command = out)
heyecalibration= tkinter.Button(frame,text = 'heyecalibration',command = handeye)
# canvs = FigureCanvasTkAgg(fig, win)
# canvs.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
frame.focus_set()  # 必须获取焦点
frame.pack()
win.mainloop()
# status, data = niryo_one_client.move_pose(-0.01, -0.23, 0.12,-0., 1.57, -1.57)
# niryo_one_client.change_tool(gripper_used)
# niryo_one_client.open_gripper(gripper_used, 110)
# if status is False:
#     print("Error: " + data)
niryo_one_client.quit()
