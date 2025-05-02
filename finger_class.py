import pygame
import math


class finger():
    def __init__(self, pos):
        self.image = (pygame.image.load("roatate image.png")).convert_alpha()
        self.__angle = 0

    def update(self, angle):
        self.__angle = angle

    def draw(self, surface, pos, striking):
        if striking == True:
            # the finger should only show if the striking varaible is set to the boolean value True
            # so this means the finger image will not show whilst any of the pieces (including the striker) are in motion

            self.display = pygame.transform.rotate(self.image, self.__angle)
            # the original image is rotated through the specified angle and stored in the "display_image" variable
            self.rect = self.display.get_rect(topleft=(pos[0]-self.image.get_width()+30,
                                                       pos[1]-self.image.get_height()+130))
            surface.blit(self.display, (pos[0]-self.image.get_width()+30,
                                        pos[1]-self.image.get_height()+70))

            # now the rotated image is displayed onto the screen at the sepcified co-ordinates
            # always relative to the width and height of the image

    def calculate_angle(self, angle):
        angle_of_projection = angle + 210
        # here a new angle of projection is calculated relative to the angle that the finger in relation to the striker

        # impulse in the horizontal direction
        x_angle = math.cos(math.radians(angle_of_projection))
        # impulse in the vertical direction
        y_angle = math.sin(math.radians(angle_of_projection))

        return x_angle, y_angle
        # both components of the angle must be returned for further calculation
