import eventmanager as evmgr
import game
import view
import controller
import sound

def run():
    son = sound.Sound("assets/son/sound.mp3")
    ev_manager = evmgr.EventManager()
    gamemodel = game.GameEngine(ev_manager)
    keyboard = controller.Keyboard(ev_manager, gamemodel)
    graphics = view.GraphicalView(ev_manager, gamemodel)
    gamemodel.run()

if __name__ == '__main__':
    run()