import pygame
import random


# inicializando pygame
pygame.init()

# creando la pantalla
screen = pygame.display.set_mode((800, 600))

# creando el escenario
background = pygame.image.load("background.png")

# Título e icono del juego
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Jugador
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemigo
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

# Bala
# 'ready' no puedes ver la bala en la pantalla
# 'fire' la bala se mueve por la pantalla
balaImg = pygame.image.load('bullet.png')
balaX = 0
balaY = 480
balaX_change = 4
balaY_change = 10
bala_estado = "ready"



def player(x,y):
    screen.blit(playerImg,(x,y))
    

def enemy(x,y):
    screen.blit(enemyImg,(x,y))
    
def dispara_bala(x,y):
    global bala_estado
    bala_estado = "fire"
    screen.blit(balaImg, (x+16,y+10))



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
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bala_estado is "ready":
                    balaX = playerX
                    dispara_bala(balaX, balaY)

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # controlando límites de la nave en la pantalla
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # controlando límites del enemigo en la pantalla
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    # controlando movimiento de la bala
    if balaY <=0:
        balaY = 480
        bala_estado = "ready"
    if bala_estado is "fire":
        dispara_bala(balaX, balaY)
        balaY -= balaY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()





