"""
3.7.2 Two-dimensional arrays
Let's also assume that a predefined symbol named EMPTY designates an empty field on the chessboard.

So, if we want to create a list of lists representing the whole chessboard, it may be done in the following way:


board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
 
Note:

the inner part of the loop creates a row consisting of eight elements (each of them equal to EMPTY) and appends it to the board list;
the outer part repeats it eight times;
in total, the board list consists of 64 elements (all equal to EMPTY)
This model perfectly mimics the real chessboard, which is in fact an eight-element list of elements, all being single rows. Let's summarize our observations:

the elements of the rows are fields, eight of them per row;
the elements of the chessboard are rows, eight of them per chessboard.
The board variable is now a two-dimensional array. It's also called, by analogy to algebraic terms, a matrix.

As list comprehensions can be nested, we can shorten the board creation in the following way:


board = [[EMPTY for i in range(8)] for j in range(8)]
 
The inner part creates a row, and the outer part builds a list of rows.

Access to the selected field of the board requires two indices ‒ the first selects the row; the second ‒ the field number inside the row, which is de facto a column number.

Take a look at the chessboard. Every field contains a pair of indices which should be given to access the field's contents:



Glancing at the figure shown above, let's set some chess pieces on the board. First, let's add all the rooks:


board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
 
If you want to add a knight to C4, you do it as follows:


board[4][2] = KNIGHT
 
And now a pawn to E5:


board[3][4] = PAWN
"""