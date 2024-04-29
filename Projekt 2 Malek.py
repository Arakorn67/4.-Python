# projekt_2.py: první projekt do Engeto Online Python Akademie
# author: Ondrej Malek
# email: ondrej.malek@dpb.cz
# discord: Arakorn67//76

def print_board(board):
    print("============================================")
    for row in board:
        print("+---+---+---+")
        print("|", " | ".join(row), "|")
    print("+---+---+---+")
    print("============================================")

def check_win(board):
    # Kontrola všech možných výherních kombinací
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player} | Please enter your move number: ")) - 1
            if move not in range(9) or board[move // 3][move % 3] != ' ':
                print("Invalid move, try again.")
            else:
                return move
        except ValueError:
            print("Please enter a number.")

def update_board(move, player, board):
    board[move // 3][move % 3] = player
    return board

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic Tac Toe")
    print("GAME RULES:\nEach player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:\n* horizontal,\n* vertical or\n* diagonal row\nLet's start the game")

    while True:
        print_board(board)
        move = get_move(player, board)
        board = update_board(move, player, board)
        if check_win(board):
            print_board(board)
            print(f"Congratulations, the player {player} WON!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = switch_player(player)

if __name__ == "__main__":
    main()

