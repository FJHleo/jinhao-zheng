import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

fig, ax = plt.subplots()
(line1,) = ax.plot([], [])
(line2,) = ax.plot([], [])
ax.set_xlim(0, 800)
ax.set_ylim(-100, 100)

amplitude = 100
frequency = 1
angle = 0
running = False
time = 0


def update(f):
    global angle, running, time
    if running:
        x = np.arange(0, 800, 5)
        xx = np.arange(0, 800, 5)
        y = amplitude * np.sin(frequency * (x + time) * np.pi / 180)
        yy = amplitude * np.cos(frequency * (xx + time) * np.pi / 180 + angle)
        line1.set_data(x, y)
        line2.set_data(xx, yy)
        time += 5
    return line1, line2


def start_animation(event):
    global running
    running = True


def stop_animation(event):
    global running
    running = False


def update_amplitude(val):
    global amplitude
    amplitude = val


def update_frequency(val):
    global frequency
    frequency = val


def update_angle(val):
    global angle
    angle = val


start_button = Button(plt.axes([0.8, 0.01, 0.1, 0.05]), "Start")
start_button.on_clicked(start_animation)

stop_button = Button(plt.axes([0.65, 0.01, 0.1, 0.05]), "Stop")
stop_button.on_clicked(stop_animation)

amplitude_slider = Slider(
    plt.axes([0.15, 0.96, 0.7, 0.03]), "Amplitude", 0, 100, valinit=amplitude
)
amplitude_slider.on_changed(update_amplitude)

frequency_slider = Slider(
    plt.axes([0.15, 0.93, 0.7, 0.03]), "Frequency", 0, 5, valinit=frequency
)
frequency_slider.on_changed(update_frequency)

angle_slider = Slider(plt.axes([0.15, 0.9, 0.7, 0.03]), "angle", 0, 90, valinit=angle)
angle_slider.on_changed(update_angle)

ani = FuncAnimation(fig, update, frames=10, interval=50, blit=True)
plt.show()
