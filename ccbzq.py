import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255,0,0)
black = (0, 0, 0)

screen = pygame.display.set_mode((600,650))
pygame.display.set_caption("车诚爆炸棋")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf', 25)

class grid:   
    def __init__(self, num, color, posX, posY):
        self.numberOfChess = num
        self.chessColor = color
        self.posX = posX + 100
        self.posY = posY + 100
    def update(self):
        text = font.render(str(self.numberOfChess), True, self.chessColor)
        screen.blit(text,(self.posX, self.posY))
        pass

grid00 = grid(0,black,0,50)
grid10 = grid(0,black,200,50)
grid20 = grid(0,black,400,50)
grid01 = grid(0,black,0,250)      
grid11 = grid(0,black,200,250)
grid21 = grid(0,black,400,250)      
grid02 = grid(0,black,0,450)
grid12 = grid(0,black,200,450)      
grid22 = grid(0,black,400,450)
    
def updateAll():
    grid00.update() 
    grid10.update()
    grid20.update()
    grid01.update()   
    grid11.update() 
    grid21.update()       
    grid02.update() 
    grid12.update()      
    grid22.update() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))    
    pygame.draw.rect(screen, (0,0,0), [0 , 50, 600, 650],1)

    #vertical lines
    pygame.draw.line(screen, ((0,0,0)), [200, 50], [200,650], 1)
    pygame.draw.line(screen, ((0,0,0)), [400, 50], [400,650], 1)
    #horizontal lines
    pygame.draw.line(screen, ((0,0,0)), [0, 250], [600,250], 1)
    pygame.draw.line(screen, ((0,0,0)), [0, 450], [600,450], 1)
    pos = pygame.mouse.get_pos()
    mouse1,mouse2,mouse3 = pygame.mouse.get_pressed()
    
    if mouse1 == True:
        pygame.time.wait(100)
        print(pos)    

    

    pygame.time.wait(50)
    pygame.display.update()


