from model import Lavoro
from model import CustomException
from view import ViewModificaImpiego
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ControllerModificaImpiego:
    @staticmethod
    def show(lavoratori_reg, tmp, listbox_lavori, datilavoro, listbox_selection, lista_file):
        ViewModificaImpiego.ViewModificaImpiego(lavoratori_reg, tmp, listbox_lavori, datilavoro, listbox_selection, lista_file)

    @staticmethod
    def mod_job(lavoratori_reg, lavoratore, dati, listbox_lavori, window, listbox_selection, lista_file):
        nome_azienda, ubicazione, data_inizio, data_fine, retribuzione, impiego = dati
        impieghi = [item.strip() for item in impiego.get().split(",")]
        try:

            if relativedelta(datetime.today(), datetime.strptime(data_fine.get(), "%d/%m/%Y")).years > 5:
                raise CustomException.LavoroTroppoVecchioException

            lavoro = Lavoro.Lavoro(nome_azienda.get().strip(), ubicazione.get().strip(), data_inizio.get(), data_fine.get(), retribuzione.get(), impieghi, lavoratore.getDataDiNascitaDate())
            lavoratore.rimuoviLavoro(listbox_selection)
            lavoratore.aggiungiLavoro(lavoro)
            lavoratori_reg.lavoro_obj_to_csv(lavoro, lavoratore)
            with open('Data\lavori.csv', 'w') as f:
                f.truncate(0)
                f.write("email_lavoratore;nomeazienda;ubicazione;datainizio;datafine;retribuzione;impiego\n")
            for lavoratori in lavoratori_reg.getLavoratori():
                for lavori in lavoratori.getLavori():
                    lavoratori_reg.lavoro_obj_to_csv(lavori,lavoratori)

            'svuoto la listbox'
            listbox_lavori.delete(0, END)
            'ripopolo la listbox'
            for lav in lavoratore.getLavori():
                listbox_lavori.insert("end", lav.toString())

            window.destroy()
        except ValueError as va:
            messagebox.showerror("Errore", str(va))
        except CustomException.CampoVuotoException as vuoto:
            messagebox.showerror("Campo vuoto", str(vuoto))
        except CustomException.CampoContententeNumeriException as numeri:
            messagebox.showerror("Campo contiene numeri", str(numeri))
        except CustomException.CampoContieneAlpha as alpha:
            messagebox.showerror("Campo contiene caratteri", str(alpha))
        except CustomException.ActualDateExceedStartDate:
            messagebox.showerror("Data inizio supera data odierna", "La data di inizio supera la data attuale")
        except CustomException.ActualDateExceedEndDate:
            messagebox.showerror("Data fine supera data odierna", "La data di fine supera la data attuale")
        except CustomException.LavoroTroppoVecchioException:
            messagebox.showerror("Lavoro troppo vecchio", "Il lavoro inserito è terminato più di 5 anni fa")
        except CustomException.DataNascitaSuperaDataInizioException:
            messagebox.showerror("Data nascita supera data inizio",
                                 "La data di nascita del lavoratore supera la data di inizio del lavoro")
        except CustomException.DataNascitaSuperaDataFineException:
            messagebox.showerror("Data nascita supera data fine",
                                 "La data di nascita del lavoratore supera la data di fine del lavoro")
        except CustomException.LavoroDaMinorenneException:
            messagebox.showerror("Lavoratore illegale", "Nelle date inserite il lavoratore era minorenne")





