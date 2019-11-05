import pygame

pygame.init()

surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('My Drawable Objects')

drawables = []
newHouse = House(100, 100, (255, 0, 0))
drawables.append(newHouse)
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN
        and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
    surface.fill((255, 255, 255))
    for drawable in drawables:
        drawable.draw(surface)
    pygame.display.update()