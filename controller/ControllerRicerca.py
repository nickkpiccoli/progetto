from controller import ControllerHome
from view import ViewRicerca
from tkinter import *
from tkinter import messagebox
import customtkinter
from datetime import datetime
from model import CustomException
from csv import reader


class ControllerRicerca:
    @staticmethod
    def show(master):
        ViewRicerca.ViewRicerca(master)

    @staticmethod
    def back_home(frame: customtkinter.CTkFrame, master: customtkinter.CTk):
        frame.destroy()
        ControllerHome.ControllerHome.show(master)

    @staticmethod
    def has_patenti(patenti_richieste, lavoratore):
        if len(patenti_richieste) == 0:
            return True
        else:
            for p in patenti_richieste:
                if p not in lavoratore.getPatenti():
                    return False
            return True

    @staticmethod
    def has_lingue(entry_lingue, lavoratore):
        if entry_lingue.get() != '':
            lingue_ricerca = [item.strip().lower() for item in entry_lingue.get().split(",")]
            getlingue = [item.strip().lower() for item in lavoratore.getLingue()]
            for lingue in lingue_ricerca:
                if lingue not in getlingue:
                    return False
        return True

    @staticmethod
    def has_spec(entry_spec, lavoratore):
        if entry_spec.get() != '':
            spec = [item.strip().lower() for item in entry_spec.get().split(",")]
            getimpieghi = [item.strip().lower() for item in lavoratore.getImpieghi()]
            for s in spec:
                if s not in getimpieghi:
                    return False
        return True

    @staticmethod
    def has_availability(entry_dispoinit, entry_dispoend, lavoratore):
        dispoinit = entry_dispoinit.get()
        dispoend = entry_dispoend.get()

        if dispoinit == '' and dispoend != '':
            fine = datetime.strptime(dispoend, '%d/%m/%Y')
            return lavoratore.getInizioDisp().date() <= fine.date() <= lavoratore.getFineDisp().date()
        elif dispoinit != '' and dispoend == '':
            inizio = datetime.strptime(dispoinit, '%d/%m/%Y')
            return lavoratore.getInizioDisp().date() <= inizio.date() <= lavoratore.getFineDisp().date()
        elif dispoinit == '' and dispoend == '':
            return True
        else:
            inizio = datetime.strptime(dispoinit, '%d/%m/%Y')
            fine = datetime.strptime(dispoend, '%d/%m/%Y')
            return lavoratore.getInizioDisp().date() <= inizio.date() and lavoratore.getFineDisp().date() >= fine.date()

    @staticmethod
    def cerca(valori_ricerca: tuple, listbox_result: Listbox, lavoratori_reg):
        listbox_result.delete(0, END)

        '''entry della view ricerca'''
        entry_nome, entry_cognome, entry_indirizzo, entry_spec, entry_lingue, entry_dispoinit, entry_dispoend, \
        radio_auto, check_AM, check_A, check_B, check_C, switch = valori_ricerca

        '''variabili prima stringa'''
        valoristringa = (entry_nome, entry_cognome, entry_indirizzo, radio_auto, switch)
        entrytupla = [entry_nome, entry_cognome, entry_indirizzo]
        radio_switch = [radio_auto, switch]
        # array di valori 0,1 utilizzato nella formazione della stringa
        arrvalentry = ControllerRicerca.costruiscilista(entrytupla, radio_switch)
        # aray di stringhe per recuperare valori delle entry
        arrentry = ["entry_nome.get().lower().strip()", "entry_cognome.get().lower().strip()",
                    "entry_indirizzo.get().lower().strip()", "radio_auto.get()", "switch.get()"]
        # array di stringhe per recuperare dati del lavoratore
        arrlav = ["lavoratore.getNome().lower().strip()", "lavoratore.getCognome().lower().strip()",
                  "lavoratore.getIndirizzo().lower().strip()",
                  "lavoratore.isAutomunito()"]

        '''variabili stringa filtered'''
        patenti = [check_AM.get(), check_A.get(), check_B.get(), check_C.get()]
        patenti_richieste = [p for p in patenti if p != '']
        valoristringa_filtered = (entry_spec.get(), entry_lingue.get(), patenti_richieste)
        valoristringa_date = (entry_dispoinit.get(), entry_dispoend.get())
        valoristringa_unique = (entry_spec, entry_lingue, patenti_richieste, entry_dispoinit, entry_dispoend, switch)
        arrvalentry_filtered = ControllerRicerca.costruiscilista_filtered(valoristringa_filtered, valoristringa_date)
        arrentry_filtered = ["ControllerRicerca.has_spec(entry_spec,lavoratore)",
                             "ControllerRicerca.has_lingue(entry_lingue, lavoratore)",
                             "ControllerRicerca.has_patenti(patenti_richieste, lavoratore)",
                             "ControllerRicerca.has_availability(entry_dispoinit,entry_dispoend,lavoratore)"]

        '''inizio ricerca'''
        lista = []
        try:

            stringa = ControllerRicerca.creastringa(arrvalentry, arrentry, arrlav, valoristringa)
            stringa_filtered = ControllerRicerca.crestringa_filtered(valoristringa_unique, arrvalentry_filtered, arrentry_filtered)

            print(f"1: {stringa}")
            print(f"2: {stringa_filtered}")

            finalstring = ""
            if stringa != "" and stringa_filtered != "":
                finalstring += stringa + " and " + stringa_filtered if switch.get() else stringa + " or " + stringa_filtered
            elif stringa == "":
                finalstring += stringa_filtered
            else:
                finalstring += stringa

            # proseguimento ricerca con lista filtrata
            if finalstring == "":
                for l in lavoratori_reg.getLavoratori():
                    lista.append(l)
            else:
                for lavoratore in lavoratori_reg.getLavoratori():
                    if eval(finalstring):
                        lista.append(lavoratore)

        except ValueError as ve:
            messagebox.showerror("Errore formato data", str(ve))
        except CustomException.ComuneNonEsistenteException:
            messagebox.showerror("Comune inesistente", "Il comune cercato non esiste in Italia")

        for l in lista:
            listbox_result.insert("end", l.toStringBox())

        ControllerRicerca.reset(valori_ricerca)

    @staticmethod
    def creastringa(arrvalentry, arrentry, arrlav, valori_ricerca):
        entry_nome, entry_cognome, entry_indirizzo, radio_auto, switch = valori_ricerca
        if arrvalentry[2] != 0:
            with open('Data\comuni.csv', 'r') as f:
                csv_reader = reader(f)
                rows = list(csv_reader)
                presente = False
                for element in rows:
                    row = element[0].split(";")
                    if entry_indirizzo.get().lower().strip() == row[0].lower().strip():
                        presente = True
                if not presente:
                    raise CustomException.ComuneNonEsistenteException()

        tmp = ""
        operator = "and" if arrvalentry[len(arrvalentry) - 1] == 1 else "or"
        for i in range(len(arrvalentry) - 1):
            if arrvalentry[i] == 1:
                if radio_auto.get() == 1:
                    tmp += " " + arrentry[i] + " == " + arrlav[i] + " " + operator
                else:
                    if not (arrentry[i] == "radio_auto.get()"):
                        tmp += " " + arrentry[i] + " == " + arrlav[i] + " " + operator

        final = tmp[0:(len(tmp) - 3)] if operator == "and" else tmp[0:(len(tmp) - 2)]
        return final

    @staticmethod
    def crestringa_filtered(valoristringa_unique, arrvalentry_filtered, arrentry):
        entry_spec, entry_lingue, patenti_richieste, entry_dispoinit, entry_dispoend, switch = valoristringa_unique

        tmp = ""
        operator = "and" if switch.get() else "or"
        for i in range(len(arrvalentry_filtered)):
            if arrvalentry_filtered[i] == 1:
                tmp += " " + arrentry[i] + " " + operator

        final = tmp[0:(len(tmp) - 3)] if operator == "and" else tmp[0:(len(tmp) - 2)]
        return final

    @staticmethod
    def costruiscilista(entrytupla, radio_switch):
        tmp = []
        for ele in entrytupla:
            if ele.get() == "":
                tmp.append(0)
            else:
                tmp.append(1)
        tmp.append(0) if radio_switch[0].get() == 0 else tmp.append(1)
        tmp.append(0) if radio_switch[1].get() is False else tmp.append(1)
        return tmp

    @staticmethod
    def costruiscilista_filtered(valoristringa_filtered, valoristringa_date):
        tmp = []

        for ele in valoristringa_filtered:
            if len(ele) == 0:
                tmp.append(0)
            else:
                tmp.append(1)
        check = False

        for ele in valoristringa_date:
            if len(ele) != 0:
                check = True
        tmp.append(1) if check else tmp.append(0)

        return tmp

    @staticmethod
    def reset(valori_ricerca: tuple):
        entry_nome, entry_cognome, entry_indirizzo, entry_spec, entry_lingue, entry_dispoinit, entry_dispoend, \
        radio_auto, check_AM, check_A, check_B, check_C, switch = valori_ricerca

        entry_nome.delete(0, END)
        entry_cognome.delete(0, END)
        entry_indirizzo.delete(0, END)
        entry_spec.delete(0, END)
        entry_lingue.delete(0, END)
        entry_dispoinit.delete(0, END)
        entry_dispoend.delete(0, END)
        radio_auto.set(0)
        check_AM.set('')
        check_A.set('')
        check_B.set('')
        check_C.set('')
        switch.set(False)
