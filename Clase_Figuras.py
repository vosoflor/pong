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

    def mover(self, altura_pantalla, ancho_pantalla):
        self.pos_x += self.vx
        self.pos_y += self.vy
        
        if self.pos_x < (0 + self.radio):
            self.vx *= -1
            self.contador_izquierda += 1
        if self.pos_x >= ancho_pantalla - self.radio:
            self.vx *= -1
            self.contador_derecha += 1
        if self.pos_y < (0 + self.radio) or self.pos_y >= altura_pantalla - self.radio:
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
