import Clase_Figuras
import pygame as pg
from tools import * #Para utilizar la clase inicializadora en donde están lo comun

class Partida:

    def __init__(self):

        # Para crear pantalla base y asignar un nombre
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong :D !!!")
        
        # Definir tasa de refresco de nuestro bucle de fotogramas (fotograma por segundo = FPS)
        self.tasarefresco = pg.time.Clock()

        # Para crear pelota y raquetas con parámetros mínimos requeridos; de los otros parámetros toma los valores por default
        self.pelota = Clase_Figuras.Pelota(ANCHO/2, ALTO/2, vy = 2)
        self.raqueta1 = Clase_Figuras.Raqueta(10, ALTO/2 - 50, vy = 5)
        self.raqueta2 = Clase_Figuras.Raqueta(ANCHO - 20 - 10, ALTO/2 - 50, vy = 2)

        #Crear variables para marcadores
        self.contador1 = 0
        self.contador2 = 0
        self.punto_para = 0

        #self.Font a utilizar en programa
        self.font = pg.font.Font("fonts/PressStart2P-Regular.ttf", 20)

        self.temporizador = 15000
    
    def bucle_fotograma(self):
        
        # Bucle para mantener la pantalla activa mientras se desarrolla el código
        game_over = False

        while not game_over:
            
            # La función tick permite conocer los milisegundos que tarda entre cada fotograma
            # Cuando se incluye parámetro se está definiendo la cantidad máxima de fotogramas a imprimir en un segundo
            salto_tiempo = self.tasarefresco.tick(400) #1000/100 = cantidad de fotogramas por segundo

            # Sirve para asignar un tiempo de juego y una vez alcanzado el mismo cierra el programa
            self.temporizador -= salto_tiempo
            if self.temporizador//1000 <= 0:
                game_over = True
                #return "Resultado"

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            # Método para mover raqueta si las teclas definidas están presionadas
            self.raqueta1.mover(pg.K_w, pg.K_s, ALTO)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN, ALTO)

            # Método para mover pelota y que rebote cuando choque con las raquetas. Devuelve left o right si toca el borde del campo de juego para asignar puntos.
            self.punto_para = self.pelota.mover(self.pantalla_principal, self.raqueta1, self.raqueta2)

            # Método para asignar color a la pantalla y línea del medio
            self.pantalla_principal.fill(self.fijar_fondo())
            for i in range(60, 601, 60):
                pg.draw.line(self.pantalla_principal, BLANCO, (400, i), (400, i + 40), 10)

            # Método para dibujar pelota, raquetas, jugadores, marcadores y temporizador
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugador()
            cronometro = self.font.render(str(self.temporizador//1000)+"s", 1, BLANCO)
            self.pantalla_principal.blit(cronometro, (380,20))

            # Método para dibujar y mostrar lo parametrizado anteriormente
            pg.display.flip()
        
        # Para finalizar pygame
        return "Resultado"
        pg.quit()

    def mostrar_jugador(self):
        
        # Asigna puntos
        if self.punto_para == "right":
            self.contador1 += 1
        elif self.punto_para == "left":
            self.contador2 += 1

        # Métodos para crear superficie para cada jugador y su marcador
        jugador1 = self.font.render("Jugador 1", 1, BLANCO)
        marcador1 = self.font.render(str(self.contador1), 1, BLANCO)
        jugador2 = self.font.render("Jugador 2", 1, BLANCO)    
        marcador2 = self.font.render(str(self.contador2), 1, BLANCO)

        # Método para dibujar y mostrar lo parametrizado anteriormente
        self.pantalla_principal.blit(jugador1, (110,20))
        self.pantalla_principal.blit(marcador1, (180,60))
        self.pantalla_principal.blit(jugador2, (510,20))
        self.pantalla_principal.blit(marcador2, (580,60))

    def fijar_fondo(self):
        if self.temporizador//1000 > 10:
            return VERDE
        elif self.temporizador//1000 > 5:
            return NEGRO
        else:
            if (self.temporizador//400)%2 != 0:
                return ROJO
            else:
                return NEGRO

class Menu:
    def __init__(self):

        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Menu Pong")
        self.tasarefresco = pg.time.Clock()
        
        self.imagenFondo = pg.image.load("images/portada.jpg")
        self.font = pg.font.Font("fonts/PressStart2P-Regular.ttf", 20)
    
    def bucle_pantalla(self):
        game_over = False

        while not game_over:

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.pantalla_principal.blit(self.imagenFondo, (0,0))
            nuevoJuego = self.font.render("Presione ENTER para jugar", 1, BLANCO)
            self.pantalla_principal.blit(nuevoJuego, (150, 200))
            nuevoJuego = self.font.render("Presione R para ver puntuaciones", 1, BLANCO)
            self.pantalla_principal.blit(nuevoJuego, (80,300))

            if pg.key.get_pressed()[pg.K_RETURN]:
                game_over = True
                return "Nuevo juego"

            if pg.key.get_pressed()[pg.K_r]:
                game_over = True
                return "Score"

            pg.display.flip()
        
        pg.quit()

class Resultado:
    def __init__(self):

        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Resultado Pong")
        self.tasarefresco = pg.time.Clock()
        
        self.contador1 = 0
        self.contador2 = 0
        
        self.imagenFondo = pg.image.load("images/portada.jpg")
        self.font = pg.font.Font("fonts/PressStart2P-Regular.ttf", 20)
    
    def bucle_pantalla(self):

        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.pantalla_principal.blit(self.imagenFondo, (0,0))

            # Métodos para crear superficie para cada jugador y su marcador
            jugador1 = self.font.render("Jugador 1", 1, BLANCO)
            marcador1 = self.font.render(str(self.contador1), 1, BLANCO)
            jugador2 = self.font.render("Jugador 2", 1, BLANCO)    
            marcador2 = self.font.render(str(self.contador2), 1, BLANCO)

            # Método para dibujar y mostrar lo parametrizado anteriormente
            self.pantalla_principal.blit(jugador1, (110, 160))
            self.pantalla_principal.blit(marcador1, (180, 200))
            self.pantalla_principal.blit(jugador2, (510, 160))
            self.pantalla_principal.blit(marcador2, (580, 200))
            
            if self.contador1 < self.contador2:
                resultado1 = self.font.render("El GANADOR del juego fue..." , 1, BLANCO)
                resultado2 = self.font.render("el JUGADOR 2" , 1, BLANCO)
            elif self.contador1 > self.contador2:
                resultado1 = self.font.render("El GANADOR del juego fue..." , 1, BLANCO)
                resultado2 = self.font.render("el JUGADOR 1" , 1, BLANCO)
            else:
                resultado1 = self.font.render("El juego terminó en EMPATE" , 1, BLANCO)
                resultado2 = self.font.render("" , 1, BLANCO)
            
            self.pantalla_principal.blit(resultado1, (140, 300))
            self.pantalla_principal.blit(resultado2, (300, 340))

            pg.display.flip()
        
        pg.quit()

    def recibirResultado(self, marcador1, marcador2):
        self.contador1 = marcador1
        self.contador2 = marcador2


class Score:
    
    def __init__(self):

        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Tabla de posiciones Pong")
        self.tasarefresco = pg.time.Clock()
        self.imagenFondo = pg.image.load("images/portada.jpg")
        self.font = pg.font.Font("fonts/PressStart2P-Regular.ttf", 20)
    
    def bucle_pantalla(self):

        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.pantalla_principal.blit(self.imagenFondo, (0,0))

            pg.display.flip()
        
        pg.quit()
