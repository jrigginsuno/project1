import tkinter as tk

class VotingApp:
    """
    Initialize variables
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Voting App")
        
        self.candidates = {"Bianca": 0, "Edward": 0, "Felicia": 0}
        self.total_votes = 0
        self.selected_candidate = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        self.vote_label = tk.Label(self.master, text="VOTE MENU", font=("Helvetica", 16))
        self.vote_label.pack()

        self.total_votes_label = tk.Label(self.master, text="Total Votes: {}".format(self.total_votes))
        self.total_votes_label.pack()

        self.candidates_votes_label = tk.Label(self.master, text="Candidates Votes: Bianca - {}, Edward - {}, Felicia - {}".format(self.candidates["Bianca"], self.candidates["Edward"], self.candidates["Felicia"]))
        self.candidates_votes_label.pack()

        self.vote_button = tk.Button(self.master, text="Proceed to Candidate Menu", command=self.show_candidate_menu)
        self.vote_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

    def show_candidate_menu(self):
        self.vote_label.config(text="CANDIDATE MENU")

        self.candidate_frame = tk.Frame(self.master)
        self.candidate_frame.pack()

        for candidate in self.candidates:
            rb = tk.Radiobutton(self.candidate_frame, text=candidate, variable=self.selected_candidate, value=candidate)
            self.selected_candidate.set(None)
            rb.pack(anchor="w")
            
        self.vote_button.pack_forget()
        self.exit_button.pack_forget()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.record_vote, state="disabled")
        self.submit_button.pack()

        self.selected_candidate.trace_add("write", self.enable_submit_button)

    def enable_submit_button(self, *args):
        if self.selected_candidate.get():
            self.submit_button.config(state="normal")
        else:
            self.submit_button.config(state="disabled")

    def record_vote(self):
        selected_candidate = self.selected_candidate.get()
        if selected_candidate in self.candidates:
            self.candidates[selected_candidate] += 1
            self.total_votes += 1
            self.reset_candidate_menu()
            self.update_main_menu()

    def reset_candidate_menu(self):
        self.vote_label.config(text="VOTE MENU")
        self.vote_button.config(text="Proceed to Candidate Menu")

        self.candidate_frame.destroy()
        self.submit_button.destroy()
        
        self.vote_button.pack()
        self.exit_button.pack()

    def update_main_menu(self):
        self.total_votes_label.config(text="Total Votes: {}".format(self.total_votes))
        self.candidates_votes_label.config(text="Candidates Votes: Bianca - {}, Edward - {}, Felicia - {}".format(self.candidates["Bianca"], self.candidates["Edward"], self.candidates["Felicia"]))

def main():
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
