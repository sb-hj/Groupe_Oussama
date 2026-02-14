import pygame
import game
import eventmanager as evmgr
from tiles.colors import BLACK
from utils import CELL_SIZE, GRID_SIZE, HEIGHT, WIDTH
from listener import Listener
from views.player_view import PlayerView
from views.world_view import WorldView

class GraphicalView(Listener):
    """
    Cette classe est responsable de l'affichage graphique du jeu en utilisant Pygame. 
    Elle écoute les événements du jeu et met à jour l'affichage en conséquence. 
    Elle utilise des sous-vues pour dessiner le monde et le joueur.
    """

    def __init__(self, ev_manager, model):
        """
        ev_manager: l'instance de EventManager pour s'abonner aux événements du jeu
        model: l'instance du modèle de jeu pour accéder aux données du jeu à afficher       

        La fonction d'initialisation configure les attributs de la classe,
        s'abonne aux événements du jeu et initialise les sous-vues pour le joueur et le monde.
        """

        self.ev_manager = ev_manager
        ev_manager.register(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.smallfont = None
        
        # Sub-views
        self.player_view = PlayerView()
        self.world_view = WorldView()

    def notify(self, event):
        """
        Reçoit les événements du jeu et met à jour l'affichage en conséquence.
         - InitializeEvent: initialise l'affichage graphique
         - QuitEvent: ferme l'affichage graphique et quitte le jeu
         - TickEvent: met à jour l'affichage du jeu en cours
        """

        if isinstance(event, evmgr.InitializeEvent):
            self.initialize()
        elif isinstance(event, evmgr.QuitEvent):
            # shut down the pygame graphics
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event, evmgr.TickEvent):
            if not self.isinitialized:
                return
            self.renderplay(self.model.player,self.model.grid)
            # limit the redraw speed to 30 frames per second
            self.clock.tick(30)

    def renderplay(self,player,grid):
        """
        Fonction de rendu qui met à jour l'affichage du jeu en cours.
         - player: l'instance du joueur pour accéder à sa position et son état
         - grid: l'instance de la grille du jeu pour accéder à l'état du monde
        """
        self.draw(player,grid)
    
    def draw(self,player,grid):
        self.screen.fill((255, 255, 255))
        pygame.image.load("src/views/char_shielded_static_down.png")
        
        # Delegate drawing to sub-views
        self.world_view.draw(self.screen, grid, player.pos)
        self.player_view.draw(self.screen)

        pygame.display.flip()

    def initialize(self):
        """
        Initialise l'affichage graphique du jeu en configurant Pygame et les sous-vues.
        """

        _ = pygame.init()
        # pygame.font.init() # Disabled for Python 3.14 compatibility
        pygame.display.set_caption('Extraction Game')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        # self.smallfont = pygame.font.Font(None, 40) # Disabled for Python 3.14 compatibility
        self.smallfont = None
        self.isinitialized = True