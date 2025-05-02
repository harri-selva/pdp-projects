
from pieces_class import Pieces
import pygame
from constants import *
from board_class import Board
import pymunk


class Striker(Pieces):
    def __init__(self):
        self.image = (pygame.image.load("striker.png")).convert_alpha()
        self.radius = 16
        self.piece_points = -1
        self.pocketed = False
        self.colour = "yellow"

    def create_piece(self, location, my_space):
        self.body = pymunk.Body()
        self.body.position = location
        self.shape = pymunk.Circle(self.body, self.radius)
        # defing both the body and shape is necessary for the creation for the piece
        self.pivot = pymunk.PivotJoint(my_space.static_body, self.body,
                                       (0, 0),
                                       (0, 0))

        # defining the modulus of elasticity of the carrom pieces
        # fundamentally determinng the speeds of the pieces after they collide
        self.shape.elasticity = 0.81
        self.shape.mass = 13
        self.pivot.max_force = 50
        self.pivot.max_bias = 0
        # adding all the components to the physics space
        my_space.add(self.shape,
                     self.body,
                     self.pivot)
        return self.shape

# polymorphism has been implmented as a tehcnique because the striker is made more bouncier than other piece as the eleasticity has increased
# therefore overriding the method in the base class ("Pieces class")

    def shoot(self, striking, x, y, power):
        if striking == True:
            self.body.apply_impulse_at_local_point((power * (-1*x), power * y),
                                                   (0, 0))
            # apply the impulse by multiplying the component of the angle by the power
            # applying the impulse at the centre of the body

    def position_striker(self, striking):
        if striking == True:
            # positioning the striker should only be allowed when the striking variable is True (not when the pieces are moving)
            # the position of the cursor is attained
            cursor_position = pygame.mouse.get_pos()

            if cursor_position[0] >= (outer_board_x + outer_board_thickness + 105 + 369):
                self.body.position = ((outer_board_x + outer_board_thickness + 105 + 369),
                                      (self.body.position[1]))
                # if the position of the striker reaches the very right end of the board it should not leave the tramlines defined on the right
            elif cursor_position[0] <= (outer_board_x + outer_board_thickness + 105):
                self.body.position = ((outer_board_x + outer_board_thickness + 105),
                                      (self.body.position[1]))
                # if the position of the striker reaches the very left end of the board it should not leave the tramlines defined on the left
            else:
                self.body.position = (cursor_position[0],
                                      (self.body.position[1]))
                # if both cases are not true then the striker and subsequently the finger will follow the x co-ordinate of the mouse position

    # the striker must be returned to the baseline after each turn when all the pieces in the stop moving
    def reposition_on_baseline(self, pieces, striking, queue, black_carrom_men, white_carrom_men, striker_object, my_space, ice_breaker, question_state, display):
        if striking == False:
            # the "if" statement makes sure that during the repositioning that the striker is in open play
            # and is being repositioned after it has been hit
            if Pieces.is_moving(pieces) == False:
                # if statement checking if all the peices have stopped moving

                try:
                    player = queue.seek()
                # checks for the player's turn has just passed from the queue using the "seek" command
                # returns the player_object at the top of the queue
                except:
                    print("there are no players in the queue")

                if player.pocketed_queen == True and queue.switch == True:
                    player.due += 15
                    player.score -= 15
                    player.pocketed_queen = False

                player.pay_due(striker_object, queue,
                               black_carrom_men,
                               white_carrom_men,
                               pieces,
                               my_space,
                               display)
                # ice_breaker questions displayed along with repositioning (if the option is chosen to)
                # question_state is passed in as an arguement taking into account the user's preferences to show the ice_breaker questions or not
                self.body.position = (
                    outer_board_x + outer_board_thickness + (inner_dimension/2) + 210, 630)
                # striker positon redefined back to the baseline
                self.position_striker(striking)

                ice_breaker.display_question(queue, question_state)

                # able to positions striker again

                # pay due method used to see if the user has pocketed anything that has to be put back having been on a negative score
                # and is used to pay back any due that is remaining while on a positive score
                # this invloves paying back a pentaly from pocketing the striker

                # the switchturn command is used to move the queue pointer to the next object of the player_class
                queue.switchturn()
                Board.rotateboard(pieces,
                                  queue)
                # rotatebaord command used to rotate all the pieces existing on the board (all the peices in the "pieces" list)
                # if pointer from the queue has moved forward
                queue.switch = True
                striking = True
                # once the striker has reached the baseline the game is ready to process another shot
                # so the striking attribtue is set to the boolean value "True"

    def return_to_original_position(self):
        self.body.position = (
            outer_board_x + outer_board_thickness + (inner_dimension/2) + 30, 630)
        self.body.velocity = (0.0, 0.0)
