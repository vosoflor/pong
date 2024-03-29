import Clase_Figuras
import pygame as pg

# Para inicializar pygame
pg.init()

# Para crear pantalla base y asignar un nombre
pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong :D !!!")

# Definir tasa de refresco de nuestro bucle de fotogramas (fotograma por segundo = FPS)
cronometro = pg.time.Clock()

# Para crear pelota y raquetas con parámetros mínimos requeridos;
# de los otros parámetros toma los valores por default
pelota = Clase_Figuras.Pelota(pantalla_principal.get_width()/2, pantalla_principal.get_height()/2)
raqueta1 = Clase_Figuras.Raqueta(10, 250)
raqueta2 = Clase_Figuras.Raqueta(800-10-20, 250)

# Bucle para mantener la pantalla activa mientras se desarrolla el código
game_over = False

while not game_over:
    
    # La función tick permite conocer los milisegundos que tarda entre cada fotograma
    # Cuando se incluye parámetro se está definiendo la cantidad máxima de fotogramas a imprimir en un segundo
    milisegundos = cronometro.tick(100)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    
    # Método para mover raqueta si las teclas definidas están presionadas
    raqueta1.mover(pg.K_w, pg.K_s, pantalla_principal.get_height())
    raqueta2.mover(pg.K_UP, pg.K_DOWN, pantalla_principal.get_height())

    # Método para mover pelota y que rebote cuando choque con las raquetas o asigne puntos si toca el borde del campo de juego
    pelota.mover(pantalla_principal, raqueta1, raqueta2)

    # Método para asignar color a la pantalla y línea del medio
    pantalla_principal.fill((0, 128, 94))
    for i in range(20,601,100):
        pg.draw.line(pantalla_principal, (255,255,255), (400,i), (400,i+60), 10)

    # Método para crear pelota de juego y raquetas
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    # Método para dibujar y mostrar lo parametrizado anteriormente
    pelota.marcador(pantalla_principal)
    pg.display.flip()

pg.quit()