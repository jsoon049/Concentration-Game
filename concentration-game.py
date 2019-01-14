#Family name: Jeremy Soong
#Student number: 300016044
# Course: IT1 1120 
# Assignment Number 3

import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    print("Shuffling the deck...\n")
    random.shuffle(deck)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    discovered[p1-1]=original_board[p1-1]
    discovered[p2-1]=original_board[p2-1]
    print_board(discovered)
        
    

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str
    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    for item in l[:]:
        if item=='*':
            l.remove(item)
        elif l.count(item)==1:
            l.remove(item)
        elif l.count(item)%2!=0:
            l.remove(item)
    playable_board=l
    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.
    Precondition: Every element in the list appears even number of times
    '''

    if len(l)==0:
        return True
    elif len(l)>0:
        for item in l:
            if l.count(item)/2!=1:
                return False
        return True
        

####################################################################

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    guess=0
    optimal=len(board)/2
    a=[]
    for i in range(len(board)):
        a.append('*')
    while a.count('*')>0:
        print("\n"*40)
        print_board(a)
        print('\n')
        print("\nEnter two distinct positions on the board that you want revealed.")
        print("i.e two integers in the range [1, "+str(len(board))+"]")
        p1=int(input("Enter position 1: "))
        p2=int(input("Enter position 2: "))
        while (p1==p2) or (p1<=0) or (p1>52) or (p2<=0) or (p2>52) or ((a[p1-1]!='*' or a[p2-1]!='*') and p1==p2) or (a[p1-1]!='*' or a[p2-1]!='*'):
            if  (p1<=0) or (p1>52) or (p2<=0) or (p2>52):
                print("One or both of your chosen positions is out of range")
                print("Please try again. This guess did not count. Your current number of guesses is "+str(guess)+"\n")
                p1=int(input("Enter position 1: "))
                p2=int(input("Enter position 2: "))
            elif (a[p1-1]!='*' or a[p2-1]!='*') and p1==p2:
                print("One or both of your chosen positions has already been paired.\nYou chose the same positions.")
                print("Please try again. This guess did not count. Your current number of guesses is "+str(guess)+"\n")
                p1=int(input("Enter position 1: "))
                p2=int(input("Enter position 2: "))
            elif p1==p2:
                print("You chose the same positions.")
                print("Please try again. This guess did not count. Your current number of guesses is "+str(guess)+"\n")
                p1=int(input("Enter position 1: "))
                p2=int(input("Enter position 2: "))
            elif a[p1-1]!='*' or a[p2-1]!='*':
                print("One or both of your chosen positions has already been paired.")
                print("Please try again. This guess did not count. Your current number of guesses is "+str(guess)+"\n")
                p1=int(input("Enter position 1: "))
                p2=int(input("Enter position 2: "))
        print_revealed(a, p1, p2, board)
        guess=guess+1
        print('\n')
        if board[p1-1]!=board[p2-1]:
            a[p1-1]='*'
            a[p2-1]='*'
        wait_for_player()
        print("\n"*40)
    diff=int(guess-optimal)
    print("Congratulations! You completed the game with "+str(guess)+" guesses. That is "+str(diff)+" more than the best possible.")
    


####################################################################
#Additional Helper Function

def name_plaque(name):
    ''' (str)->None
    Draws/Prints name plaque'''
    print()
    print(5*"*"+len(name)*"*"+5*"*")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print("*  "+2*"_"+name+2*"_"+"  *")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print(5*"*"+len(name)*"*"+5*"*")
    print()

    
#main
    
# CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
name_plaque("Welcome to my Concentration game")
print("Would you like (enter 1 or 2 to indicate your choice):")
print("(1) me to generate a rigorous deck of cards for you")
print("(2) or, would you like me to read a deck from a file?")
answer=str(input())
while answer.strip()!="1" and answer.strip()!="2":
    print(str(answer)+" is not an existing option. Please try again. Enter 1 or 2 to indicate your choice")
    answer=str(input())
    
# CODE FOR OPTION 1 GOES HERE
if answer.strip()=="1":
    print("You have chose to have a rigorous deck generated for you\n")
    print("How many cards do you want to play with?")
    size=int(input("Enter an even number between 0 and 52: "))
    while size%2!=0 or (size<=0 or size>52):
        print("\nHow many cards do you want to play with?")
        size=int(input("Enter an even number between 0 and 52: "))
    board=create_board(size)
    shuffle_deck(board)
    wait_for_player()
    print("\n"*40)
    play_game(board)
    

# CODE FOR OPTION 2 GOES HERE
if answer.strip()=='2':
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    is_rigorous(board)
    if is_rigorous(board)==False:
        name_plaque("This deck is now playable but not rigorous and it has "+str(len(board))+" cards.")
    else:
        name_plaque("This deck is now playable and rigorous and it has "+str(len(board))+" cards.")
    wait_for_player()
    if len(board)==0:
        print("\n"*40)
        print("The resulting board is empty.\nPlaying Concentration Game with an empty board is impossible.\nGood bye")
    else:
        print("\n"*40)
        shuffle_deck(board)
        wait_for_player()
        print("\n"*40)
        play_game(board)
    


    

