import customtkinter
import tkinter as tk
from PIL import ImageTk, Image
from RulePage_class import RulePage


class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

    def create_widgets(self):
        self._canvas = customtkinter.CTkCanvas(
            self.parent, width=1500, height=1200)
        self._canvas.pack()
        background = Image.open(
            "f09ed6_bd0ea8ee74144d889fd5550e9ff15309~mv2.webp").resize((1500, 1200))
        background_tk = ImageTk.PhotoImage(background)
        self._canvas.create_image(0, 0, anchor=tk.NW, image=background_tk)

        main_title = Image.open("Picture 1.png")
        main_title_tk = ImageTk.PhotoImage(main_title)
        self.image1 = self._canvas.create_image(
            400, 5, anchor=tk.NW, image=main_title_tk)

        carrom_3 = Image.open(
            "Screenshot_2023-10-08_at_18.41.01-removebg-preview.png").resize((350, 350))
        carrom_3_tk = ImageTk.PhotoImage(carrom_3)
        self._canvas.create_image(255, 170, anchor=tk.NW, image=carrom_3_tk)
        carrom_5 = Image.open("5 player board.png").resize((350, 350))
        carrom_5_tk = ImageTk.PhotoImage(carrom_5)
        self._canvas.create_image(795, 125, anchor=tk.NW, image=carrom_5_tk)
        carrom_4 = Image.open(
            "Screenshot 2023-09-25 at 07.28.39.png").resize((400, 400))
        carrom_4_tk = ImageTk.PhotoImage(carrom_4)
        self._canvas.create_image(550, 170, anchor=tk.NW, image=carrom_4_tk)

        self.button = customtkinter.CTkButton(self._canvas,
                                              width=200,
                                              height=40,
                                              text="4 Player",
                                              font=("Arial", 18),
                                              hover_color="#009f4d",
                                              command=lambda: [self.lets_play()])  # 4 player button
        self.button.place(x=650, y=550)

        self.mainloop()

    def clear_frame(self):
        for child in self.winfo_children():
            child.place_forget()

    def lets_play(self):
        self.switch = customtkinter.CTkButton(self._canvas,
                                              width=200,
                                              height=40,
                                              bg_color="transparent",
                                              text="LETS PLAY",
                                              command=lambda: [self.clear_frame(),
                                                               self.controller.change_page(RulePage)])  # switch page to rule page

        self.switch.place(x=980, y=620)
