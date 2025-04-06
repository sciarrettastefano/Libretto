from dataclasses import dataclass

#E' il nostro DTO --> deve avere i dunder methods __eq__ e __hash__ (gli altri possono esserci ma non sono necessari)
# Ricorda: DTO ha scopo principale di essere un collettore di informazioni

@dataclass(order=True) # questa dataclass non implementa eq, facciamo noi
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

    """def __eq__(self, other):
            return (self.materia == other.materia and
                    self.punteggio == other.punteggio and
                    self.lode == other.lode)"""
    def __eq__(self, other):
        return self.materia == other.materia

    def hash(self):
        hash(self.materia)
