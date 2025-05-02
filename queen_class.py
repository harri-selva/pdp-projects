from pieces_class import Pieces
import pygame




class Queen(Pieces):    
    def __init__(self):
        self.image = (pygame.image.load("queen.png")).convert_alpha()
        self.radius = 13
        self.piece_points = -25
        self.colour = "red"
        self.pocketed = False  
        
    # "Queen" class inherits from pieces class 