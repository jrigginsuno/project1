import tkinter as tk
from voting import Vote


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.vote = Vote()
        self.test = 'test'
        self.title('Voting App')
        self.geometry('300x350')
        self.resizable(False, False)

        self.__create_widgets()

    def __create_widgets(self):
        #
        # Write widgets here
        #
        pass
