from material import *

#Check out my sorting-algo repo! : https://github.com/periiDevl/Sorting_Algorithms_PERII/blob/main/sorting/sort.py
def selection_sort_matrial(array):
    arr_copy = array.copy()
    size = len(arr_copy)
    for s in range(size):
        min_idx = s
         
        for i in range(s + 1, size):
             
            if arr_copy[i].x < arr_copy[min_idx].x:
                min_idx = i
        (arr_copy[s].x, arr_copy[min_idx].x) = (arr_copy[min_idx].x, arr_copy[s].x)
    return arr_copy

def PawnGal(original_row, original_col, row, col, is_white):
    # Detecting pawn moves
    if is_white:
        if original_col == 6 and original_col - col == 2 and original_row == row:
            # Regular move: two squares forward for white pawn from the initial position
            return True
        if original_col - col == 1 and original_row == row:
            # Regular move: one square forward for white pawn
            return True
        return False
    else:
        if original_col == 1 and original_col - col == -2 and original_row == row:
            # Regular move: two squares forward for black pawn from the initial position
            return True
        if original_col - col == -1 and original_row == row:
            # Regular move: one square forward for black pawn
            return True
        return False


def KingGal(original_row, original_col, row, col):
    # King can move one step in any direction
    if abs(original_row - row) <= 1 and abs(original_col - col) <= 1 and (original_row != row or original_col != col):
        return True
    else:
        return False
def QueenGal(original_row, original_col, row, col):
    # Queen can move horizontally, vertically, or diagonally
    if original_row == row or original_col == col or abs(original_row - row) == abs(original_col - col):
        return True
    else:
        return False

def RookGal(original_row, original_col, row, col):
    # Rook can move horizontally or vertically
    if original_row == row or original_col == col:
        return True
    else:
        return False
def KnightGal(original_row, original_col, row, col):
    # Knight can move in an L-shaped pattern
    if (abs(original_row - row) == 2 and abs(original_col - col) == 1) or (abs(original_row - row) == 1 and abs(original_col - col) == 2):
        return True
    else:
        return False
def BishopGal(original_row, original_col, row, col):
    # Bishop can move diagonally
    if abs(original_row - row) == abs(original_col - col):
        return True
    else:
        return False
   
def is_in_front_of_black(original_row, original_col, row, col, black):
    for piece in black:
        if piece.x < original_row and piece.x > row and piece.y == col and piece.y == original_col:
            return False
        
        if piece.x > original_row and piece.x < row and piece.y == col and piece.y == original_col:
            return False
        
        if piece.y < original_col and piece.y > col and piece.x == row and piece.x == original_row:
            return False
        
        if piece.y > original_col and piece.y < col and piece.x == row and piece.x == original_row:
            return False
        
        if piece.x < original_row and piece.x > row and piece.y < original_col and piece.y > col and abs(piece.x - original_row) == abs(piece.y - original_col):
            return False
        
        if piece.x > original_row and piece.x < row and piece.y < original_col and piece.y > col and abs(piece.x - original_row) == abs(piece.y - original_col):
            return False
        
        if piece.x < original_row and piece.x > row and piece.y > original_col and piece.y < col and abs(piece.x - original_row) == abs(piece.y - original_col):
            return False
        
        if piece.x > original_row and piece.x < row and piece.y > original_col and piece.y < col and abs(piece.x - original_row) == abs(piece.y - original_col):
            return False
    
    return True



def GlobalGal(black, white, Material, original_row, original_col, row, col, is_white):
    for i in range(len(white)):
        if white[i].x == row and white[i].y == col:
            return False

    if not is_in_front_of_black(original_row, original_col, row, col, black):
        return False

    if not is_in_front_of_black(original_row, original_col, row, col, white):
        return False
    

    
    if Material.type != "Pawn":
        for i in range(len(black)):
            if black[i].x == row and black[i].y == col:

                black.pop(i)
                return True
            
    else:
        for p in black:
            if (is_white):
                if (p.y == original_col - 1 and p.x == original_row - 1 or p.x == original_row + 1):
                    if p.x == row and p.y == col:
                        black.pop(black.index(p))
                        return True
                if p.x == row and p.y == col:
                    return False
            else:
                if (p.y == original_col + 1 and p.x == original_row - 1 or p.x == original_row + 1):
                    if p.x == row and p.y == col:
                        black.pop(black.index(p))
                        return True
                if p.x == row and p.y == col:
                    return False


    if Material.type == "King":
        return KingGal(original_row, original_col, row, col)
    if Material.type == "Queen":
        return QueenGal(original_row, original_col, row, col)
    if Material.type == "Bishop":
        return BishopGal(original_row, original_col, row, col)
    if Material.type == "Knight":
        return KnightGal(original_row, original_col, row, col)
    if Material.type == "Rook":
        return RookGal(original_row, original_col, row, col)
    if Material.type == "Pawn":
        return PawnGal(original_row, original_col, row, col, is_white)
