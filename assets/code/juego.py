# Módulos
import sys, pygame, random
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
            self.speed[0] = -self.speed[0]
        if self.rect.right >= WIDTH:
            puntos[0] += 1
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
            self.speed[0] = -self.speed[0]

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
            color = (4, 72, 35)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/tenista.wav'))
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            color = (157, 3, 15)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/tenista.wav'))

        return puntos, color
    
class Pala(pygame.sprite.Sprite):
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.4
        
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_w]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_s]:
                self.rect.centery += self.speed * time

    def mover2(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
    
    def ia(self, time, bola):
        if bola.speed[0] >= 0 and bola.rect.centerx >= WIDTH/2:
            rand = random.randint(-2,10) #Negativo -> Ir en dirección contraria a la bola
            if self.rect.centery < bola.rect.centery:
                if rand >= 0:
                    self.rect.centery += self.speed * time
                else:
                    self.rect.centery -= self.speed * time
            if self.rect.centery > bola.rect.centery:
                if rand >= 0:
                    self.rect.centery -= self.speed * time
                else:
                    self.rect.centery += self.speed * time
        
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
# Programa principal
# ---------------------------------------------------------------------
 
def main():
    print("¿Desea 1 o 2 jugadores?")
    modo = int(input("Ingrese 1 o 2: "))

    if (modo >=1 and modo <=2):    
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego en Pygame")

        #background_image = load_image('images/fondo_pong.png')
        
        bola = Bola()
        pala_jug = Pala(10)
        pala_cpu = Pala(WIDTH-10)
        puntos = [0, 0]
        color = (4, 72, 35)
        angulo = 0

        clock = pygame.time.Clock()
        #Música de fondo
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/bgm.ogg'))
        pygame.mixer.Channel(0).set_volume(0.3, 0.3)
        
        while True:
            time = clock.tick(60)
            keys = pygame.key.get_pressed()
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

            puntos, color = bola.actualizar(time, pala_jug, pala_cpu, puntos, color)        
            pala_jug.mover(time, keys)
            if (modo == 1):
                pala_cpu.ia(time,bola)
            if (modo == 2):
                pala_cpu.mover2(time, keys)

            p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)
            p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)

            #Imagen de fondo
            #screen.blit(background_image, (0, 0))
            
            #Color de fondo
            screen.fill(color)
            
            #Línea central
            pygame.draw.line(screen, (255,255,255), (WIDTH/2,0), (WIDTH/2, HEIGHT),3)

            angulo = (angulo+5)%360
            bolarotada = pygame.transform.rotate(bola.image, angulo)
            
            #Actualizar imágenes
            screen.blit(bolarotada, bola.rect)
            screen.blit(pala_jug.image, pala_jug.rect)
            screen.blit(pala_cpu.image, pala_cpu.rect)
            screen.blit(p_jug, p_jug_rect)
            screen.blit(p_cpu, p_cpu_rect)

            #Actualizar línea y fondo
            pygame.display.update()

            #Actualizar imágenes
            pygame.display.flip()
        
            
    return 0
 
if __name__ == '__main__':
    pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init()
    main()
