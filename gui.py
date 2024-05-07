import tkinter as tk
from typing import Type
from voting import Vote


class HeaderFrame(tk.Frame):
    def __init__(self, container, vote):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        self.label_menu_title = tk.Label(self, text='VOTE MENU', font=('Helvetica', 16))
        self.label_menu_title.pack()

        self.label_total = tk.Label(self)
        self.label_total.pack()

        self.label_candidate = []
        for _ in range(3):
            self.label_candidate.append(tk.Label(self, text=f'temp{_}'))
            self.label_candidate[_].pack()


class InputFrame(tk.Frame):
    def __init__(self, container, vote):
        super().__init__(container)
        self.selected_candidate = tk.IntVar()
        self.selected_candidate.set(-1)
        self.__create_widgets(vote)

    def __create_widgets(self, vote):
        for _ in range(3):
            rb = tk.Radiobutton(self, text=vote.get_candidate(_), variable=self.selected_candidate, value=_)
            rb.pack(anchor='w')
        self.selected_candidate.trace_add('write', self.enable_submit)

        self.button_submit = tk.Button(self, text='Submit', state='disabled')
        self.button_submit.pack()

    def enable_submit(self, *args):
        if self.selected_candidate.get() >= 0:
            self.button_submit.config(state='normal')
        else:
            self.button_submit.config(state='disabled')


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.vote = Vote()

        self.test = 'test'
        self.title('Voting App')
        self.geometry('300x350')
        self.resizable(False, False)
        self.__create_widgets()

        self.update_votes()

    def __create_widgets(self):
        self.frame_header = HeaderFrame(self, self.vote)
        # frame_header.label_menu_title.config(text='CANDIDATE MENU')
        self.frame_header.label_candidate[1].config(text='hi')

        self.frame_header.pack()

        self.frame_input = InputFrame(self, self.vote)
        self.frame_input.pack()
        self.frame_input.button_submit.bind('<Button-1>', self.submit_vote())

    def submit_vote(self):
        print(self.frame_input.selected_candidate.get())
        self.vote.add_vote(self.frame_input.selected_candidate.get())
        self.update_votes()

    def update_votes(self):
        self.frame_header.label_total.config(text=f'Total Votes: {self.vote.get_total()}')
        self.frame_header.label_total.pack()
        for _ in range(3):
            self.frame_header.label_candidate[_].config(text=f'{self.vote.get_candidate(_)} - {self.vote.get_vote(_)}')
            self.frame_header.label_candidate[_].pack()

    # def create_header(self):
        # frame = tk.Frame(container)
        # self.label_menu_title = tk.Label(self.frame_header, text='VOTE MENU', font=('Helvetica', 16))
        # self.label_menu_title.pack()
        # self.frame_header.pack()

    #    return frame

    # def main_menu(self):
    #    pass

    # def candidate_menu(self):
    #    pass

    # def submit(self):
    #    pass
