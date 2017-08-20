import turtle

def pretvori_v_slovar(ime_datoteke):
    with open(ime_datoteke, encoding = 'utf-8') as f:
        slovar = dict()
        for vrstica in f:
            besedi = vrstica.split(',')
            slovar[besedi[0]] = besedi[1].strip()
    return slovar

slovar_besed = pretvori_v_slovar("slovar.txt")
#print(slovar_besed)

slo_besede = {'nedelja': 'sunday', 'konj': 'horse', 'miza': 'table', 'stopnice': 'stairs', 'dnevna soba': 'living room'}
besede = {'nedelja': 'sunday'}

turtle.shape('turtle')
turtle.color("white")
turtle.hideturtle()

def postavi_besede(slo_besede):
    y = -300
    for slo, ang in slo_besede.items():
        turtle.sety(y)
        turtle.setx(-200)
        turtle.color("black")
        turtle.write(slo,font=("Arial", 10, "normal"))
        turtle.color("white")
        turtle.setx(200)
        turtle.color("black")
        turtle.write(ang,font=("Arial", 10, "normal"))
        turtle.color("white")
        y += 100


#turtle.write('svgbfhhg',font=("Arial", 10, "normal")).setpos(1,1)
postavi_besede(slo_besede)

#ts = turtle.getscreen()
#ts.bgcolor('pink')
#ts.setworldcoordinates(-2,-2,20,20)
#turtle.write('frtdj')
#ts.setworldcoordinates(-80,-80,60,60)
#turtle.write('frtdj')


