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

        # input vars
        self.selected_candidate = tk.IntVar()
        self.selected_candidate.set(-1)

        self.frame_input = tk.Frame(self)
        self.__create_widgets()

        self.update_votes()

    def __create_widgets(self):

        # HEADER
        self.frame_header = tk.Frame(self)
        self.label_menu_title = tk.Label(self.frame_header,
                                         text='VOTE MENU',
                                         font=('Helvetica', 16))
        self.label_menu_title.pack()

        self.label_total = tk.Label(self.frame_header)
        self.label_total.pack()

        self.label_candidate = []
        for _ in range(3):
            self.label_candidate.append(tk.Label(self.frame_header,
                                                 text=f'temp{_}'))
            self.label_candidate[_].pack()

        self.frame_header.pack()

        # INPUT
        for _ in range(3):
            radio_candidate = tk.Radiobutton(self.frame_input,
                                             text=self.vote.get_candidate(_),
                                             variable=self.selected_candidate,
                                             value=_)
            radio_candidate.pack()
        self.selected_candidate.trace_add('write', self.enable_submit)

        self.button_submit = tk.Button(self.frame_input, text='Submit', state='disabled', command=self.submit_vote)
        self.button_submit.pack()

        self.button_exit = tk.Button(self.frame_input, text='Exit', command=self.destroy)
        self.button_exit.pack()

        self.frame_input.pack()

    def enable_submit(self, *args):
        if self.selected_candidate.get() >= 0:
            self.button_submit.config(state='normal')
        else:
            self.button_submit.config(state='disabled')

    def submit_vote(self):
        self.vote.add_vote(self.selected_candidate.get())
        self.update_votes()
        self.selected_candidate.set(-1)

    def update_votes(self):
        self.label_total.config(text=f'Total Votes: {self.vote.get_total()}')
        self.label_total.pack()
        for _ in range(3):
            self.label_candidate[_].config(text=f'{self.vote.get_candidate(_)} - {self.vote.get_vote(_)}')