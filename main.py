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
    milisegundos = cronometro.tick(300)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    
    # Método para mover raqueta si las teclas definidas están presionadas
    raqueta1.mover(pg.K_w, pg.K_s, pantalla_principal.get_height())
    raqueta2.mover(pg.K_UP, pg.K_DOWN, pantalla_principal.get_height())

    # Método para mover pelota y que rebote dentro del campo de juego
    pelota.mover(pantalla_principal.get_height(), pantalla_principal.get_width())

    # Métodos para crear superficie de marcadores para cada jugador
    marcador1 = pg.font.Font(None, 100).render(str(pelota.contador_derecha), 1, (255,255,255))
    marcador2 = pg.font.Font(None, 100).render(str(pelota.contador_izquierda), 1, (255,255,255))

    # Método para asignar color a la pantalla y línea del medio
    pantalla_principal.fill((0, 128, 94))
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), 2)
    
    # Método para crear pelota de juego y raquetas
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    # Método para dibujar y mostrar lo parametrizado anteriormente
    pantalla_principal.blit(marcador1, (150,10))
    pantalla_principal.blit(marcador2, (550,10))
    pg.display.flip()