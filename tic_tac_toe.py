# Tic Tac Toe
from itertools import count
from termcolor import colored, cprint #for color text in consol
import os
import random  
import time

#define colors for texts in game
print_red_on_cyan = lambda x: cprint(x, 'grey', 'on_cyan') 
print_red = lambda x: cprint(x, 'red', attrs=['blink'])
print_yellow = lambda x: cprint(x, 'yellow', attrs=['bold'])
tieText = colored("Tie!\n", 'green', attrs=['bold', 'blink'])

X = "X"
O = "O"
EMPTY = "."
TIE = "TIE"
NUM_SQUARES = 9
items = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

def display_instruct():
    cprint(
        """
        Hey, hi, hello! Welcome to the greatest intellectual challenge of all time - Tic Tac Toe. 
        You can play with your friend, brother or sister, mum, maybe sun. Depends who you have at hand. Plus, you don't waste paper.
        If you don't have anyone at hand, we have a great solution for you - play against the computer - simply or smart.
        If you overestimate your strength, play with the smart one. 
        And if you are a fan of streams, you can always watch the computer face its alter ego.

        Make your move by entering one of empty field (A1 - C3).
    
                    A1| A2 | A3
                    -----------
                    B1| B2 | B3
                    -----------
                    C1| C2 | C3

        Get ready, Player. Nothing venture, nothing gain. \n
    """, 'red'
    )


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number():
    response1 = input("Your turn. Choose wisely: ")
    response = response1.lower()

    if response == 'quit':
        cprint("\tAbsence makes the heart grow fonder. See ya!", 'yellow')
        response = quit(0)

    if response == 'a1':
        response = 0

    elif response == 'a2':
        response = 1

    elif response == 'a3':
        response = 2

    elif response == 'b1':
        response = 3

    elif response == 'b2':
        response = 4

    elif response == 'b3':
        response = 5

    elif response == 'c1':
        response = 6

    elif response == 'c2':
        response = 7

    elif response == 'c3':
        response = 8
    else:
        while response not in items:
            cprint("Every man has his faults - wrong input! Try again:", 'red')
            response = input()

    return response


def pieces():
    go_first = ask_yes_no("Do you want to start first? (y/n): ")
    if go_first == "y":
        print("\nSo the first move is yours. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour courage will lose you ... I will make the first move.")
        computer = X
        human = O
    return computer, human

def pieces1():
    go_first = ask_yes_no("X marker will be first, 0 will be second. Do you want to start with X? (y/n)")
    if go_first == "y":
        print("\nOk X so this is your turn!")
        human = X
        human1 = O
    else:
        print("\nOk, welcome player2 you will be X and it is your turn!")
        human = X
        human1 = O
    return human1, human


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    rowTop = colored('''\n\t\t  1   2   3''', 'yellow', attrs=['bold'])
    rowBottom1 = colored(f"\t\tA {board[0]} | {board[1]} | {board[2]}", 'yellow', attrs=['bold'])
    rowBottom2 = colored(f"\t\t  ---------", 'yellow', attrs=['bold'])
    rowBottom3 = colored(f"\t\tB {board[3]} | {board[4]} | {board[5]}", 'yellow', attrs=['bold'])
    rowBottom4 = colored("\t\t  ---------", 'yellow', attrs=['bold'])
    rowGround = colored(f"\t\tC {board[6]} | {board[7]} | {board[8]}\n", 'yellow', attrs=['bold'])

    print(rowTop)
    print(rowBottom1)
    print(rowBottom2)
    print(rowBottom3)
    print(rowBottom4)
    print(rowGround)

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number()
        if move not in legal:
            print("\nThis field is already taken, silly Human. Choose another\n")
    print("Better late than never.\n")
    return move

def human_move1(board, human, human1):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number()
        if move not in legal:
            print("\nThis field is already taken, silly Human. Choose another\n")
    print("Better late than never.")
    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            return move
        # take back move
        board[move] = EMPTY

    # block human win
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            return move
        # back move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            return move

def computer1_move(board, computer1, computer,):

    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    
    for move in legal_moves(board):
        board[move] = computer1
        if winner(board) == computer1:
            return move
        board[move] = EMPTY
    
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            return move


