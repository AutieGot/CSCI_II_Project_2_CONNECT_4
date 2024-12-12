from PyQt6.QtWidgets import *
from main_gui import *

class Main_Logic(QMainWindow, Ui_window_main):
    def __init__(self, one: str, two: str):
        """
        Initializes the game's variables, buttons, and visuals. Takes in two names.

        :param one: Player one's name.
        :param two: Player two's name.
        """
        super().__init__()
        self.setupUi(self)

        self.player_name_one = one
        self.player_name_two = two
        self.label_player.setText(f'{self.player_name_one}\'s turn')
        self.player_one = True
        self.winner = 0
        self.col = -1
        self.numeric = False
        self.connect_board = []
        for x in range(6):
            self.connect_board.append([''] * 7)
        self.print_board()
        self.button_save.setVisible(False)

        self.button_0.clicked.connect(lambda : self.column_0())
        self.button_1.clicked.connect(lambda : self.column_1())
        self.button_2.clicked.connect(lambda : self.column_2())
        self.button_3.clicked.connect(lambda : self.column_3())
        self.button_4.clicked.connect(lambda : self.column_4())
        self.button_5.clicked.connect(lambda : self.column_5())
        self.button_6.clicked.connect(lambda : self.column_6())
        self.button_save.clicked.connect(lambda : self.save())

    def column_0(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 0
        self.check_numeric()

    def column_1(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 1
        self.check_numeric()

    def column_2(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 2
        self.check_numeric()

    def column_3(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 3
        self.check_numeric()

    def column_4(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 4
        self.check_numeric()

    def column_5(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 5
        self.check_numeric()

    def column_6(self):
        """
        Assigns column to button when pressed then checks if the column is still available.
        """
        self.col = 6
        self.check_numeric()

    def check_numeric(self):
        """
        Checks that the column still has space and continues to carry out functions. If column does not have space, runs the invalid function.
        """
        if self.connect_board[0][self.col] != 'X' and self.connect_board[0][self.col] != 'O':
            self.numeric = True
            self.place_symbol()
            self.print_board()
            self.check_winner_1()
            if self.winner != 0:
                self.display_winner()
        else:
            self.invalid_input()

    def place_symbol(self):
        """
        Now that the column is free, this will place the player's symbol in the lowest possible row.
        """
        x = 5
        while x >= 0:
            if self.connect_board[x][self.col] != 'X' and self.connect_board[x][self.col] != 'O':
                if self.player_one:
                    self.connect_board[x][self.col] = 'X'
                    self.label_player.setText(f'{self.player_name_two}\'s turn')
                else:
                    self.connect_board[x][self.col] = 'O'
                    self.label_player.setText(f'{self.player_name_one}\'s turn')
                self.player_one = not self.player_one
                break
            x -= 1

    def print_board(self):
        """
        Assigns each label in the GUI to one piece of the 2-dimensional connect board.
        """
        self.label_0_0.setText(self.connect_board[0][0])
        self.label_0_1.setText(self.connect_board[0][1])
        self.label_0_2.setText(self.connect_board[0][2])
        self.label_0_3.setText(self.connect_board[0][3])
        self.label_0_4.setText(self.connect_board[0][4])
        self.label_0_5.setText(self.connect_board[0][5])
        self.label_0_6.setText(self.connect_board[0][6])
        self.label_1_0.setText(self.connect_board[1][0])
        self.label_1_1.setText(self.connect_board[1][1])
        self.label_1_2.setText(self.connect_board[1][2])
        self.label_1_3.setText(self.connect_board[1][3])
        self.label_1_4.setText(self.connect_board[1][4])
        self.label_1_5.setText(self.connect_board[1][5])
        self.label_1_6.setText(self.connect_board[1][6])
        self.label_2_0.setText(self.connect_board[2][0])
        self.label_2_1.setText(self.connect_board[2][1])
        self.label_2_2.setText(self.connect_board[2][2])
        self.label_2_3.setText(self.connect_board[2][3])
        self.label_2_4.setText(self.connect_board[2][4])
        self.label_2_5.setText(self.connect_board[2][5])
        self.label_2_6.setText(self.connect_board[2][6])
        self.label_3_0.setText(self.connect_board[3][0])
        self.label_3_1.setText(self.connect_board[3][1])
        self.label_3_2.setText(self.connect_board[3][2])
        self.label_3_3.setText(self.connect_board[3][3])
        self.label_3_4.setText(self.connect_board[3][4])
        self.label_3_5.setText(self.connect_board[3][5])
        self.label_3_6.setText(self.connect_board[3][6])
        self.label_4_0.setText(self.connect_board[4][0])
        self.label_4_1.setText(self.connect_board[4][1])
        self.label_4_2.setText(self.connect_board[4][2])
        self.label_4_3.setText(self.connect_board[4][3])
        self.label_4_4.setText(self.connect_board[4][4])
        self.label_4_5.setText(self.connect_board[4][5])
        self.label_4_6.setText(self.connect_board[4][6])
        self.label_5_0.setText(self.connect_board[5][0])
        self.label_5_1.setText(self.connect_board[5][1])
        self.label_5_2.setText(self.connect_board[5][2])
        self.label_5_3.setText(self.connect_board[5][3])
        self.label_5_4.setText(self.connect_board[5][4])
        self.label_5_5.setText(self.connect_board[5][5])
        self.label_5_6.setText(self.connect_board[5][6])

    def check_winner_1(self):
        """
        Checks for a winner horizontally across the board. If no winner is found, continues to the second check.
        """
        x = 5
        y = 0
        for i in range(6):
            while y <= 3 and x >= 0:
                if self.connect_board[x][y] == '':
                    y += 1
                elif self.connect_board[x][y] == 'X' and self.connect_board[x][y + 1] == 'X' and self.connect_board[x][y + 2] == 'X' and self.connect_board[x][y + 3] == 'X':
                    self.winner = 1
                    break
                elif self.connect_board[x][y] == 'O' and self.connect_board[x][y + 1] == 'O' and self.connect_board[x][y + 2] == 'O' and self.connect_board[x][y + 3] == 'O':
                    self.winner = 2
                    break
                else:
                    y += 1
            if self.winner != 0:
                break
            elif self.winner == 0:
                x -= 1
                y = 0
        if self.winner == 0:
            self.winner_check_2()

    def winner_check_2(self):
        """
        Checks for a winner vertically across the board. If no winner is found, continues to the third check.
        """
        x = 5
        y = 0
        for i in range(3):
            while x >= 3 and y <= 6:
                if self.connect_board == '':
                    y += 1
                elif self.connect_board[x][y] == 'X' and self.connect_board[x - 1][y] == 'X' and self.connect_board[x - 2][y] == 'X' and self.connect_board[x - 3][y] == 'X':
                    print("Player one wins!")
                    self.winner = 1
                    break
                elif self.connect_board[x][y] == 'O' and self.connect_board[x - 1][y] == 'O' and self.connect_board[x - 2][y] == 'O' and self.connect_board[x - 3][y] == 'O':
                    print("Player two wins!")
                    self.winner = 2
                    break
                else:
                    y += 1
            if self.winner != 0:
                break
            elif self.winner == 0:
                x -= 1
                y = 0
        if self.winner == 0:
            self.winner_check_3()

    def winner_check_3(self):
        """
        Checks for a winner in the positive diagonal across the board. If no winner is found, continues to check 4.
        """
        x = 5
        y = 0
        for i in range(3):
            while x >= 3 >= y:
                if self.connect_board == '':
                    y += 1
                elif self.connect_board[x][y] == 'X' and self.connect_board[x - 1][y + 1] == 'X' and self.connect_board[x - 2][y + 2] == 'X' and self.connect_board[x - 3][y + 3] == 'X':
                    print("Player one wins!")
                    self.winner = 1
                    break
                elif self.connect_board[x][y] == 'O' and self.connect_board[x - 1][y + 1] == 'O' and self.connect_board[x - 2][y + 2] == 'O' and self.connect_board[x - 3][y + 3] == 'O':
                    print("Player two wins!")
                    self.winner = 2
                    break
                else:
                    y += 1
            if self.winner != 0:
                break
            elif self.winner == 0:
                x -= 1
                y = 0
        if self.winner == 0:
            self.winner_check_4()

    def winner_check_4(self):
        """
        Checks for a winner in the negative diagonal across the board. If no winner is found, continues to check draw.
        """
        x = 2
        y = 0
        for i in range(3):
            while x >= 0 and y <= 3:
                if self.connect_board == '':
                    y += 1
                elif self.connect_board[x][y] == 'X' and self.connect_board[x + 1][y + 1] == 'X' and self.connect_board[x + 2][y + 2] == 'X' and self.connect_board[x + 3][y + 3] == 'X':
                    print("Player one wins!")
                    self.winner = 1
                    break
                elif self.connect_board[x][y] == 'O' and self.connect_board[x + 1][y + 1] == 'O' and self.connect_board[x + 2][y + 2] == 'O' and self.connect_board[x + 3][y + 3] == 'O':
                    print("Player two wins!")
                    self.winner = 2
                    break
                else:
                    y += 1
            if self.winner != 0:
                break
            elif self.winner == 0:
                x -= 1
                y = 0
        if self.winner == 0:
            self.check_draw()

    def check_draw(self):
        """
        Checks the board to see if it is full.
        """
        draw = False
        if self.connect_board[0][0] != '' and self.connect_board[0][1] != '' and self.connect_board[0][2] != '' and self.connect_board[0][3] != '' and self.connect_board[0][4] != '' and self.connect_board[0][5] != '' and self.connect_board [0][6] != '':
            draw = True
        if draw:
            self.label_player.setText('Draw!!')
            self.end_game()

    def end_game(self):
        """
        If the game has ended to either player winning or a draw, this will disable the buttons and allow the results to be saved.
        """
        self.button_0.setVisible(False)
        self.button_1.setVisible(False)
        self.button_2.setVisible(False)
        self.button_3.setVisible(False)
        self.button_4.setVisible(False)
        self.button_5.setVisible(False)
        self.button_6.setVisible(False)
        self.button_save.setVisible(True)

    def display_winner(self):
        """
        If a winner has been found, winner will be displayed and game will be ended.
        """
        if self.winner == 1:
            self.label_player.setText(f'{self.player_name_one} wins!!')
        elif self.winner == 2:
            self.label_player.setText(f'{self.player_name_two} wins!!')
        self.end_game()

    def invalid_input(self):
        """
        Creates a pop-up window if the column selected is not available.
        """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Error!")
        dlg.setText("Try another column.")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Warning)
        dlg.exec()

    def save(self):
        """
        Allows the players to save the results of their game into a txt file and close the game. If there is an issue with the file, the game will not close.
        """
        try:
            with open('connect_four_history.txt', 'a') as outfile:
                if self.winner == 1:
                    outfile.write('Player 1 wins\n')
                elif self.winner == 2:
                    outfile.write('Player 2 wins\n')
                else:
                    outfile.write('Draw\n')
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Success!")
                dlg.setText("Results were successfully saved!")
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.setIcon(QMessageBox.Icon.Information)
                dlg.exec()
                self.close()
        except FileNotFoundError:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText("File has not been found!")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()