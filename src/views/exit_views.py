import pygame
from views.tile_view import TileView
from tiles.colors import SPECIAL

class ExitTileView(TileView):

    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        pygame.draw.rect(screen, SPECIAL, rect)
