from pieces_class import Pieces
import pygame


class White_Carrom_men(Pieces):
    def __init__(self):
        self.image = (pygame.image.load(
            "white carrom piece.png")).convert_alpha()
        self.radius = 13
        self.piece_points = 10
        self.colour = "white"
        self.pocketed = False

        # the white_carrom_men class inherits from the pieces class

    def generate_new(white_carrom_men, pieces, my_space):
        new_white_carrom_men1 = White_Carrom_men()
        new_white_carrom_men1.create_piece(
            [580, 420], my_space)  # added to the physics space
        new_white_carrom_men1.pocketed = False  # set to not pocketed yet
        white_carrom_men.append(new_white_carrom_men1)
        pieces.append(new_white_carrom_men1)

        # creates a new white piece and adds it to the list white carrom men so it is able to diplsayed on the screen
        # it is also added to the pieces list
