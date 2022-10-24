from datetime import datetime
from model import CustomException
from dateutil.relativedelta import relativedelta


class Lavoro:
    def __init__(self, nomeazienda: str, ubicazione: str, datainizio: str, datafine: str, retribuzione: float,
                 impiego: list, datanascita):
        self._nomeazienda = nomeazienda
        self._ubicazione = ubicazione
        self._datainizio = datetime.strptime(datainizio, "%d/%m/%Y")
        self._datafine = datetime.strptime(datafine, "%d/%m/%Y")
        self._retribuzione = retribuzione
        self._impiego = impiego

        if nomeazienda == "":
            raise CustomException.CampoVuotoException("Nome Azienda")

        if ubicazione == "":
            raise CustomException.CampoVuotoException("Ubicazione")

        if retribuzione == "":
            raise CustomException.CampoVuotoException("Retribuzione")

        if impiego == "":
            raise CustomException.CampoVuotoException("Impieghi")

        if any(i.isdigit() for i in ubicazione):
            raise CustomException.CampoContententeNumeriException("Ubicazione")

        try:
            float(retribuzione)
        except ValueError:
            raise CustomException.CampoContieneAlpha("Retribuzione")

        if datetime.strptime(datainizio, "%d/%m/%Y") > datetime.strptime(datafine, "%d/%m/%Y"):
            raise CustomException.StartDateExceedEndDate

        if datetime.strptime(datainizio, "%d/%m/%Y") > datetime.today():
            raise CustomException.ActualDateExceedStartDate

        if datetime.strptime(datafine, "%d/%m/%Y") > datetime.today():
            raise CustomException.ActualDateExceedEndDate

        if datetime.strptime(datainizio, "%d/%m/%Y") < datanascita:
            raise CustomException.DataNascitaSuperaDataInizioException

        if datetime.strptime(datafine, "%d/%m/%Y") < datanascita:
            raise CustomException.DataNascitaSuperaDataFineException

        if relativedelta(datetime.strptime(datainizio, "%d/%m/%Y"), datanascita).years < 16:
            raise CustomException.LavoroDaMinorenneException

    def nomeAzienda(self):
        return self._nomeazienda

    def ubicazione(self):
        return self._ubicazione

    def dataInizio(self):
        return self._datainizio

    def getInizioString(self):
        return self._datainizio.strftime("%d/%m/%Y")

    def dataFine(self):
        return self._datafine

    def getFineString(self):
        return self._datafine.strftime("%d/%m/%Y")

    def retribuzione(self):
        return self._retribuzione

    def getImpiego(self):
        return self._impiego

    def toString(self):
        return f"\nPresso: {self._nomeazienda} Ubicazione: {self._ubicazione} Dal: {self._datainizio.date()} Al: {self.dataFine().date()} " \
               f"Retribuzione lorda: {self._retribuzione}€ Impiego: {self._impiego}"


if __name__ == '__main__':
    pensione = Lavoro("ciccioS.p.a", "cornedo", "23/05/2020", "24/09/2023", 3423.32, "bagnino")
    print(pensione.toString())
