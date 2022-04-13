from pygame import *

back = (42, 169, 219)
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
window.fill(back)


game = True

finish = False

clock = time.Clock()

FPS = 60


while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)