import urllib.request
from tkinter import *
from tkinter.ttk import *




########## funkcije ###########
def preberi_bs():
    vrni = dict()
    vrni["EUR"] = 1
    xml = urllib.request.urlopen("http://www.bsi.si/_data/tecajnice/dtecbs.xml").read().decode("ascii")
    podatki = xml.split(' ')
    drzava = ""
    for x in podatki:
        if 'oznaka' in x:
            drzava = x[-4:-1]
        elif 'sifra' in x:
            vrednost = x[12:18]
            vrni[drzava] = vrednost
    return vrni


def convert():
    koliko = float(vpis.get()) #preberemo vsebino text fielda
    iz_katere_valute = combo_iz_katere.get()  #preberemo valuto s prvega lista
    v_katero_valuto = combo_v_katero.get()    #prebermo valuto z drugega lista
    vrednost.set("{0:.2f}".format((koliko / float(slovar_drzav_in_vrednosti[iz_katere_valute])) * float(slovar_drzav_in_vrednosti[v_katero_valuto])))


root = Tk()
root.wm_title('Pretvornik valut')  #poimenovanje okna


slovar_drzav_in_vrednosti = preberi_bs()
seznam_valut = [x for x in slovar_drzav_in_vrednosti.keys()]  #seznam valut za Combobox


#vpis vrednosti v okno
okno = Frame()
vpis = Entry(okno)

#gumb ki klice funkcijo
na_knofu = Button(okno, text="Pretvori", command=convert)


#izpis nove valute
vrednost = StringVar()
besedilo = Label(okno, textvariable=vrednost)


#prvi list za valute
prva1 = StringVar(okno)
prva1.set(seznam_valut[0])
combo_iz_katere = Combobox(okno, textvariable=prva1, state="readonly")
combo_iz_katere["values"] = seznam_valut

#drugi list za valute
prva2 = StringVar(okno)
prva2.set(seznam_valut[1])
combo_v_katero= Combobox(okno, textvariable=prva2, state="readonly")
combo_v_katero["values"] = seznam_valut


####### pakirano #####
okno.pack()
vpis.pack()
combo_iz_katere.pack()
combo_v_katero.pack()
na_knofu.pack()
besedilo.pack()



