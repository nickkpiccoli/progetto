from view import ViewModifyNext
from view import ViewModify
from controller import ControllerHome, ControllerModifyNext
import customtkinter
from tkinter import messagebox


class ControllerModify:
    @staticmethod
    def show(master: customtkinter.CTk):
        ViewModify.ViewModify(master)

    @staticmethod
    def back_home(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerHome.ControllerHome.show(master)

    @staticmethod
    def procedi(frame: customtkinter.CTkFrame, master: customtkinter.CTk, lavoratori_reg, entry_mail):
        tmp = None
        for lavoratore in lavoratori_reg.getLavoratori():
            if lavoratore.getEmail() == entry_mail:
                frame.destroy()
                tmp = lavoratore
                ControllerModifyNext.ControllerModifyNext.show(master, tmp, lavoratori_reg)

        if entry_mail == '':
            messagebox.showwarning("Campo non compilato", "Inserire un'e-mail!")
        elif tmp is None:
            messagebox.showerror('Lavoratore non esistente', 'Lavoratore non esistente!')
