#tic-tac-toe v1.5

import random
import sys

game_dict = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
availableTiles = [1,2,3,4,5,6,7,8,9]
winning_points = [{2, 5, 8}, {1, 5, 9}, {3, 5, 7}, {4, 5, 6}]
player1_tiles = set()
player2_tiles = set()
ai_tiles = set()

def randomPlayerSelect():
    player = random.choice([1,2])
    return player

def selectTile(player):
    if player == 'ai':
        tile = random.choice(availableTiles);
        ai_tiles.add(tile)
        availableTiles.remove(tile)
        game_dict[tile]=player
        print(ai_tiles)
        determine_winner()
        return True
    else:
        tile = input("Choose a tile form the available tiles")
        if int(tile) in availableTiles:
            availableTiles.remove(int(tile))
            print(availableTiles)
            game_dict[int(tile)]= player

            if player == 1:
                player1_tiles.add(int(tile))
                print (player1_tiles)
                determine_winner()
            else:
                player2_tiles.add(int(tile))
                print (player2_tiles)
                determine_winner()
                return True
        else:
            return False

def printCurrentGameBoard():
    i = 1
    while i <=9:
        print (f"----- {game_dict[i]} -----", end = '',)
        if i%3 == 0:
            print ('\n\n\n')
        i+=1

def play_game(player):
    play = selectTile(player)
    if play:
        return True
    else:
        return False

def determine_winner():
    for i in winning_points:
        if i == player1_tiles:
            print ("Player 1 wins")
            sys.exit()
        elif i == player2_tiles:
            print("Player 2 wins")
            sys.exit()

def play_with_human():
    print ("Welcome to Tic Tac Toe")
    player1 = randomPlayerSelect()
    player2 = player1 - 1
    if player2 == 1:
        player2 = 1
    else:
        player2 = 2
    while len(availableTiles)>1:
        printCurrentGameBoard()
        print (f"Player {player1}, its your turn")
        game = play_game(player1);
        
        
        if game:
            printCurrentGameBoard()
            print (f"Player {player2}, its your trun")
            game = play_game(player2);
    else:
        print ("Out of moves")

def play_with_ai():
    print ("Welcome to Tic Tac Toe")
    player1 = 'ai'
    player2 = 'human'
    while len(availableTiles) > 1:
        printCurrentGameBoard()
        print (f"Player {player1}, it's your turn")
        game = play_game(player1);
        if game:
            printCurrentGameBoard()
            print (f"Player {player2}, its your trun")
            game = play_game(player2);
    else:
        print ("Out of Moves")

def main():
    response = input("Do you want to play with Computer (c) or Human (h)? Pls select");
    if response == 'c':
        play_with_ai()
    elif response == 'h':
        play_with_human()
    else:
        sys.exit("Invalid Response")

#randomPlayerSelect()
main()
