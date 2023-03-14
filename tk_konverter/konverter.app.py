from tkinter import *

def km_to_mi():
    """
    #amit a bementebe beírtunk a get-el megkapjuk
    szam = bemenet1.get()
    print(szam)
    """
    try:
        # 1km = 1 / 1.609344
        km = bemenet1.get() #megkapom amit az entry widgetbe beírtunk
        ktm = float(km) / 1.609344 #matek
        text1['state'] = NORMAL #státuszt megváltoztatom hogy tudjunk bele írni
        text1.delete(1.0, END) # delete-vel törlöm ami benne van
        ktm = str(ktm) #string konvert
        text1.insert(END, ktm[0:5]) #text widgetbe belerakom és egy szeletelés hogy 0-tól 5ig elemig jelenitse meg
        text1['state'] = DISABLED #disable a statusz hogy ne lehessen bele írni/klikkelni

    except:
        text1['state'] = NORMAL
        text1.delete(1.0, END)
        text1.insert(END, 'Csak számokat!')
        text1['state'] = DISABLED


    # f = c * 9/5 +32
def cel_to_far():
    try:
        cel =bemenet2.get()
        ctf= float(cel) * 9/5 + 32
        text2['state'] = NORMAL
        text2.delete(1.0, END)
        ctf = str(ctf)
        text2.insert(END, ctf[0:5])
        text2['state'] = DISABLED
    except:
        text2['state'] = NORMAL
        text2.delete(1.0, END)
        text2.insert(END, 'Csak számokat!')
        text2['state'] = DISABLED


# az alap ablak
win = Tk()
# az ablak neve/cime
win.title('Konverter')
# az ablak merete
win.geometry('800x600')

# text / szöveg
Label(win, text="kilometer", font="Helvetica 12 bold").grid(row=0, column=1)
Label(win, text="merfold", font="Helvetica 12 bold").grid(row=1, column=1)

Label(win, text="celsius", font="Helvetica 12 bold").grid(row=0, column=1)
Label(win, text="farenheit", font="Helvetica 12 bold").grid(row=1, column=1)



#gomb lenyomasaval vegrehajtóduk a matek
Button(win, text="calculate km to mi", command=km_to_mi, font="Helvetica 12 bold").grid(row=2, column=0)
Button(win, text="calculate c to f", command=cel_to_far, font="Helvetica 12 bold").grid(row=5, column=0)




#ide írjuk be a km-t számokban
bemenet1 = Entry(win, font="Helvetica 20 bold")
bemenet1.grid(row=0, column=0)

#celsius számokban
bemenet2 = Entry(win, font="Helvetica 20 bold")
bemenet2.grid(row=3, column=0)



#itt jelenik meg a számítás mint mérföld
#state disable miatt nem tudunk beleklikkelni és írni
text1 = Text(win, height=1, width=20, state=DISABLED, font="Helvetica 20 bold")
text1.grid(row=1, column=0)

#itt fog a farenheit megjelenni
text2 = Text(win, height=1, width=20, state=DISABLED, font="Helvetica 20 bold")
text2.grid(row=4, column=0)





#ez a ciklus tartja életben az appot
win.mainloop()