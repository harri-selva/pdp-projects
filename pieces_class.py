
from constants import *
import math
import pymunk


class Pieces:
    def __init__(self, piece_points, radius, colour):
        self.piece_points = piece_points
        self.radius = radius
        self.colour = colour
        self.pocketed = False
        # attributes

    def create_piece(self, location, my_space):
        self.body = pymunk.Body()
        self.body.position = location
        self.shape = pymunk.Circle(self.body,
                                   self.radius)

        # defing both the body and shape is necessary for the creation of the piece

        self.pivot = pymunk.PivotJoint(my_space.static_body,
                                       self.body,
                                       (0, 0),
                                       (0, 0))

        self.shape.elasticity = 0.8
        # defining the modulus of elasticity of the carrom pieces
        # fundamentally determinng the speeds of the pieces after they collide
        self.shape.mass = 12
        self.pivot.max_force = 50
        self.pivot.max_bias = 0

        # adding all the components to the physics space
        my_space.add(self.shape,
                     self.body,
                     self.pivot)

        return self.shape

    def return_to_original_position(self):
        self.body.position = (580, 420)

    def clear(self, my_space, pieces):
        my_space.remove(self.body,
                        self.pivot,
                        self.shape)
        self.pocketed = True
        pieces.remove(self)

    def is_moving(pieces):
        moving = 0
        for piece in pieces:
            if (piece.body.velocity[0]) != 0.0 and (piece.body.velocity[1]) != 0.0:
                # both the x component and the y component of the velocity must be checked to ensure that each piece has come to a stop
                moving += 1

        if moving > 0:
            return True
        # if at least one is moving the subroutine is exited and is called again later on
        else:
            return False

        # checking the pieces' veolcities and if at least one is moving the subroutine is exited and is called again later on
        # if all the pieces are stationary the Boolean value false is returned

        # this method runs mutltiple times after the striker leaves the baseline because
        # the program needs to continously check if the pieces have come to a halt for it to intitiate other processes

    def check_pocketed(pieces, pocket_centres, player, striking, queue, my_space, striker_object):
        if striking == False:
            for piece in pieces:  # loop through each piece present on the board
                for pocket in pocket_centres:
                    piece_y_dist = abs(piece.body.position[1] - pocket[1])
                    piece_x_dist = abs(piece.body.position[0] - pocket[0])
                    squared_dist = (piece_x_dist ** 2) + (piece_y_dist ** 2)
                    piece_dist = math.sqrt(squared_dist)
                    # the pythagoras theorem is used to calculate the distance between the centres of the pockets and the position of the pieces
                    # this is looped through all of the pockets and pieces
                    if piece_dist <= pocket_radius:
                        # if the distance calculated is less than the pocket radius the intersection between the piece and pocket is adequate
                        # for the piece to fall into the pocket
                        if piece.colour == "yellow":  # identify if the stirker has been pocketed
                            player.due += 5  # if so add 5 to the player's due tally
                            player.pocketed_striker = True  # switching this attribute to true
                            striker_object.pocketed = True

                        try:
                            my_space.remove(piece.body,
                                            piece.pivot,
                                            piece.shape)
                        except:
                            print("piece has already been removed from the space")
                        # when the piece falls into the pocket the body and shape related must be removed from the physics space
                        # a try and except clause used in the case that the piece may already be removed from the space
                        # and continue with the game
                        piece.pocketed = True
                        pieces.remove(piece)

                        # append the piece to the pocketed_pieces list attribute for that specific player
                        player.pocketed_pieces.append(piece)
                        player.point_calcuation(queue, player)
                        # after a piece is pocketed the points calculation is performed

    def display_image(self, display):
        if self.pocketed == False:
            display.blit(self.image,
                         ((self.body.position[0]-self.radius),
                          (self.body.position[1]-self.radius))
                         )  # the pieces are all displayed on the scren using this method
