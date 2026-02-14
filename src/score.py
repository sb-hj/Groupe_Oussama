import pygame
pygame.init()
font = pygame.font.SysFont("Arial", 30) # Créer une police

import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            score += 1 # Exemple : le score augmente à chaque touche


    # 3. Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()