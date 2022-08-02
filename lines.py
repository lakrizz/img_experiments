from helper import nearest
import pygame
import random

num_points = 5000
pt_minmax = (5, 10)
line_minmax = (5,20)
points = []

img = pygame.image.load("m.jpg")
img = pygame.transform.scale(img, (1280, 720))
for i in range(num_points):
    x = random.randint(0, img.get_width()-1)
    y = random.randint(0, img.get_height()-1)
    points.append({"x": x, "y": y, "color": (img.get_at((x, y))), "connected": False})

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([img.get_width(), img.get_height()])

running = True
drawn = False
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.blit(img, (0,0))

    if not drawn:
        for p in points:
            pygame.draw.circle(screen, p['color'], (p['x'], p['y']), random.randint(pt_minmax[0], pt_minmax[1]))
            n = nearest(p, points)
            if n > len(points):
                break
            pn = points[n]
            points[n]['connected'] = True
            pygame.draw.line(screen, p['color'], (p['x'], p['y']), (pn['x'], pn['y']), width=random.randint(line_minmax[0], line_minmax[1]))
        pygame.display.flip()

        drawn = True

# Done! Time to quit.
pygame.quit()