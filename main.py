import pygame

print('Iniciando Jogo')
pygame.init();
window = pygame.display.set_mode(size=(800,550))
print('Setup Start')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
