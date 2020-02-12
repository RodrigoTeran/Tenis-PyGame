import pygame
import sys
from pygame.locals import *
from random import randint
pygame.init()
# RGB (0-255)
color = (255, 255, 255)
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Hola Mundo")
# Bola
posicion_X, posicion_Y = 550, 500
velocidad_bola_x = 1
velocidad_bola_y = 1
izquierda = False
arriba = False
quieto = True
timerQuieto = 0
# Paneles
pos_Y_panel_i = 0
pos_Y_panel_d = 0
arriba_panel_i = False
abajo_panel_i = False
arriba_panel_d = False
abajo_panel_d = False
velocidad_panel = 1
text = pygame.font.Font(None, 80)
punt_i = 0
punt_d = 0
while True:
    window.fill(color)
    bola = pygame.draw.circle(window, (0, 0, 0), (posicion_X, posicion_Y), 20)
    izq_1 = pygame.draw.rect(window, (255, 255, 255), (-25, 0, 50, 800))
    der_1 = pygame.draw.rect(window, (255, 255, 255), (1175, 0, 50, 800))
    izq = pygame.draw.rect(window, (0, 0, 0), (0, pos_Y_panel_i, 50, 100))
    der = pygame.draw.rect(window, (0, 0, 0), (1155, pos_Y_panel_d, 50, 100))
    my_text = text.render(f"{punt_i} : {punt_d}", 0, (0, 0, 0))
    window.blit(my_text, (550, 0))
    # No pierde
    if bola.colliderect(izq):
        izquierda = False
    if bola.colliderect(der):
        izquierda = True
    # Pierde
    if bola.colliderect(izq_1):
        quieto = True
        posicion_X = 610
        posicion_Y = randint(0, 700)
        punt_d = punt_d + 1
    if bola.colliderect(der_1):
        quieto = True
        posicion_X = 610
        posicion_Y = randint(0, 700)
        punt_i = punt_i + 1
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        # Mover los paneles manuales
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_w:
                arriba_panel_i = True
            if evento.key == K_s:
                abajo_panel_i = True
            if evento.key == K_UP:
                arriba_panel_d = True
            if evento.key == K_DOWN:
                abajo_panel_d = True
        if evento.type == pygame.KEYUP:
            if evento.key == K_w:
                arriba_panel_i = False
            if evento.key == K_s:
                abajo_panel_i = False
            if evento.key == K_UP:
                arriba_panel_d = False
            if evento.key == K_DOWN:
                abajo_panel_d = False
    # Mover la bola (automatico)
    if timerQuieto > 1000:
        quieto = False
        timerQuieto = 0
    timerQuieto += 1
    if not quieto:
        if not izquierda:
            posicion_X += velocidad_bola_x
            if posicion_X == 1180:
                izquierda = True
        if izquierda:
            posicion_X -= velocidad_bola_x
            if 0 > posicion_X:
                izquierda = False
        if not arriba:
            posicion_Y += velocidad_bola_y
            if posicion_Y == 800:
                arriba = True
        if arriba:
            posicion_Y -= velocidad_bola_y
            if 20 > posicion_Y:
                arriba = False
    # Mover los paneles (i)
    if arriba_panel_i:
        if pos_Y_panel_i > 0:
            pos_Y_panel_i -= velocidad_panel
    if abajo_panel_i:
        if pos_Y_panel_i < 700:
            pos_Y_panel_i += velocidad_panel
    # Mover los paneles (d)
    if arriba_panel_d:
        if pos_Y_panel_d > 0:
            pos_Y_panel_d -= velocidad_panel
    if abajo_panel_d:
        if pos_Y_panel_d < 700:
            pos_Y_panel_d += velocidad_panel
    pygame.display.update()
