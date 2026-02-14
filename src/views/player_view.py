import pygame
from utils import CELL_SIZE, GRID_SIZE
from tiles.colors import BLACK

class PlayerView:
    """Cette classe est responsable de l'affichage du joueur dans le monde de jeu."""
    def draw(self, screen):
        # DESSIN DU JOUEUR (Toujours au centre de l'écran)
        screen_center = (
            (GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2,
            (GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2
        )
        # pygame.draw.circle(screen, BLACK, screen_center, CELL_SIZE // 3)
        image =pygame.image.load("src/views/char_idle_down_anim.gif")
        # screen.blit(image,screen_center)
          

 
        screen.blit(pygame.transform.scale(image,(30,30)),screen_center)