import random
import eventmanager as evmgr
from entities.player import Player
from grid.lazy_grid import LazyGrid
from tiles.colors import BLUE
from tiles.colors import YELLOW
from utils import Position
from listener import Listener
from tiles.water_tile import WaterTile
from tiles.tresor import TresorTile
from tiles.desert_tile import DesertTile
from tiles.lava import LavaTile

class GameEngine(Listener):
    """
    Cette classe est le moteur principal du jeu. 
    Elle gère la logique du jeu, y compris le déplacement du joueur et l'interaction avec la grille du monde. 
    Elle écoute les événements du jeu pour mettre à jour l'état
    """

    def __init__(self, ev_manager):
        """
        ev_manager: l'instance de EventManager pour s'abonner aux événements du jeu
        """

        self.ev_manager = ev_manager
        ev_manager.register(self)
        self.running = False
        
        # Initialisation : Monde infini commençant à (1000, 1000)
        self.grid = LazyGrid(seed=random.randint(0, 99999))
        self.player = Player(Position(1000, 1000))

    def move_player(self,direction):
        """
        Tente de déplacer le joueur dans la direction spécifiée.
         - direction: une chaîne indiquant la direction du mouvement ('up', 'down', 'left', 'right')
         - Vérifie si la nouvelle position est un tile d'eau avant de
        """
        new_pos = Position(self.player.pos.x, self.player.pos.y)
        new_pos.move(direction)
        if not isinstance(self.grid.get_tile(new_pos.x, new_pos.y), WaterTile):
            self.player.move(direction)
            
    def notify(self, event):
        """
        Reçoit les événements du jeu et met à jour l'état du jeu en conséquence.
         - QuitEvent: arrête le moteur de jeu
         - InputEvent: tente de déplacer le joueur en fonction de l'entrée utilisateur  
        """

        if isinstance(event, evmgr.QuitEvent):
            self.running = False

        if isinstance(event, evmgr.InputEvent):  
            self.move_player(event.input_type)

    def run(self):
        """
        Démarre la boucle principale du jeu en postant des événements de Tick pour mettre à jour le jeu.  
        """
        self.running = True
        self.ev_manager.post(evmgr.InitializeEvent())
        while self.running:
            newTick = evmgr.TickEvent()
            self.ev_manager.post(newTick)