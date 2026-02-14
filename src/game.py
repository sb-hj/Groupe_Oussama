import random
import eventmanager as evmgr
from entities.player import Player
from grid.lazy_grid import LazyGrid
from tiles.colors import BLUE
from utils import Position
from listener import Listener
from tiles.water_tile import WaterTile
import pygame

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
        pygame.init() # Assure-toi que pygame est initialisé
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Menu")
        
        font = pygame.font.Font(None, 74)
        button_rect = pygame.Rect(300, 250, 200, 80) # Position du bouton
        text = font.render("START", True, (0, 255, 255))
        
        # Phase 1 : Le Menu
        menu_active = True
        while menu_active:
            screen.fill((255, 255, 51)) # Efface l'écran (fond gris foncé)
            
            # Dessiner le bouton et le texte
            pygame.draw.rect(screen, (0, 128, 255), button_rect)
            screen.blit(text, (button_rect.x + 20, button_rect.y + 10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return # Quitter complètement
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        print("Le bouton a été cliqué !")
                        menu_active = False # Sort du menu
                        self.running = True # Lance le jeu

            pygame.display.flip()

        # Phase 2 : La boucle de jeu (Tick)
        self.ev_manager.post(evmgr.InitializeEvent())
        while self.running:
            # Pense à ajouter la gestion du QUIT ici aussi
            newTick = evmgr.TickEvent()
            self.ev_manager.post(newTick)
 