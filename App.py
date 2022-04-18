import tkinter as tk

class App:
    '''
    Class responsible for displaying main user graphical interface
    '''
    def __init__(self):
        '''
        Class constructor
        '''
        self.window = tk.Tk()

    def run(self):
        '''
        Method which launches window
        '''
        self.window.mainloop()