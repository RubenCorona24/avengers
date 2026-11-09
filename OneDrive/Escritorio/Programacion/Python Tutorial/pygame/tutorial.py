#Pygame tutorial

#importar librería
import pygame
pygame.init() #inicializar el programa

#configurar la ventana
screen = pygame.display.set_mode([500,500])

#correr programa hasta que el usuario lo quite
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        screen.fill((255,255,255))

        #dibujar un circulo azul
        pygame.draw.circle(screen,(0,0,255),(250,250),75)

        #girar la pantalla
        pygame.display.flip()
#Finalizar programa
pygame.quit()