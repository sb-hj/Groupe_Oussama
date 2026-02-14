import random
import eventmanager as evmgr
from entities.player import Player
from grid.lazy_grid import LazyGrid
from tiles.colors import BLUE
from utils import Position
from listener import Listener
from tiles.water_tile import WaterTile
from tiles.lava import LavaTile
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
        if not isinstance(self.grid.get_tile(new_pos.x, new_pos.y), WaterTile) and not isinstance(self.grid.get_tile(new_pos.x, new_pos.y), LavaTile):
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
        # button_rect = pygame.Rect(300, 250, 200, 80) # Position du bouton
        # text_play = font.render("Jouer", True, (255, 255, 255))
        # text_quit = font.render("Quitter", True, (255, 255, 255))
        
        # Phase 1 : Le Menu
        menu_active = True
        while menu_active:
            screen.fill((0, 0, 0)) # Efface l'écran (fond gris foncé)
            
            # Dessiner le bouton et le texte
            text_play = font.render("START", True, (255, 255, 255))
            text_quit = font.render("Quitter", True, (255, 255, 255))

            play_rect = pygame.Rect(200, 100, 200, 80)
            quit_rect = pygame.Rect(200, 400, 200, 80)

    
            pygame.draw.rect(screen, (0, 128, 255), play_rect, 2)
            pygame.draw.rect(screen, (0, 128, 255), quit_rect, 2)

            screen.blit(text_play, (play_rect.centerx - text_play.get_width()//2, play_rect.centery - text_play.get_height()//2))
            screen.blit(text_quit, (quit_rect.centerx - text_quit.get_width()//2, quit_rect.centery - text_quit.get_height()//2))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return # Quitter complètement
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_rect.collidepoint(event.pos):
                        print("Le bouton a été cliqué !")
                        self.running = False # Lance le jeu
                        menu_active = False # Sort du menu
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(event.pos):
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
 

# """import pygame

# pygame.init()

# # 1. On change la taille de la fenêtre
# screen_width = 600
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# font = pygame.font.Font(None, 74)

# # Textes
# text_play = font.render("Jouer", True, (255, 255, 255))
# text_options = font.render("Options", True, (255, 255, 255))
# text_quit = font.render("Quitter", True, (255, 255, 255))

# # 2. On adapte les coordonnées 'x' pour centrer les boutons (x = 200)
# # Et on réduit un peu l'espacement vertical 'y' pour que tout tienne
# play_rect = pygame.Rect(200, 100, 200, 80)
# options_rect = pygame.Rect(200, 250, 200, 80)
# quit_rect = pygame.Rect(200, 400, 200, 80)

# running = True
# while running:
#     screen.fill((0, 0, 0))
    
#     # Dessin des boutons (rectangles)
#     pygame.draw.rect(screen, (0, 128, 255), play_rect, 2)
#     pygame.draw.rect(screen, (0, 128, 255), options_rect, 2)
#     pygame.draw.rect(screen, (0, 128, 255), quit_rect, 2)

#     # Affichage du texte centré sur les boutons
#     screen.blit(text_play, (play_rect.centerx - text_play.get_width()//2, play_rect.centery - text_play.get_height()//2))
#     screen.blit(text_options, (options_rect.centerx - text_options.get_width()//2, options_rect.centery - text_options.get_height()//2))
#     screen.blit(text_quit, (quit_rect.centerx - text_quit.get_width()//2, quit_rect.centery - text_quit.get_height()//2))

#     pygame.display.flip()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if play_rect.collidepoint(event.pos):
#                 print("Jouer")
#             elif options_rect.collidepoint(event.pos):
#                 print("Options")
#             elif quit_rect.collidepoint(event.pos):
#                 print("Quitter")

# pygame.quit()"""