import pygame


class Leaderboard:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.SysFont(None, 50)

    def get_name():
        pass

    def display_leaderbaord(self, player_object, player_turn, run):
        if run == True:
            store = []
            for i in player_object:
                # storing the names and points of each in a 2D ARRAY
                store.append([i.name, i.score])

            title = self.font.render('Points tally',
                                     True,
                                     (0, 0, 0))
            self.display.blit(title,
                              (1000, 50))

            for index, item in enumerate(store, 1):
                if player_turn.name == item[0]:
                    text = self.font.render(f"{index}.{item[0]} - {item[1]}",
                                            True,
                                            (255, 0, 0))
                else:
                    text = self.font.render(f"{index}.{item[0]} - {item[1]}",
                                            True,
                                            (0, 0, 0))

                self.display.blit(text,
                                  (1000, 50 + (50 * index)))

                #  displaying the text on the game
