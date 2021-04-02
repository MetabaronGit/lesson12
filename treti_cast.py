import random


# Hlavni funkce
def main():
    # Tisk pravidel
    print_intro()

    # Pripraveni hry
    board, player = setup_game()
    # Hra konci u vyhry/prohry, nebo remízy
    while True:

        # Tisk hraci plochy
        print_board(board)

        # Tah hrace
        board = make_move(player, board)
        # Kontrola vitezneho tahu
        if check_game_over(board, player):
            # Zaverecna zprava 1
            print_game_over(player)
            # Konec loopu
            break

        # Kontrola remízy
        elif board_full(board):
            # Zaverecna zprava 2
            print_tie()
            break
        # Vymena hracu
        player = swap_players(player)

    # Tisk vysledne hraci plochy
    print_board(board)


#######################
# Pripraveni hry
def setup_game():
    # Ziskani velikosti hraci plochy
    size = int(input('Please enter the board size: '))

    # List pro radky hraci plochy
    board = []

    # Nahrani jednotlivych poli
    for row in range(size):
        board.append([' '] * size)

    # Zvoleni hrace
    player_to_start = random.choice(['x', 'o'])
    # Vraceni tuplu hraci plochy a hrace
    return board, player_to_start


#######################
# Uvod
def print_intro():
    # Tisk uvodni zpravy
    print('''
    ===========================
    Welcome to Tic Tac Toe
    GAME RULES:
    Each player can place one mark (or stone) per turn on the 3x3 grid
    The WINNER is who succeeds in placing three of their marks in a
    * horizontal,
    * vertical or
    * diagonal row
    Let's start the game
''', end='\n\n\n')


# Tisk hraci plochy
def print_board(board):
    # List pro tisk hraci plochy
    b = []

    # Velikost hraci plochy
    size = len(board)

    # Nahrati vrchniho ohraniceni hraci plochy do b
    b.append('\n' + '-' * size * 2 + '\n')

    # Pro kazdy radek
    for row in board:
        # Nahrej cleny radku do b, spoj je znakem '|' a zakonci novym radkem
        b.append('|'.join(row) + '\n')
        # Nahrej size-krat znak '-' do b a zakonci novym radkem
        b.append('-' * size * 2 + '\n')

        # Vytiskni jako string vsechny cleny b
    print(''.join(b))


#######################
# Tah
def make_move(player, board):
    # Loop pro zadani mozne pozice
    while True:

        # Vyzva k tahu
        move = int(input('Player {} | Please enter your move number:'.format(player)))

        # Ziskani souradnic se zadane pozice
        row, col = to_coord(move, len(board))

        # Pokud je pole prazdne
        if board[row][col] == ' ':
            # Vloz symbol hrace
            board[row][col] = player
            break

        # Pokud je plne
        else:
            print('\nThis position is already taken\n')

    # Vrat upravenou hraci plochu
    return board


# Pomocna funkce pro tah
def to_coord(scalar_pos, size):
    # Ziskani souradnice slopce ze skalaru
    column = (scalar_pos - 1) % size

    # Ziskani souradnice radku ze skalaru
    row = round((scalar_pos - column) // size)

    # Vracenime radek a sloupec
    return row, column


#######################
# Tah druheho hrace
def swap_players(player):
    # Vraceni opacneho symbolu
    return 'x' if player == 'o' else 'o'


#######################
# Ukonceni hry - Vyhra/Prohra
def check_game_over(board, player):
    # Velikost hraci plochy
    size = len(board)

    # Prevod na 1-dimensionalni list
    flat_board = flatten(board)

    # Prochazime kazdou radu
    for i in range(size):

        # Kontrola radku a sloupcu
        if set(flat_board[i * size:i * size + size]) == set(player) \
                or set(flat_board[i:size ** 2:size]) == set(player):
            return True  # row & column

        # Kontrola diagonaly zleva dolu
        if i == 0 and set(flat_board[i:size ** 2:size + 1]) == set(player):
            return True

        # Kontrola diagonaly zprava dolu
        elif i == size - 1 and set(flat_board[i:size ** 2 - 1:size - 1]) == set(player):
            return True


# Pomocna funkce pro ukonceni hry
def flatten(board):
    # Pomocna promenna pro 1-dimensionalni list
    flat = []

    # Secti jednotlive radky board do flat
    for row in board:
        flat += row

    # Vrat 1-dimensionalni list
    return flat


# Funkce pro tisk vyherce
def print_game_over(player):
    # Oddelovac
    print('\n{}\n'.format('=' * 20))

    # Vyherce
    print('Congratulations, the player {} WON!'.format(player))


#######################
# Ukonceni hry - Remiza
def board_full(board):
    # Je nejake volne misto v board?
    return ' ' not in flatten(board)


# Funkce pro tisk remízy
def print_tie():
    # Oddelovac
    print('\n{}\n'.format('=' * 20))

    # Remiza
    print('Nobody wins, this is a tie')


main()