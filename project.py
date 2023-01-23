import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill("white")
pygame.display.set_caption('Фото')

name = input()

n = name.split('.')
short_name = n[0] + ".txt"
a_point = 0

image_surf = pygame.image.load(name)
screen = pygame.display.set_mode(image_surf.get_rect().size, 0, 32)
image_rect = image_surf.get_rect(
    topleft=(0, 0))
screen.blit(image_surf, image_rect)

f = open(short_name,'r')
print(f.readline())
st = f.readline()
print(st)
st = st.replace('(', '')
st = st.replace(')', '')
st = st.replace(',', '')
st = st.replace('\n', '')
st = st.split(' ')
end = f.readline()
end = end.replace('(', '')
end = end.replace(')', '')
end = end.replace(',', '')
end = end.replace('\n', '')
end = end.split(' ')
pygame.draw.rect(screen, (0, 0, 0),
                 (int(st[0]), int(st[1]), int(end[0]) - int(st[0]), int(end[1]) - int(st[1]), 5))


def write_name(a, st, end, short):
    with open(short, 'w') as f:
        f.write(a)
        f.write('\n')
        f.write(str(st))
        f.write('\n')
        f.write(str(end))
        f.write('\n')
        f.close()



pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if a_point == 0:
                    start_point = event.pos
                    a_point = 1
                else:
                    end_point = event.pos
                    pygame.draw.rect(screen, (0, 0, 0),
                 (start_point[0], start_point[1], end_point[0] - start_point[0], end_point[1] - start_point[1]), 5)
                    a = input()
                    write_name(a, start_point, end_point, short_name)
                    a_point = 0

    pygame.display.flip()
