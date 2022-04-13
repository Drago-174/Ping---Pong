from pygame import *

back = (42, 169, 219)
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_z))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
       
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_W] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_S] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
       
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
