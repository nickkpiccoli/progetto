import customtkinter
from datetime import datetime
from view import ViewCensimento
from model import Lavoratore, CustomException
from tkinter import messagebox
from controller import ControllerHome, ControllerCensimentoNext


class ControllerCensimento:
    @staticmethod
    def show(master: customtkinter.CTk):
        ViewCensimento.ViewCensimento(master)

    @staticmethod
    def back_home(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerHome.ControllerHome.show(master)

    @staticmethod
    def continua(frame, master, lavoratori_reg, valori):
        # unpacking tupla
        nome, cognome, compleanno, luogonascita, nazionalita, indirizzo, telefono, \
        email, lingue, auto, AM, A, B, C, datainizio, datafine, zona = valori

        try:
            listalingue = [item.strip() for item in lingue.get().split(",")]
            listapatenti = [AM.get(), A.get(), B.get(), C.get()]
            listapatenti_possedute = [p for p in listapatenti if p != '']
            listazone = [item.strip() for item in zona.get().split(",")]

            for lavoratore_reg in lavoratori_reg.getLavoratori():
                if email.get() == lavoratore_reg.getEmail():
                    raise CustomException.LavoratoreGiaEsistenteException

            if datetime.today() > datetime.strptime(datainizio.get(), "%d/%m/%Y"):
                raise CustomException.ActualDateExceedStartDate()

            if datetime.today() >= datetime.strptime(datafine.get(), "%d/%m/%Y"):
                raise CustomException.ActualDateExceedEndDate()

            tmp = Lavoratore.Lavoratore(nome.get().strip(), cognome.get().strip(), compleanno.get(), luogonascita.get().strip(), nazionalita.get(),
                                        indirizzo.get().strip(), telefono.get(),
                                        email.get().strip(), listalingue, auto.get(), listapatenti_possedute, datainizio.get(),
                                        datafine.get(), listazone, [], [])

            frame.destroy()
            ControllerCensimentoNext.ControllerCensimentoNext.show(master, lavoratori_reg, tmp)
        except ValueError:
            messagebox.showerror('Formato data invalido', 'Formato data invalido!\nFormato corretto: dd/mm/yyyy')

        except CustomException.LavoratoreGiaEsistenteException:
            messagebox.showerror('Lavoratore esistente', 'La mail inserita appartiene ad\nun lavatore registrato!')

        except CustomException.UnderAgeException:
            messagebox.showerror('Lavoratore minorenne', 'Lavoratore minore di 16 anni!')

        except CustomException.BirthExceedActualDate:
            messagebox.showerror('Data di nascita invalida', 'Data di nascita eccede data odierna!')

        except CustomException.BirthExceedStartDate:
            messagebox.showerror('Data di nascita invalida', "Data di nascita eccede data di inizio disponibilità")

        except CustomException.StartDateExceedEndDate:
            messagebox.showerror('Periodo di disponibilità non valido',
                                 "Data di fine disponibilità precede data di inizio disponibilità!")

        except CustomException.ActualDateExceedStartDate:
            messagebox.showerror('Periodo di disponibilità non valido',
                                 "Data odierna eccede data di inizio disponibilità!")

        except CustomException.ActualDateExceedEndDate:
            messagebox.showerror('Lavoratore minorenne', "Data odierna eccede data di fine disponibilità!")

        except CustomException.ComuneNonEsistenteException:
            messagebox.showerror('Comune di residenza non valido', 'Il comune inserito non esiste tra i comuni italiani')

        except CustomException.EmailNotValidException:
            messagebox.showerror('Email non valida', 'La mail inserita non è valida')

        except CustomException.AutomunitoSenzaPatenteException:
            messagebox.showerror('Automunito senza patente', 'Inserire almeno una patente se il lavoratore è automunito')

        except CustomException.ZonaNonEsistenteException:
            messagebox.showerror('Zona disponibilità inesistente',
                                 'È presente un comune di disponibilità non esistente tra i comuni italiani')

        except CustomException.CampoVuotoException as vuoto:
            messagebox.showerror('Campo vuoto', str(vuoto))

        except CustomException.CampoContententeNumeriException as numeri:
            messagebox.showerror('Campo contiene numeri', str(numeri))

        except CustomException.CampoContieneAlpha as alpha:
            messagebox.showerror('Telefono contiene alpa', str(alpha))
