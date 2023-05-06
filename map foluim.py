from tkinter import *
import tkintermapview

root = Tk()
root.geometry("1920x1080")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=1500,height=800)
map_widget.set_position( 31.43751,31.678356)
map_widget.set_zoom(15)

map_widget.pack()

root.mainloop()