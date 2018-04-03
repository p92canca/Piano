from tkinter import *
import tkinter.font as tkf
from tkinter import ttk
# Import the package that allows me to play sounds.
import simpleaudio as sa
# Import the package that allows me to keep track of time.
import time as t
import tkinter.ttk as ttk

start = t.time()

##### White keys ####
def keyC():
	key.set("C")
	sound = pygame.mixer.Sound("sounds/C1.wav")
	sound.play()
	return

def keyD():
	key.set("D")
	sound = pygame.mixer.Sound("sounds/D1.wav")
	sound.play()
	return

def keyE():
	key.set("E")
	sound = pygame.mixer.Sound("sounds/E1.wav")
	sound.play()
	return

def keyF():
	key.set("F")
	sound = pygame.mixer.Sound("sounds/F1.wav")
	sound.play()
	return

def keyG():
	key.set("G")
	sound = pygame.mixer.Sound("sounds/G1.wav")
	sound.play()
	return

def keyA():
	key.set("A")
	sound = pygame.mixer.Sound("sounds/A1.wav")
	sound.play()
	return

def keyB():
	#key.set("B")
	#sound = pygame.mixer.Sound("sounds/B1.wav")
	#sound.play()
	wave_obj = sa.WaveObject.from_wave_file("sounds/B1.wav")
	wave_obj.play()
	print("B")
	return

##### Blacks keys ####
def keyC():
	key.set("C#")
	sound = pygame.mixer.Sound("sounds/C1#.wav")
	sound.play()
	print("C#")
	return

def keyD():
	key.set("D")
	sound = pygame.mixer.Sound("sounds/D1#.wav")
	sound.play()
	return

def keyF():
	key.set("F")
	sound = pygame.mixer.Sound("sounds/F1#.wav")
	sound.play()
	return

def keyG():
	key.set("G")
	sound = pygame.mixer.Sound("sounds/G1#.wav")
	sound.play()
	return

def keyA():
	#key.set("A")
	sound = pygame.mixer.Sound("sounds/A1#.wav")
	sound.play()
	return

def acercaDe():
	#Ventana acerca de
	otherwindow = Toplevel(root)
	otherwindow.resizable(width=TRUE, height=TRUE)
	otherwindow.title("Virtual Piano")
	otherwindow.transient(root) # this makes otherwindow modal
	otherwindow.grab_set()
	labelAcerca = Label(otherwindow, text="Virtual Piano Aplication created for subject URO of VSB", font=fontBnt)
	labelAcerca.pack(pady=5)
	labelAcerca1 = Label(otherwindow, text="Version 0.1\nBuild date 27 March 2018", font=fontBnt)
	labelAcerca1.pack(pady=5)
	labelAcerca2 = Label(otherwindow, text="(c) 2018 Alberto Cañete", font=fontBnt)
	labelAcerca2.pack()
	labelAcerca3 = Label(otherwindow, text="alberto.canete.carpintero.st@vsb.cz", font=fontUnder)
	labelAcerca3.pack(pady=10)
	btn1 = Button(otherwindow, text="Close", command=otherwindow.destroy, font=fontBnt)
	btn1.pack(padx=10, pady=10)

	return

def sound():
	#Ventana sound
	otherwindow = Toplevel(root)
	otherwindow.resizable(width=TRUE, height=TRUE)
	otherwindow.title("Sound")
	otherwindow.transient(root) # this makes otherwindow modal
	otherwindow.grab_set()
	speakerLabel = Label(otherwindow, text="Speaker", font=fontDisplay)
	speakerLabel.pack(side="top", expand=1, fill="x", padx=5, pady=5)
	speakerSlider = Scale(otherwindow, orient=HORIZONTAL, length=300, width=15, font=fontBnt).pack()

	microLabel = Label(otherwindow, text="Microphone", font=fontDisplay)
	microLabel.pack(side="top", expand=1, fill="both", padx=5, pady=5)
	microSlider = Scale(otherwindow, orient=HORIZONTAL, length=300, width=15, font=fontBnt).pack()
	btn1 = Button(otherwindow, text="Close", command=otherwindow.destroy, font=fontBnt)
	btn1.pack(padx=10, pady=10)

	return

