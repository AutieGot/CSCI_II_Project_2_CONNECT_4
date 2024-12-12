from intro_logic import *
from main_logic import *

def main():
    """
    Runs the intro window to get the player names. If enter was clicked, will continue to the game with the player names.
    """
    application = QApplication([])
    intro_window = Intro_Logic()
    intro_window.show()
    application.exec()
    if intro_window.pressed_enter():
        main_window = Main_Logic(intro_window.get_player_name_one(), intro_window.get_player_name_two())
        main_window.show()
        application.exec()

if __name__ == '__main__':
    main()