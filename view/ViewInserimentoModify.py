import customtkinter
from tkinter import *
from controller import ControllerInserimentoModify


class ViewInserimentoModify:
    def __init__(self, lavoratori_reg, lavoratore, listbox_lavori):
        # INIZIO DICHIARAZIONI
        # inizio dichiarazione frame utilizzati
        self.window = customtkinter.CTkToplevel()
        self.window.title("Esperienze lavorative")
        self.window.geometry('600x600')

        # appartententi a generalm frame
        self.frame1 = customtkinter.CTkFrame(master=self.window, corner_radius=5)

        # appartenteni a self.frame1
        self.frame_nomeazienda = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_ubicazione = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_initwork = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_endwork = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_retribuzione = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_impiego = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')

        # inzio dichiarazione label
        self.label_nomeazienda = customtkinter.CTkLabel(master=self.frame_nomeazienda, text="Nome Azienda", width=10,
                                                        height=10,
                                                        text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_ubicazione = customtkinter.CTkLabel(master=self.frame_ubicazione, text="Ubicata presso", width=10,
                                                       height=10,
                                                       text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_initwork = customtkinter.CTkLabel(master=self.frame_initwork, text="Inizio lavoro", width=10,
                                                     height=10,
                                                     text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_endwork = customtkinter.CTkLabel(master=self.frame_endwork, text="Fine lavoro", width=10, height=10,
                                                    text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_retribuzione = customtkinter.CTkLabel(master=self.frame_retribuzione, text="Retribuzione lorda "
                                                                                              "giornaliera", width=10,
                                                         height=10,
                                                         text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_impiego = customtkinter.CTkLabel(master=self.frame_impiego, text="Impieghi svolti", width=10,
                                                    height=10,
                                                    text_font=('Roboto', 7), bg_color='#565B5E')
        # fine dichiarazione label

        # inizio dichiarazione entry
        self.entry_nomeazienda = customtkinter.CTkEntry(master=self.frame_nomeazienda, placeholder_text="Inserisci "
                                                                                                        "azienda")
        self.entry_ubicazione = customtkinter.CTkEntry(master=self.frame_ubicazione, placeholder_text="Inserisci "
                                                                                                      "ubicazione")
        self.entry_initwork = customtkinter.CTkEntry(master=self.frame_initwork, placeholder_text="gg/mm/aaaa")
        self.entry_endwork = customtkinter.CTkEntry(master=self.frame_endwork, placeholder_text="gg/mm/aaaa")
        self.entry_retribuzione = customtkinter.CTkEntry(master=self.frame_retribuzione, placeholder_text="€€€€")
        self.entry_impiego = customtkinter.CTkEntry(master=self.frame_impiego,
                                                    placeholder_text="Inserisci le mansioni separate da "
                                                                     "virgola", width=300)
        # fine dichiarazione entry

        dati = (self.entry_nomeazienda, self.entry_ubicazione, self.entry_initwork, self.entry_endwork,
                self.entry_retribuzione, self.entry_impiego)

        # dichiarazione bottone fine
        self.button_inserisci = customtkinter.CTkButton(master=self.frame1, text="Inserisci e chiudi finestra",
                                                        command=lambda: ControllerInserimentoModify.ControllerInserimentoModify.add_job(
                                                            lavoratori_reg, lavoratore, dati, listbox_lavori,
                                                            self.window))

        # FINE DICHIARAZIONI

        # disposizione frame generale/1/2/3/4
        self.frame1.place(relx=0.5, rely=0.5, anchor=CENTER)

        # disposizione interna a self.frame1
        self.frame_nomeazienda.grid(row=0, column=0, padx=10, pady=10, ipadx=2.5, ipady=1.5)
        self.label_nomeazienda.pack()
        self.entry_nomeazienda.pack()

        self.frame_ubicazione.grid(row=0, column=1, padx=10, pady=10, ipadx=2.5, ipady=1.5)
        self.label_ubicazione.pack()
        self.entry_ubicazione.pack()

        self.frame_initwork.grid(row=1, column=0, padx=10, ipadx=2.5, ipady=1.5)
        self.label_initwork.pack()
        self.entry_initwork.pack()

        self.frame_endwork.grid(row=1, column=1, padx=10, ipadx=2.5, ipady=1.5)
        self.label_endwork.pack()
        self.entry_endwork.pack()

        self.frame_retribuzione.grid(row=3, column=0, columnspan=2, padx=10, ipadx=2.5, ipady=1.5)
        self.label_retribuzione.pack()
        self.entry_retribuzione.pack()

        self.frame_impiego.grid(row=2, column=0, columnspan=2, pady=10, ipadx=2.5, ipady=1.5)
        self.label_impiego.pack()
        self.entry_impiego.pack()

        # disposizione bottone
        self.button_inserisci.grid(row=4, column=0, columnspan=2, pady=10)
