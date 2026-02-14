from entities.entity import Entity
from tiles.tile import Tile
from utils import Position


class ExitTile(Tile):

    def __init__(self, position: Position):
        super().__init__(position)

    def on(self, entity: Entity):
        return None
