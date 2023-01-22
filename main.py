from Clase_Pantallas import Partida, Menu, Resultado

menu = Menu()
pantalla = menu.bucle_pantalla()

if pantalla == "Nuevo juego":   
    juego = Partida() #Creamos objeto de clase Partida
    pantalla = juego.bucle_fotograma()

if pantalla == "Resultado":   
    result = Resultado(juego.contador1, juego.contador2)
    pantalla = result.bucle_pantalla()