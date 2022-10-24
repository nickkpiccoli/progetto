from tkinter import *
import customtkinter
from controller import ControllerRicerca
from model import LavoratoreDaoImpl


class ViewRicerca:
    def __init__(self, master):
        """ Ottengo lavoratori dal csv """
        self.lavoratori_reg = LavoratoreDaoImpl.LavoratoreDaoImpl()

        """ Variabili per RadioButtons, CheckBoxes e Switch """
        self.auto = IntVar()
        self.auto.set(0)

        self.AM = StringVar()
        self.AM.set('')
        self.A = StringVar()
        self.A.set('')
        self.B = StringVar()
        self.B.set('')
        self.C = StringVar()
        self.C.set('')

        self.switch = BooleanVar()
        self.switch.set(False)

        # INIZIO DICHIARAZIONI
        # inizio dichiarazione frame utilizzati
        self.generalframe = customtkinter.CTkFrame(master=master, corner_radius=5)

        # appartententi a generalm frame
        self.frame1 = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5)
        self.frame2 = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5, fg_color=self.generalframe.detect_color_of_master(master_widget=self.generalframe))
        self.frame3 = customtkinter.CTkFrame(master=self.generalframe, corner_radius=5)

        # appartenteni a self.frame1
        self.frame_nome = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_cognome = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_lingue = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_dispo_init = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_dispo_end = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_indirizzo = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_spec = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color='#565B5E')
        self.frame_patenti = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color=self.frame1.detect_color_of_master(master_widget=self.frame1),
                                                    border_width=4, border_color='#565B5E')
        self.frame_and = customtkinter.CTkFrame(master=self.frame1, corner_radius=5, fg_color=self.frame1.detect_color_of_master(master_widget=self.frame1))
        self.frame_checkbox = customtkinter.CTkFrame(master=self.frame_patenti, corner_radius=5, fg_color=self.frame1.detect_color_of_master(master_widget=self.frame1))
        # fine dichiarazione frame utilizzati

        # inzio dichiarazione label
        self.label_nome = customtkinter.CTkLabel(master=self.frame_nome, text="Nome", width=10, height=10,
                                                 text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_cognome = customtkinter.CTkLabel(master=self.frame_cognome, text="Cognome", width=10, height=10,
                                                    text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_indirizzo = customtkinter.CTkLabel(master=self.frame_indirizzo, text="Comune di residenza", width=10,
                                                      height=10,
                                                      text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_spec = customtkinter.CTkLabel(master=self.frame_spec, text="Specializzazioni/lavori", width=10,
                                                 height=10,
                                                 text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_lingue = customtkinter.CTkLabel(master=self.frame_lingue, text="Lingue Conosciute", width=10,
                                                   height=10,
                                                   text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_automunito = customtkinter.CTkLabel(master=self.frame_patenti, text="Automunito", width=10)
        self.label_patenti = customtkinter.CTkLabel(master=self.frame_patenti, text="Patenti possedute")
        self.label_dispoinit = customtkinter.CTkLabel(master=self.frame_dispo_init, text="dal giorno",
                                                      width=10, height=10,
                                                      text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_dispoend = customtkinter.CTkLabel(master=self.frame_dispo_end, text="al giorno", width=10,
                                                     height=10,
                                                     text_font=('Roboto', 7), bg_color='#565B5E')
        self.label_and = customtkinter.CTkLabel(master=self.frame_and, text="Ricerca OR/AND",
                                                text_font=('Roboto', 8))
        # fine dichiarazione label

        # inizio dichiarazione entry
        self.entry_nome = customtkinter.CTkEntry(master=self.frame_nome, placeholder_text="inserisci nome")
        self.entry_cognome = customtkinter.CTkEntry(master=self.frame_cognome, placeholder_text="inserisci cognome")
        self.entry_indirizzo = customtkinter.CTkEntry(master=self.frame_indirizzo,
                                                      placeholder_text="inserisci indirizzo")
        self.entry_spec = customtkinter.CTkEntry(master=self.frame_spec,
                                                 placeholder_text="inserisci specializzazioni e lavori separti da virgola")
        self.entry_lingue = customtkinter.CTkEntry(master=self.frame_lingue,
                                                   placeholder_text="inserisci le lingue conosciute separete da virgola")
        self.entry_dispoinit = customtkinter.CTkEntry(master=self.frame_dispo_init, placeholder_text="gg/mm/yyyy")
        self.entry_dispoend = customtkinter.CTkEntry(master=self.frame_dispo_end, placeholder_text="gg/mm/yyyy")
        # fine dichiarazione entry

        # dichiarazione NON FINITA radiobutton frame patenti
        self.car = customtkinter.CTkSwitch(master=self.frame_patenti, text='', variable=self.auto, onvalue=1,
                                           offvalue=0)

        # dichiarazione NON FINITA checkbox
        self.entry_am = customtkinter.CTkCheckBox(master=self.frame_checkbox, text="AM", onvalue="AM", offvalue="",
                                                  variable=self.AM)
        self.entry_a = customtkinter.CTkCheckBox(master=self.frame_checkbox, text="A", onvalue="A", offvalue="",
                                                 variable=self.A)
        self.entry_b = customtkinter.CTkCheckBox(master=self.frame_checkbox, text="B", onvalue="B", offvalue="",
                                                 variable=self.B)
        self.entry_c = customtkinter.CTkCheckBox(master=self.frame_checkbox, text="C", onvalue="C", offvalue="",
                                                 variable=self.C)

        # switch ricerc ìa incrociata
        self.switch_and = customtkinter.CTkSwitch(master=self.frame_and, onvalue=True, offvalue=False,
                                                  variable=self.switch, text="")
        valori_ricerca = (
            self.entry_nome, self.entry_cognome, self.entry_indirizzo, self.entry_spec, self.entry_lingue,
            self.entry_dispoinit, self.entry_dispoend, self.auto, self.AM,
            self.A, self.B, self.C, self.switch
        )

        # dichiarazione listbox
        self.listbox_result = Listbox(self.frame3, height=27, width=100, font = ('Cambria', '11'))
        # dichiarazione bottone
        self.button_cerca = customtkinter.CTkButton(master=self.frame1, text="Cerca", width=310,
                                                    command=lambda: ControllerRicerca.ControllerRicerca.cerca(
                                                        valori_ricerca, self.listbox_result, self.lavoratori_reg))
        self.button_home = customtkinter.CTkButton(master=self.frame2, text="Torna alla home", fg_color='#32972E', hover_color='#316F2E',
                                                   text_font=('Roboto', 7), width=10, height=5, corner_radius=5,
                                                   command=lambda: ControllerRicerca.ControllerRicerca.back_home(
                                                       self.generalframe,
                                                       master))

        # FINE DICHIARAZIONI

        # disposizione frame generale/1/2/3/4
        self.generalframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame1.grid(row=1, column=0, padx=20, pady=10, ipady=5)
        self.frame2.grid(row=0, column=1, sticky='e')
        self.frame3.grid(row=1, column=1, padx=20)

        # disposizione interna a self.frame1
        self.frame_nome.grid(row=0, column=0, padx=5, ipadx=2.5, ipady=1.5)
        self.label_nome.pack()
        self.entry_nome.pack()

        self.frame_cognome.grid(row=0, column=1, padx=5, pady=10, ipadx=2.5, ipady=1.5)
        self.label_cognome.pack()
        self.entry_cognome.pack()

        self.frame_indirizzo.grid(row=1, column=0, padx=5, pady=10, ipadx=2.5, ipady=1.5)
        self.label_indirizzo.pack()
        self.entry_indirizzo.pack()

        self.frame_spec.grid(row=1, column=1, padx=5, pady=10, ipadx=2.5, ipady=1.5)
        self.label_spec.pack()
        self.entry_spec.pack()

        self.frame_lingue.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=2.5, ipady=1.5)
        self.label_lingue.pack()
        self.entry_lingue.pack()

        self.frame_dispo_init.grid(row=3, column=0, padx=5, pady=10, ipadx=2.5, ipady=1.5)
        self.frame_dispo_end.grid(row=3, column=1, padx=5, pady=10, ipadx=2.5, ipady=1.5)
        self.label_dispoinit.pack()
        self.entry_dispoinit.pack()
        self.label_dispoend.pack()
        self.entry_dispoend.pack()

        self.frame_patenti.grid(row=4, column=0, padx=20, pady=15, columnspan=2, rowspan=2, ipady=10)

        self.frame_and.grid(row=7, column=0, columnspan=2)
        self.label_and.grid(row=0, column=0, sticky='e')
        self.switch_and.grid(row=0, column=1)

        self.label_automunito.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.car.grid(row=0, column=1, sticky='w')

        self.label_patenti.grid(row=1, column=0, columnspan=2)
        self.frame_checkbox.grid(row=2, column=0, columnspan=2, padx=60)
        self.entry_am.grid(row=0, column=0, padx=5)
        self.entry_a.grid(row=0, column=1)
        self.entry_b.grid(row=0, column=2, padx=5)
        self.entry_c.grid(row=0, column=3)

        # disposizione interna a self.frame2
        self.button_cerca.grid(row=6, column=0, columnspan=2, pady=5)
        self.button_home.grid(row=0, column=2, padx=20, pady=5, sticky='s')

        # disposizione interna a self.frame3
        self.listbox_result.pack()
