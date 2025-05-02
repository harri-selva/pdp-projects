from constants import *
from pieces_class import Pieces
import pygame
from mergesort_class import mergesort
from white_carrom_men_class import White_Carrom_men
from black_carrom_men_class import Black_Carrom_men

# the player class is created below for each player to be instantiated


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.due = 0
        self.pocketed_striker = False
        self.pocketed_queen = False
        self.pocketed_pieces = []
        self.put_back = []
        self.point_values = {"black": 5,
                             "white": 10,
                             "yellow": -5,
                             "red": 20}

        # a dictionary is created to hold the colour of the pieces and their associated values

    # the attributes of the players are defined in the constructor

    def point_calcuation(self, queue, player):
        # as a defualt, if the player has pocketed a piece they should not lose their go
        queue.switch = False
        piece = (self.pocketed_pieces[-1])
        # the last pocketed piece is extracted as the last piece added to the player's pocketed pieces

        if piece.colour == "red":  # pocketing the queen is a special case so an if-else statement is used
            player.pocketed_queen = True  # player's pocketed queen set to true

        else:
            if player.pocketed_queen == True and self.point_values[piece.colour] == 5:
                # on the turn after or the same turn as pocketing the queen, a black carrom piece is pocketed
                # add the points value of the red for whihc it refers to it in dictionary
                self.score += self.point_values["red"]
                self.pocketed_queen = False  # pocketed queen is set to false

            elif (player.pocketed_queen == True and self.point_values[piece.colour] == 10) or (player.pocketed_queen == True and self.point_values[piece.colour] == -5):
                # if a piece other than the black piece is pocketed whilst the pocketed queen attribute is true
                # this does not count as covering the queen
                if self.score > 15:
                    self.due += 15  # a due of 15 is added to thep player
                    self.score -= 15  # 15 points are taken off the player's score total
                    self.pocketed_queen = False  # pocketed queen is set to false

                elif self.score == 10:
                    self.put_back.append("white")
                    self.score -= 15  # 15 points are taken off the player's score total
                    self.pocketed_queen = False  # pocketed queen is set to false

                elif self.score == 5:
                    self.put_back.append("black")
                    self.score -= 15  # 15 points are taken off the player's score total
                    self.pocketed_queen = False  # pocketed queen is set to false

                elif self.score == 0:
                    self.score -= 15  # 15 points are taken off the player's score total
                    self.pocketed_queen = False  # pocketed queen is set to false

            if (self.point_values[piece.colour] == 10 and (self.score) == -5):
                # accomodating for the special case when the player is one 5 points and goes on to pocket a white piece
                # a black piece must be put back to the centre circle
                # put_back is reffered to in the pay_due method
                self.put_back.append("black")
                player.due = 0  # there is no due as the put_back list deals with it

            elif self.point_values[piece.colour] != -5 and (self.point_values[piece.colour] + self.score) <= 0:
                # whilst on a negative points total and pockets a piece to remain on a negative total
                # you must put back the piece that you had just pocketed back to the centre circle
                # added to the put_back list
                self.put_back.append(piece.colour)
                player.due = 0  # there is no due as the put_back list deals with it

            # add the point values of the pocketed piece to the score of the player
            self.score += self.point_values[piece.colour]

    def pay_due(self, striker_object, queue, black_carrom_men, white_carrom_men, pieces, my_space, display):

        if len(self.put_back) > 0:
            for i in self.put_back:
                if i == "black":
                    Black_Carrom_men.generate_new(black_carrom_men,
                                                  pieces,
                                                  my_space)

            # this is an exmple of method overloading where the same method name is used
            # the method name generate_new exists in both the "Black_carrom_men" class and the "White_carrom_men" class
            # however perform different algorithms

                if i == "white":
                    White_Carrom_men.generate_new(white_carrom_men,
                                                  pieces,
                                                  my_space)

            self.put_back = []
            queue.switch = False

        elif self.due > 0 and self.score > -5:
            while (self.due > 0 and self.score > 0) or (self.due > 0 and self.score > -5 and striker_object.pocketed == True):
                # in the case that the score is positive and the due is also positive
                if self.due >= 10:
                    White_Carrom_men.generate_new(white_carrom_men,
                                                  pieces,
                                                  my_space)
                    self.due -= 10
                if self.due == 5:
                    Black_Carrom_men.generate_new(black_carrom_men,
                                                  pieces,
                                                  my_space)
                    self.due -= 5

            queue.switch = True

        if self.pocketed_striker == True and Pieces.is_moving(pieces) == False:
            queue.switch = True  # the player turn must be switched if the striker is pocketed
            striker_object.create_piece(
                (outer_board_x + outer_board_thickness + (inner_dimension/2) + 210, 630), my_space)
            striker_object.display_image(display)  # display striker image
            pieces.append(striker_object)  # append ot pieces list
            striker_object.pocketed = False
            self.pocketed_striker = False

            # if the striker is pocketed another striker_object is created and positioned at the baseline

    def check_and_determine_winner(player_queue, pieces, display, striker_object, game_timer):
        font = pygame.font.SysFont(None, 50)
        num = len(player_queue.list)

        if (len(pieces) == 1 and striker_object.pocketed == False) or (game_timer > 1107000):
            # 18 minutes and 27 seconds = 1107000 milliseconds
            # if the number of pieces on the board is 1 and the striker has not been pocketed or the time limit for the game has finished
            # a winner can be determined
            display.fill(White)  # a new white screen is created
            points_array = []
            for i in player_queue.list:
                # all the points collected by the player objects in the queue are transffered to a seprate array
                points_array.append(i.score)
            ordered_points_array = mergesort.merge_sort_method(
                points_array)  # merge sort used to sort the points totals
            point_margin = ordered_points_array[-1] - ordered_points_array[-2]
            # point margin calculated by the difference between the last and penultimate score totals in the ordered list
            # the mergesort algorithm is used to determine which player has the highest points tally and therefore can be determined the winner
            move_down_1 = 50
            move_down_2 = 50

            for i in player_queue.list:  # iterating thorugh the whole queue
                # the last item in the list is the highest value
                if ordered_points_array[-1] == i.score:
                    title = font.render(f'{i.name} WINS!!!', True, (0, 0, 0))
                    sub_title = font.render(
                        f'{point_margin} points between first and second', True, (0, 0, 0))
                    display.blit(title, (400, 200 + move_down_1))
                    display.blit(sub_title, (400, 400 + move_down_1))
                    move_down_1 += 50
                    # The winner's name is displayed on the screen, as well as the points margin between first and second place

            # iterated through the list according to how many players are in the queue
            for i in range(0, num):
                text = font.render(
                    f'{player_queue.list[0].name} got {player_queue.list[0].score} points', True, (0, 0, 0))
                # this is to display each players' points totals individually
                # added to the screen
                display.blit(text, (800, 500 + move_down_2))
                # dequeue method to remove the player at the top of the queue using the first in first out principle
                player_queue.dequeue()
                # this is in order to change which player is at the top of the queue during the iterations
                move_down_2 += 50

            pygame.time.delay(1000)  # time delay to display the screen
