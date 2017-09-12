import urllib.request



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