def next_turn(turn):

    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        cprint(f"{the_winner}, is the winner!\n", 'green', attrs=['bold'])
    else:
        print(tieText)

    if the_winner == computer:
        print("Ha! I won! , Proof that computers are superior to humans in every way.  \n" \
              "Do not cry for the moon. Time heals all wounds")

    elif the_winner == human:
        print("Oh no! How? It is impossible! Oh Now I see... \n" \
              "beware of a silent dog and still water!")

    elif the_winner == TIE:
        print("It is a TIE human!" \
              "Now I know to never judge a book by its cover." \
              )
    print_red('Press ENTER to continue.')
    input()
    
def congrat_winner1(the_winner, human, human1):
    if the_winner != TIE:
        print(the_winner, "is the winner!\n")
    else:
        print(tieText)

    if the_winner == human1:
        print("This is how it is, sometimes one wins and sometimes the other.")

    elif the_winner == human:
        print("This is how it is, sometimes one wins and sometimes the other.\n")

    elif the_winner == TIE:
        print("A friend in need is a friend indeed. ")
    print_red('Press ENTER to continue.')
    input()

def congrat_winnerAi(the_winner, computer, computer1):
    if the_winner != TIE:
        print(the_winner, "is the winner!\n")
    else:
        print(tieText)

    if the_winner == computer1:
        print("Even AI can be smarter than the other!")

    elif the_winner == computer:
        print("Even AI can be smarter than the other!")

    elif the_winner == TIE:
        print("Knowledge is power!")
    print_red('Press ENTER to continue.')
    input()

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

def pVp():
    display_instruct()
    human, human1 = pieces1()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = human_move1(board, human, human1)
            board[move] = human1
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner1(the_winner, human, human1)

def AiVsAi():
    os.system('cls')
    cprint('\tNow you see how the most intelligent IQ plays...', attrs=['bold'])
    cprint('\tGet ready...', attrs=['bold'])
    time.sleep(5)

    turn = X
    computer = O
    computer1 = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == computer1:
            move = computer1_move(board, computer1, computer)
            board[move] = computer1
        else:
            move = computer1_move(board, computer, computer1)
            board[move] = computer
        display_board(board)
        time.sleep(2)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winnerAi(the_winner, computer, computer1)

def simplyComputer_move(board, simplyComputer, human):
    board = board[:]
    simply_moves = []
    for i in range(0,8):
        count = random.randrange(8)
        simply_moves.append(count)
    for move in simply_moves:
        if move in legal_moves(board):
            return move


def scVp():
    display_instruct()
    simplyComputer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = simplyComputer_move(board, simplyComputer, human)
            board[move] = simplyComputer
        display_board(board)
        turn = next_turn(turn)
    computer = simplyComputer
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# main program
logo = colored("""
\t╔╦╗┬┌─┐╔╦╗┌─┐┌─┐╔╦╗┌─┐┌─┐
\t ║ ││   ║ ├─┤│   ║ │ │├┤ 
\t ╩ ┴└─┘ ╩ ┴ ┴└─┘ ╩ └─┘└─┘
""", 'green', attrs=['blink'])
while True:
    os.system('cls')
    print(logo)
    cprint("\tCreated by: Iga Dobek and Daniel Kupracz - Crazy Coders Software\n\tversion 1.0 May 2022", 'yellow', attrs=['bold'])
    print_red_on_cyan("""\tChoose an option:                                      """)
    print_red_on_cyan("""\t1. Player (or maybe prayer) vs Unbeatable Computer     """)
    print_red_on_cyan("""\t2. Player vs Player                                    """)
    print_red_on_cyan("""\t3. Computer vs Computer                                """)
    print_red_on_cyan("""\t4. Player vs (Un)Intelligent Computer                  """)
    print_red_on_cyan("""\tq. Quit game                                           """)
    menuChoise = input()
    if menuChoise == '1':
        main()
    elif menuChoise == '2':
        pVp()
    elif menuChoise == '3':
        AiVsAi()
    elif menuChoise == '4':
        scVp()
    elif menuChoise == 'q' or menuChoise == 'Q':
        cprint("\tAbsence makes the heart grow fonder. See ya!", 'yellow')
        break
    else:
        continue

print_red('\n\tTo confirm game over - press ENTER.')
input()
