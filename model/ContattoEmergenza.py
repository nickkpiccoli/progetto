from .Persona import Persona
from .CustomException import *


class ContattoEmergenza(Persona):

    def __init__(self, email: str, nome: str, cognome: str, telefono: str):

        if telefono == '':
            raise CampoVuotoException("Telfono")

        super().__init__(email, nome, cognome, telefono)

    def toString(self):
        return f"nome: {self._nome} cognome:{self._cognome} mail: {self._email} telefono: {self._telefono}"

    def tocsv(self):
        return f"{self._nome};{self._cognome};{self._telefono};{self._email}"
