import customtkinter
from view import ViewHome
from controller import ControllerLogin, ControllerRicerca, ControllerCensimento, ControllerModify


class ControllerHome:
    @staticmethod
    def show(master: customtkinter.CTk):
        ViewHome.ViewHome(master)

    @staticmethod
    def logout(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerLogin.ControllerLogin.show(master)

    @staticmethod
    def add_worker(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerCensimento.ControllerCensimento.show(master)

    @staticmethod
    def search(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerRicerca.ControllerRicerca.show(master)

    @staticmethod
    def modify(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerModify.ControllerModify.show(master)

