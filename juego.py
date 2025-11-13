import pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Juego")
tiempo = pygame.time.Clock()
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill((0, 0, 0))
    pygame.display.flip()
    tiempo.tick(60)
pygame.quit()
