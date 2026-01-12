#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # plus large pour aligner le plateau

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Vérifie si toutes les cases sont remplies (match nul)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Boucle jusqu'à obtenir des coordonnées valides
        while True:
            try:
                row = int(input(f"Enter row (0-2) for player {player}: "))
                col = int(input(f"Enter column (0-2) for player {player}: "))
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Coordinates out of range! Try again.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break  # entrée valide
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        # Placer le symbole
        board[row][col] = player

        # Vérifier victoire
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Vérifier match nul
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
