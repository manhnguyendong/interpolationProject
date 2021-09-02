from tkinter import *
from tkinter.ttk import *
import numpy as np
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

master = Tk()
master.title('Lagrange Interpolation')
master.geometry('700x700')
x = np.array([])
y = np.array([])


class frame_button:
    def __init__(self, root):
        frame = Frame(root)
        frame.grid(column=0, row=0)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)
        self.inputX = DoubleVar()
        self.inputY = DoubleVar()
        self.inputY.set('')
        self.inputX.set('')
        #Create Label
        self.x_label = Label(frame, text='x:')
        self.x_label.grid(column=0, row=0)
        self.y_label = Label(frame, text='y:')
        self.y_label.grid(column=0, row=1)
        #Create Entry-Widget
        self.xEntry = Entry(frame, textvariable=self.inputX, width=20)
        self.xEntry.grid(column=1, row=0)
        self.yEntry = Entry(frame, textvariable=self.inputY, width=20)
        self.yEntry.grid(column=1, row=1, pady=5)
        # Button
        self.addButton = Button(frame, text='Add Point', command=self.add_point)
        self.addButton.grid(column=1, row=2)
        #Create framePlot
        self.frame_plot = Frame(root)
        self.frame_plot.grid(column=1, row=0)

        #Button Plot
        self.buttonPlot = Button(self.frame_plot, text='Plot', command=self.plot)
        self.buttonPlot.grid(column=1, row=0)

        #Create numpy array
        self.x = np.array([])
        self.y = np.array([])


    def add_point(self):
        x = self.inputX.get()
        y = self.inputY.get()
        print('Added successfully')
        self.x = np.append(self.x, x)
        self.y = np.append(self.y, y)
        print(self.x, self.y)
        self.inputY.set('')
        self.inputX.set('')

    def plot(self):
        fig = Figure(figsize=(4, 4), dpi=100)
        plot1 = fig.add_subplot(111)
        self.min = np.min(self.x)
        self.max = np.max(self.x)
        self.xplt = np.linspace(self.min - 30, self.max + 30)
        self.yplt = np.array([])
        for xp in self.xplt:
            lagrange = 0
            for (xi, yi) in zip(self.x, self.y):
                p = np.prod((xp - self.x[self.x != xi])/(xi - self.x[self.x != xi]))
                lagrange += p * yi
            self.yplt = np.append(self.yplt, lagrange)
        plot1.plot(self.xplt, self.yplt)
        canvas = FigureCanvasTkAgg(fig, master=self.frame_plot)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1)

        toolbar = NavigationToolbar2Tk(canvas, self.frame_plot)
        toolbar.update()
        canvas.get_tk_widget().grid(column=1)

def main():
    global master, x, y
    master.columnconfigure(0, weight=2)
    master.columnconfigure(1, weight=20)
    ButtonandLabel = frame_button(master)
    mainloop()

if __name__ == "__main__":
    main()