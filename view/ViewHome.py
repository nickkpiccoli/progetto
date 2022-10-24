from tkinter import *
import customtkinter
from controller import ControllerHome


class ViewHome:
    def __init__(self, master):
        self.home_frame = customtkinter.CTkFrame(master=master, corner_radius=5)

        self.top_frame = customtkinter.CTkFrame(master=self.home_frame, corner_radius=5,
                                                fg_color=self.home_frame.detect_color_of_master(
                                                    master_widget=self.home_frame))

        self.logout_btn = customtkinter.CTkButton(master=self.top_frame, text='Logout', text_font=('Roboto', 7),
                                                  width=10, height=5, corner_radius=5, fg_color='#F25252',
                                                  hover_color='#B52222', command=lambda: ControllerHome.ControllerHome.logout(self.home_frame, master))

        self.options_frame = customtkinter.CTkFrame(master=self.home_frame, corner_radius=5)

        self.add_btn = customtkinter.CTkButton(master=self.options_frame, text='Registra lavoratori', width=155,
                                               corner_radius=5, command=lambda: ControllerHome.ControllerHome.add_worker(self.home_frame, master))

        self.search_btn = customtkinter.CTkButton(master=self.options_frame, text='Ricerca lavoratori', width=155,
                                                  corner_radius=5, command=lambda: ControllerHome.ControllerHome.search(self.home_frame, master))

        self.mod_btn = customtkinter.CTkButton(master=self.options_frame, text='Aggiungi/Modifica lavori',
                                               corner_radius=5, command=lambda: ControllerHome.ControllerHome.modify(self.home_frame, master))

        self.home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.top_frame.grid(row=0, column=0, sticky='e')
        self.options_frame.grid(row=1, column=0, ipadx=10)

        self.logout_btn.pack(padx=5, pady=5)

        self.add_btn.pack(pady=10)
        self.search_btn.pack(padx=10)
        self.mod_btn.pack(pady=10)
