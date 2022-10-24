from tkinter import *
from view import ViewEmergenza
from model import ContattoEmergenza, CustomException
from tkinter import messagebox


class ControllerEmergenza:
    @staticmethod
    def show(lavoratore, registration_button):
        ViewEmergenza.ViewEmergenza(lavoratore, registration_button)

    @staticmethod
    def registra(lavoratore, anagrafiche, registration_button):
        nome, cognome, telefono, email = anagrafiche
        try:
            tmp = ContattoEmergenza.ContattoEmergenza(email.get().strip(), nome.get().strip(), cognome.get().strip(), telefono.get())
            lavoratore.aggiungiContatto(tmp)
            registration_button.configure(state=NORMAL)

        except CustomException.CampoVuotoException as vuoto:
            messagebox.showerror('Campo vuoto', str(vuoto))
        except CustomException.CampoContieneAlpha as alpha:
            messagebox.showerror('Campo contiene alpha', str(alpha))
        except CustomException.CampoContententeNumeriException as numeri:
            messagebox.showerror('Campo contiene numeri', str(numeri))
        except CustomException.EmailNotValidException:
            messagebox.showerror("Email non valida", "Inserisci un email valida")

        nome.delete(0, END)
        cognome.delete(0, END)
        telefono.delete(0, END)
        email.delete(0, END)

    @staticmethod
    def continua(window):
        window.destroy()
