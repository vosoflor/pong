import Clase_Figuras
import pygame as pg

# Para inicializar pygame
pg.init()

# Para crear pantalla base y asignar un nombre
pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong :D !!!")

# Para crear pelota y raquetas con parámetros mínimos requeridos;
# de los otros parámetros toma los valores por default
pelota = Clase_Figuras.Pelota(pantalla_principal.get_width()/2, pantalla_principal.get_height()/2)
raqueta1 = Clase_Figuras.Raqueta(10, 250)
raqueta2 = Clase_Figuras.Raqueta(800-10-20, 250)

# Bucle para mantener la pantalla activa mientras se desarrolla el código
game_over = False

while not game_over:
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    
    if pg.key.get_pressed()[pg.K_DOWN]:
        raqueta1.pos_y += 1
        raqueta2.pos_y += 1
    if pg.key.get_pressed()[pg.K_UP]:
        raqueta1.pos_y -= 1
        raqueta2.pos_y -= 1
    
    # Método para asignar color a la pantalla y línea del medio
    pantalla_principal.fill((0, 128, 94))
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), 2)
    
    # Método para dibujar pelota de juego y raquetas
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    # Método para dibujar y mostrar lo parametrizado anteriormente
    pg.display.flip()


