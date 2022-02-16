import imp
from string import punctuation
import pygame
from pygame import mixer
import random
import math


# inicializando pygame
pygame.init()

# creando la pantalla
screen = pygame.display.set_mode((800, 600))

# creando el escenario
background = pygame.image.load("background.png")

# sonido de fondo
mixer.music.load('background.wav')
mixer.music.play(-1)

# Título e icono del juego
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Jugador
jugadorImg = pygame.image.load('player.png')
jugadorX = 370
jugadorY = 480
jugadorX_change = 0

# Enemigo
enemigoImg = []
enemigoX = []
enemigoY = []
enemigoX_change = []
enemigoY_change = []
num_de_enemigos = 6

for i in range (num_de_enemigos):
    enemigoImg.append(pygame.image.load('enemy.png'))
    enemigoX.append(random.randint(0,735))
    enemigoY.append(random.randint(50,150))
    enemigoX_change.append(4)
    enemigoY_change.append(40)

# Bala
# 'ready' no puedes ver la bala en la pantalla
# 'fire' la bala se mueve por la pantalla
balaImg = pygame.image.load('bullet.png')
balaX = 0
balaY = 480
balaX_change = 4
balaY_change = 10
bala_estado = "ready"

# Puntuación
valor_puntuacion = 0
font = pygame.font.Font('cubic.ttf', 32)
textX = 10
textY = 10

def muestra_puntuacion(x,y):
    puntuacion = font.render("Puntos: " + str(valor_puntuacion), True, (255,255,255))
    screen.blit(puntuacion,(x,y))




def jugador(x,y):
    screen.blit(jugadorImg,(x,y))
    

def enemigo(x,y,i):
    screen.blit(enemigoImg[i],(x,y))
    
def dispara_bala(x,y):
    global bala_estado
    bala_estado = "fire"
    screen.blit(balaImg, (x+16,y+10))

def esColision(enemigoX, enemigoY, balaX, balaY):
    distancia = math.sqrt((math.pow(enemigoX - balaX,2)) + (math.pow(enemigoY - balaY,2)))

    if distancia < 27:
        return True
    else:
        return False







# game loop
running = True
while running:


    screen.fill((0,0,0))
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # comprobando si se ha pulsado izda o der
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                jugadorX_change = -5
            if event.key == pygame.K_RIGHT:
                jugadorX_change = 5
            if event.key == pygame.K_SPACE:
                if bala_estado is "ready":
                    bala_sonido = mixer.Sound('laser.wav')
                    bala_sonido.play()
                    balaX = jugadorX
                    dispara_bala(balaX, balaY)

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugadorX_change = 0


    # controlando límites de la nave en la pantalla
    jugadorX += jugadorX_change

    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 736:
        jugadorX = 736

    # controlando límites del enemigo en la pantalla
    for i in range (num_de_enemigos):
        enemigoX[i] += enemigoX_change[i]

        if enemigoX[i] <= 0:
            enemigoX_change[i] = 2
            enemigoY[i] += enemigoY_change[i]
        elif enemigoX[i] >= 736:
            enemigoX_change[i] = -2
            enemigoY[i] += enemigoY_change[i]

        # colisión entre bala y enemigo
        colision = esColision(enemigoX[i],enemigoY[i], balaX, balaY)
        if colision:
            explosion_sonido = mixer.Sound('explosion.wav')
            explosion_sonido.play()
            balaY = 480
            bala_estado = "ready"
            valor_puntuacion += 1
            enemigoX[i] = random.randint(0,735)
            enemigoY[i] = random.randint(50,150)

        enemigo(enemigoX[i], enemigoY[i], i)


    # controlando movimiento de la bala
    if balaY <=0:
        balaY = 480
        bala_estado = "ready"
    if bala_estado is "fire":
        dispara_bala(balaX, balaY)
        balaY -= balaY_change






    jugador(jugadorX, jugadorY)
    muestra_puntuacion(textX, textY)

    pygame.display.update()





