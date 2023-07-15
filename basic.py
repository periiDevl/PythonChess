import pygame

def load_and_scale_texture(image_path, scale):
    texture_image = pygame.image.load(image_path)
    scaled_texture = pygame.transform.scale(texture_image, scale)
    return scaled_texture

piece_size = 60
w_pawn_tex = load_and_scale_texture("Assets/w_pawn.png", (piece_size, piece_size))
b_pawn_tex = load_and_scale_texture("Assets/b_pawn.png", (piece_size, piece_size))

w_bishop_tex = load_and_scale_texture("Assets/w_bishop.png", (piece_size, piece_size))
b_bishop_tex = load_and_scale_texture("Assets/b_bishop.png", (piece_size, piece_size))

w_knight_tex = load_and_scale_texture("Assets/w_knight.png", (piece_size, piece_size))
b_knight_tex = load_and_scale_texture("Assets/b_knight.png", (piece_size, piece_size))

w_rook_tex = load_and_scale_texture("Assets/w_rook.png", (piece_size, piece_size))
b_rook_tex = load_and_scale_texture("Assets/b_rook.png", (piece_size, piece_size))

w_queen_tex = load_and_scale_texture("Assets/w_queen.png", (piece_size, piece_size))
b_queen_tex = load_and_scale_texture("Assets/b_queen.png", (piece_size, piece_size))

w_king_tex = load_and_scale_texture("Assets/w_king.png", (piece_size, piece_size))
b_king_tex = load_and_scale_texture("Assets/b_king.png", (piece_size, piece_size))

def draw_material(screen,white, Material, square_size):
        if (Material.type == "Pawn"):
            if (white):
                screen.blit(w_pawn_tex, (Material.x * square_size, Material.y * square_size))
            else :
                 screen.blit(b_pawn_tex, (Material.x * square_size, Material.y * square_size))
        elif (Material.type == "Knight"):
            if (white):
                screen.blit(w_knight_tex, (Material.x * square_size, Material.y * square_size))
            else :
                 screen.blit(b_knight_tex, (Material.x * square_size, Material.y * square_size))
        elif (Material.type == "Bishop"):
            if (white):
                screen.blit(w_bishop_tex, (Material.x * square_size, Material.y * square_size))
            else :
                 screen.blit(b_bishop_tex, (Material.x * square_size, Material.y * square_size))
        elif (Material.type == "Rook"):
            if (white):
                screen.blit(w_rook_tex, (Material.x * square_size, Material.y * square_size))
            else :
                 screen.blit(b_rook_tex, (Material.x * square_size, Material.y * square_size))
        elif (Material.type == "Queen"):
            if (white):
                screen.blit(w_queen_tex, (Material.x * square_size, Material.y * square_size))
            else :
                 screen.blit(b_queen_tex, (Material.x * square_size, Material.y * square_size))
        elif (Material.type == "King"):
            if (white):
                screen.blit(w_king_tex, (Material.x * square_size, Material.y * square_size))
            else :
                 screen.blit(b_king_tex, (Material.x * square_size, Material.y * square_size))
