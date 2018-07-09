# -*- coding:utf-8 -*-
from matplotlib import pyplot
import cv2

def on_press(event):
    if event.button==1:
        ax.scatter(event.xdata, event.ydata)
        pyplot.plot([event.xdata, event.xdata], [event.ydata, 600])
        pyplot.plot([event.xdata, 0], [event.ydata, event.ydata])
        fig.canvas.draw()
    elif event.button==3:
        print("x,y=",event.xdata, event.ydata)
if __name__ == "__main__":
    img = cv2.imread('01.png')
    cv2.imshow("src", img)
    fig = pyplot.figure()
    fig.canvas.mpl_connect("button_press_event", on_press)
    ax = fig.add_subplot(111)
    ax.imshow(img)
    pyplot.axis("off")
    pyplot.show()
