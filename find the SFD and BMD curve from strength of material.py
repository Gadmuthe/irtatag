Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
l = 10
w = 20
positions = [0]
shear_force = [0]
bending_moment = [0]
def calculate_sfd_bmd(l,w):
...     dx = 0.1
...     x = dx
...     while x <= l:
...         positions.append(x)
...         shear_force.append(-w*x)
...         bending_moment.append(-0.5*w*x*x)
...         x += dx
... 
...         
>>> calculate_sfd_bmd(l,w)
>>> #plot SFD
>>> plt.figure(1)
<Figure size 640x480 with 0 Axes>
>>> plt.plot(positions, shear_force, label = 'Shear Force (V)' )
[<matplotlib.lines.Line2D object at 0x0000016A4829B0B0>]
>>> plt.xlabel('Position (m)')
Text(0.5, 0, 'Position (m)')
>>> plt.ylabel('Shear Force (N)')
Text(0, 0.5, 'Shear Force (N)')
>>> plt.title('Shear Force Diagram')
Text(0.5, 1.0, 'Shear Force Diagram')
>>> plt.grid(True)
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0000016A4829B1D0>
>>> #plot BMD
>>> plt.figure(2)
<Figure size 640x480 with 0 Axes>
>>> plt.plot(positions, bending_moment, label = 'Bending Moment (M)')
[<matplotlib.lines.Line2D object at 0x0000016A4903F350>]
>>> plt.xlabel('Position (m)')
Text(0.5, 0, 'Position (m)')
>>> plt.ylabel('Bending Moment (Nm)')
Text(0, 0.5, 'Bending Moment (Nm)')
>>> plt.title('Bending Moment Diagram')
Text(0.5, 1.0, 'Bending Moment Diagram')
>>> plt.grid(True)
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0000016A4903F500>
>>> plt.show()