def equalizer():
	otherwindow = Toplevel(root)
	otherwindow.resizable(width=TRUE, height=TRUE)
	otherwindow.title("Equalizer")
	otherwindow.transient(root) # this makes otherwindow modal
	otherwindow.grab_set()
	
	#Slider60hz
	freqLabel = Label(otherwindow, text="60 Hz", font=fontDisplay)
	freqLabel.place(x=10, y=5)
	slider1 = Scale(otherwindow, length=300, width=15, font=fontBnt, from_=20, to=-20)
	slider1.set(0)
	slider1.place(x=10, y=50)
	
	#Slider310hz
	freqLabel = Label(otherwindow, text="310 Hz", font=fontDisplay)
	freqLabel.place(x=110, y=5)
	slider1 = Scale(otherwindow, length=300, width=15, font=fontBnt, from_=20, to=-20)
	slider1.set(0)
	slider1.place(x=110, y=50)
	
	#Slider1khz
	freqLabel = Label(otherwindow, text="1 KHz", font=fontDisplay)
	freqLabel.place(x=210, y=5)
	slider1 = Scale(otherwindow, length=300, width=15, font=fontBnt, from_=20, to=-20)
	slider1.set(0)
	slider1.place(x=210, y=50)
	
	#Slider3khz
	freqLabel = Label(otherwindow, text="3 KHz", font=fontDisplay)
	freqLabel.place(x=310, y=5)
	slider1 = Scale(otherwindow, length=300, width=15, font=fontBnt, from_=20, to=-20)
	slider1.set(0)
	slider1.place(x=310, y=50)
	
	#Slider6khz
	freqLabel = Label(otherwindow, text="6 KHz", font=fontDisplay)
	freqLabel.place(x=410, y=5)
	slider1 = Scale(otherwindow, length=300, width=15, font=fontBnt, from_=20, to=-20)
	slider1.set(0)
	slider1.place(x=410, y=50)
	
	#Slider14khz
	freqLabel = Label(otherwindow, text="14 KHz", font=fontDisplay)
	freqLabel.place(x=510, y=5)
	slider1 = Scale(otherwindow, length=300, width=15, font=fontBnt, from_=20, to=-20)
	slider1.set(0)
	slider1.place(x=510, y=50)
	
	btn1 = Button(otherwindow, text="Ok", command=otherwindow.destroy, font=fontBnt)
	btn1.place(x=300, y=400)
	
	w = 650
	h = 450
	sw = root.winfo_screenwidth()
	sh = root.winfo_screenheight()
	x = (sw - w) / 2
	y = (sh - h) / 2
	otherwindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	return

root = Tk()
root.title("Project 1 URO")
fontDisplay = tkf.Font(family="Segoe UI Semibold", size=16, weight='normal')
fontBnt = tkf.Font(family="Segoe UI Semibold", size=11, weight='normal')
fontUnder= tkf.Font(family="Segoe UI Semibold", size=11, weight='bold', underline=1)

# The 2-dimensional array keys holds the locations, names and after the
# for loops are executed below, the Labels that are needed
# to create each key, both white and black.
imagenWhiteKey = PhotoImage(file="pictures/white_key.gif")
imagenBlackKey = PhotoImage(file="pictures/black_key.gif")
c=1
keys = [
    [0, 'C1'],
    [35, 'C#1'],
    [50, 'D1'],
    [85, 'D#1'],
    [100, 'E1'],
    [150, 'F1'],
    [185, 'F#1'],
    [200, 'G1'],
    [235, 'G#1'],
    [250, 'A1'],
    [285, 'A#1'],
    [300, 'B1'],
    [350, 'C2'],
    [385, 'C#2'],
    [400, 'D2'],
    [435, 'D#2'],
    [450, 'E2'],
    [500, 'F2'],
    [535, 'F#2'],
    [550, 'G2'],
    [585, 'G#2'],
    [600, 'A2'],
    [635, 'A#2'],
    [650, 'B2']
]
for key in keys:
	if len(key[1]) == 2:
		btn = Button(root, text=key, image=imagenWhiteKey, command=keyB)
		btn.place(x=key[0], y=100)
		labelName = Label(root, text=key[1], font=fontBnt)
		labelName.place(x=key[0]+20, y=305)
		root.columnconfigure(c, weight=1)
		c+=1

