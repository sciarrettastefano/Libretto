from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry", "Potter", 11, " ","castani",
                "Grifondoro", "civetta", "Expecto Patronum")
mylib = Libretto("Harry", [])

# Ricorda: posso creare l'oggetto voto e "appenderlo" successivamente
# oppure "appendere" alla lista direttamente un oggetto che creo al momento.
# Di seguito si vedono entrambi i metodi

v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)      # primo metodo
v2 = Voto("Babbanologia", 30 , "2022-02-12", False)
mylib.append(v1)
mylib.append(v2)
mylib.append(Voto("Pozioni", 21, "2022-06-14", False))  # secondo metodo --> PREFERIBILE (NON CREO VARIABILI IN GIRO INUTILMENTE)

mylib.calcolaMedia()

votiFiltrati = mylib.getVotiByPunti(21, False)
print(votiFiltrati)      # essendo una lista non stampa con la formattazione definita nella classe da noi
                         # ma con quella creata automaticamente dalla dataclass.
                         # Se stampassimo il singolo voto, es.: votiFiltrati[0], allora verrebbe usata
                         # la nostra implementazione del metodo.

votoTrasfigurazione = mylib.getVotoByName("Trasfigurazione")
if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione)

print("Verifico metodo hasVoto()")
print(mylib.hasVoto(v1))
print(mylib.hasVoto(Voto("Aritmanzia", 30, "2023-07-10", False)))
print(mylib.hasVoto(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)))

print("Verifico metodo hasConflitto()")
print(mylib.hasConflitto(Voto("Difesa contro le arti oscure", 28, "2022-01-30", False)))

print("Verifico metodo append() modificata in Libretto")
mylib.append(Voto("Aritmanzia", 30, "2023-07-10", False))
# mylib.append(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)) darà errore


mylib.append(Voto("Divinazione", 27, "2021-02-08", False))
mylib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))
print("-------------------------------------------------------------")
print("Libretto originario")
print(mylib)
print("-------------------------------------------------------------")

nuovoLib = mylib.creaMigliorato()

print("Libretto migliorato")
print(nuovoLib)

print("-------------------------------------------------------------")
ordinato = mylib.creaLibrettoOrdinatoPerMateria()
print("Libretto ordinato per materia")
print(ordinato)

print("-------------------------------------------------------------")
ordinato2 = mylib.creaLibrettoOrdinatoPerVoto()
print("Libretto ordinato per voto")
print(ordinato2)

print("-------------------------------------------------------------")
print("Libretto a cui ho eliminato i voti inferiori a 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)
