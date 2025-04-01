class Person:
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self._cognome = cognome
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.__prova = None
        self.incantesimo = incantesimo

    def __str__(self):
        return f"Person: {self.nome} {self._cognome} \n"

    @property
    def cognome(self):  # eq. GETTER
        return self._cognome

    @cognome.setter
    def cognome(self, value):  # eq. SETTER
        # CONTROLLI per verificare che value sia compativile con _cognome
        self._cognome = value


class Student(Person):
    #def __init__(self, *args, **kargs):  #per non passare di nuovo tutti i parametri

    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale

    def __str__(self):
        return f"Student: {self.nome} - {self._cognome} - {self.casa} \n "

    def __repr__(self):
        return f"Student(nome, cognome, eta, capelli, occhi, casa, animale)"

    def copy(self):
        return (self.nome, self.cognome, self.eta, self.capelli, self.occhi, self.casa, self.animale, self.incantesimo)

    def prettyPrint(self):
        print("Voglio stampare meglio")

class Teacher(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia
    def __str__(self):
        return f"Teacher: {self.nome} - {self._cognome} - {self.materia} \n "

class Casa:
    def __init__(self, nome, studenti = [] ): # studenti è una lista ---> RICORDA: python non è tipizzato!!
        self.nome = nome
        self.studenti = studenti # posso costruire la lista vuota (e definirla dopo) o con già dei parametri al suo interno

    def addStudente(self, studente):
        self.studenti.append(studente) # --> [ x,x,x [s1, s2]]
        #self.studenti.extend(studente) # --> [ x,x,x, s1, s2 ]

    def __str__(self):
        if len(self.studenti) == 0:
            return "La casa {self.nome} + è vuota."

        mystr = f"\n Lista degli studenti iscritti alla casa {self.nome} \n"
        for s in self.studenti:
            mystr += str(s)

        return mystr

class Scuola:
    def __init__(self, case):
        self.case = case

    def __str__(self):
        mystr = ""
        for c in self.case:
            mystr += str(c)
        return mystr