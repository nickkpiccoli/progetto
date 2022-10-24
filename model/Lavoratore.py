from .Persona import Persona
from .CustomException import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from csv import reader


class Lavoratore(Persona):

    def __init__(
            self,
            nome: str,
            cognome: str,
            data_di_nascita: str,
            luogo_di_nascita: str,
            nazionalita: str,
            indirizzo: str,
            telefono: str,
            email: str,
            lingue: list,
            auto: int,
            patenti: list,
            start_disp: str,
            end_disp: str,
            zona_disp: list,
            lavori: list,
            contatti_emergenza: list
    ):
        super().__init__(email, nome, cognome, telefono)

        ''' Controlli sui parametri '''

        if luogo_di_nascita == "":
            raise CampoVuotoException("Luogo di nascita")

        if any(i.isdigit() for i in luogo_di_nascita):
            raise CampoContententeNumeriException("Luogo di nascita")

        if lingue == "":
            raise CampoVuotoException("Lingue")

        if any(i.isdigit() for i in lingue):
            raise CampoContententeNumeriException("Lingue")

        if zona_disp == "":
            raise CampoVuotoException("Zone disponibilità")

        if any(i.isdigit() for i in zona_disp):
            raise CampoContententeNumeriException("Zone disponibilità")

        if relativedelta(datetime.today(), datetime.strptime(data_di_nascita, "%d/%m/%Y")).years < 16:
            raise UnderAgeException()

        if datetime.strptime(start_disp, "%d/%m/%Y") > datetime.strptime(end_disp, "%d/%m/%Y"):
            raise StartDateExceedEndDate()

        if datetime.strptime(data_di_nascita, "%d/%m/%Y") >= datetime.today():
            raise BirthExceedActualDate()

        if datetime.strptime(data_di_nascita, "%d/%m/%Y") >= datetime.strptime(start_disp, "%d/%m/%Y"):
            raise BirthExceedStartDate()

        #controllo comune di residenza
        with open('Data\comuni.csv', 'r') as f:
            csv_reader = reader(f)
            rows = list(csv_reader)
            presente = False
            for element in rows:
                row = element[0].split(";")
                if indirizzo.lower().strip() == row[0].lower().strip():
                    presente = True

        if presente is False:
            raise ComuneNonEsistenteException

        #controllo patente se automunito
        if auto == 1:
            if len(patenti) == 0:
                raise AutomunitoSenzaPatenteException()

        #controllo zone disponibilità comuni italiani
        with open('Data\comuni.csv', 'r') as f:
            csv_reader = reader(f)
            rows = list(csv_reader)
            listafalse = [False for _ in range(len(zona_disp))]
            count = 0
            for element in zona_disp:
                for entry in rows:
                    row = entry[0].split(';')
                    if element.lower().strip() == row[0].lower().strip():
                        listafalse[count] = True
                        count += 1
            if False in listafalse:
                raise ZonaNonEsistenteException()

        self._data_di_nascita = datetime.strptime(data_di_nascita, "%d/%m/%Y")
        self._luogo_di_nascita = luogo_di_nascita
        self._nazionalita = nazionalita
        self._indirizzo = indirizzo
        self._lingue = lingue
        self._auto = auto
        self._patenti = patenti
        self._start_disp = datetime.strptime(start_disp, "%d/%m/%Y")
        self._end_disp = datetime.strptime(end_disp, "%d/%m/%Y")
        self._zona_disp = zona_disp
        self._lavori = lavori
        self._contatti_emergenza = contatti_emergenza

    def getDataDiNascitaDate(self):
        return self._data_di_nascita

    def getDataDiNascitaString(self):
        return self._data_di_nascita.strftime("%d/%m/%Y")

    def getLuogoDiNascita(self):
        return self._luogo_di_nascita

    def getNazionalita(self):
        return self._nazionalita

    def getIndirizzo(self):
        return self._indirizzo

    def getLingue(self):
        return self._lingue

    def isAutomunito(self):
        return self._auto

    def getPatenti(self):
        return self._patenti

    def getInizioDisp(self):
        return self._start_disp

    def getFineDisp(self):
        return self._end_disp

    def getInizioDispString(self):
        return self._start_disp.strftime("%d/%m/%Y")

    def getFineDispString(self):
        return self._end_disp.strftime("%d/%m/%Y")

    def getZonaDisp(self):
        return self._zona_disp

    def getLavori(self):
        return self._lavori

    def getImpieghi(self):
        lista = []
        for lavoro in self.getLavori():
            lista += lavoro.getImpiego()
        return lista

    def getContattiEmergenza(self):
        return self._contatti_emergenza

    def modificaLavoro(self):
        pass

    def aggiungiLavoro(self, lavoro):
        self._lavori.append(lavoro)

    def rimuoviLavoro(self, index):
        self._lavori.pop(index)

    def aggiungiContatto(self, contatto):
        self._contatti_emergenza.append(contatto)

    def toString(self):
        stringa = ""
        for contact in self._contatti_emergenza:
            stringa += contact.toString() + " "
        return f"Nome:{self._nome}, Cognome:{self._cognome}, email{self._email}, telefono{self._telefono}," \
               f" nato il: {self._data_di_nascita.date()}, a: {self._luogo_di_nascita}, contatti: {stringa}"

    def toStringBox(self):
        stringa = ""
        munito = ""
        munito = "si" if self.isAutomunito() else "no"

        if self.getTelefono() == "":
            return f"Nome: {self._nome}, Cognome: {self._cognome}, Indirizzo email: {self.getEmail()}"
        else:
            return f"Nome: {self._nome}, Cognome: {self._cognome}, Indirizzo email: {self.getEmail()}, Telefono: {self.getTelefono()}"

