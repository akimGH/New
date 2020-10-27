import pygame

W = 800
H = 600
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
NAVY = (5, 0, 50)

pygame.init()
pygame.display.set_caption("Текст")
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont("Arial", 40, True, False)
font1 = pygame.font.SysFont("Arial", 25, True, False)

screen.fill(NAVY)
pygame.draw.rect(screen, (RED), (400, 200, 50, 50))
screen.blit(font.render("Всем привет", True, WHITE), (300, 250))
screen.blit(font1.render("Задание на урок", True, YELLOW), (323, 300))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()
