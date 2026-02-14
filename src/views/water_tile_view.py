import pygame
from views.tile_view import TileView
from tiles.colors import BLUE
image =pygame.image.load("src/views/tile_1_0.png")
class WaterTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles d'eau dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        # pygame.draw.rect(screen, BLUE, rect)
        

        # rec=[rect[0],rect[1],rect[2]+100,rect[3]+200]
        screen.blit(pygame.transform.scale(image,(40,40)),rect)