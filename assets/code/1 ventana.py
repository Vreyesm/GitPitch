# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480

# ---------------------------------------------------------------------
# Clases
# ---------------------------------------------------------------------
 
# --------------------------------------------------------------------- 
# Funciones
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pr  uebas Pygame")
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()