import random
import pygame
pygame.init()

#colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)



screen_width =900
screen_height = 600
gamewindow= pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("Snakeswithdev")
pygame.display.update()






clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)


f = open("dev.txt","r+")
#f.write(str(30))
hiscore=f.read()
               
#print(hiscore)
f.close()


def text_screen(text,color,x,y):
    sscreen_text=font.render(text,True,color)
    gamewindow.blit(sscreen_text,[x,y])



def ploat_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,black,[x, y, snake_size, snake_size])

# pygame.draw.rect(gamewindow,red,[food_x, food_y, snake_size, snake_size])

#game loop


def gameloop():

    exit_game = False
    game_over = False
    snake_x=45
    snake_y=55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    score=0

    snk_list=[]
    snk_length = 1

    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    snake_size=20
    fps=40


    while not exit_game:

        if game_over:
            gamewindow.fill(white)
            text_screen("Game over ! prees Enter to continue",red,100,250)


            for event in pygame.event.get():
                

                if event.type==pygame.QUIT:
                        exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
                        

        else:

        
            for event in pygame.event.get():
                

                if event.type==pygame.QUIT:
                        exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                
                
            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score+=10
                
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snk_length +=5


            





            gamewindow.fill(white)
            
            text_screen("Highscore: "+hiscore,red,200,5)
            
            
            text_screen("score: "+str(score),red,5,5)
            pygame.draw.rect(gamewindow,red,[food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            

            if len(snk_list)>snk_length:
                del snk_list[0]


            if head in snk_list[ :-1]:
                game_over = True
            
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                

            

            ploat_snake(gamewindow,black,snk_list, snake_size)
        
        pygame.display.update()

        clock.tick(fps)


    pygame.quit()
    quit()


gameloop()
fo=open("dev.txt","r+")
if score>hiscore:
    fo.truncate(0)
    fo.write(score)
fo.close()
    

