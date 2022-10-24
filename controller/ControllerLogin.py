import customtkinter
import pandas as pd
from tkinter import messagebox
from view import ViewHome, ViewLogin
from controller import ControllerHome


class ControllerLogin:
    @staticmethod
    def show(master: customtkinter.CTk):
        ViewLogin.ViewLogin(master)

    @staticmethod
    def check_account(user: str, password: str, frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        """ Inizializzazione strutture dati """
        personale = pd.read_csv(filepath_or_buffer='Data/Accounts.csv', sep=';')
        tmp = pd.Series(personale['Password'])
        tmp.index = personale['Username']
        accounts = dict(tmp)

        if user == "" or password == "":
            messagebox.showwarning('Credenziali mancanti', 'Inserite le vostre credenziali!')
        elif (user, password) in accounts.items():
            frame.destroy()
            ControllerHome.ControllerHome.show(master)
        else:
            messagebox.showerror('Credenziali invalide', 'Username o password errati!')

