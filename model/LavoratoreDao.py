from abc import ABC, abstractmethod
from model import Lavoratore


class LavoratoreDao(ABC):

    @abstractmethod
    def getLavoratori(self):
        pass

    @abstractmethod
    def getLavoratore(self, mail: str):
        pass

    @abstractmethod
    def addLavoratore(self, lavoratore: Lavoratore):
        pass

    @abstractmethod
    def lavoratore_csv_to_obj(self):
        pass

    @abstractmethod
    def emergenza_csv_to_obj(self, emailcont):
        pass

    @abstractmethod
    def lavori_csv_to_obj(self, emailcont, datanascita):
        pass

    @abstractmethod
    def lavoratori_obj_to_csv(self, lavoratore):
        pass

    @abstractmethod
    def emergenza_obj_to_csv(self, lavoratore):
        pass

    @abstractmethod
    def lavori_obj_to_csv(self, lavoratore):
        pass

    @abstractmethod
    def lavoro_obj_to_csv(self, lavoro, lavoratore):
        pass

    @abstractmethod
    def getlavori_worker(self, mail):
        pass