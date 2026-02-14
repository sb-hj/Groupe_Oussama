import pygame

class Sound :

    def __init__(self,son):
    
        # 1. Initialisation
        pygame.init()
        pygame.mixer.init()

        self.son = son

        # 2. Chargement
        pygame.mixer.music.load(son)
        pygame.mixer.music.play(-1) # -1 pour jouer en boucle

        # 3. Lecture (dans la boucle de jeu)
        # son_clic.play()

    






