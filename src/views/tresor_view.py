import pygame
from views.tile_view import TileView
from tiles.colors import BLACK

class TresorTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles tresor dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        pygame.draw.rect(screen, BLACK, rect)
