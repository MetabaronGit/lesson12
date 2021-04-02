# bulls and cows vzor
# Import modulu
import random


#######################
# Hlavni funkce
def main():
    # Pomocna fce 1
    print_intro()

    # Pomocna fce 2
    my_num = generate_num(4)
    num_guesses = 0

    # Hra bezi, dokud check_game_over nize nevrati True
    while True:
        your_num = input('\nEnter your number: ')
        num_guesses += 1

        # Pomocna fce 3
        if wrong_input(your_num):
            continue

        # Pomocna fce 4
        bulls, cows = count_bulls_cows(your_num, my_num)

        # Pomocna fce 5
        if check_game_over(bulls, cows, num_guesses):
            break


#######################
# Predstaveni hry
def print_intro():
    # Uvodni text
    print('''
    Hi there!
    I've generated a secret random 4 digit number for you.
    Your task is to guess, what number it is.
    Enter a 4 digit number where 
        * the digits will not repeat and
        * the number cannot begin with 0.
    If the matching digits:
        * are in their right positions, they are "bulls", 
        * if in different positions, they are "cows".
    Try to guess what number I am thinking of
    ''')


#######################
# Generovani 4-mistneho cisla
def generate_num(length):
    # Pomocna promenna
    num = ''

    # Dokud nemam 4-cif cislo s unikatnimi cislicemi
    while len(set(num)) != length or num[0] == 0:
        # Generuj cislo od 1000 do 9999
        num = str(random.randint(1000, 9999))

    # Vratim cislo
    print("CISLOOO", num)
    return num


#######################
# Kontrola vstupu
def wrong_input(inpt):
    # Pomocna promenna
    result = False

    # Je vstup 4 mistne cele cilo?
    if not inpt.isdecimal() or len(inpt) != 4:
        print('\nPlease enter a whole 4-digit number')
        result = True

    # Ma cislo unikatni cislice?
    if len(set(inpt)) != 4:
        print('\nPlease enter a number not repeating the digits')
        result = True

    # Vraceni testovani
    return result


#######################
# Porovnavani
def count_bulls_cows(inpt, secret_num):
    # Overeni bulls & cows
    bulls = cows = 0

    # Porovnavani
    for index, num in enumerate(inpt):
        if num == secret_num[index]:
            bulls += 1
        elif num in secret_num:
            cows += 1

    # Vraceni porovnani
    return bulls, cows


#######################
# Ukonceni hry
def check_game_over(bulls, cows, num_guesses):
    # Aktualni stav
    status = '| {} bulls | {} cows | {} guesses |'

    # Stav hry
    game_over = False

    # Presahnuti poctu hadani
    if bulls == 4:
        suffix = 'es' if num_guesses > 1 else ''
        print('\nGame Over, found it after %d guess%s'
              % (num_guesses, suffix))
        print('That is %s' % (evaluation(num_guesses)), end='\n\n')
        game_over = True

    # Tisk aktualniho stavu
    else:
        print(status.format(bulls, cows, num_guesses))

    # Stavu hry
    return game_over


# Pomocna fce pro ukonceni hry
def evaluation(guesses):
    # Vyhodnoceni 1
    if guesses <= 2: return 'Amazing'

    # Vyhodnoceni 2
    if guesses <= 5: return 'Good'

    # Vyhodnoceni 3
    return 'Not so good'


main()