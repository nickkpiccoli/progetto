class UnderAgeException(Exception):
    pass


class BirthExceedActualDate(Exception):
    pass


class BirthExceedStartDate(Exception):
    pass


class StartDateExceedEndDate(Exception):
    pass


class ActualDateExceedStartDate(Exception):
    pass


class ActualDateExceedEndDate(Exception):
    pass


class ComuneNonEsistenteException(Exception):
    pass


class ZonaNonEsistenteException(Exception):
    pass


class EmailNotValidException(Exception):
    pass


class AutomunitoSenzaPatenteException(Exception):
    pass


class LavoroTroppoVecchioException(Exception):
    pass


class CampoVuotoException(Exception):
    def __init__(self, campo):
        self.campo = campo
        self.message = f'Il campo {campo} è vuoto'
        super().__init__(self.message)


class CampoContententeNumeriException(Exception):
    def __init__(self, campo):
        self.message = f'Il campo {campo} contiene caratteri numerici'
        super().__init__(self.message)


class CampoContieneAlpha(Exception):
    def __init__(self, campo):
        self.message = f'Il campo {campo} contiene caratteri che non sono numeri'
        super().__init__(self.message)


class DataNascitaSuperaDataInizioException(Exception):
    pass


class DataNascitaSuperaDataFineException(Exception):
    pass


class LavoroDaMinorenneException(Exception):
    pass


class LavoratoreGiaEsistenteException(Exception):
    pass
