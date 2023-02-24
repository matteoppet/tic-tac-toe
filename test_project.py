from project import assign_symbol, check_tris, first_move_information


def test_assign_symbol():
    assert assign_symbol("X") == {"Player": "X", "Bot": "O"}
    assert assign_symbol("O") == {"Player": "O", "Bot": "X"}


def test_check_tris():
    ''''
        X in green = \x1b[32mX\x1b[0m
        O in red = \x1b[31mO\x1b[0m
    '''
    dict_symbols = {"Player": "X", "Bot": "O"}


    # Win X
    win_x_horizontal = ['\x1b[32mX\x1b[0m', '\x1b[32mX\x1b[0m', '\x1b[32mX\x1b[0m', 4, 5, 6, 7, 8, 9]
    win_x_diagonal = ['\x1b[32mX\x1b[0m', 2, 3, 4, '\x1b[32mX\x1b[0m', 6, 7, 8, '\x1b[32mX\x1b[0m']
    win_x_vertical = ['\x1b[32mX\x1b[0m', 2, 3, '\x1b[32mX\x1b[0m', 5, 6, '\x1b[32mX\x1b[0m', 8, 9]

    assert check_tris("X", win_x_horizontal, dict_symbols) == "\nThe winner of this game is: \x1b[32mX\x1b[0m"
    assert check_tris("X", win_x_diagonal, dict_symbols) == "\nThe winner of this game is: \x1b[32mX\x1b[0m"
    assert check_tris("X", win_x_vertical, dict_symbols) == "\nThe winner of this game is: \x1b[32mX\x1b[0m"

    # Win O
    win_o_horizontal = ['\x1b[31mO\x1b[0m', '\x1b[31mO\x1b[0m', '\x1b[31mO\x1b[0m', 4, 5, 6, 7, 8, 9]
    win_o_diagonal = ['\x1b[31mO\x1b[0m', 2, 3, 4, '\x1b[31mO\x1b[0m', 6, 7, 8, '\x1b[31mO\x1b[0m']
    win_o_vertical = ['\x1b[31mO\x1b[0m', 2, 3, '\x1b[31mO\x1b[0m', 5, 6, '\x1b[31mO\x1b[0m', 8, 9]

    assert check_tris("O", win_o_horizontal, dict_symbols) == "\nThe winner of this game is: \x1b[31mO\x1b[0m"
    assert check_tris("O", win_o_diagonal, dict_symbols) == "\nThe winner of this game is: \x1b[31mO\x1b[0m"
    assert check_tris("O", win_o_vertical, dict_symbols) == "\nThe winner of this game is: \x1b[31mO\x1b[0m"


def test_first_move_information():
    assert first_move_information("X", {"Player": "O", "Bot": "X"}) == "> First move by: X"
    assert first_move_information("O", {"Player": "O", "Bot": "X"}) == "> First move by: O"