import sys, pygame
pygame.init()

smallfont = pygame.font.SysFont("Times New Roman", 35)

width = 600
height = 600
screen = pygame.display.set_mode((width, height))

image = pygame.image.load("sunflower.jpg")
image = pygame.transform.scale(image, (400, 400))
x = 100
y = 150

color = (0, 0, 0)

text = smallfont.render("Choose complexity:", True, color)
fours = smallfont.render("2x2", True, color)
sixes = smallfont.render("2x3", True, color)
eights = smallfont.render("2x4", True, color)

while True:
    screen.fill((255, 255, 255))
    screen.blit(image, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(text, (10, 0))
    screen.blit(fours, (10, 50))
    screen.blit(sixes, (10+100, 50))
    screen.blit(eights, (10+100+100, 50))

    pygame.display.update()



pygame.quit()
quit()