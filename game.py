from snake import Snake
from board import  Board
from apple import Apple
from bomb import Bomb
import game_display

class Game:
    def __init__ (self):
        self.__snake_game = Snake((10,10),3,"Right")
        self.__board_game = Board()
        self.__apples_game = [Apple(),Apple(),Apple()]
        self.__bomb_game = Bomb()
        self.__game_values = {}
        for row in range (self.__board_game.get_height()):
            for col in range(self.__board_game.get_width()):
                for apple in self.__apples_game:
                    if apple.get_location()[0]== row and apple.get_location()[1]==col:
                        self.__game_values[(row,col)] = "green"
                if self.__bomb_game.get_position()[0]== row and self.__bomb_game.get_position()[1]==col:
                    self.__game_values[(row,col)] = "red"
                for i in range(len(self.__snake_game.starting_tuples())):
                    if row == self.__snake_game.get_position()[i][0] and col == self.__snake_game.get_position()[i][1]:
                        self.__game_values[(row, col)] = "black"

    def get_game_value(self):
        return self.__game_values

    def inital_three_apples(self)->list:
        pass

    def snake_eat_apple(self):
        for apple in self.__apples_game:
            if apple.get_location() in self.__snake_game.get_position():
                # self.__game_values[apple.get_location()] = "black"
                del (self.__game_values[apple.get_location()])
                self.__game_values[apple.get_location()] = "black"
                new_apple = Apple()
                self.__apples_game.append(new_apple)
                ##TODO every iteration to that self.__snake_game.eat_apple()

    def snake_meets_bomb(self):
        for bomb in self.__bomb_game.get_position():
            if bomb == self.__snake_game.get_position():
                # TODO terminates game
                pass

    # TODO snake out of borders

    def apple_bomb(self):
        for bomb in self.__bomb_game.get_position():
            for apple in self.__apples_game:
                if apple.get_location() == bomb:
                    apple_loc = apple.get_location()
                    self.__game_values.pop(apple_loc)
                    new_apple = Apple()
                    self.__apples_game.append(new_apple)

    def snake_move(self, key_clicked):
        self.__snake_game.snake_move(key_clicked)
        print(self.__snake_game.get_position())
        for row in range(self.__board_game.get_height()):
            for col in range(self.__board_game.get_width()):
                if (row, col) in self.__snake_game.get_position():
                    self.__game_values[(row, col)] = "black"
                try:
                    if self.__game_values[(row, col)] == "black" and (row, col) not in self.__snake_game.get_position():
                        del (self.__game_values[(row, col)])
                except KeyError:
                    continue

    def meetings(self):
        self.snake_meets_bomb()
        self.apple_bomb()
        self.snake_eat_apple()

    def get_snake(self):
        return self.__snake_game.get_position()

    # def delete_tail(self):
    #     for tup in self.__game_values:
    #         if tup == "black" and tup not in self.get_snake():
    #             del (self.__game_values[tup])
