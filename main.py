from tkinter import*

okno = Tk()

okno.geometry('600x700')
okno.title("Hamburgr konfigurace")


# nazev formu
nazev_form = Label(okno, text="Konfigurátor burgeru",width=20,font=("bold", 40))
nazev_form.place(x=0,y=53)


# nazev burgeru
nazev_burgeru = Label(okno, text="Nazev burgeru",width=20,font=("bold", 16))
nazev_burgeru.place(x=50,y=130)

nazev_burgeru_vstup = Entry(okno)
nazev_burgeru_vstup.place(x=250,y=135)

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

# druhy_zemli
druhy_zemli = ["Klasická", "Sezamová", "Bramborová", "Kaiserka", "Ciabatta"]
clicked = StringVar()
clicked.set("Klasická")
drop = OptionMenu( okno , clicked , *druhy_zemli )
drop.pack()

zemle = Label(okno, text="Vyberte druh žemle", width=20, font=("bold", 16))
zemle.place(x=60,y=320)
drop.place(x=100,y=350)


# zelenina
zelenina = Label(okno, text="Vyberte si zeleninu", width =20, font=("bold", 16))
zelenina.place(x=60,y=380)

rajce_vyber = IntVar()
salat_vyber = IntVar()
okurka_vyber = IntVar()
cibule_vyber = IntVar()

Checkbutton(okno, text="rajče",variable=rajce_vyber).place(x=100,y=410)
Checkbutton(okno, text="salát",variable=salat_vyber).place(x=100,y=430)
Checkbutton(okno, text="okurka",variable=okurka_vyber).place(x=100,y=450)
Checkbutton(okno, text="cibule",variable=cibule_vyber).place(x=100,y=470)

# omacky
omacky = ["Kečup", "Majonéza", "BBQ", "Texaský dresing"]
vyber_omacky = StringVar()
vyber_omacky.set("Kečup")
drop_omacky = OptionMenu( okno , vyber_omacky , *omacky )
drop_omacky.pack()

omacky_text = Label(okno, text="Vyberte omačku", width=20, font=("bold", 16))
omacky_text.place(x=60,y=500)
drop_omacky.place(x=100,y=530)

#submit
Button(okno, text='Submit',width=20,bg='green',fg='white').place(x=180,y=570)

okno.mainloop()

