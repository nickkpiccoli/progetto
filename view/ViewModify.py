from tkinter import *
import customtkinter
from controller import ControllerModify
from model import LavoratoreDaoImpl


class ViewModify:
    def __init__(self, master):
        """ Ottengo lavoratori dal csv """
        self.lavoratori_reg = LavoratoreDaoImpl.LavoratoreDaoImpl()

        # INIZIO DICHIARAZIONI
        # inizio dichiarazione frame utilizzati
        self.generalframe = customtkinter.CTkFrame(master=master, corner_radius=5)

        # appartenteni a frame1
        self.frame_mail = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5, fg_color='#565B5E')
        self.frame_bottoni = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5,
                                                    fg_color=self.generalframe.detect_color_of_master(
                                                        master_widget=self.generalframe))

        # inzio dichiarazione label
        self.label_mail = customtkinter.CTkLabel(master=self.frame_mail, text="E-mail lavoratore", width=10,
                                                 height=10, text_font=('Roboto', 7), bg_color='#565B5E')

        # inizio dichiarazione entry
        self.entry_mail = customtkinter.CTkEntry(master=self.frame_mail, placeholder_text="esempio@dominio.it", width=250)
        # fine dichiarazione entry

        # dichiarazione bottone fine
        self.button_procedi = customtkinter.CTkButton(master=self.frame_bottoni, text="Procedi",
                                                      command=lambda: ControllerModify.ControllerModify.procedi(
                                                          self.generalframe, master, self.lavoratori_reg,
                                                          self.entry_mail.get()), width=250)
        self.button_return = customtkinter.CTkButton(master=self.generalframe, text="Torna alla home",
                                                     text_font=('Roboto', 7), width=10, height=5, corner_radius=5,
                                                     fg_color='#32972E', hover_color='#316F2E',
                                                     command=lambda: ControllerModify.ControllerModify.back_home(
                                                         self.generalframe,
                                                         master))

        # FINE DICHIARAZIONI

        # disposizione frame generale/1/2/3/4
        self.generalframe.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.frame_mail.grid(row=1, column=0, ipadx=2.5, ipady=1.5, padx=10)
        self.label_mail.pack()
        self.entry_mail.pack()

        # disposizione bottone
        self.frame_bottoni.grid(row=2, column=0)
        self.button_procedi.grid(row=0, column=0, padx=10, pady=10)
        self.button_return.grid(row=0, column=0, padx=10, pady=10, sticky='e')
