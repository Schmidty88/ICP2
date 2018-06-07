def horizontal():
    print(" --- " * board)

def vertical():
    print("|   " * (board + 1))

if __name__ == "__main__" :
    board = int(input("What size of game board? "))

    for index in range(board):
        horizontal()
        vertical()
    horizontal()