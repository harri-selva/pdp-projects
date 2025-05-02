from constants import *
import pygame
import pymunk
import pymunk.pygame_util
import math
import pymunk.matplotlib_util


class Board:
    def __init__(self, surface, space):
        self.surface = surface
        self.pocket_centres = pocket_centres
        self.space = space

    def display_board(self):
        # I used relative co-ordinates and dimensions to the outer board so outer_board can be altered while the inner designs will be attached with it
        pygame.draw.rect(self.surface,
                         Black,
                         [outer_board_x, outer_board_y,
                             outer_board_dimension, outer_board_dimension],
                         outer_board_thickness)  # defining the region and colour for the outer board
        pygame.draw.rect(self.surface,
                         Peach,
                         [(outer_board_x + outer_board_thickness), (outer_board_y + outer_board_thickness), (inner_dimension), (inner_dimension)])  # defining the region and colour for the inner board

        pygame.draw.circle(self.surface,
                           Pocket_colour,
                           ((outer_board_x + outer_board_thickness + pocket_radius),
                            (outer_board_y + outer_board_thickness + pocket_radius)),
                           pocket_radius)
        pygame.draw.circle(self.surface,
                           Pocket_colour,
                           ((outer_board_x + outer_board_thickness + (inner_dimension) -
                            pocket_radius), (outer_board_y + outer_board_thickness + pocket_radius)),
                           pocket_radius)

        pygame.draw.circle(self.surface,
                           Pocket_colour,
                           ((outer_board_x + outer_board_thickness + (inner_dimension) - pocket_radius),
                            (outer_board_y + outer_board_thickness + (inner_dimension) - pocket_radius)),
                           pocket_radius)
        pygame.draw.circle(self.surface, Pocket_colour,
                           ((outer_board_x + outer_board_thickness + pocket_radius), (outer_board_y + outer_board_thickness + (inner_dimension) - pocket_radius)), pocket_radius)

        # the four pockets in the corners of the board are created

        pygame.draw.circle(self.surface,
                           Red,
                           (outer_board_x + outer_board_thickness + ((inner_dimension))//2,
                            outer_board_y + outer_board_thickness + ((inner_dimension))//2),
                           13)

        pygame.draw.circle(self.surface,
                           Black,
                           (outer_board_x + outer_board_thickness + ((inner_dimension))//2,
                            outer_board_y + outer_board_thickness + ((inner_dimension))//2),
                           67,
                           width=2)

        pygame.draw.circle(self.surface,
                           Red,
                           (3, 2),
                           3)

        pygame.draw.circle(self.surface,
                           Red,
                           (3, 2),
                           3)

        pygame.draw.circle(self.surface,
                           Red,
                           (3, 2),
                           3)

        pygame.draw.circle(self.surface,
                           Red,
                           (3, 2),
                           3)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 105),
                            (outer_board_y + outer_board_thickness+65 + 13)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 105),
                            (outer_board_y + outer_board_thickness+65 + 13)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 105 + 369),
                            (outer_board_y + outer_board_thickness+65+13)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 105 + 369),
                            (outer_board_y + outer_board_thickness+65+13)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 105),
                            (outer_board_y + outer_board_thickness+515-13)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 105),
                            (outer_board_y + outer_board_thickness+515-13)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 105 + 369),
                            (outer_board_y + outer_board_thickness+515-13)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 105 + 369),
                            (outer_board_y + outer_board_thickness+515-13)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 515-13),
                            (outer_board_y + outer_board_thickness+105)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 515-13),
                            (outer_board_y + outer_board_thickness+105)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 515-13),
                            (outer_board_y + outer_board_thickness+105+369)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 515-13),
                            (outer_board_y + outer_board_thickness+105+369)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 65+25-13),
                            (outer_board_y + outer_board_thickness+105)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 65+25-13),
                            (outer_board_y + outer_board_thickness+105)),
                           10)

        pygame.draw.circle(self.surface,
                           Black,
                           ((outer_board_x + outer_board_thickness + 65+25-13),
                            (outer_board_y + outer_board_thickness+105+369)),
                           13)

        pygame.draw.circle(self.surface,
                           Red,
                           ((outer_board_x + outer_board_thickness + 65+25-13),
                            (outer_board_y + outer_board_thickness+105+369)),
                           10)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 105),
                          (outer_board_y + outer_board_thickness+65)),
                         ((outer_board_x + outer_board_thickness + 105 + 369),
                          (outer_board_y + outer_board_thickness+65)),
                         5)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 105),
                          (outer_board_y + outer_board_thickness+65+25)),
                         ((outer_board_x + outer_board_thickness + 105 + 369),
                          (outer_board_y + outer_board_thickness+65+25)),
                         1)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 105),
                          (outer_board_y + outer_board_thickness+515)),
                         ((outer_board_x + outer_board_thickness + 105 + 369),
                          (outer_board_y + outer_board_thickness+515)),
                         5)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 105),
                          (outer_board_y + outer_board_thickness+490)),
                         ((outer_board_x + outer_board_thickness + 105 + 369),
                          (outer_board_y + outer_board_thickness+490)),
                         1)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 515),
                          (outer_board_y + outer_board_thickness+105)),
                         ((outer_board_x + outer_board_thickness + 515),
                          (outer_board_y + outer_board_thickness+105+369)),
                         5)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 490),
                          (outer_board_y + outer_board_thickness+105)),
                         ((outer_board_x + outer_board_thickness + 490),
                          (outer_board_y + outer_board_thickness+105+369)),
                         1)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 65),
                          (outer_board_y + outer_board_thickness+105)),
                         ((outer_board_x + outer_board_thickness + 65),
                          (outer_board_y + outer_board_thickness+105+369)),
                         5)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + 65+25),
                          (outer_board_y + outer_board_thickness+105)),
                         ((outer_board_x + outer_board_thickness + 65 + 25),
                          (outer_board_y + outer_board_thickness+105+369)),
                         1)

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + (inner_dimension) - pocket_radius-30),
                          (outer_board_y + outer_board_thickness + pocket_radius+30)),
                         ((outer_board_x + outer_board_thickness + (inner_dimension) - pocket_radius-30-130), (outer_board_y + outer_board_thickness + pocket_radius+30+130)))

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + pocket_radius+30),
                          (outer_board_y + outer_board_thickness + pocket_radius+30)),
                         ((outer_board_x + outer_board_thickness + pocket_radius+30+130), (outer_board_y + outer_board_thickness + pocket_radius+30+130)))

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + (inner_dimension) - pocket_radius-30),
                          (outer_board_y + outer_board_thickness + (inner_dimension) - pocket_radius-30)),
                         ((outer_board_x + outer_board_thickness + (inner_dimension) - pocket_radius-30-130), (outer_board_y + outer_board_thickness + (inner_dimension) - pocket_radius-30-130)))

        pygame.draw.line(self.surface,
                         Black,
                         ((outer_board_x + outer_board_thickness + pocket_radius+30),
                          (outer_board_y + outer_board_thickness + (inner_dimension) - pocket_radius-30)),
                         ((outer_board_x + outer_board_thickness + pocket_radius+30+130), (outer_board_y + outer_board_thickness + (inner_dimension) - pocket_radius-30-130)))

        pygame.draw.arc(self.surface,
                        Black,
                        (427, 267, 50, 50),
                        Pi, Pi/2)

        pygame.draw.arc(self.surface,
                        Black,
                        (684, 267, 50, 50),
                        -3*Pi/2, 0)

        pygame.draw.arc(self.surface,
                        Black,
                        (427, 524, 50, 50),
                        3*Pi/2, Pi)

        pygame.draw.arc(self.surface,
                        Black,
                        (684, 524, 50, 50),
                        0, 3*Pi/2)

    # the "self.surface_board" subroutine contains all the design for the board including the dimesnions and colours so it can be created at runtime

    def create_walls(self, co_ord1, co_ord2):
        # the type of body must be static so it is stationary
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = ((0, 0))
        shape = pymunk.Segment(body,
                               co_ord1,
                               co_ord2,
                               1)
        # defining the modulus of elasticity is essential for the collisions
        shape.elasticity = 0.8
        self.space.add(shape, body)

    # the boundaries for which the carrom pieces are able to rebound off
    # essentially confining the pieces within the 4 walls of the rectangular board

    @staticmethod
    def rotateboard(pieces, queue):
        if queue.switch == True:  # only if the pointer on the queue is being incremented can the rotation be performed because
            # if this was not the case the user would have another go and the board would not be rotated
            #  #making sure all of the pieces have been rotated
            for i in range(0, (len(pieces))):
                (x, y) = pieces[i].body.position
                displacement_x = (580-x)
                displacement_y = (420 - y)
                # rotation around the center (580,420)
                matrix_calc = (pymunk.Transform(math.cos(math.radians(-90)),
                                                math.sin(math.radians(-90)),
                                                (-1*math.sin(math.radians(-90))),
                                                math.cos(math.radians(-90)))
                               @ pymunk.Transform(displacement_x, displacement_y))  # transformation matrix
                new_x = 580 + matrix_calc[0]
                new_y = 420 + matrix_calc[1]
                new_coord = (new_x, new_y)
                # matrix results added back onto the centre to form the pieces new_position
                pieces[i].body.position = new_coord
                # switching the position attributes of the pieces
                # and therefore physcically switching their positions on the board

# this subroutine essentially simulates the board being rotated
# By looping through all of the pieces and performing a rotational matrix about the centre of the body
# it calculates the new positions of all the pieces on the board and switches their position
