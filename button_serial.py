import tkinter 
import serial

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
time.sleep(3)

root = Tk()


def onClick():
	ser.write(b'h')
def offClick(): 
	ser.write(b'l')

onButton = Button(root, text = "LED On", padx=50, pady=50, command=onClick)
offButton = Button(root, text = "LED Off", padx=50, pady=50, command=offClick)

onButton.pack()
offButton.pack()

root.mainloop()

