import customtkinter
from tkinter import messagebox
from view import ViewModifyNext
from controller import ControllerHome, ControllerInserimentoModify, ControllerModificaImpiego


class ControllerModifyNext:
    @staticmethod
    def show(master: customtkinter.CTk, lavoratore, lavoratori_reg):
        ViewModifyNext.ViewModifyNext(master, lavoratore, lavoratori_reg)

    @staticmethod
    def inserisci(lavoratori_reg, tmp, listbox_lavori):
        ControllerInserimentoModify.ControllerInserimentoModify.show(lavoratori_reg, tmp, listbox_lavori)

    @staticmethod
    def populate(listbox_lavori, lavoratore):
        listalavori = lavoratore.getLavori()
        for lavoro in listalavori:
            listbox_lavori.insert("end", lavoro.toString())

    @staticmethod
    def modifica(lavoratori_reg, tmp, listbox_selection, listbox_lavori):
        try:
            lista_file = ["email_lavoratore;nomeazienda;ubicazione;datainizio;datafine;retribuzione;impiego\n"]
            selectedwork = tmp.getLavori()[listbox_selection[0]]
            datilavoro = (selectedwork.nomeAzienda(), selectedwork.ubicazione(), selectedwork.getInizioString(), selectedwork.getFineString(),
                              selectedwork.retribuzione(), selectedwork.getImpiego())

            ControllerModificaImpiego.ControllerModificaImpiego.show(lavoratori_reg, tmp, listbox_lavori, datilavoro, listbox_selection[0], lista_file)
        except IndexError:
            messagebox.showwarning('Nessun lavoro selezionato', 'Seleziona un lavoro dalla listbox!')

    @staticmethod
    def back_home(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerHome.ControllerHome.show(master)
