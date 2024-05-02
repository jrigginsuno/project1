from gui import *


def main():
    window = tk.Tk()
    window.title('Voting App')
    window.geometry('300x200')

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()


