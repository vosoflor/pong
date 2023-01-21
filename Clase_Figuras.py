import pygame as pg

class Pelota:
    
    def __init__(self, pos_x, pos_y, radio = 20, color = (255,255,255), vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.contador_derecha = 0
        self.contador_izquierda = 0
    
    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.pos_x, self.pos_y), self.radio)

    def mover(self, pantalla, raqueta1, raqueta2):
        self.pos_x += self.vx
        self.pos_y += self.vy
                
        if self.pos_x - self.radio <= raqueta1.pos_x + raqueta1.w and self.pos_y >= raqueta1.pos_y and self.pos_y <= raqueta1.pos_y + raqueta1.h:
            self.vx *= -1
        elif self.pos_x <= - self.radio:
            self.contador_izquierda += 1
            self.posicion_inicial(pantalla)

        if self.pos_x + self.radio >= raqueta2.pos_x and self.pos_y >= raqueta2.pos_y and self.pos_y <= raqueta2.pos_y + raqueta2.h:
            self.vx *= -1
        elif self.pos_x - self.radio >= pantalla.get_width():
            self.contador_derecha += 1
            self.posicion_inicial(pantalla)

        if self.pos_y < (0 + self.radio) or self.pos_y >= pantalla.get_height() - self.radio:
            self.vy *= -1

    def marcador(self, pantalla_principal):
        # Métodos para crear superficie de marcadores para cada jugador
        #jugador1 = pg.font.Font(None, 50).render("Jugador 1", 1, (255,255,255))
        marcador1 = pg.font.Font(None, 100).render(str(self.contador_derecha), 1, (255,255,255))
        #jugador2 = pg.font.Font(None, 50).render("Jugador 2", 1, (255,255,255))
        marcador2 = pg.font.Font(None, 100).render(str(self.contador_izquierda), 1, (255,255,255))        
        
        # Método para dibujar y mostrar lo parametrizado anteriormente
        #pantalla_principal.blit(jugador1, (120,10))
        pantalla_principal.blit(marcador1, (180,60))
        #pantalla_principal.blit(jugador2, (520,10))
        pantalla_principal.blit(marcador2, (580,60))
    
    def posicion_inicial(self, pantalla):
        self.pos_x = pantalla.get_width()/2
        self.pos_y = pantalla.get_height()/2
        self.vx *= -1
        self.vy *= -1

class Raqueta:
    
    def __init__(self, pos_x, pos_y, w = 20, h = 100, color = (255,255,255), vx = 1, vy = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy
    
    def dibujar(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.pos_x, self.pos_y, self.w, self.h))

    def mover(self, tecla_arriba, tecla_abajo, altura_pantalla):

        if pg.key.get_pressed()[tecla_arriba] and self.pos_y > 0:
            self.pos_y -= self.vy
        if pg.key.get_pressed()[tecla_abajo] and self.pos_y < altura_pantalla - self.h:
            self.pos_y += self.vy
