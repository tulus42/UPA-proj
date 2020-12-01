import tkinter as tk
import matplotlib.pyplot as plt
import datetime
from tkinter import messagebox
from matplotlib.widgets import Slider  # import the Slider widget
import numpy as np

def show_grapfh_abs_illness(table):
    
    dates = [x[0] for x in table]
    values = [x[1] for x in table]

    fig, ax = plt.subplots()
    ax.plot_date(dates, values, marker='', linestyle='solid')
    fig.autofmt_xdate()
    ax.set_xlim([dates[0], dates[-1]])
    plt.ylabel("Prírastok nakazených")
    plt.xlabel("Dátum")
    plt.show()


def show_grapfh_perc_illness(table, pop):
    
    dates = [x[0] for x in table]
    values = [x[1]*100/pop for x in table]

    fig, ax = plt.subplots()
    ax.plot_date(dates, values, marker='', linestyle='solid')
    fig.autofmt_xdate()
    ax.set_xlim([dates[0], dates[-1]])
    plt.ylabel("Prírastok nakazených [%]")
    plt.xlabel("Dátum")
    plt.show()


def show_moving_average(table):
    values = [x[1] for x in table]

    x = 2/(len(values) + 1)

    ema = 0

    for i in values:
        ema += x * (i - ema)

    messagebox.showinfo("Kĺzavý priemer", "Kĺzavý priemer za obdobie\n"+str(table[0][0])+" - "+str(table[-1][0])+"\nje\n"+str(ema))



def moving_graph(table, date_from, region):
    a_min = 0    # the minimial value of the paramater a
    a_max = len(table)   # the maximal value of the paramater a
    a_init = len(table)-10   # the value of the parameter a to be used initially, when the graph is created

    x = [x[0] for x in table[0]]
    y = [int(y[1]) for y in table[-10]]
    lines = [line for line in table]
    values = []
    for line in lines:
        for value in line:
            values.append(int(value[1]))
    max_y = max(values)
    max_x = len(x)

    fig = plt.figure(figsize=(12,7))

    # # first we create the general layount of the figure
    # # with two axes objects: one for the plot of the function
    # # and the other for the slider
    y_ax = plt.axes([0.1, 0.3, 0.8, 0.55])
    slider_ax = plt.axes([0.1, 0.02, 0.8, 0.05])
    slider_ax.set_xticks([0,1,2,3])

    # # in plot_ax we plot the function with the initial value of the parameter a
    plt.axes(y_ax) # select sin_ax
    plt.title(region + ' od ' + date_from)
    plt.bar(x,y)
    plt.tick_params(rotation=60)
    plt.xlim(0, max_x)
    plt.ylim(0, max_y)

    # # here we create the slider
    a_slider = Slider(slider_ax,      # the axes object containing the slider
                    'a',            # the name of the slider parameter
                    a_min,          # minimal value of the parameter
                    a_max,          # maximal value of the parameter
                    valinit=a_init  # initial value of the parameter
                    )

    # # Next we define a function that will be executed each time the value
    # # indicated by the slider changes. The variable of this function will
    # # be assigned the value of the slider.
    def update(a):
        plt.cla()
        plt.axes(y_ax)
        plt.title(region + ' od ' + date_from)
        plt.tick_params(rotation=60)
        plt.xlim(0, max_x)
        plt.ylim(0, max_y)
        y = [int(y[1]) for y in table[int(a)]]
        plt.bar(x,y)


    a_slider.on_changed(update)

    plt.show()


