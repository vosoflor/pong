from Clase_Pantallas import *

class SceneController():
    
    def __init__(self) -> None:
        self.menu = Menu()
        self.juego = Partida()
        self.resultado = Resultado()
        self.records = Score()

    def start(self):
        
        seguir = True
        cerrar = False

        while seguir:
            cerrar = self.menu.bucle_pantalla()
            if cerrar:
                break
            cerrar = self.juego.bucle_fotograma()
            if cerrar:
                break
            self.resultado.recibirResultado(self.juego.contador1, self.juego.contador2)
            cerrar = self.resultado.bucle_pantalla()
            if cerrar:
                break