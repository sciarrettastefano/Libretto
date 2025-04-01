import operator
from dataclasses import dataclass
import flet

@dataclass(eq= False) # questa dataclass non implementa eq, facciamo noi
class Voto:
    materia: str
    punteggio: int   # i tipi presunti che scriviamo sono ignorati in compilazione
    data: str        # ma li scriviamo perchè l'editor ci segnala il presunto errore di tipo ( prima del run )
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    def copy(self):
        """
        Crea una copia del voto
        :return: istanza della classe Voto
        """
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    def hash(self):
        pass

    """def __eq__(self, other):
        return (self.materia == other.materia and
                self.punteggio == other.punteggio and
                self.lode == other.lode)"""

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto):
        # self.voti.append(voto)   # principio del DUCK TYPING: vorremmo che Libretto si comportasse come una lista
                                 # perciò chiamiamo i suoi metodi proprio come quelli di una lista
                                 # ---> li trattiamo allo stesso modo
        if (self.hasConflitto(voto) is False and self.hasVoto(voto) is False):
            self.voti.append(voto)
        else:
            raise ValueError("Voto già esistente")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario}\n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)    # vado avanti con la caratterizzazione del Libretto come fosse una lista
                                 # len ha la stessa funzione sia nelle liste sia in Libretto

    def calcolaMedia(self):
        """
        restituisce la media dei voti attualmente presenti nel libretto
        :return: valore numerico della media, oppure ValueError nel caso la lista fosse vuota
        """

        # media = sommaVoti / numeroEsami
        # numeroEsami = len(self.voti)

        voti = [v.punteggio for v in self.voti]
        # modo veloce per fare:
        # voti = []
        # for v1 in self.voti:
        #   voti.append(v1.punteggio)

        if len(self.voti) == 0:
            raise ValueError("Attenzione. lista esami vuota.")
        return sum(voti) / len(voti)
        # si può anche fare (importando math):
        # return math.mean(voti)

    def getVotiByPunti(self, punti, lode):  # metodo che "filtra" i risultati, lo useremo sempre in futuro, punto 2 es
        """
        restituisce una lista di esami con punteggio uguale a punti (e lode se applicabile)
        :param punti: variabile di tipo intero che rappresenta il punteggio da cercare
        :param lode: variabile booleana che indica se cosiderare la lode
        :return: lista di voti secondo i parametri inseriti
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)
        # si può ridurre in una riga come visto sopra e con una lambda function (vedremo più avanti)
        return votiFiltrati

    def getVotoByName(self, nome):  # simile al metodo precedente, restituisce il singolo voto dell'insegnamento, punto 3 es
        """
        restituisce un oggetto Voto il cui campo materia è uguale al nome in input
        :param nome: stringa che indica il nome della materia dell'esame da ricercare
        :return: oggetto di tipo Voto oppure None in caso di voto non trovato
        """
        for v in self.voti:
            if v.materia == nome:
                return v

    def hasVoto(self, voto): # punto 4 esercizio
        """
        Il metodo controlla se il libretto contiene già il voto.
        Il voto è considerato uguale ad un altro se hanno stesso campo materia
        e stesso campo voto (punteggio + lode)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: True se il voto è già presente nel libretto, False altrimenti
        """
        for v in self.voti:
            if (v.materia == voto.materia and
                v.punteggio == voto.punteggio and
                v.lode == voto.lode):
                return True
        return False
        # altro modo era if v == voto:
        # ma presenterebbe problemi se voti uguali
        # non fossero la stessa istanza
        # Si potrebbe ovviare al problema implementando un __eq__ come si vete sopra
        # nella classe Voto, ma porterebbe dei problemi nelle verifiche con ==
        # per controllare se due istanze siano uguali
        # (si dovrebbe verificare ogni campo uguale nel __eq__)

    def hasConflitto(self, voto):
        """
        Il metodo controlla che il voto "voto" non crei un conflitto con i voti già
        presente nel libretto. Consideriamo due voti in conflitto quando hanno lo
        stesso campo materia e ma diversa coppia (punteggio, lode)
        :param voto: istanza della classe Voto
        :return: True se voto è in conflitto, False altrimenti
        """
        for v in self.voti:
            if (v.materia == voto.materia and
                not(v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        """
        Crea una nuova copia del libretto
        :return: istanza della classe Libretto
        """
        nuovo = Libretto(self.proprietario, [])
        for v in self.voti:
            nuovo.append(v.copy())
        return nuovo

    def creaMigliorato(self): # metodo di "factoring", crea nuove istanze della classe
        """
        Crea nuovo oggetto Libretto, in cui i voti sono migliorati secondo
        la seguente logica:
        se il voto è >= 18 e < 24 aggiungo +1
        se il voto è >= 24 e < 29 aggiungo +2
        se il voto è 29 aggiungo +1
        se il voto è 30 rimane 30
        :return: nuovo Libretto migliorato
        """
        nuovo = self.copy() # copy() per non andare poi a modificare i voti "originali"
        # In questo modo le due copie del libretto sono affettivamente indipendenti,
        # cosa che non avviene se copiassi le stesse istanze in due liste diverse
        # rendendole praticamente la stessa lista

        # modifico i voti in nuovo
        for v in nuovo.voti:
            if 18<= v.punteggio <= 24:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 29:
                v.punteggio += 2
            elif 29 <= v.punteggio <= 29:
                v.punteggio = 30
        return nuovo

    def sortByMateria(self):
        """
        Il metodo ordina la lista di voti nel libretto per materia (alfabeticamente)
        :return:
        """
        # self.voti.sort(key=estraiMateria)
        self.voti.sort(key=operator.attrgetter("materia")) #voto.materia



    # Per il punto 8 dell'esercizio:
    #Opzione 1: creo due metodi di stampa che ordinano e poi stampano
    #Opzione 2: creo due metodi che ordinano la lista di self e poi un unico metodo di stampa
    #Opzione 3: creo due metodi che si fanno una copia (deep) autonoma della lista, la ordinano e la restituiscono
    #           poi un altro metodo si occuperà di stampare le nuove liste
    #Opzione 4: creo una shallow copy di self.voti e ordino quella

    def creaLibrettoOrdinatoPerMateria(self):
        """
        Crea nuovo oggetto Libretto, e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibrettoOrdinatoPerVoto(self):
        """
        Crea nuovo oggetto Libretto, e lo ordina per voto
        :return: nuova istanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v: (v.punteggio, v.lode), reverse=True) # lambda per funzioni in line che servono solo qua
        return nuovo
        # NB: True è maggiore di False

    def cancellaInferiori(self, punteggio):
        """
        Questo metodo agisce sul librtto corrente eliminando tutti i voti
        inferiori al parametro punteggio
        :param punteggio: intero indicante valore minimo accettato
        :return:
        """
        # modo 1
        """for i in range(len(self.voti)):
            if self.voti[i].punteggio < punteggio:
                self.voti.pop(i)""" # problema con il contatore e gli indici della lista
                                 # --> alcuni elementi non vengono valutati
        # modo 2
        """for v in self.voti:
            if v.punteggio < punteggio:
                self.voti.remove(v)""" # stesso problema del modo 1 nello scorrere la lista

        #NB: il problema non sorge se cicliamo le liste dal fondo

        # modo 3: ragiono al contrario, aggiungo ad una nuova lista i voti >= voto in ingresso
        """nuovo = []
        for v in self.voti:
            if v.punteggio >= punteggio:
                nuovo.append(v)
        self.voti = nuovo""" # per aggiornare effettivamente la lista

        nuovo = [v for v in self.voti if v.punteggio >= punteggio] # <---- equivalente a sopra


def estraiMateria(voto): # equivalente alla lambda function (key =) lambda v: v.materia
    """
    Questo metodo restituisce il campo materia dell'oggetto voto
    :param voto: istanza classe Voto
    :return: stringa rappresentante il nome della materia
    """
    return voto.materia


# metto il codice in una funzione per non creare eventuali probemi di nomi di variabili (NAME POLLUTION)
def testVoto():
    print("Ho usato in maniera standalone")  # cioè da solo, al fine di testare il modulo
    v1 = Voto("Trasfigurazioni", 24, "2022-02-14", False)
    v2 = Voto("Pozioni", 30, "2022-02-18", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-02-23", False)
    print(v1)

    mylib = Libretto("Harry", [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)
    print(flet.Text(mylib))

if __name__ == "__main__":
    testVoto()

    # altro modo per testare un modulo come lo usassi in modo indipendente
    # se eseguo un file che importa voto, __name__ vale come voto,
    # se eseguo il file stesso da solo, la variabile __name__ vale __main__ ed eseguirà le istruzioni
    # per testare il modulo
    # succede così per le proprietà stesse di __name__ (che appare tra l'altro nelle
    # variabili speciali quando "runno", se volessi controllarne il valore)