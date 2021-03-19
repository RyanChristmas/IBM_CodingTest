import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

#define the text font
font = pygame.font.SysFont('calibri',52)
#text
text = font.render('HelloIS5312',True,(0,128,0))

#program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill((255,255,255))
    screen.blit(text,(100,200))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()