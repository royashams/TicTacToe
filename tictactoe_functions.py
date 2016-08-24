import math
EMPTY = '-'


def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    
    return min_value <= value <= max_value

   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.

def game_board_full(game_board):
    """ (str) -> bool
    
    Return true if and only if there are no empty characters in the game board.
    
    >>> game_board_full('xoxooxxox')
    True
    >>> game_board_full('xo-xoxo-x')
    False
    """
    
    if EMPTY in game_board[:]:
        return False
    else: 
        return True
    
def get_board_size(game_board):
    """ (str) -> int
    
    Precondition: number of characters in the game_board string of game_board
    must be a perfect square.
    
    Return an integer of each side of the given tic-tac-toe game board.
    
    >>> get_board_size('xoxoxoxox')
    3
    >>> get_board_size('xo-x')
    2
    """

    return int(math.sqrt(len(game_board)))

def make_empty_board(get_board_size):
    """(int) -> str
    
    Return all of the cells on game_board to EMPTY characters.
    
    >>>make_empty_board(3)
    '---------'
    >>>make_empty_board(4)
    '----------------'
    """
    
    return ('-' * ((get_board_size)**2))

def get_position(row_index, col_index, get_board_size):
    
    """(int, int, int) -> int
    
    Precondition: row_index, col_index <= get_board_size
    
    Return the str_index of the corresponding string representation of the
    board given row, column, and game board size indices.
    
    >>>get_position(3, 2, 4)
    9
    >>>get_position(2, 2, 3)
    4
    """
    
    return (row_index - 1) * get_board_size + col_index - 1  

def make_move( char, row_index, col_index, game_board):
    """( str, int, int, str) -> str
    
    Return the tic-tac-toe board that results when the given char is placed
    at the given cell position.
    
    >>>make_move('o', 2, 2, 'xox-')
    'xoxo'
    >>>make_move('x', 2, 1, 'xoo-xox-x')
    'xooxxox-x'
    """
    
    select = get_position(row_index, col_index, get_board_size(game_board))
    #this gives the position when all of the parameters are written. It is a bit
    #lengthy to write several times so it is compiled into "select" 
    #as a variable.
    new_board = game_board[:select] + char + game_board[select + 1:]
    #this puts in the char in between the position (select) and one space after
    #the position (select + 1)
    return new_board

def extract_line(game_board, direction, rowcol):
    """(str, str, int) -> str
    
    Precondition: rowcol<= get_board_size(game_board)
    Second parameter must always be either 'across', 'down', 'down_diagonal', 
    or 'up_diagonal'
    
    Return the characters that make up the specified row 
    (when the second parameter is 'across'),
    column (when the second parameter is 'down'), or diagonal from the
    given tic-tac-toe game board.
    
    >>> extract_line('xoox', 'down', 2)
    ox
    >>> extract_line('xoo-xox-x', 'up_diagonal', 3)
    xxx
    """
    
    GBS = get_board_size(game_board)
    
    if direction == 'across':
        return game_board[(rowcol-1) *( GBS):(rowcol) * (GBS)]
    if direction == 'down':
        return game_board[rowcol-1::get_board_size(game_board)] 
    if direction == 'down_diagonal':
        return game_board[::(GBS + 1)]
    if direction == 'up_diagonal':
        return game_board[(GBS**2) - (GBS):0:(-(GBS - 1))]
    else: 
        return 'error! try again.'
        
    
