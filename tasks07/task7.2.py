import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

fig, ax = plt.subplots()
(line1,) = ax.plot([], [])
(line2,) = ax.plot([], [])
ax.set_xlim(0, 800)
ax.set_ylim(-100, 100)

amplitude = 70
frequency = 1
angle = 0
time = 0
miu = 1
sigma = 0
running = False


def Gauss_noise(x, y):
    for i in range(len(x)):
        y[i] += np.random.normal(miu, sigma)


def update(f):
    global angle, running, time
    if running:
        x = np.arange(0, 800, 5)
        xx = np.arange(0, 800, 5)
        y = amplitude * np.sin(frequency * (x + time) * np.pi / 180)
        yy = amplitude * np.cos(frequency * (xx + time) * np.pi / 180 + angle)
        Gauss_noise(x, y)
        Gauss_noise(xx, yy)
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


def update_miu(val):
    global miu
    miu = val


def update_sigma(val):
    global sigma
    sigma = val


# button
start_button = Button(plt.axes([0.84, 0.01, 0.08, 0.05]), "Start")
start_button.on_clicked(start_animation)

stop_button = Button(plt.axes([0.71, 0.01, 0.08, 0.05]), "Stop")
stop_button.on_clicked(stop_animation)

# slider
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


miu_slider = Slider(plt.axes([0.15, 0.01, 0.5, 0.03]), "miu", -10, 10, valinit=miu)
miu_slider.on_changed(update_miu)


sigma_slider = Slider(plt.axes([0.15, 0.043, 0.5, 0.03]), "sigma", 0, 10, valinit=sigma)
sigma_slider.on_changed(update_sigma)


ani = FuncAnimation(fig, update, frames=20, interval=30, blit=True)


plt.show()
