import re
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Utilities import settings, utils


class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        content = ttk.Frame(self)

        # create widgets
        self.top_frame = Frame(content, bg='blue', width=settings.WIDTH, height=utils.height_prct(25))
        self.head_label = ttk.Label(content, text='The Enchanted Chasm', font=('typewriter', 40), background='blue')
        self.right_frame = Frame(content, bg='white', width=utils.width_prct(25), height=utils.height_prct(75))
        self.lbl_frame = ttk.Label(content, text='Notes', font=('typewriter', 20), background='white')
        self.txt_box = Text(content, height=10, width=42)

        content.grid(column=0, row=0)
        self.top_frame.grid(column=0, row=0, columnspan=4, rowspan=1)
        self.head_label.grid(column=2, row=0)
        self.right_frame.grid(column=3, row=1, columnspan=2, rowspan=4)
        self.lbl_frame.grid(column=3, row=1, sticky=tk.N, columnspan=2, rowspan=1)
        self.txt_box.grid(column=3, row=1, sticky=tk.S, columnspan=2, rowspan=1)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)        

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.configure(bg='gray')
        self.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
        self.title('Enchanted Chasm')
        self.resizable(True, True)

        # create a model
        model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        view = View(self)
        view.grid(column=0, row=0)
        # view.grid(row=0, column=0, padx=10, pady=10)
        #
        # # create a controller
        #controller = Controller(model, view)
        #
        # # set the controller to view
        # view.set_controller(view)


if __name__ == '__main__':
    app = App()
    app.mainloop()            