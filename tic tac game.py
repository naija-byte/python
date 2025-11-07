import random

board = [' '] * 9

print('--------------------------------------------------------')
print()
print(board[0] + ' | ' + board[1] + ' | ' + board[2])
print('---------------------------------------------------------')
print(board[3] + ' | ' + board[4] + ' | ' + board[5])
print('--------------------------------------------------------')
print(board[6] + ' | ' + board[7] + ' | ' + board[8])
print('-------------------------------------------------------')
print()


win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]              
]


current_player = 'X'  
while True:
    if current_player == 'X':
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = 'X'
            
            print(board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('--+---+--')
            print(board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('--+---+--')
            print(board[6] + ' | ' + board[7] + ' | ' + board[8])
            
            for condition in win_conditions:
                if board[condition[0]] == board[condition[1]] == board[condition[2]] == 'X':
                    print("Congratulations! You win!")
                    exit()
            current_player = 'O'
        else:
            print("Invalid move. Try again.")
    else:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
       
            print(board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('--+---+--')
            print(board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('--+---+--')
            print(board[6] + ' | ' + board[7] + ' | ' + board[8])
          
            for condition in win_conditions:
                if board[condition[0]] == board[condition[1]] == board[condition[2]] == 'O':
                    print("Computer wins!")
                    exit()
            current_player = 'X'

    if ' ' not in board:
        print("It's a draw!")
        break
