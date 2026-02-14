import pygame
from views.tile_view import TileView
from tiles.colors import SPECIAL

image =pygame.image.load("src/views/tile_32_0.png")
class ExitTileView(TileView):

    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        screen.blit(pygame.transform.scale(image,(40,40)),rect)

