# MODEL ---> CONTIENE LA LOGICA E LE FUNZIONALITà DEL PROGRAMMA, COMUNICA CON CONTROLLER

import flet as ft
from UI.controller import Controller
from UI.view import View

# Struttura MVC DA QUI...
def main(page: ft.Page):
    v = View(page) # gli "diamo" page perchè sarà view che si occupa di modificare la pagina (view si occupa di grafica)
    c = Controller(v)
    v.setController(c)
    v.loadInterface()
# ...A QUI

ft.app(target=main)
