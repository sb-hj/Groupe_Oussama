import pygame
from views.tile_view import TileView
from tiles.colors import LAVA
image=pygame.image.load("src/views/tile_3_19.png")
class LavaTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles d'eau dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        screen.blit(pygame.transform.scale(image,(40,40)),rect)
