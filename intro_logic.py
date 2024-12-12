from PyQt6.QtWidgets import *
from intro_gui import *

class Intro_Logic(QMainWindow, Ui_window_intro):
    def __init__(self):
        """
        Initializes appropriate variables for the player names, whether or not enter was pressed, and assigns a function to the enter button.
        """
        super().__init__()
        self.setupUi(self)
        self.input_player_name_one.setFocus()
        self.player_name_one = ''
        self.player_name_two = ''
        self.was_enter_pressed = False

        self.button_enter.clicked.connect(lambda : self.enter())

    def enter(self):
        """
        Checks that input names are valid, then sets them to their respective variables and changes the enter variable to True. If the input is not valid, inputs will clear and refocus.
        """
        if self.input_player_name_one.text().strip() == '' or self.input_player_name_two.text().strip() == '' or self.input_player_name_one.text().strip() == self.input_player_name_two.text().strip():
            self.label_instructions.setText('Names must be unique')
            self.input_player_name_one.clear()
            self.input_player_name_two.clear()
            self.input_player_name_one.setFocus()
        else:
            self.player_name_one = self.input_player_name_one.text().strip()
            self.player_name_two = self.input_player_name_two.text().strip()
            self.was_enter_pressed = True
            self.close()

    def pressed_enter(self) -> bool:
        """
        Allows an outside file to access whether or not the enter button was pressed.

        :return: Whether the enter button was pressed.
        """
        return self.was_enter_pressed

    def get_player_name_one(self) -> str:
        """
        Allows an outside file to access the first player's name.

        :return: Player one's name.
        """
        return self.player_name_one

    def get_player_name_two(self) -> str:
        """
        Allows an outside file to access the second player's name.

        :return: Player two's name.
        """
        return self.player_name_two