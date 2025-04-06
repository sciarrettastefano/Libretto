# CONTROLLER ---> GESTISCE LE HANDLE TRA VIEW E MODEL, FA DA TRAMITE TRA VIEW E MODEL
from scuola import Student
from UI.view import View
from voto.model import Libretto
import flet as ft
from voto.voto import Voto

# Struttura MVC DA QUI...
class Controller:
    def __init__(self, v: View):
        self._view = v  # il controller sa chi è la view
# ...A QUI
        self._student = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri",
                                casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
        self._model = Libretto(self._student, [])
        # self.fillLibretto() <-- non lo usiamo più, usiamo il dao dal modello per "caricarci" gli esami


    def handleAggiungi(self, e):
        # Raccoglie tutte le ifno per cerare un nuovo voto
        # Crea un oggetto Voto
        # Fa append sul libretto
        nome = self._view._txtInNome.value
        if nome == "":
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Il campo nome non può essere vuoto", color="red"))
            self._view._page.update()
            return

        punti = self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Selezionare un voto", color="red"))
            self._view._page.update()
            return

        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Selezionare una data", color="red"))
            self._view._page.update()
            return

        if punti == "30L":
            self._model.append(Voto(nome, 30, f"{data.year}-{data.month}-{data.day}", True))
        else:
            self._model.append(Voto(nome, int(punti), f"{data.year}-{data.month}-{data.day}", False))
        self._view._txtOut.controls.append(
            ft.Text("Voto correttamente aggiunto", color="green"))
        self._view._page.update()

    def handleStampa(self, e):   # ricorda il secondo input, necessario perchè la funzione è legata ad un veento su u npulsante
        self._view._txtOut.controls.append(
            ft.Text(str(self._model), color="black")
        )
        self._view._page.update()

    def getStudent(self):
        """
        Restituisce informazioni dello studente, usando
        il __str__ dello Student
        :return:
        """
        return str(self._student)

    # Non è competenza del controller fare l'azione di riempire il libretto
    """def fillLibretto(self):
        # Voti di esempio
        self._model.append(Voto("Difesa contro le arti oscure", 25, "2022-01-30", False))
        self._model.append(Voto("Babbanologia", 30, "2022-02-12", False))
        self._model.append(Voto("Pozioni", 21, "2022-06-14", False))
        self._model.append(Voto("Trasfigurazione", 21, "2022-06-14", False))"""




