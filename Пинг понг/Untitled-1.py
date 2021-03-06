import pygame
import time

time.sleep(3)

back = (42, 169, 219)
win_width = 800
win_height = 700
window = pygame.display.set_mode((win_width, win_height))

window.fill(back)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_z,player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x,size_z))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
       
    def update_l(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
       
game = True

finish = False

clock = pygame.time.Clock()

FPS = 60

line = 0


pygame.mixer.init()
pygame.mixer.music.load('213.ogg')
pygame.mixer.music.set_volume(1.2)
pygame.mixer.music.play()

racket = Player('22222222.jpg' , -150,200,200, 145, 15)
racket2 = Player('1111111.jpg' , 750,200,200, 145, 15)

ball = GameSprite('22.png', 280, 200,40, 40, 15)

dx = 3
dy = 3

pygame.font.init()
#font = font.Font(None, 36)
#pygame.lose1 = pygame.font.render('PlAYER 1 lOSE', True ,(180, 0, 0))
#pygame.lose2 = pygame.font.render('PlAYER 2 lOSE', True ,(180, 0, 0))



score_left = 0

score_right = 0




Balls = -2
while game:

    for e in pygame.event.get():
        if type == pygame.QUIT:
            game = False




    if finish != True:

        window.fill(back)

        ball.rect.x += dx
        ball.rect.y += dy

        if pygame.sprite.collide_rect(racket, ball) or pygame.sprite.collide_rect(racket2, ball):
            dx *= -1

        if ball.rect.y < 0 or ball.rect.y > win_height - 40:
            dy *= -1




        if ball.rect.x < 0:
            ball.rect.x = 280
            ball.rect.y = 200
            score_right +=1
            #dx *= Balls - 0,5
        
            


        
        
        #score_l = pygame.font.render(str(score_left), True , (0, 0, 0))
        #score_r = pygame.font.render(str(score_right), True , (0, 0, 0))
        #window.blit(score_l, (10,10))
        #window.blit(score_r, (win_width-25, 10))


        if ball.rect.x > win_width:
            score_left +=1
            ball.rect.x = 280
            ball.rect.y = 200


        if score_left >= 5:
            finish= True
            window.blit(lose1, (260,220))

        if score_right >= 5:
            finish= True
            window.blit(lose2, (260,220))




        racket.update_l()
        racket2.update_r()

        racket.reset()
        racket2.reset()
        ball.reset()


    pygame.display.update()
    clock.tick(FPS)