c=1
for key in keys:
	if len(key[1]) > 2:
		btn = Button(root, text=key, image=imagenBlackKey)
		btn.place(x=key[0], y=100)
		labelName = Label(root, text=key[1], font=fontBnt)
		labelName.place(x=key[0]+5, y=75)
		c+=1

#Crea sound button
imagenSound = PhotoImage(file="pictures/sound.png")
soundthBtn = Button(root, bg="gray90", relief=GROOVE, borderwidth=3, width=40, height=40, font=fontBnt, image=imagenSound, command=sound)
soundthBtn.place(x=750, y=50)

#Crea equalizer button
imagenEqualizer = PhotoImage(file="pictures/equalizer.png")
equalizerBtn = Button(root, bg="gray90", relief=GROOVE, borderwidth=3, width=40, height=40, font=fontBnt, image=imagenEqualizer, command=equalizer)
equalizerBtn.place(x=750, y=120)

#Crea rec button
imagenRec = PhotoImage(file="pictures/rec.png")
recBtn = Button(root, bg="gray90", relief=GROOVE, borderwidth=3, width=40, height=40, font=fontBnt, image=imagenRec)
recBtn.place(x=750, y=190)

#Crea stop button
imagenStop = PhotoImage(file="pictures/stop.png")
stopBtn = Button(root, bg="gray90", relief=GROOVE, borderwidth=3, width=40, height=40, font=fontBnt, image=imagenStop)
stopBtn.place(x=750, y=260)

# Crear label octave
labelOctave = Label(root, text="Base Octave: ", font=fontBnt)
labelOctave.place(x=10, y=20)

cbx = ttk.Combobox(root, values=["1", "2", "3", "4"])
cbx.set("1")
cbx.configure(width=5, font=fontBnt)
cbx.place(x=130, y=20)

# Crear label transpose
labelTranspose = Label(root, text="Transpose: ", font=fontBnt)
labelTranspose.place(x=230, y=20)

cbx = ttk.Combobox(root, values=["-4", "-3", "-2", "-1", "1", "2", "3", "4"])
cbx.set("1")
cbx.configure(width=5, font=fontBnt)
cbx.place(x=333, y=20)

# Crear label bank
labelBank = Label(root, text="Bank: ", font=fontBnt)
labelBank.place(x=440, y=20)

cbx = ttk.Combobox(root, values=["Grand Piano", "Guitar", "Trumpet", "Synth", "Soft Piano"])
cbx.set("Grand Piano")
cbx.configure(width=17, font=fontBnt)
cbx.place(x=500, y=20)

# Crear el menu principal
menubarra = Menu(root, font=fontBnt)

# Crea un menu desplegable y lo agrega al menu barra
menuarchivo = Menu(menubarra, tearoff=0, font=fontBnt)
menuarchivo.add_command(label="New recording")
menuarchivo.add_command(label="Stop")
menuarchivo.add_separator()
menuarchivo.add_command(label="Save")
menuarchivo.add_command(label="Save as")
menuarchivo.add_separator()
menuarchivo.add_command(label="Exit", command=root.quit)
menubarra.add_cascade(label="File", menu=menuarchivo)

# Crea dos menus desplegables mas
menueditar = Menu(menubarra, tearoff=0, font=fontBnt)
menueditar.add_command(label="Sound", command=sound)
menueditar.add_command(label="Equalizer", command=equalizer)
menuarchivo.add_separator()
menueditar.add_command(label="Language")
menubarra.add_cascade(label="Tools", menu=menueditar)
menuayuda = Menu(menubarra, tearoff=0, font=fontBnt)
menuayuda.add_command(label="About", command=acercaDe)
menubarra.add_cascade(label="Help", menu=menuayuda)


# This group of lines centers the window on the screen
# and specifies the size of the window.
w = 850
h = 350
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) / 2
y = (sh - h) / 2
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.config(menu=menubarra)
root.mainloop()
