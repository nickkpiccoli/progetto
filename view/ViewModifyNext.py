from tkinter import *
from controller import ControllerModifyNext
import customtkinter

# Impostazione del tema
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('blue')

window = customtkinter.CTk()
window.geometry("900x650")


class ViewModifyNext:
    def __init__(self, master: customtkinter.CTk, lavoratore, lavoratori_reg):
        # INIZIO DICHIARAZIONI
        # inizio dichiarazione frame utilizzati
        self.generalframe = customtkinter.CTkFrame(master=master, corner_radius=5)
        self.top_frame = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5,
                                                fg_color=self.generalframe.detect_color_of_master(
                                                    master_widget=self.generalframe))
        self.bottom_frame = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5)
        self.buttonframe = customtkinter.CTkFrame(master=self.bottom_frame, corner_radius=5,
                                                  fg_color=self.bottom_frame.detect_color_of_master(master_widget=self.bottom_frame))

        # inzio dichiarazione label
        self.label_title = customtkinter.CTkLabel(master=self.bottom_frame,
                                                  text="Attuali Esperienze Lavorative Registrate")
        self.label_option = customtkinter.CTkLabel(master=self.buttonframe, text='oppure', width=100)
        # fine dichiarazione label

        # inizio dichiarazione listbox
        self.listbox_lavori = Listbox(self.bottom_frame, width=135, height=20)
        ControllerModifyNext.ControllerModifyNext.populate(self.listbox_lavori, lavoratore)

        # dichiarazione bottone fine
        self.button_aggiungi = customtkinter.CTkButton(master=self.buttonframe, text="Aggiungi lavoro",
                                                       command=lambda: ControllerModifyNext.ControllerModifyNext.inserisci(lavoratori_reg,
                                                                                                      lavoratore, self.listbox_lavori))
        self.button_return = customtkinter.CTkButton(master=self.top_frame, text="Torna alla home", width=10,
                                                     height=10, text_font=('Roboto', 7), fg_color='#32972E', hover_color='#316F2E',
                                                     command=lambda: ControllerModifyNext.ControllerModifyNext.back_home(self.generalframe,
                                                                                                    master))
        self.button_modifica = customtkinter.CTkButton(master=self.buttonframe, text="Modifica lavoro", command=lambda: ControllerModifyNext.ControllerModifyNext.modifica(lavoratori_reg, lavoratore, self.listbox_lavori.curselection(), self.listbox_lavori))

        # FINE DICHIARAZIONI
        # disposizione frame generale/1/2/3/4
        self.generalframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.bottom_frame.grid(row=2, column=0, padx=10, pady=10)

        # disposizione interna a self.generalframe
        self.label_title.grid(row=0, column=0)
        self.listbox_lavori.grid(row=1, column=0, padx=30)
        self.buttonframe.grid(row=2, column=0, pady=10)

        self.button_aggiungi.grid(row=0, column=0)
        self.label_option.grid(row=0, column=1)
        self.button_modifica.grid(row=0, column=2)

        self.button_return.pack()
