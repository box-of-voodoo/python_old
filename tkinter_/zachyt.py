from tkinter import *

hlavni = Tk()

def kolecko(udalost):
    print (u"kolecko", udalost.delta)

def dvakrat(udalost):
    print('dvakrat x:',udalost.x,'y:',udalost.y)

def mys1(udalost):
    print('leve t. na myši x:',udalost.x,'y:',udalost.y)

def mys2(udalost):
    print('kolecko stisknuto x:',udalost.x,'y:',udalost.y)

def mys3(udalost):
    print('prave tlacitko mysi x:',udalost.x,'y:',udalost.y)

def klavesa(udalost):
    print('klavesa',repr(udalost.char))
    

ramec = Frame(hlavni, width=200, height=200)
ramec.bind("<MouseWheel>", kolecko)
#ramec.bind("<Double-Button-1>", nejakafunkce)
ramec.bind("<Button-1>", mys1)
ramec.bind("<Button-2>", mys2)
ramec.bind("<Button-3>", mys3)
ramec.bind("<Key>", klavesa)
ramec.pack()

ramec.focus_set()
hlavni.mainloop()

#Cancel, BackSpace, Tab, Return (klávesa Enter), Shift_L (levá klávesa Shift), Control_L (levá klávesa Control), Alt_L (levá klávesa Alt), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock a Scroll_Lock.
#a,<space>,<1>(myš),1(klavesnice),
