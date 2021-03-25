from tf import HomogeneousMatrix
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
np.set_printoptions(suppress=True)

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.
    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


base = HomogeneousMatrix()
joint1 = HomogeneousMatrix()
joint2 = HomogeneousMatrix()
joint3 = HomogeneousMatrix()
jointx = HomogeneousMatrix()
joint4 = HomogeneousMatrix()
joint5 = HomogeneousMatrix()
joint6 = HomogeneousMatrix()
jointy = HomogeneousMatrix()
end = HomogeneousMatrix()
# --- Robotic Arm construction ---

#    Joint Angle variables
a=[0.00582975956336, 0.521079202543, -1.39077808109, 0.00307177948351, 0.0107512281923, 0.0]
b=[]
for j in a:
    b.append(j/3.14*180)
print(b)
b=[0,0,0,0,0,0]
def findf(b):
    q1, q2, q3 = b[0], b[1], b[2]
    q4, q5, q6 = b[3], b[4], b[5]
    #    ---------------------

    joint1.set_d(103)
    joint1.set_theta(q1)

    joint2.set_d(80)
    joint2.set_alpha(90)
    joint2.set_theta(90)
    joint2.set_theta(q2)
    # joint2.set_theta(0)

    joint3.set_a(210)
    joint3.set_theta(-90)
    joint3.set_theta(q3)

    jointx.set_a(41.5)
    jointx.set_theta(-90)

    joint4.set_a(-30)
    joint4.set_alpha(-90)
    joint4.set_theta(0)
    joint4.set_theta(q4)

    joint5.set_d(180)
    joint5.set_alpha(90)
    # joint5.set_theta(90)
    joint5.set_theta(90)
    joint5.set_theta(q5)

    joint6.set_a(23.7)
    # joint6.set_d(5.5)
    joint6.set_theta(-90)

    jointy.set_a(5.5)
    jointy.set_alpha(-90)
    jointy.set_theta(q6)

    end.set_d(20)
    # ---------------------------------

    joint1.set_parent(base.get())
    joint2.set_parent(joint1.get())
    joint3.set_parent(joint2.get())
    jointx.set_parent(joint3.get())
    joint4.set_parent(jointx.get())
    joint5.set_parent(joint4.get())
    joint6.set_parent(joint5.get())
    jointy.set_parent(joint6.get())
    end.set_parent(jointy.get())
    print(jointy.get())
    return jointy.get()

# q1, q2, q3 = 0, 80, -80
# q4, q5, q6 = 0, 40, 0

# Prepare the coordinates for plotting

X = [base[0, 3], joint1[0, 3],
     joint2[0, 3], joint3[0, 3],jointx[0,3],
     joint4[0, 3], joint5[0, 3],
     joint6[0, 3],   jointy[0, 3],end[0, 3]]
Y = [base[1, 3], joint1[1, 3],
     joint2[1, 3], joint3[1, 3],jointx[1,3],
     joint4[1, 3], joint5[1, 3],
     joint6[1, 3],   jointy[1, 3],end[1, 3]]
Z = [base[2, 3], joint1[2, 3],
     joint2[2, 3], joint3[2, 3],jointx[2,3],
     joint4[2, 3], joint5[2, 3],
     joint6[2, 3],   jointy[2, 3],end[2, 3]]

# Plot

ax = plt.axes(projection='3d')
# ax.set_aspect('equal')
ax.plot3D(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

set_axes_equal(ax)
plt.show()