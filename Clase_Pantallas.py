import Clase_Figuras
import pygame as pg

#Variables en mayúsuclas signifcan que son variables constantes
ANCHO = 800
ALTO = 600

class Partida:

    def __init__(self):

        # Para inicializar pygame
        pg.init()

        # Para crear pantalla base y asignar un nombre
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong :D !!!")
        
        # Definir tasa de refresco de nuestro bucle de fotogramas (fotograma por segundo = FPS)
        self.tasarefresco = pg.time.Clock()

        # Para crear pelota y raquetas con parámetros mínimos requeridos; de los otros parámetros toma los valores por default
        self.pelota = Clase_Figuras.Pelota(ANCHO/2, ALTO/2, vy = 2)
        self.raqueta1 = Clase_Figuras.Raqueta(10, ALTO/2 - 50, vy = 5)
        self.raqueta2 = Clase_Figuras.Raqueta(ANCHO - 20 - 10, ALTO/2 - 50, vy = 2)
    
    def bucle_fotograma(self):
        
        # Bucle para mantener la pantalla activa mientras se desarrolla el código
        game_over = False

        while not game_over:
            
            # La función tick permite conocer los milisegundos que tarda entre cada fotograma
            # Cuando se incluye parámetro se está definiendo la cantidad máxima de fotogramas a imprimir en un segundo
            milisegundos = self.tasarefresco.tick(100)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            # Método para mover raqueta si las teclas definidas están presionadas
            self.raqueta1.mover(pg.K_w, pg.K_s, ALTO)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN, ANCHO)

            # Método para mover pelota y que rebote cuando choque con las raquetas o asigne puntos si toca el borde del campo de juego
            self.pelota.mover(self.pantalla_principal, self.raqueta1, self.raqueta2)

            # Método para asignar color a la pantalla y línea del medio
            self.pantalla_principal.fill((0, 128, 94))
            for i in range(10, 601, 60):
                pg.draw.line(self.pantalla_principal, (255, 255, 255), (400, i), (400, i + 40), 10)

            # Método para dibujar pelota titulo jugador, pelota de juego y raquetas
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            # Método para dibujar y mostrar lo parametrizado anteriormente
            self.mostrar_jugador()
            self.pelota.marcador(self.pantalla_principal)
            pg.display.flip()
        
        # Para inicializar pygame
        pg.quit()

    def mostrar_jugador(self):
        # Métodos para crear superficie para cada jugador
        jugador1 = pg.font.Font(None, 50).render("Jugador 1", 1, (255,255,255))
        jugador2 = pg.font.Font(None, 50).render("Jugador 2", 1, (255,255,255))      
        
        # Método para dibujar y mostrar lo parametrizado anteriormente
        self.pantalla_principal.blit(jugador1, (120,10))
        self.pantalla_principal.blit(jugador2, (520,10))