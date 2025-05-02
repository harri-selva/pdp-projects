import random
import pygame
import pygamepopup
from pygamepopup.components import InfoBox, TextElement
from pygamepopup.menu_manager import MenuManager


class ice_breaker_questions():
    def __init__(self, display):
        pygamepopup.init()
        self.menumanager = MenuManager(display)
        self.question_displayed = False
        self.array_of_questions = ["Where did you grow up?",
                                   "What day in your life would you like to relive?",
                                   "What is the kindest act you have ever done?",
                                   "Describe yourself in three words.",
                                   "What was your dream job as a kid?",
                                   "What are the top three items on your bucket list?",
                                   "What movie scene is worthy of an Oscar?",
                                   "What is your proudest achievement?",
                                   "Five things that make you happy?",
                                   "What is your favorite cereal?",
                                   "Which two companies would you like to be sponsored by?",
                                   "What was your last Netflix binge?",
                                   "If you could be a character in any movie, what character and what movie would it be?",
                                   "If you invented an ice cream flavor, what ingredients would it have, and what would it be called?",
                                   "If you could make an office rule that everyone had to follow for a day, what would it be?",
                                   "What is the best concert/ festival you have ever been to?",
                                   "A genie grants you one wish; what do you wish for?",
                                   "What would you title your biography?",
                                   "What three items would you bring with you on a deserted island?",
                                   "What's your favorite sandwich and why?",
                                   "What is your favorite meal to cook and why?",
                                   "If you could live in a different country for a year, which country would you choose?",
                                   "Would you rather have every traffic light turn green or always have the best parking spot?",
                                   "Who is the most famous person you have met",
                                   "Which one do you like: hot chocolate or hot coffee?",
                                   "Which one do you prefer: to dress smart or dress casually?",
                                   "If you had to eat one food for the rest of time, what would it be?",
                                   "What school year would you like to do over?",
                                   "Have you ever considered a different career to go into?",
                                   "What is something you most look forward to doing when you retire?",
                                   "Who is your favourite teacher in school?",
                                   "Would you rather be an Olympic gold medalist or an astronaut?",
                                   "What's your go-to comfort food?",
                                   "What's your favorite video game?",
                                   "Who was your childhood best friend?",
                                   "Have you ever laughed at something inappropriate or at the wrong time?",
                                   "What is the worst haircut you have ever had?",
                                   "Favourite Holiday?",
                                   "Favourite Pizza topping?",
                                   "Favourite Thing to do after school?",
                                   "Favourite Restaurant?",
                                   "Favourite Season?",
                                   "Favourite Food?",
                                   "Favourite Ice cream flavor?",
                                   "Favourite Book?",
                                   "Favourite Movie?",
                                   "Favourite TV show?",
                                   "If you could meet anyone, living or dead, who would it be?",
                                   "Describe your dream house, including its location.",
                                   "If you could invent something to make life easier, what would it be?",
                                   "Describe the last time you laughed really, really hard",
                                   "If you could be any age for the rest of your life, what age would you be and why?",
                                   "if you could try an adventurous activity like skydiving or bungee jumping, what would it be?",
                                   "If you had to delete all but three apps from your phone, which ones would you keep?",
                                   "What motivates you?",
                                   "Do you prefer the beach, forest, or mountains?",
                                   "What did you do for your last birthday?"
                                   ]

        # array of questions to choose from

    def display_question(self, queue, question_state):
        if question_state == True and queue.switch == True:
            # questions are only displayed if the ice_breaker option on the GUI was ticked and the player has pocketed the striker
            # or pocketed no pieces in their turn
            # the question number is chosen at random
            qs_number = random.randint(0, (len(self.array_of_questions)-1))
            # display questions activated
            POPUP = InfoBox(
                "Question",
                [
                    [
                        TextElement(
                            text=self.array_of_questions[qs_number]
                        )
                    ],
                ],
                width=300,)
            # question displayed on the screen
            self.menumanager.open_menu(POPUP)
            self.menumanager.display()
            pygame.display.update()
            pygame.time.delay(10000)
            # question displayed for 10000 milli-seconds or 10 seconds
            self.question_displayed = True

    def exit(self):
        self.exit_request = True
