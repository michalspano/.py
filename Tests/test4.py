import tkinter
from PIL import ImageTk, Image
canvas = tkinter.Canvas()
canvas.pack()

photo = Image.open("/Users/michalspano/Google Drive/P-4th Grade/Revision exercises/flowers/flower1.png")
resized = photo.resize((300, 225), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)

canvas.create_image(100, 100, image=new_pic)

canvas.mainloop()
