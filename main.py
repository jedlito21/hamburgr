from tkinter import*

okno = Tk()

okno.geometry('500x500')
okno.title("Hamburgr konfigurace")


# nazev formu
nazev_form = Label(okno, text="Konfigurátor burgeru",width=20,font=("bold", 40))
nazev_form.place(x=0,y=53)


# nazev burgeru
nazev_burgeru = Label(okno, text="Nazev burgeru",width=20,font=("bold", 16))
nazev_burgeru.place(x=50,y=130)

nazev_burgeru_vstup = Entry(okno)
nazev_burgeru_vstup.place(x=220,y=130)

# propečenost masa burgeru
propecenost = Label(okno, text="Vyberte propečenost masa",width=20,font=("bold", 16))
propecenost.place(x=95,y=175)

propecenost_vyber = IntVar() # propecenost_vyber je variable ke který přiřazuju radiobuttony
Radiobutton(okno, text="Well-Done",padx = 5, variable=propecenost_vyber, value=1).place(x=100,y=200)
Radiobutton(okno, text="Medium-Well",padx = 5, variable=propecenost_vyber, value=2).place(x=100,y=220)
Radiobutton(okno, text="Medium",padx = 5, variable=propecenost_vyber, value=3).place(x=100,y=240)
Radiobutton(okno, text="Rare",padx = 5, variable=propecenost_vyber, value=4).place(x=100,y=260)
Radiobutton(okno, text="Medium-Rare",padx = 5, variable=propecenost_vyber, value=5).place(x=100,y=280)
Radiobutton(okno, text="Blue-Rare",padx = 5, variable=propecenost_vyber, value=6).place(x=100,y=300)

okno.mainloop()

