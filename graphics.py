import pygame
from material import *
from basic import *
from collections import namedtuple
import leaglizer
import time

selectedPieceDrawn = Material("Pawn",0, 0)
def switch_perspective():
    for material in white:
        material.x = 7 - material.x
        material.y = 7 - material.y

    for material in black:
        material.x = 7 - material.x
        material.y = 7 - material.y

white = [
    Material("Rook", 0, 7),
    Material("Knight", 1, 7),
    Material("Bishop", 2, 7),
    Material("Queen", 3, 7),
    Material("King", 4, 7),
    Material("Bishop", 5, 7),
    Material("Knight", 6, 7),
    Material("Rook", 7, 7),

    Material("Pawn", 7, 6),
    Material("Pawn", 6, 6),
    Material("Pawn", 5, 6),
    Material("Pawn", 4, 6),
    Material("Pawn", 3, 6),
    Material("Pawn", 2, 6),
    Material("Pawn", 1, 6),
    Material("Pawn", 0, 6),
]

black = [
    Material("Rook", 0, 0),
    Material("Knight", 1, 0),
    Material("Bishop", 2, 0),
    Material("Queen", 3, 0),
    Material("King", 4, 0),
    Material("Bishop", 5, 0),
    Material("Knight", 6, 0),
    Material("Rook", 7, 0),

    Material("Pawn", 7, 1),
    Material("Pawn", 6, 1),
    Material("Pawn", 5, 1),
    Material("Pawn", 4, 1),
    Material("Pawn", 3, 1),
    Material("Pawn", 2, 1),
    Material("Pawn", 1, 1),
    Material("Pawn", 0, 1),
]


whiteTurn = True


selectedPiece = -1
pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess.com 2.0 ~ Joanthan peri")

grid_size = 8
square_size = screen_width // grid_size

light_color = (240, 217, 181)
dark_color = (181, 136, 99)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (whiteTurn):
                    for Material in white:
                        if (Material.x == col and Material.y == row):
                            #print(Material.type)
                            selectedPiece = white.index(Material)
                else:
                    for Material in black:
                        if (Material.x == col and Material.y == row):
                            #print(Material.type)
                            selectedPiece = black.index(Material)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if (whiteTurn):
                    if (selectedPiece >= 0 and leaglizer.GlobalGal(black,white,white[selectedPiece],white[selectedPiece].x, white[selectedPiece].y, col,row, True)):
                        white[selectedPiece].x = col
                        white[selectedPiece].y = row
                        selectedPiece = -1
                        whiteTurn = not whiteTurn
                        #evaluate(white, black)
                        #switch_perspective()
                    else:
                        selectedPiece = -1
                else:
                    if (selectedPiece >= 0 and leaglizer.GlobalGal(white,black,black[selectedPiece],black[selectedPiece].x, black[selectedPiece].y, col,row, False)):
                        black[selectedPiece].x = col
                        black[selectedPiece].y = row
                        selectedPiece = -1
                        whiteTurn = not whiteTurn
                        #evaluate(white, black)
                        #switch_perspective()
                    else:
                        selectedPiece = -1

            
    mouse_x, mouse_y = pygame.mouse.get_pos()
    row = mouse_y // square_size
    col = mouse_x // square_size
    

       
    screen.fill((255, 255, 255))

    

    for y in range(grid_size):
        for x in range(grid_size):
            rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, light_color, rect)
            else:
                pygame.draw.rect(screen, dark_color, rect)

    #font = pygame.font.Font(None, 36)
    #text = font.render(f"({row}, {col})", True, (0, 0, 0))
    #screen.blit(text, (10, 10))
    for Material in white:
        if (white.index(Material) != selectedPiece or not whiteTurn):
            draw_material(screen, True, Material, square_size)
    for Material in black:
        if (black.index(Material) != selectedPiece or whiteTurn):
            draw_material(screen, False, Material, square_size)

    if (selectedPiece >= 0):

        if (whiteTurn):
            selectedPieceDrawn.type = white[selectedPiece].type
            draw_material(screen, True, selectedPieceDrawn, 1)
        else:
            selectedPieceDrawn.type = black[selectedPiece].type
            draw_material(screen, False, selectedPieceDrawn, 1)

        selectedPieceDrawn.x = mouse_x - piece_size / 2
        selectedPieceDrawn.y = mouse_y - piece_size / 2
    #evaluate(white, black)
    pygame.display.flip()

pygame.quit()
