import pyglet
window = pyglet.window.Window()

import sys
from time import sleep

hp = 100

doing_image = pyglet.image.load('assets/hero/sliced/kick.png')
doing = pyglet.sprite.Sprite(doing_image, x=20, y=50)

hairspray_image = pyglet.image.load('assets/hero/sliced/parachute.png')
hairspray = pyglet.sprite.Sprite(hairspray_image, x=50, y=100)

img_image = pyglet.image.load('assets/hero/sliced/idle-1.png')
img = pyglet.sprite.Sprite(img_image, x=50, y=50)

como_image = pyglet.image.load('assets/hero/sliced/idle-2.png')
como = pyglet.sprite.Sprite(como_image, x=100, y=50)

other_image = pyglet.image.load('assets/hero/sliced/idle-3.png')
other = pyglet.sprite.Sprite(other_image, x=150, y=50)

hello_image = pyglet.image.load('assets/setting.png')
hello = pyglet.sprite.Sprite(hello_image, x=150, y=300)

txt = pyglet.text.Label('hi', x = 300, y = 200) 

stuff = pyglet.text.Label('Hi', x = 200, y = 200) 

health_bar = pyglet.text.Label(str(hp), x = 200, y = 100)    

keys = pyglet.window.key.KeyStateHandler()

jump = False

def action():
    pass

           #global jump
           #jump = True
    #while jump == True:
        #img.y += 1
        #sleep(0.02)
        #if img.y > 500:
            #jump = False
           # img.y -= 1
            #sleep(0.02) 

up = True
down = True
left = True
right = True



def update(dt):
    window.push_handlers(keys) 
    global up
    global down
    global left
    global right
    global hp

    if hp > 0:
        health_bar.text = str(hp)
    else:
        health_bar.text = "Game over"

    if keys[pyglet.window.key.UP] and up == True:
        img.y += 2
    if keys[pyglet.window.key.DOWN] and down == True:
        img.y -= 2
    if keys[pyglet.window.key.LEFT] and left == True:
        img.x -= 2
    if keys[pyglet.window.key.RIGHT] and right == True:
        img.x += 2
    
    if img.y > 462:
        up = False
        hp -= 1
    else:
        up = True
    if img.y < 3:
        down = False
        hp -= 1
    else:
        down = True
    if img.x < 3:
        left = False
        hp -= 1
    else:
        left = True
    if img.x > 622:
        right = False
        hp -= 1
    else:
        right = True


@window.event
def on_draw():
    window.clear()
    img.draw()
    health_bar.draw()
    hello.draw()
    como.draw()
    doing.draw()
    hairspray.draw()
    txt.draw()
    stuff.draw()

pyglet.clock.schedule(update)
pyglet.app.run()