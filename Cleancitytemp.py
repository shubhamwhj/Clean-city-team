import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=600
height=350
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("city3.jpg").convert_alpha()
images["bin"] = pygame.image.load("bin.png").convert_alpha()
  

class Dustbin:
    
        
    def display(self):
        screen.blit(images["bin"],self.bin)
        


while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
    
    
    
    screen.blit(images["bg"],[0,0])

    

    pygame.display.update()
    clock.tick(30) 