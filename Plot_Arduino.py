import numpy as np
import serial
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame*
def init():
    line.set_data([], [])
    return line,


# serial
ser = serial.Serial('/dev/ttyUSB0', 9600)


# animation function.  This is called sequentially
def animate(i):
    data = ser.readline()
    x = np.linspace(0, 2, 1000)
    y = np.sin(int(data.decode()) * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()

