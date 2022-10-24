from model import Lavoro, CustomException
from view import ViewInserimentoImpiego
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter import messagebox


class ControllerInserimentoImpiego:
    @staticmethod
    def show(lavoratore):
        ViewInserimentoImpiego.ViewInserimentoImpiego(lavoratore)

    @staticmethod
    def add_job(lavoratore, dati, window):
        nome_azienda, ubicazione, data_inizio, data_fine, retribuzione, impiego = dati
        impieghi = [item.strip() for item in impiego.get().split(",")]
        try:
            if relativedelta(datetime.today(), datetime.strptime(data_fine.get(), "%d/%m/%Y")).years > 5:
                raise CustomException.LavoroTroppoVecchioException

            lavoro = Lavoro.Lavoro(nome_azienda.get().strip(), ubicazione.get().strip(), data_inizio.get(), data_fine.get(), retribuzione.get(), impieghi, lavoratore.getDataDiNascitaDate())
            lavoratore.aggiungiLavoro(lavoro)
            window.destroy()
        except ValueError as ve:
            messagebox.showerror('Formato data invalido', str(ve))
        except CustomException.CampoContententeNumeriException as numeri:
            messagebox.showerror("Campo contiene numeri", str(numeri))
        except CustomException.CampoVuotoException as vuoto:
            messagebox.showerror('Campo vuoto', str(vuoto))
        except CustomException.CampoContieneAlpha as alpha:
            messagebox.showerror('Campo contiene alpha', str(alpha))
        except CustomException.StartDateExceedEndDate:
            messagebox.showerror('Data inizio supera data fine', 'La data di inizio supera la data di fine')
        except CustomException.ActualDateExceedStartDate:
            messagebox.showerror('Data inizio supera data attuale', 'La data di inizio supera la data attuale')
        except CustomException.ActualDateExceedEndDate:
            messagebox.showerror('Data fine supera data attuale', 'La data di fine supera la data attuale')
        except CustomException.LavoroTroppoVecchioException:
            messagebox.showerror('Lavoro tropppo vecchio', 'Il lavoro inserito è terminato più di 5 anni fa')
        except CustomException.DataNascitaSuperaDataInizioException:
            messagebox.showerror('Data nascita supera inizio', 'Il lavoro inserito inizia prima della nascita del lavoratore')
        except CustomException.DataNascitaSuperaDataFineException:
            messagebox.showerror('Data nascita supera fine', 'Il lavoro inserito termina dopo la nascita del lavoratore')
        except CustomException.LavoroDaMinorenneException:
            messagebox.showerror('Lavoratore minorenne', 'Nella data di inizio inserita il lavoratore era minore di 16 anni')


