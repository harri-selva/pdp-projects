from pieces_class import Pieces
import pygame


class Black_Carrom_men(Pieces):  # inherits from pieces class
    def __init__(self):
        self.image = (pygame.image.load(
            "black carrom piece.png")).convert_alpha()
        self.radius = 13
        self.piece_points = 5
        self.colour = "black"
        self.pocketed = False

        # attributes of a black carrom piece

    def generate_new(black_carrom_men, pieces, my_space):
        new_black_carrom_men1 = Black_Carrom_men()
        new_black_carrom_men1.create_piece([580, 420], my_space)
        new_black_carrom_men1.pocketed = False  # set to not pocketed yet
        # add to black carrom men list
        black_carrom_men.append(new_black_carrom_men1)
        pieces.append(new_black_carrom_men1)  # add to pieces list
