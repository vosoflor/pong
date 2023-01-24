from Clase_Pantallas import *

class SceneController():
    
    def __init__(self) -> None:

        # Para crear pantalla base y asignar un nombre
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        # Definir tasa de refresco de nuestro bucle de fotogramas (fotograma por segundo = FPS)
        self.tasarefresco = pg.time.Clock()

        self.pantallas = [Menu(self.pantalla_principal, self.tasarefresco), Partida(self.pantalla_principal, self.tasarefresco),
        Resultado(self.pantalla_principal, self.tasarefresco), Score(self.pantalla_principal, self.tasarefresco)]

    def start(self):
        
        seguir = True
        cerrar = False
        indice = 0

        while seguir:

            self.pantallas[2].recibirResultado(self.pantallas[1].contador1, self.pantallas[1].contador2)
            cerrar = self.pantallas[indice].bucle_pantalla()
            if cerrar:
                break

            if indice < 3:
                indice += 1
            else:
                indice = 0