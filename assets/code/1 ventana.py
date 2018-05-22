# Módulos
import sys, pygame
from pygame.locals import *

# ---------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------
WIDTH = 640
HEIGHT = 480


# ---------------------------------------------------------------------
# Clases
# ---------------------------------------------------------------------
class Bola(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/bola.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.4, -0.4]
        
    def actualizar(self, time, pala_jug, pala_cpu, puntos, color):
        #Movimiento
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        #Puntaje
        if self.rect.left <= 0:
            puntos[1] += 1            
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
        if self.rect.right >= WIDTH:
            puntos[0] += 1
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2

        #Colisión con bordes
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

        #Colisión con palas
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            color = (255,0,0)
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            color = (0,255,0)

        return puntos, color
    
class Pala(pygame.sprite.Sprite):
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5
        
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
                
    def ia(self, time, bola):
        if bola.speed[0] >= 0 and bola.rect.centerx >= WIDTH/2:
            if self.rect.centery < bola.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > bola.rect.centery:
                self.rect.centery -= self.speed * time
        
# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except (pygame.error, message):
        raise (SystemExit, message)
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("fonts/DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego en Pygame")

    #background_image = load_image('images/fondo_pong.png')
    
    bola = Bola()
    pala_jug = Pala(10)
    pala_cpu = Pala(WIDTH-10)
    puntos = [0, 0]
    color = (255,0,0)

    clock = pygame.time.Clock()
    
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                pygame.quit()
                sys.exit(0)

        puntos, color = bola.actualizar(time, pala_jug, pala_cpu, puntos, color)        
        pala_jug.mover(time, keys)
        pala_cpu.ia(time, bola)

        p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)
        p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)
        
        #screen.blit(background_image, (0, 0))
        screen.fill(color)        
        screen.blit(bola.image, bola.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)
        screen.blit(p_jug, p_jug_rect)
        screen.blit(p_cpu, p_cpu_rect)
        pygame.display.flip()
        pygame.display.update()
        
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
