import tkinter
from tkinter import *

wn = tkinter.Tk()
wn.config(bg="yellow")
wn.minsize(width=300, height=300)


kilo = tkinter.Label(text="kilonuzu yaziniz (kg)")
kilo.config(bg="black", fg="white", font=("Arial", 10, "normal"))
kilo.pack(pady=5)

kilo_input = tkinter.Entry(width=10)
kilo_input.pack(pady=5)

boy = tkinter.Label(text="boyunuzu giriniz (cm)")
boy.config(bg="black", fg="white", font=("Arial", 10, "normal"))
boy.pack(pady=5)

boy_input = tkinter.Entry(width=10)
boy_input.pack(pady=5)


def hesaplama():
    kilo1 = kilo_input.get()
    boy1 = boy_input.get()

    if kilo1 == "" or boy1 == "":
        sonuc.config(text="boy ve kilo girmelisiniz")
    else:
        try:
            bmi = float(kilo1) / (float(boy1) / 100) ** 2
            if bmi <= 18.5:
                sonuc.config(text=f"vki degeriniz : {bmi} ideal kilonun altindasiniz ")
            elif 18.5 <= bmi and bmi <= 24.9:
                sonuc.config(text=f"vki degeriniz : {bmi} ideal kilodasiniz")
            elif 24.9 <= bmi and bmi <=29.9:
                sonuc.config(text=f"vki degeriniz : {bmi} ideal kilonun ustundesiniz")
            elif 29.9 <= bmi and bmi <= 39.9:
                sonuc.config(text=f"vki degeriniz : {bmi} ideal kilonun cok ustundesiniz(obez)")
            elif 39.9 <= bmi :
                sonuc.config(text="ideal kilonun cok ustundesiniz (morbid obez)")

        except:
            sonuc.config(text="sayilar ile girmeyi deneyin")


buton = tkinter.Button(text="Onayla" , command=hesaplama )
buton.pack()

sonuc = tkinter.Label()
sonuc.pack()


mainloop()
