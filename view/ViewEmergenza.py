from tkinter import *
import customtkinter
from controller import ControllerEmergenza


class ViewEmergenza:
    def __init__(self, lavoratore, registration_button):
        # INIZIO DICHIARAZIONI
        # inizio dichiarazione frame utilizzati
        self.window = customtkinter.CTkToplevel()
        self.window.title("Contatti d'emergenza")
        self.window.geometry('400x400')

        self.generalframe = customtkinter.CTkFrame(master=self.window, corner_radius=5)

        # appartententi a generalm frame
        self.frame1 = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5)
        self.frame2 = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5, fg_color=self.generalframe.detect_color_of_master(master_widget=self.generalframe))

        # appartenteni a self.frame1
        self.frame_nomeurg = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_cognomeurg = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_telurg = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_mailurg = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')

        # inzio dichiarazione label
        self.label_nomeurg = customtkinter.CTkLabel(master=self.frame_nomeurg, text="Nome", width=10, height=10,
                                                    text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_cognomeurg = customtkinter.CTkLabel(master=self.frame_cognomeurg, text="Cognome", width=10,
                                                       height=10,
                                                       text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_telurg = customtkinter.CTkLabel(master=self.frame_telurg, text="Numero di telefono", width=10,
                                                   height=10,
                                                   text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_mailurg = customtkinter.CTkLabel(master=self.frame_mailurg, text="Indirizzo E-Mail", width=10,
                                                    height=10,
                                                    text_font=('Roboto', 7), bg_color='#565B5E')
        # fine dichiarazione label

        # inizio dichiarazione entry
        self.entry_nomeurg = customtkinter.CTkEntry(master=self.frame_nomeurg, placeholder_text="Inserisci nome")
        self.entry_cognomeurg = customtkinter.CTkEntry(master=self.frame_cognomeurg,
                                                       placeholder_text="Inserisci cognome")
        self.entry_telurg = customtkinter.CTkEntry(master=self.frame_telurg, placeholder_text="Inserisci telefono")
        self.entry_mailurg = customtkinter.CTkEntry(master=self.frame_mailurg, placeholder_text="esempio@dominio.it")
        # fine dichiarazione entry

        anagrafiche = (self.entry_nomeurg, self.entry_cognomeurg, self.entry_telurg, self.entry_mailurg)

        # dichiarazione bottone fine
        self.button_registra = customtkinter.CTkButton(master=self.generalframe, text="Registra contatto",
                                                       command=lambda: ControllerEmergenza.ControllerEmergenza.registra(
                                                           lavoratore,
                                                           anagrafiche,
                                                           registration_button))

        self.option_lbl = customtkinter.CTkLabel(master=self.frame2, text="oppure", text_font=('Roboto', 8))

        self.button_fine = customtkinter.CTkButton(master=self.frame2, text="Continua e chiudi finestra",
                                                   command=lambda: ControllerEmergenza.ControllerEmergenza.continua(
                                                       self.window))

        # FINE DICHIARAZIONI

        # disposizione frame generale/1/2/3/4
        self.generalframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame1.grid(row=0, column=0, padx=10, pady=10)
        self.frame2.grid(row=2, column=0, padx=10, pady=10)

        # disposizione interna a self.frame1
        self.frame_nomeurg.grid(row=0, column=0, ipadx=2.5, ipady=1.5, padx=10, pady=10)
        self.label_nomeurg.pack()
        self.entry_nomeurg.pack()

        self.frame_cognomeurg.grid(row=0, column=1, ipadx=2.5, ipady=1.5, padx=10, pady=10)
        self.label_cognomeurg.pack()
        self.entry_cognomeurg.pack()

        self.frame_telurg.grid(row=1, column=0, ipadx=2.5, ipady=1.5, padx=10, pady=10)
        self.label_telurg.pack()
        self.entry_telurg.pack()

        self.frame_mailurg.grid(row=1, column=1, ipadx=2.5, ipady=1.5, padx=10, pady=10)
        self.label_mailurg.pack()
        self.entry_mailurg.pack()

        # disposizione bottone
        self.button_registra.grid(row=1, column=0)
        self.option_lbl.pack()
        self.button_fine.pack()
