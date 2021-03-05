from copy import deepcopy
from abc import ABC, abstractmethod, abstractproperty
from typing import List, Callable
from dataclasses import dataclass
from .tic_tac_toe_common_lib import AbstractTicTacToeGame, TicTacToeTurn, TicTacToeGameInfo

class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str) -> None:
        super().__init__(game_id, first_player_id, second_player_id)
        self.game_id = game_id
        self.field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.sequence_of_turns = []
        self.first_player_id = first_player_id
        self.second_player_id = second_player_id
        self.winner_id = ""
        self.player = self.first_player_id

    def get_game_info(self) -> TicTacToeGameInfo:
        return deepcopy(TicTacToeGameInfo(
            game_id = self.game_id,
            field = self.field,
            sequence_of_turns = self.sequence_of_turns,
            first_player_id = self.first_player_id,
            second_player_id = self.second_player_id,
            winner_id = self.winner_id
        ))

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.winner_id == "":
            if (turn.y_coordinate <= 2 and turn.y_coordinate >= 0 and turn.x_coordinate <= 2
            and turn.x_coordinate >= 0 and turn.player_id == self.player):
                if self.field[turn.y_coordinate][turn.x_coordinate] != " ":
                    return False
                return True
        return False

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) is False:
            return self.get_game_info()
        if turn.player_id == self.first_player_id:
            self.field[turn.y_coordinate][turn.x_coordinate] = "X"
            self.sequence_of_turns.append(turn)
            for y in range(3):
                if self.field[y][0] == self.field[y][1] == self.field[y][2] == "X":
                    self.winner_id = self.first_player_id
            for x in range(3):
                if self.field[0][x] == self.field[1][x] == self.field[2][x] == "X":
                    self.winner_id = self.first_player_id
            if self.field[0][0] == self.field[1][1] == self.field[2][2] == "X":
                self.winner_id = self.first_player_id
            if self.field[-1][-1] == self.field[-2][-2] == self.field[-3][-3] == "X":
                self.winner_id = self.first_player_id
            counter = 0
            for y_coord in range(3):
                for x_coord in range(3):
                    if self.field[y_coord][x_coord] == " ":
                        counter += 1
            if counter == 0:
                self.winner_id = "nobody"
            self.player = self.second_player_id
            return self.get_game_info()
        self.field[turn.y_coordinate][turn.x_coordinate] = "O"
        self.sequence_of_turns.append(turn)
        for y in range(3):
            if self.field[y][0] == self.field[y][1] == self.field[y][2] == "O":
                self.winner_id = self.first_player_id
        for x in range(3):
            if self.field[0][x] == self.field[1][x] == self.field[2][x] == "O":
                self.winner_id = self.first_player_id
        if self.field[0][0] == self.field[1][1] == self.field[2][2] == "O":
            self.winner_id = self.first_player_id
        if self.field[-1][-1] == self.field[-2][-2] == self.field[-3][-3] == "O":
            self.winner_id = self.first_player_id
        counter = 0
        for y_coord in range(3):
            for x_coord in range(3):
                if self.field[y_coord][x_coord] == " ":
                    counter += 1
        if counter == 0:
            self.winner_id = "nobody"
        self.player = self.first_player_id
        return self.get_game_info()
