from Clase_Pantallas import *

class SceneController():
    
    def __init__(self) -> None:
        self.menu = Menu()
        self.juego = Partida()
        self.resultado = Resultado()
        self.records = Score()

    def start(self):
        self.menu.bucle_pantalla()
        self.juego.bucle_fotograma()
        self.resultado.recibirResultado(self.juego.contador1, self.juego.contador2)
        self.resultado.bucle_pantalla()
        self.records.bucle_pantalla