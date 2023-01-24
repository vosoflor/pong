from Clase_Pantallas import Partida, Menu, Resultado, Score
from scene_controller import SceneController
'''
menu = Menu()
pantalla = menu.bucle_pantalla()

if pantalla == "Nuevo juego":   
    juego = Partida() #Creamos objeto de clase Partida
    pantalla = juego.bucle_pantalla()

if pantalla == "Resultado":   
    result = Resultado(juego.contador1, juego.contador2)
    pantalla = result.bucle_pantalla()

if pantalla == "Score":
    score = Score()
    score.bucle_pantalla()
'''

inicio = SceneController()
inicio.start()