import customtkinter
from HomePage_class import HomePage
from RulePage_class import RulePage
from GamePage_class import GamePage


class mainwindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        self.title("Carrom GUI")
        self.geometry('1500x1200')

        container = customtkinter.CTkFrame(self, width=1500, height=1200)
        # frame created
        container.pack(expand=1, fill="both")
        # fill the screen
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for page in (HomePage, RulePage, GamePage):
            # create the objects of each page class
            frame = page(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[page] = frame

        # Using a method to switch frames

        self.change_page(HomePage)  # first switch to home page

    def change_page(self, cont):

        frame = self.frames[cont]
        frame.create_widgets()
# raises the current frame to the top


if __name__ == "__main__":
    CarromGUI = mainwindow()
    CarromGUI.mainloop()  # calls the main window loop
