from voto import Voto, Libretto

v1 = Voto("Trasfigurazioni", 24, "2022-02-14", False)
v2 = Voto("Pozioni", 30, "2022-02-18", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-02-23", False)
print(v1)

mylib = Libretto("Harry", [v1, v2])
print(mylib)
mylib.append(v3)
print(mylib)

# un modo per testare un modulo