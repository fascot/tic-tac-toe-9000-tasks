from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

game = TicTacToeGame(
    game_id="0001",
    first_player_id="Petya",
    second_player_id="Vasya"
)

game.game_info.winner_id = "ee"

assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=1,
            y_coordinate=2
        )
    ) == True
print("vnb")