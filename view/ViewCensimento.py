from tkinter import *
import customtkinter
from controller import ControllerCensimento
from model import LavoratoreDaoImpl


class ViewCensimento:
    def __init__(self, master):
        """ Ottengo lavoratori dal csv """
        self.lavoratori_reg = LavoratoreDaoImpl.LavoratoreDaoImpl()

        """ Variabili per RadioButtons e CheckBoxes"""
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

        self.box_var = StringVar()
        
        """ Frame principale """
        self.frame_censimento = customtkinter.CTkFrame(master=master, corner_radius=5)

        self.back_frame = customtkinter.CTkFrame(master=self.frame_censimento, corner_radius=5,
                                                 fg_color=self.frame_censimento.detect_color_of_master(
                                                     master_widget=self.frame_censimento))
        self.home_btn = customtkinter.CTkButton(master=self.back_frame, text='Torna alla home', text_font=('Roboto', 7),
                                                width=10, height=5, fg_color='#32972E', hover_color='#316F2E',
                                                command=lambda: ControllerCensimento.ControllerCensimento.back_home(self.frame_censimento,
                                                                                               master))

        self.top_left_frame = customtkinter.CTkFrame(master=self.frame_censimento, corner_radius=5)
        self.bottom_left_frame = customtkinter.CTkFrame(master=self.frame_censimento, corner_radius=5)
        self.top_right_frame = customtkinter.CTkFrame(master=self.frame_censimento, corner_radius=5)
        self.bottom_right_frame = customtkinter.CTkFrame(master=self.frame_censimento, corner_radius=5)
        self.reg_button = customtkinter.CTkButton(master=self.frame_censimento, text='Continua', corner_radius=5,
                                                  command=lambda: ControllerCensimento.ControllerCensimento.continua(self.frame_censimento, master, self.lavoratori_reg, anagrafiche))
        self.campiobbl_lbl = customtkinter.CTkLabel(master=self.frame_censimento, text='* campi obbligatori', text_font=('Roboto', 7))

        """ Top left frame: dati anagrafici """
        self.name_frame = customtkinter.CTkFrame(master=self.top_left_frame, corner_radius=5, fg_color='#565B5E')
        self.surname_frame = customtkinter.CTkFrame(master=self.top_left_frame, corner_radius=5, fg_color='#565B5E')
        self.birthday_frame = customtkinter.CTkFrame(master=self.top_left_frame, corner_radius=5, fg_color='#565B5E')
        self.birthplace_frame = customtkinter.CTkFrame(master=self.top_left_frame, corner_radius=5, fg_color='#565B5E')
        self.nationality_frame = customtkinter.CTkFrame(master=self.top_left_frame, corner_radius=5, fg_color='#565B5E')

        # Inserimento del nome
        self.name_lbl = customtkinter.CTkLabel(master=self.name_frame, text='Nome*', width=10, height=10,
                                               text_font=('Roboto', 7), bg_color='#565B5E')
        self.name_entry = customtkinter.CTkEntry(master=self.name_frame, placeholder_text='Inserisci il nome')

        # Inserimento del cognome
        self.surname_lbl = customtkinter.CTkLabel(master=self.surname_frame, text='Cognome*', width=10, height=10,
                                                  text_font=('Roboto', 7), bg_color='#565B5E')
        self.surname_entry = customtkinter.CTkEntry(master=self.surname_frame, placeholder_text='Inserisci il cognome')

        # Inserimento della data di nascita
        self.birthday_lbl = customtkinter.CTkLabel(master=self.birthday_frame, text='Data di nascita*', width=10,
                                                   height=10, text_font=('Roboto', 7), bg_color='#565B5E')
        self.birthday_entry = customtkinter.CTkEntry(master=self.birthday_frame, placeholder_text='gg/mm/aaaa')

        # Inserimento del luogo di nascita
        self.birthplace_lbl = customtkinter.CTkLabel(master=self.birthplace_frame, text='Luogo di nasicta*',
                                                     width=10, height=10, text_font=('Roboto', 7), bg_color='#565B5E')
        self.birthplace_entry = customtkinter.CTkEntry(master=self.birthplace_frame,
                                                       placeholder_text='Inserisci il luogo di nascita')

        # Inserimento della nazionalità
        self.nationality_lbl = customtkinter.CTkLabel(master=self.nationality_frame, text='Nazionalità', width=10,
                                                      height=10, text_font=('Roboto', 7), bg_color='#565B5E')

        with open('Data\stati.csv') as csv_file:
            nazioni = []
            for line in csv_file:
                nazioni.append(line.split('\n')[0])
        self.nationality_box = customtkinter.CTkComboBox(master=self.nationality_frame, values=nazioni, variable=self.box_var)

        """ Bottom left frame: recapito """
        self.address_frame = customtkinter.CTkFrame(master=self.bottom_left_frame, corner_radius=5, fg_color='#565B5E')
        self.phone_frame = customtkinter.CTkFrame(master=self.bottom_left_frame, corner_radius=5, fg_color='#565B5E')
        self.email_frame = customtkinter.CTkFrame(master=self.bottom_left_frame, corner_radius=5, fg_color='#565B5E')

        # Inserimento dell'indirizzo
        self.address_lbl = customtkinter.CTkLabel(master=self.address_frame, text='Comune di residenza*', width=10, height=10,
                                                  text_font=('Roboto', 7), bg_color='#565B5E')
        self.address_entry = customtkinter.CTkEntry(master=self.address_frame, placeholder_text="Inserisci il comune di residenza")

        # Inserimento del numero di telefono
        self.phone_lbl = customtkinter.CTkLabel(master=self.phone_frame, text='Numero di telefono', width=10, height=10,
                                                text_font=('Roboto', 7), bg_color='#565B5E')
        self.phone_entry = customtkinter.CTkEntry(master=self.phone_frame,
                                                  placeholder_text="Inserisci il numero di telefono")

        # Inserimento email
        self.email_lbl = customtkinter.CTkLabel(master=self.email_frame, text='Indirizzo E-Mail*', width=10, height=10,
                                                text_font=('Roboto', 7), bg_color='#565B5E')
        self.email_entry = customtkinter.CTkEntry(master=self.email_frame, placeholder_text="esempio@dominio.it")

        """ Right frame: informazioni """
        self.car_frame = customtkinter.CTkFrame(master=self.top_right_frame, corner_radius=5, fg_color=self.top_right_frame.detect_color_of_master(master_widget=self.top_right_frame))
        self.opt2_frame = customtkinter.CTkFrame(master=self.car_frame, corner_radius=5, fg_color=self.top_right_frame.detect_color_of_master(master_widget=self.top_right_frame))

        # Inserimento delle informazioni lavo
        self.language_frame = customtkinter.CTkFrame(master=self.top_right_frame, corner_radius=5, fg_color='#565B5E')

        # Inserimento delle lingue conosciute
        self.language_lbl = customtkinter.CTkLabel(master=self.language_frame, text='Lingue conosciute*', width=10,
                                                   height=10, text_font=('Roboto', 7), bg_color='#565B5E')
        self.language_entry = customtkinter.CTkEntry(master=self.language_frame,
                                                     placeholder_text='es. Italiano, Inglese, Spagnolo', width=250)

        # Inserimento informazioni sul trasporto/patenti
        self.car_lbl = customtkinter.CTkLabel(master=self.car_frame, text='Automunito')

        self.car = customtkinter.CTkSwitch(master=self.car_frame, text='', variable=self.auto, onvalue=1, offvalue=0)

        self.license_lbl = customtkinter.CTkLabel(master=self.car_frame, text='Patenti (obbligatorie se automunito)')
        self.license_AM = customtkinter.CTkCheckBox(master=self.opt2_frame, text='AM', variable=self.AM, onvalue='AM',
                                                    offvalue='')
        self.license_A = customtkinter.CTkCheckBox(master=self.opt2_frame, text='A', variable=self.A, onvalue='A',
                                                   offvalue='')
        self.license_B = customtkinter.CTkCheckBox(master=self.opt2_frame, text='B', variable=self.B, onvalue='B',
                                                   offvalue='')
        self.license_C = customtkinter.CTkCheckBox(master=self.opt2_frame, text='C', variable=self.C, onvalue='C',
                                                   offvalue='')

        # Inserimento informazioni sulla disponibilità
        self.start_frame = customtkinter.CTkFrame(master=self.bottom_right_frame, corner_radius=5, fg_color='#565B5E')
        self.end_frame = customtkinter.CTkFrame(master=self.bottom_right_frame, corner_radius=5, fg_color='#565B5E')
        self.place_frame = customtkinter.CTkFrame(master=self.bottom_right_frame, corner_radius=5, fg_color='#565B5E')

        self.start_lbl = customtkinter.CTkLabel(master=self.start_frame, text='Disponibile dal giorno*', width=10, height=10,
                                                text_font=('Roboto', 7), bg_color='#565B5E')
        self.start_entry = customtkinter.CTkEntry(master=self.start_frame, placeholder_text="gg/mm/aaaa")
        self.end_lbl = customtkinter.CTkLabel(master=self.end_frame, text='al giorno*', width=10, height=10,
                                              text_font=('Roboto', 7), bg_color='#565B5E')
        self.end_entry = customtkinter.CTkEntry(master=self.end_frame, placeholder_text="gg/mm/aaaa")
        self.place_lbl = customtkinter.CTkLabel(master=self.place_frame, text='in zona*', width=10, height=10,
                                                text_font=('Roboto', 7), bg_color='#565B5E')
        self.place_entry = customtkinter.CTkEntry(master=self.place_frame, placeholder_text="Inserisci una zona")

        anagrafiche = (self.name_entry, self.surname_entry, self.birthday_entry, self.birthplace_entry,
                       self.nationality_box, self.address_entry, self.phone_entry, self.email_entry,
                       self.language_entry,
                       self.auto, self.AM, self.A, self.B, self.C, self.start_entry, self.end_entry, self.place_entry)

        """ Disposizione a schermo """
        # Frame principale
        self.frame_censimento.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Frame di raccoglimento + bottone per tornare alla home + bottone logout + bottone di regstrazione
        self.back_frame.grid(row=0, column=0, columnspan=2, ipadx=10, sticky='e')
        self.home_btn.grid(row=0, column=0, pady=5, sticky='s')
        self.top_left_frame.grid(row=1, column=0, padx=10, pady=10)
        self.bottom_left_frame.grid(row=2, column=0)
        self.top_right_frame.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5)
        self.bottom_right_frame.grid(row=2, column=1, padx=10, pady=10)
        self.reg_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.campiobbl_lbl.grid(row=4, column=0, columnspan=2, sticky='e')

        # Inserimento dati anagrafici
        self.name_frame.grid(row=0, column=0, ipadx=2.5, ipady=1.5, padx=10, pady=10)
        self.surname_frame.grid(row=0, column=1, ipadx=2.5, ipady=1.5, padx=10, pady=10)
        self.birthday_frame.grid(row=1, column=0, ipadx=2.5, ipady=1.5)
        self.birthplace_frame.grid(row=1, column=1, ipadx=2.5, ipady=1.5)
        self.nationality_frame.grid(row=2, column=0, columnspan=2, ipadx=2.5, ipady=1.5, padx=10, pady=10)

        self.name_lbl.pack()
        self.name_entry.pack()
        self.surname_lbl.pack()
        self.surname_entry.pack()
        self.birthday_lbl.pack()
        self.birthday_entry.pack()
        self.birthplace_lbl.pack()
        self.birthplace_entry.pack()
        self.nationality_lbl.pack()
        self.nationality_box.pack()

        # Inserimento dei dati di recapito
        self.address_frame.grid(row=0, column=0, ipadx=2.5, ipady=1.5, padx=10, pady=5)
        self.phone_frame.grid(row=0, column=1, ipadx=2.5, ipady=1.5, padx=10, pady=5)
        self.email_frame.grid(row=1, column=0, columnspan=2, ipadx=2.5, ipady=1.5, pady=5)

        self.address_lbl.pack()
        self.address_entry.pack()
        self.phone_lbl.pack()
        self.phone_entry.pack()
        self.email_lbl.pack()
        self.email_entry.pack()

        # Inseriment delle informazioni lavorative/trasporto
        self.language_frame.pack(ipadx=2.5, ipady=1.5, pady=10)
        self.car_frame.pack(pady=10, padx=55)

        self.language_lbl.pack()
        self.language_entry.pack()

        self.car_lbl.grid(row=0, column=0)
        self.car.grid(row=0, column=1, sticky='w')
        self.license_lbl.grid(row=1, column=0, columnspan=2)
        self.opt2_frame.grid(row=2, column=0, columnspan=2)
        self.license_AM.grid(row=0, column=0, padx=5)
        self.license_A.grid(row=0, column=1)
        self.license_B.grid(row=0, column=2, padx=5)
        self.license_C.grid(row=0, column=3)

        self.start_frame.grid(row=0, column=0, ipadx=2.5, ipady=1.5, padx=10, pady=5)
        self.end_frame.grid(row=0, column=1, ipadx=2.5, ipady=1.5, padx=10, pady=5)
        self.place_frame.grid(row=1, column=0, columnspan=2, ipadx=2.5, ipady=1.5, pady=5)

        self.start_lbl.pack()
        self.start_entry.pack()
        self.end_lbl.pack()
        self.end_entry.pack()
        self.place_lbl.pack()
        self.place_entry.pack()
