from tkinter import *
import customtkinter
from controller import ControllerLogin


class ViewLogin:
    def __init__(self, master):
        """ Frame principale """
        self.login_frame = customtkinter.CTkFrame(master=master, corner_radius=5)

        ''' Frame del form '''
        self.input_frame = customtkinter.CTkFrame(master=self.login_frame, corner_radius=5,
                                                  fg_color=self.login_frame.detect_color_of_master(
                                                      master_widget=self.login_frame))

        ''' Form d'inserimento nome utente e password'''
        self.usr_frame = customtkinter.CTkFrame(master=self.input_frame, corner_radius=5, fg_color='#565B5E')
        self.pswd_frame = customtkinter.CTkFrame(master=self.input_frame, corner_radius=5, fg_color='#565B5E')

        self.usr_lbl = customtkinter.CTkLabel(master=self.usr_frame, width=10, height=10, text='Username',
                                              text_font=('Roboto', 7),
                                              bg_color='#565B5E')
        self.pswd_lbl = customtkinter.CTkLabel(master=self.pswd_frame, width=10, height=10, text='Password',
                                               text_font=('Roboto', 7),
                                               bg_color='#565B5E')

        # Caselle di testo per inserimento nome utente e password
        self.usr_entry = customtkinter.CTkEntry(master=self.usr_frame, placeholder_text='Inserisci il tuo username',
                                                placeholder_text_color='gray50', width=200)
        self.pswd_entry = customtkinter.CTkEntry(master=self.pswd_frame, placeholder_text='Inserisci la tua password',
                                                 placeholder_text_color='gray50', width=200, show='●')

        ''' Pulsanti '''
        self.login_btn = customtkinter.CTkButton(master=self.login_frame, text='Login', width=70,
                                                 command=lambda: ControllerLogin.ControllerLogin.check_account(self.usr_entry.get(),
                                                                                               self.pswd_entry.get(),
                                                                                               self.login_frame,
                                                                                               master))
        self.quit_btn = customtkinter.CTkButton(master=self.login_frame, text='Quit', width=5, height=10, fg_color='#F25252',
                                                hover_color='#B52222', text_font=('Roboto', 7), command=master.quit)

        ''' Inserimento widget all'interno della finestra '''
        self.login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.quit_btn.grid(row=0, column=0, pady=5, padx=10, sticky='e')

        self.input_frame.grid(row=1, column=0, padx=5)

        self.usr_frame.grid(row=0, column=0, padx=5, pady=5, ipadx=2.5, ipady=1.5)
        self.pswd_frame.grid(row=1, column=0, padx=5, pady=2.5, ipadx=2.5, ipady=1.5)

        self.usr_lbl.pack()
        self.pswd_lbl.pack()

        self.usr_entry.pack()
        self.pswd_entry.pack()

        self.login_btn.grid(row=2, column=0, pady=5, padx=10)
