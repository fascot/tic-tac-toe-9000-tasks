from copy import deepcopy
from abc import ABC, abstractmethod, abstractproperty
from typing import List, Callable
from dataclasses import dataclass
from tic_tac_toe_common_lib import AbstractTicTacToeGame, TicTacToeTurn, TicTacToeGameInfo

class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str) -> None:
        super().__init__(game_id, first_player_id, second_player_id)
        self.game_info = TicTacToeGameInfo(
            game_id = game_id,
            field = [
                    [" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]
            ],
            sequence_of_turns = [],
            first_player_id = first_player_id,
            second_player_id = second_player_id,
            winner_id = ""
            )
        self.player = deepcopy(self.game_info.first_player_id)

    def get_game_info(self) -> TicTacToeGameInfo:
        return deepcopy(self.game_info)

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if (turn.y_coordinate <= 2 and turn.y_coordinate >= 0 and
        turn.x_coordinate <= 2 and turn.x_coordinate >= 0 and self.player == turn.player_id):
            if self.get_game_info().field[turn.y_coordinate][turn.x_coordinate] != " ":
                return False
            return True
        return False

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) is False:
            return self.get_game_info()
        if turn.player_id == self.game_info.first_player_id:
            self.game_info.field[turn.y_coordinate][turn.x_coordinate] = "X"
            self.game_info.sequence_of_turns.append(turn)
            if (self.get_game_info().field[0][0] == self.get_game_info().field[1][1]
            == self.get_game_info().field[2][0] != " " or self.get_game_info().field[2][0]
            == self.get_game_info().field[1][1] == self.get_game_info().field[0][2] != " "
            or self.get_game_info().field[0][0] == self.get_game_info().field[0][1]
            == self.get_game_info().field[0][2] != " " or self.get_game_info().field[1][0]
            == self.get_game_info().field[1][1] == self.get_game_info().field[1][2] != " "
            or self.get_game_info().field[2][0] == self.get_game_info().field[2][1]
            == self.get_game_info().field[2][2] != " " or self.get_game_info().field[0][0]
            == self.get_game_info().field[1][0] == self.get_game_info().field[2][0] != " "
            or self.get_game_info().field[0][1] == self.get_game_info().field[1][1]
            == self.get_game_info().field[2][1] != " " or self.get_game_info().field[0][2]
            == self.get_game_info().field[1][2] == self.get_game_info().field[2][2] != " "):
                self.game_info.winner_id = self.game_info.first_player_id
            counter = 0
            for y_coord in range(3):
                for x_coord in range(3):
                    if self.get_game_info().field[y_coord][x_coord] == " ":
                        counter += 1
            if counter == 0:
                self.game_info.winner_id = "nobody"
            self.player = self.get_game_info().second_player_id
            return self.game_info
        self.game_info.field[turn.y_coordinate][turn.x_coordinate] = "O"
        self.game_info.sequence_of_turns.append(turn)
        if (self.get_game_info().field[0][0] == self.get_game_info().field[1][1]
        == self.get_game_info().field[2][0] != " " or self.get_game_info().field[2][0]
        == self.get_game_info().field[1][1] == self.get_game_info().field[0][2] != " "
        or self.get_game_info().field[0][0] == self.get_game_info().field[0][1]
        == self.get_game_info().field[0][2] != " " or self.get_game_info().field[1][0]
        == self.get_game_info().field[1][1] == self.get_game_info().field[1][2] != " "
        or self.get_game_info().field[2][0] == self.get_game_info().field[2][1]
        == self.get_game_info().field[2][2] != " " or self.get_game_info().field[0][0]
        == self.get_game_info().field[1][0] == self.get_game_info().field[2][0] != " "
        or self.get_game_info().field[0][1] == self.get_game_info().field[1][1]
        == self.get_game_info().field[2][1] != " " or self.get_game_info().field[0][2]
        == self.get_game_info().field[1][2] == self.get_game_info().field[2][2] != " "):
            self.game_info.winner_id = self.game_info.second_player_id
        counter = 0
        for y_coord in range(3):
            for x_coord in range(3):
                if self.get_game_info().field[y_coord][x_coord] == " ":
                    counter += 1
        if counter == 0:
            self.game_info.winner_id = "nobody"
        self.player = self.get_game_info().first_player_id
        return self.game_info

    def game(self) -> TicTacToeGameInfo:
        while True:
            if self.player == self.game_info.first_player_id:
                print("Ходите первый игрок")
                while True:
                    flag = self.get_game_info()
                    inner = self.do_turn(TicTacToeTurn(
                        self.game_info.first_player_id,
                        int(input())-1,
                        int(input())-1)
                    )
                    if inner == flag:
                        print("такой ход невозможен")
                    else:
                        break
                print(self.game_info.field[0])
                print(self.game_info.field[1])
                print(self.game_info.field[2])
            else:
                print("Ходите второй игрок")
                while True:
                    flag = self.get_game_info()
                    inner = self.do_turn(TicTacToeTurn(
                        self.game_info.second_player_id,
                        int(input())-1,
                        int(input())-1)
                    )
                    if inner == flag:
                        print("такой ход невозможен")
                    else:
                        break
                print(self.game_info.field[0])
                print(self.game_info.field[1])
                print(self.game_info.field[2])
            if self.game_info.winner_id != "":
                print(self.game_info.winner_id)
                break

t = TicTacToeGame("0001","gg","vp")
t.game()
