import os
import time


class Game:
    def __init__(self) -> None:
        self.gameBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = "X"
        self.winner = None
        self.game_over = False

    def play(self):
        while not self.game_over:
            os.system('clear')
            self.printGameBoard()
            self.player_move()
            self.check_game_over()
            self.switch_player()

        if self.winner == 'X' or self.winner == 'O':
            print(self.winner + ' wins!')
        else:
            print('It\'s a tie!')

    def printGameBoard(self):
        for row in self.gameBoard:
            rowString = '| ' + ' | '.join(row) + ' |'
            print('-'*len(rowString))
            print(rowString)
            print('-'*len(rowString))

    def player_move(self):
        move = None
        while not (move and self.is_playable(move)):
            move = input(self.player + "'s turn. input: x,y: ")
        row = int(move[0]) - 1
        col = int(move[2]) - 1
        self.gameBoard[row][col] = self.player

    def is_playable(self, move):
        if len(move) != 3:
            return False
        if move[1] != ',':
            return False
        row = int(move[0])
        col = int(move[2])

        if row < 1 or row > 3:
            return False
        if col < 1 or col > 3:
            return False

        if self.gameBoard[row - 1][col - 1] != ' ':
            return False

        return True

    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def check_game_over(self):
        self.check_tie()
        self.check_winner()

    def check_tie(self):
        if all(all(place != ' ' for place in board) for board in self.gameBoard):
            time.sleep(0.2)
            self.game_over = True

    def check_winner(self):
        # check on rows
        for row in self.gameBoard:
            if row[0] == row[1] == row[2] != ' ':
                self.winner = row[0]
                self.game_over = True

        for col in range(len(self.gameBoard)):
            check = []
            for row in self.gameBoard:
                check.append(row[col])
            if check[0] == check[1] == check[2] != ' ':
                self.winner = check[0]
                self.game_over = True

        if self.gameBoard[0][0] == self.gameBoard[1][1] == self.gameBoard[2][2] != ' ':
            self.winner = self.gameBoard[0][0]
            self.game_over = True
        if self.gameBoard[0][2] == self.gameBoard[1][1] == self.gameBoard[2][0] != ' ':
            self.winner = self.gameBoard[0][2]
            self.game_over = True


if __name__ == '__main__':
    game = Game()
    game.play()
