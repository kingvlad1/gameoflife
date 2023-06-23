#я би один словом сказав що код гівно але ладно
#фігня якась )

def game_of_life(board):
    """
    Given a board representing the current state of the Game of Life, return a board representing the next state.
    """
    def count_live_neighbors(board, i, j):
        """
        Count the number of live cells in the 8 neighboring cells.
        """
        count = 0
        for x in range(max(0, i-1), min(len(board), i+2)):
            for y in range(max(0, j-1), min(len(board[0]), j+2)):
                if x == i and y == j:
                    continue
                count += board[x][y]
        return count

    next_board = []
    for i in range(len(board)):
        next_board.append([0] * len(board[0]))
        for j in range(len(board[0])):
            live_neighbors = count_live_neighbors(board, i, j)
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_board[i][j] = 0
                else:
                    next_board[i][j] = 1
            else:
                if live_neighbors == 3:
                    next_board[i][j] = 1
    return next_board

def display_board(board):
    """
    Display the board on the console.
    """
    for row in board:
        print(' '.join(['#' if cell else '-' for cell in row]))

def main():
    """
    The main program that runs the simulation.
    """
    board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    while True:
        display_board(board)
        board = game_of_life(board)
        input("Press Enter to continue...")

if __name__ == '__main__'::
    main()

#end code
#кінець коду
