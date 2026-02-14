import pygame
from views.tile_view import TileView
from tiles.colors import BLACK
image=pygame.image.load("src/views/tile_37_9.png")
class TresorTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles tresor dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        screen.blit(pygame.transform.scale(image,(40,40)),rect)