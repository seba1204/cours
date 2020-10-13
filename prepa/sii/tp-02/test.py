from matplotlib.widgets import Slider  # import the Slider widget

import numpy as np
import matplotlib.pyplot as plt
from math import pi
import sys

a_min = 0    # the minimial value of the paramater a
a_max = 10   # the maximal value of the paramater a
a_init = 1   # the value of the parameter a to be used initially, when the graph is created

x = np.linspace(0, 2*pi, 500)

fig = plt.figure(figsize=(10, 3))

# first we create the general layount of the figure
# with two axes objects: one for the plot of the function
# and the other for the slider
sin_ax = plt.axes([0.1, 0.2, 0.8, 0.65])


# in plot_ax we plot the function with the initial value of the parameter a
plt.axes(sin_ax)  # select sin_ax
plt.title('y = sin(ax)')
sin_plot, = plt.plot(x, np.sin(a_init*x), 'r')
plt.xlim(0, 2*pi)
plt.ylim(-1.1, 1.1)


def update(a):
    # set new y-coordinates of the plotted points
    sin_plot.set_ydata(np.sin(a_slider.val*x))
    fig.canvas.draw_idle()          # redraw the plot

    # the final step is to specify that the slider needs to
    # execute the above function when its value changes


if ('-sliders' in sys.argv):
    slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
    # here we create the slider
    a_slider = Slider(slider_ax,      # the axes object containing the slider
                      'a',            # the name of the slider parameter
                      a_min,          # minimal value of the parameter
                      a_max,          # maximal value of the parameter
                      valinit=a_init  # initial value of the parameter
                      )

    a_slider.on_changed(update)


plt.show()
