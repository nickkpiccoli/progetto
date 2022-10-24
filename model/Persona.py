from .CustomException import *
import re


class Persona:
    def __init__(self, email: str, nome: str, cognome: str, telefono: str):

        # controllo compilazione campi
        if email == '':
            raise CampoVuotoException("E-mail")

        if nome == '':
            raise CampoVuotoException("Nome")

        if cognome == '':
            raise CampoVuotoException("Cognome")


        # controllo validità campi
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, email)):
            raise EmailNotValidException()

        if any(i.isdigit() for i in nome):
            raise CampoContententeNumeriException("Nome")

        if any(i.isdigit() for i in cognome):
            raise CampoContententeNumeriException("Cognome")

        try:
            if telefono != "":
                int(telefono)
        except ValueError:
            raise CampoContieneAlpha("Telefono")

        self._email = email
        self._nome = nome
        self._cognome = cognome
        self._telefono = telefono

    def getEmail(self) -> str:
        return self._email

    def getNome(self) -> str:
        return self._nome

    def getCognome(self) -> str:
        return self._cognome

    def getTelefono(self) -> str:
        return self._telefono
