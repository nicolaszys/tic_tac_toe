# TIC TAC TOE 
#lien : https://www.youtube.com/watch?v=BHh654_7Cmw

### NOS VARIABLES FIXES
# LE PLATEAU
board = ['-','-','-', '-','-','-','-','-','-',]
# LE JEU QUI TOURNE
game_still_going = True

# LE GAGNANT
winner = None

# LE JOUEUR EN COURS
current_player = "X"

# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# play game
def play_game():
  #voir le plateau
  display_board()

  while game_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()
  # FIN DU JEU
  if winner == 'X' or winner == "O":
    print("Le gagnant est " + winner)
  elif winner == None:
    print("Egalité")

def handle_turn(player):
    print("C'est au tour de " + player)
    position = input("Choisissez un nombre entre 1-9: ")

    valid = False
    while not valid: 

        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Erreur : Choisissez un nombre entre 1-9: ")

    # but the 1st position is 0 (index) so we have to substract 1
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("La position est deja occupée, choisir une autre position")
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns 
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    # appelle la variable globale
    global game_still_going
    # verifier les symboles de la ligne
    row_1 = board[0] == board[1] == board [2] != "-"
    row_2 = board[3] == board[4] == board [5] != "-"
    row_3 = board[6] == board[7] == board [8] != "-"
    # arreter le jeux si quelqu'un gagne sur la ligne
    if row_1 or row_2 or row_3:
        game_still_going = False
    # trouver le joueur qui a gagné 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # appelle la variable globale
    global game_still_going
    column_1 = board[0] == board[3] == board [6] != "-"
    column_2 = board[1] == board[4] == board [7] != "-"
    column_3 = board[2] == board[5] == board [8] != "-"
    # arreter le jeux si quelqu'un gagne sur la ligne
    if column_1 or column_2 or column_3:
        game_still_going = False
    # trouver le joueur qui a gagné 
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # appelle la variable globale
    global game_still_going
    diagonal_1 = board[0] == board[4] == board [8] != "-"
    diagonal_2 = board[2] == board[4] == board [6] != "-"
    # arreter le jeux si quelqu'un gagne sur la ligne
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # trouver le joueur qui a gagné 
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    # appelle la variable globale
    global current_player
    # changement de joueur en fonction du joueur du moment
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()



