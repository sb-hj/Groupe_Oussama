import pygame
import eventmanager as evmgr
from game import GameEngine
from utils import Move
from listener import Listener


class Keyboard(Listener):
    """
    Cette classe est responsable de la gestion des entrées clavier du joueur. 
    Elle écoute les événements de Tick pour vérifier les touches pressées et poster des événements d'entrée
    """

    def __init__(self, ev_manager: evmgr.EventManager, model: GameEngine):
        """
        ev_manager: l'instance de EventManager pour s'abonner aux événements du jeu
        model: l'instance du modèle de jeu pour accéder aux données du jeu à afficher
        """
        self.ev_manager = ev_manager
        ev_manager.register(self)
        self.model = model

    def notify(self, event: evmgr.Event):
        """
        Reçoit les événements du jeu et vérifie les entrées clavier en conséquence.
         - TickEvent: vérifie les touches pressées et poste des événements d'entrée utilisateur

        """

        if isinstance(event, evmgr.TickEvent):
            # Called for each game tick. We check our keyboard presses here.
            for pgev in pygame.event.get():
                # handle window manager closing our window
                if pgev.type == pygame.QUIT:
                    self.ev_manager.post(evmgr.QuitEvent())
                    # The GraphicalView calls pygame.quit() upon
                    # receiving the QuitEvent. We shouldn't return to
                    # the top of the loop here. `pygame.event` might be
                    # undefined.
                    break
                # handle key down events
                if pgev.type == pygame.KEYDOWN:
                    if pgev.key == pygame.K_ESCAPE:
                        self.ev_manager.post(evmgr.QuitEvent())
                        break
                    else:
                        self.on_keydown(pgev)


    def on_keydown(self, event: pygame.event.Event):
        """
        Vérifie les touches pressées et poste des événements d'entrée utilisateur en conséquence.
         - event: l'événement de touche pressée à vérifier
        """

        match event.key:
            case pygame.K_DOWN:  self.ev_manager.post(evmgr.InputEvent(Move.DOWN,None))
            case pygame.K_LEFT:  self.ev_manager.post(evmgr.InputEvent(Move.RIGHT,None))
            case pygame.K_RIGHT: self.ev_manager.post(evmgr.InputEvent(Move.LEFT,None))
            case pygame.K_UP: self.ev_manager.post(evmgr.InputEvent(Move.UP,None))
            case pygame.QUIT: self.ev_manager.post(evmgr.QuitEvent())
            case _: pass
    