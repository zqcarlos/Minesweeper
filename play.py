from board import Board
import argparse

def main(n, num_mines):
    # TODO: Write commandline game
    board = Board(n, num_mines)
    
    while True:
        board.show()
        row = int(input('Please enter the row number:'))
        col = int(input('Please enter the column number:'))
        res, err = board.drop(row, col)
        if err == None:
            if res == 'M':
                print('Boom!')
                break
            elif res == 'END':
                print('Congratulations! You win!')
                break
        else:
            print('Try Again!')


# DO NOT EDIT--------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', nargs='?', type=int, default=10)
    parser.add_argument('num_mines', nargs='?', type=int, default=10)
    return parser.parse_args() 

if __name__ == "__main__":
    args = parse_args()
    main(args.n, args.num_mines)

# DO NOT EDIT--------------------------------------------
