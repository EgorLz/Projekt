import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill("white")
pygame.display.set_caption('Фото')

name = input()

n = name.split('.')
short_name = n[0]

image_surf = pygame.image.load(name)
screen = pygame.display.set_mode(image_surf.get_rect().size, 0, 32)
image_rect = image_surf.get_rect(
    topleft=(0, 0))
screen.blit(image_surf, image_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
