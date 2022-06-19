
import pygame
pygame.init()


centerx=368
centery=368

ground=pygame.display.set_mode((800,800))



score1 = 0
score2 = 0

ballimg=pygame.image.load('fitness-ball.png')
ballx=centerx
bally=centery

def ball(x,y):
    ground.blit(ballimg,(x,y))

score1 = 0
score2 = 0
def player1(x11,x21,y11,y21):
    pygame.draw.line(ground,(225,0,0),(x11,y11),(x21,y21),30)

def player2(x12,x22,y12,y22):
    pygame.draw.line(ground,(225,0,0),(x12,y12),(x22,y22),30)
x11=20
x21=20
y11=350
y21=450
y1move =0
x12=780
x22=780
y12=350
y22=450
y2move=0               
ballxmove = 1
ballymove=0.7
run=True
while run:


   
    ground.fill((0,0,0))


    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y1move=-1
             

            if event.key == pygame.K_DOWN:                
                y1move= 1

            if event.key == pygame.K_w:
                y2move=-1
            if event.key == pygame.K_s:
                y2move=1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                y1move=0
            if event.key == pygame.K_w or event.key==pygame.K_s:
                y2move=0

    y11 += y1move
    y21 += y1move     
    y12 += y2move
    y22 += y2move 


    ballx += ballxmove
    bally += ballymove



    if ballx==x11 and   y11 <= bally and bally<=y21:
        ballxmove= - ballxmove
    if ballx == x12 and y12 <= bally and bally<= y22:
        ballxmove= - ballxmove


    if bally >= 784:
        ballymove = -ballymove
    if bally <= 0:
        ballymove = -ballymove
    if ballx <=0 :
        score2 += 1
        ballx=centerx
        bally=centery
    if ballx >= 786:
        score1 += 1
        ballx=centerx
        bally=centery

    if score1 == 10 :
        print("the player 1 is winner")
        run=False
    if score2 == 10:
        print(" the player 2 is the winner")
        run = False
    player1(x11,x21,y11,y21)
    player2(x12,x22,y12,y22)
    ball(ballx,bally)


    pygame.display.update()