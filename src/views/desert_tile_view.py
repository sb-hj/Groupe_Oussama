import pygame
from views.tile_view import TileView
from tiles.colors import YELLOW

        
        
image =pygame.image.load("src/views/tile_0_16.png")
class DesertTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles de désert dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        screen.blit(pygame.transform.scale(image,(40,40)),rect)