from .Lavoratore import Lavoratore
from .ContattoEmergenza import ContattoEmergenza
from .LavoratoreDao import LavoratoreDao
from .Lavoro import Lavoro
from datetime import datetime
from dateutil.relativedelta import relativedelta
from csv import reader


class LavoratoreDaoImpl(LavoratoreDao):
    def __init__(self):
        self.lavoratori = self.lavoratore_csv_to_obj()

    def getLavoratori(self):
        return self.lavoratori

    def getLavoratore(self, mail: str):
        for lavoratore in self.lavoratori:
            if lavoratore.getEmail() == mail:
                return lavoratore

    def addLavoratore(self, lavoratore: Lavoratore):
        self.lavoratori.append(lavoratore)

    def lavoratore_csv_to_obj(self):
        # read csv file as a list of lists
        with open('Data\lavoratori.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            count = 0
            lista = []
            for i in range(len(rows)):
                if count != 0:
                    row = rows[i][0].split(";")
                    nome = row[0].strip()
                    cognome = row[1].strip()
                    datanascita = row[2]
                    luogonascita = row[3].strip()
                    nazionalita = row[4]
                    indirizzo = row[5].strip()
                    telefono = row[6]
                    email = row[7].strip()
                    lingue = row[8]
                    auto = row[9]
                    patenti = row[10]
                    startdisp = row[11]
                    enddisp = row[12]
                    zonadisp = row[13]
                    lingue_list = [item.strip() for item in lingue.split('-')]
                    patenti_list = patenti.split('-')
                    zonadisp_list = [item.strip() for item in zonadisp.split('-')]

                    lista.append(Lavoratore(nome, cognome, datanascita, luogonascita,
                                            nazionalita, indirizzo, telefono, email, lingue_list,
                                            int(auto), patenti_list, startdisp, enddisp, zonadisp_list,
                                            self.lavori_csv_to_obj(email, datetime.strptime(datanascita, "%d/%m/%Y")),
                                            self.emergenza_csv_to_obj(email)))
                count += 1

            return lista

            # csv to variable

    def emergenza_csv_to_obj(self, emailcont):
        with open('Data\contattiemergenza.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            lista = []
            for ele in rows:
                row = ele[0].split(';')
                # print(row)
                if emailcont in row:
                    nome = row[1].strip()
                    cognome = row[2].strip()
                    telefono = row[3]
                    email = row[4].strip()
                    lista.append(ContattoEmergenza(email, nome, cognome, telefono))
            return lista

    def lavori_csv_to_obj(self, emailcont, datanascita):
        with open('Data\lavori.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            lista = []
            for ele in rows:
                row = ele[0].split(';')
                # print(row)
                if emailcont in row:
                    nomeazienda = row[1].strip()
                    ubicazione = row[2].strip()
                    datainizio = row[3]
                    datafine = row[4]
                    retribuzione = row[5]
                    impiego = row[6]
                    impiego_list = [item.strip() for item in impiego.split('-')]
                    if relativedelta(datetime.today(), datetime.strptime(datafine, "%d/%m/%Y")).years <= 5:
                        lista.append(Lavoro(nomeazienda, ubicazione, datainizio,
                                            datafine, retribuzione, impiego_list, datanascita))
            return lista

    def lavoratori_obj_to_csv(self, lavoratore):
        with open('Data\lavoratori.csv', 'a') as read_obj:
            stringa = "\n" + lavoratore.getNome() + ';' + lavoratore.getCognome() + ';' + lavoratore.getDataDiNascitaString() + ';' + \
                      lavoratore.getLuogoDiNascita() + ';' + lavoratore.getNazionalita() + ';' + lavoratore.getIndirizzo() + ';' + lavoratore.getTelefono() + ';' + \
                      lavoratore.getEmail() + ';' + ('-'.join(lavoratore.getLingue())) + ';' + str(
                lavoratore.isAutomunito()) + ';' + ('-'.join(lavoratore.getPatenti())) \
                      + ';' + lavoratore.getInizioDispString() + ';' + lavoratore.getFineDispString() + ';' + (
                          '-'.join(lavoratore.getZonaDisp()))

            read_obj.write(stringa)

    def emergenza_obj_to_csv(self, lavoratore):
        with open('Data\contattiemergenza.csv', 'a') as read_obj:
            stringa = ""
            for contatto in lavoratore.getContattiEmergenza():
                stringa += "\n" + lavoratore.getEmail() + ";" + contatto.tocsv()
            read_obj.write(stringa)

    def lavori_obj_to_csv(self, lavoratore):
        with open('Data\lavori.csv', 'r') as f:
            first = True if len(f.readlines()) == 1 else False
        with open('Data\lavori.csv', 'a') as read_obj:
            stringa = ""
            for lavoro in lavoratore.getLavori():
                if first:
                    stringa += "\n" + lavoratore.getEmail() + ';' + lavoro.nomeAzienda() + ';' + lavoro.ubicazione() + ';' + \
                               lavoro.getInizioString() + ';' + lavoro.getFineString() + ';' + lavoro.retribuzione() + ';' + (
                                   '-'.join(lavoro.getImpiego())) + "\n"
                    first = False
                else:
                    stringa += lavoratore.getEmail() + ';' + lavoro.nomeAzienda() + ';' + lavoro.ubicazione() + ';' + \
                               lavoro.getInizioString() + ';' + lavoro.getFineString() + ';' + lavoro.retribuzione() + ';' + (
                                   '-'.join(lavoro.getImpiego())) + "\n"
            read_obj.write(stringa)

    def lavoro_obj_to_csv(self, lavoro, lavoratore):
        with open('Data\lavori.csv', 'r') as f:
            first = True if len(f.readlines()) == 1 else False
        with open('Data\lavori.csv', 'a') as read_obj:
            stringa = ""
            if first:
                stringa += lavoratore.getEmail() + ';' + lavoro.nomeAzienda() + ';' + lavoro.ubicazione() + ';' + \
                           lavoro.getInizioString() + ';' + lavoro.getFineString() + ';' + lavoro.retribuzione() + ';' + (
                               '-'.join(lavoro.getImpiego())) + "\n"
            else:
                stringa += lavoratore.getEmail() + ';' + lavoro.nomeAzienda() + ';' + lavoro.ubicazione() + ';' + \
                           lavoro.getInizioString() + ';' + lavoro.getFineString() + ';' + lavoro.retribuzione() + ';' + (
                               '-'.join(lavoro.getImpiego())) + "\n"

            read_obj.write(stringa)

    def getlavori_worker(self, mail):
        tmp = None
        for lavoratore in self.lavoratori:
            if lavoratore.getEmail() == mail:
                tmp = lavoratore
        lista = tmp.getLavori()
        return lista


'''
    if __name__ == '__main__':
        l1 = Lavoratore('fabio.orco@gmail.com', 'Fabio', 'Orco', '393917170019', '02/03/2000', 'Bassano del Grappa', 'Italiana', 'Via Pietro Storti', [], [], True, ['A', 'B'], '24/05/2022', '24/09/2022', [], [])
        l2 = Lavoratore("fabiolatroia@puttana", "orazio","pene", "3423245","03/02/2014","valdagno","tedeesco","caccaculo",[],[],True,["a","b"], "04/02/2020", "17/11/2019", [], [])
    
        squadra = LavoratoreDaoImpl()
        squadra.addLavoratore(l1)
        squadra.addLavoratore(l2)
        print(squadra.getLavoratore("fabio.orco@gmail.com").getNome())
'''
