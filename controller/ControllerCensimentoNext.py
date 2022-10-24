import customtkinter
from view import ViewCensimentoNext
from controller import ControllerHome, ControllerEmergenza, ControllerInserimentoImpiego


class ControllerCensimentoNext:
    @staticmethod
    def show(master: customtkinter.CTk, lavoratori_reg, lavoratore):
        ViewCensimentoNext.ViewCensimentoNext(master, lavoratori_reg, lavoratore)

    @staticmethod
    def back_home(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerHome.ControllerHome.show(master)

    @staticmethod
    def add_emergency(lavoratore, registration_button):
        ControllerEmergenza.ControllerEmergenza.show(lavoratore, registration_button)

    @staticmethod
    def add_job(lavoratore):
        ControllerInserimentoImpiego.ControllerInserimentoImpiego.show(lavoratore)

    @staticmethod
    def finish(frame, master, lavoratori_reg, lavoratore):
        lavoratori_reg.addLavoratore(lavoratore)
        lavoratori_reg.lavoratori_obj_to_csv(lavoratore)
        lavoratori_reg.lavori_obj_to_csv(lavoratore)
        lavoratori_reg.emergenza_obj_to_csv(lavoratore)
        for i in lavoratore.getContattiEmergenza():
            print("test: " + i.toString())
        frame.destroy()
        ControllerHome.ControllerHome.show(master)
