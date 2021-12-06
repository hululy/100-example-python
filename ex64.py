# 用tkinter画正方形和椭圆

from tkinter import  *

canvas = Canvas(width=400, height=500, bg ='pink')

left = 20
right = 50
top = 50
num = 15

for i in range(num):
    canvas.create_rectangle(20-2*i, 20-2*i, 10*(i+2), 10*(i+2))
    canvas.create_oval(250-right, 250-left, 250+right, 250+left)
    canvas.create_oval(250-20, 250-top, 250+20, 250+top)
    right += 5
    left += 5
    top += 10

canvas.pack()
mainloop()