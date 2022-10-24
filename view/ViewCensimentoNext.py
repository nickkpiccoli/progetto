import customtkinter
from tkinter import *
from controller import ControllerCensimentoNext


class ViewCensimentoNext:
    def __init__(self, master: customtkinter.CTk, lavoratori_reg, lavoratore):
        self.main_frame = customtkinter.CTkFrame(master=master, corner_radius=5)
        self.top_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=5,
                                                fg_color=self.main_frame.detect_color_of_master(
                                                    master_widget=self.main_frame))
        self.options_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=5)

        self.home_btn = customtkinter.CTkButton(master=self.top_frame, text='Torna alla Home', corner_radius=5,
                                                fg_color='#32972E', hover_color='#316F2E', text_font=('Roboto', 7),
                                                width=10, height=5, command=lambda: ControllerCensimentoNext.ControllerCensimentoNext.back_home(self.main_frame, master))
        self.job_btn = customtkinter.CTkButton(master=self.options_frame, text='Aggiungi lavoro', corner_radius=5, width=190,
                                               command=lambda: ControllerCensimentoNext.ControllerCensimentoNext.add_job(
                                                   lavoratore))

        self.emergency_btn = customtkinter.CTkButton(master=self.options_frame, text="Aggiungi contatto d'emergenza",
                                                     corner_radius=5,
                                                     command=lambda:
                                                     ControllerCensimentoNext.ControllerCensimentoNext.add_emergency(
                                                         lavoratore, self.registration_btn))

        self.info_lbl = customtkinter.CTkLabel(master=self.main_frame, text="Inserisci almeno un contatto d'emergenza\n"
                                                                            "per completare la registrazione",
                                               text_font=('Roboto', 7))

        self.registration_btn = customtkinter.CTkButton(master=self.main_frame, text='Termina Registrazione',
                                                        corner_radius=5, state=DISABLED,
                                                        command=lambda: ControllerCensimentoNext.ControllerCensimentoNext.finish(
                                                            self.main_frame,
                                                            master,
                                                            lavoratori_reg,
                                                            lavoratore))

        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.top_frame.grid(row=0, column=0, sticky='e')
        self.options_frame.grid(row=1, column=0, padx=10, ipadx=10, ipady=10)
        self.info_lbl.grid(row=2, column=0)
        self.registration_btn.grid(row=3, column=0, pady=10)

        self.home_btn.pack(padx=10, pady=5)

        self.job_btn.pack(pady=10)
        self.emergency_btn.pack()
