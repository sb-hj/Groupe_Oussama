import random
from tiles.colors import *
from tiles.desert_tile import DesertTile
from tiles.tile import Tile
from tiles.water_tile import WaterTile
from tiles.tresor import TresorTile
from tiles.lava import LavaTile
from utils import Position




class LazyGrid:
    """Génération procédurale infinie et déterministe."""
    def __init__(self, seed: int):
        self.seed = seed
        self._cache = {}

    def get_tile(self, x: int, y: int) -> Tile:
        # 1. Vérifier le cache (modifications joueur)
        if (x, y) in self._cache:
            return self._cache[(x, y)]
        
        # 2. Sécurité pour le point de départ
        if x == 1000 and y == 1000:
            return DesertTile(Position(x, y)) 

        # 3. Génération basée sur la seed et les coordonnées
        rng = random.Random(f"{self.seed}_{x}_{y}")
        rand = rng.random()
        
        if rand < 0.9:   
            return  DesertTile(Position(x, y))  # Majorité de tuiles désertiques
        else: 
            if rand < 0.9:
                return TresorTile(Position(x, y))
            else: 
                if rand < 0.93:
                    return LavaTile(Position(x,y))
                else:
                    return WaterTile(Position(x, y))  # Quelques tuiles d'eau
        
    def set_tile(self, x: int, y: int, tile: Tile):
        self._cache[(x, y)] = tile