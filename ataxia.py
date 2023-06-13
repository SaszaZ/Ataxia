import time

canvas_size=800

rot1 = 0
rot2 = 0


def setup():
    global ramie1, ramie2, staw, x_rand, y_rand, tekst, alpha, _time
    
    _time = 0
    createCanvas(canvas_size, canvas_size)
    ramie1 = loadImage('ramie1.png')
    ramie2 = loadImage('ramie2.png')
    staw = loadImage('staw.png')
    
    strokeWeight(10)
    alpha = False        
    odl=random(28,268)
    kat=random(0,2*PI)
    x_rand = 400+odl * sin(kat)
    y_rand = 400+odl * cos(kat)
    tekst = "Sprobuj"


def draw():
    global rot1, rot2, x2, y2, _time, x_rand, y_rand, tekst, alpha
    offsety = 26
    _time += 1
    if _time>=500:
        if x2 <= (x_rand + 10):
            if x2 >= (x_rand - 10):
                if y2 <= (y_rand + 10):
                    if y2 >= (y_rand - 10):
                        tekst = "Udalo Ci sie"
                else:
                    tekst = "Niestety nie udalo sie. Sprobuj jeszcze raz"
        else:
            tekst = "Niestety nie udalo sie. Sprobuj jeszcze raz"
        odl=random(28,268)
        kat=random(0,2*PI)
        x_rand = 400+odl * sin(kat)
        y_rand = 400+odl * cos(kat)
        _time=0
    if keyIsDown(38):
        rot1+=(5/1000+random((-1/100),(1/100)))
        _time = 0
    if keyIsDown(39):
        rot2+=(1/100+random((-1/10),(1/10)))
        _time = 0
    if keyIsDown(40):
        rot1-=(5/1000+random((-1/100),(1/100)))
        _time = 0
    if keyIsDown(37):
        rot2-=(1/100+random((-1/10),(1/10)))
        _time = 0
    clear()
    background(88, 88, 107)
    fill(42, 42, 43)
    noStroke()
    circle(400, 400, 400)
    fill(28, 28, 31)
    text("Sprobuj zlapac kropke", 300, 100)
    text("Poruszanie - [strzalki]", 300, 150)
    text(tekst, 300, 700)
    x1=400+sin(-rot1+PI/2)*148
    y1=400+cos(-rot1+PI/2)*148
    x2=x1+sin(-(rot1+rot2)+PI/2)*120
    y2=y1+cos(-(rot1+rot2)+PI/2)*120
    strokeWeight(10);
    stroke(51);
    point(x_rand,y_rand)
    translate(400, 400)
    rotate(rot1)
    image(ramie1, 0 - offsety, 0 - (56 / 2))
    translate(148, 0)
    rotate(rot2-PI/2)
    image(ramie2, -45 / 2, -45 / 2)
    image(staw, -17,-17)


    
    
