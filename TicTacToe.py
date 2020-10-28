from colorama import Fore, Style
import os

def display_board(board):
    '''
    Prints the board by taking in the board in the form of a list.
    '''
    os.system("clear")

    print (Style.BRIGHT)
    print (f"\t\t{Fore.LIGHTRED_EX}TicTacToe By Avius")
    print (Fore.BLUE)
    print ("\t"+ str(board[1]) + "\t|\t" + str(board[2]) + "\t|\t" + str(board[3]))
    print ("\t\t|\t\t|")
    print ("-------------------------------------------------")
    print ("\t"+ str(board[4]) + "\t|\t" + str(board[5]) + "\t|\t" + str(board[6])) 
    print ("\t\t|\t\t|")
    print ("-------------------------------------------------")
    print ("\t"+ str(board[7]) + "\t|\t" + str(board[8]) + "\t|\t" + str(board[9]))  
    print ("\t\t|\t\t|")
    print (Fore.GREEN)
    if win_check(board, 'O'):
        print("Congratulations! Player 1 wins!")

    elif win_check (board, 'X'):
        print("Congratulations! Player 2 wins!")

    if draw_check(board):
        print("GG. It's a draw.")

    print (Style.RESET_ALL)
    return None

def win_check(board, mark):
    '''	
    Checks if a specific marker has won by taking in the board and the marker to check.
    '''
    #For horizontal strikes-
    if board[1:4] == [mark, mark, mark] or board[4:7] == [mark, mark, mark] or board[7:] == [mark, mark, mark]:
        board = ['#',1, 2, 3, 4, 5, 6, 7, 8, 9]
        return True
    #For vertical strikes-
    elif board[1:8:3] == [mark, mark, mark] or board[2:9:3] == [mark, mark, mark] or board[3::3] == [mark, mark, mark]:
        return True
#For diagonal strikes-
    elif board[1::4] == [mark, mark, mark] or board[3:8:2] == [mark, mark, mark]:
        return True

    return False

def draw_check(board):
    '''
    Returns true if match is a draw. (If board is full and nobody has won, return True.)
    '''
    if full_check(board) and not win_check(board,'O') and not win_check(board,'X'):
        return True
    return False

def insert_marker(board, marker, position):
    '''
    Inserts marker (X or O) at entered position and returns new board.
    '''
    board[position] = marker
    return board

def full_check(board):
    '''
    Checks if the board is full or not.
    '''
    full = True
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for element in board: #If none of the elements are a number (all are X or O), list is full
        if element in num_list:
            return False

    return full

def success_check(board):
    '''
    Checks if a player has won yet or not.
    '''
    return win_check(board, 'O') or win_check(board, 'X')

def check_position_validity(board, position):
    '''
    Returns false if entered position is not in range 1-9 or is already filled.
    '''
    if not 1 <= position <= 9:
        return False
    if board[position] in ['X', 'O']:
        return False
    return True

def input_loop(board):
    '''
    Takes input in a loop until either the board is full or a player has won the game.
    '''
    successful = False
    full = False
    position = 0
    alternate_counter = 1 #If this is even, insert X, else insert O (O will be the first to be inserted)
    while (not successful and not full):

        #To check whether the entered position was an integer or not.
        while True:
            try:
                position = int(input("Please enter your position: "))
            except ValueError:
                print("That is not a valid position. Please try again.")
                continue
            except KeyboardInterrupt:
                print(Style.NORMAL)
                print(Fore.BLUE)
                print("\nThank you for playing!")
                print(Style.RESET_ALL)
                quit()
            else:
                break

        #If a position is already filled, ask for input again-

        while True:
            try:
                while(not check_position_validity(board, position)):
                    position = int(input("Invalid position. Please try again: "))
                print(Style.RESET_ALL)

                if alternate_counter % 2 == 0:
                    board = insert_marker(board, 'X', position)
                else:
                    board = insert_marker(board, 'O', position)
                alternate_counter += 1

                os.system("clear")
                full = full_check(board)
                successful = success_check(board)

                display_board(board)
            except ValueError:
                print("That is not a valid position. Please try again.")
                continue
            except KeyboardInterrupt:
                print(Style.NORMAL)
                print(Fore.BLUE)
                print("\nThank you for playing!")
                print(Style.RESET_ALL)
                quit()
            else:
                break


def game():
    '''
    Main function for TicTacToe that calls all the other functions to run the game.
    '''
    board = ['#',1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_board(board) #To display the board initially to show all positions to the user.
    input_loop(board) #Takes input until either the board is full or a player has won the game.

if __name__ == '__main__':
    game()
