import pygame
import sys
import random


pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Game")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

player_size = 20
player_color = (0, 128, 0)
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5


enemy_size = 10
enemy_color = (200, 0, 0)
enemy_x = random.randint(200, width - enemy_size)
enemy_y = 50
enemy_speed = 1




enemy2_size = 10
enemy2_color = (200, 0, 0)
enemy2_x = random.randint(200, width - enemy_size)
enemy2_y = 50
enemy2_speed = 1

ally_size = 20
ally_color = (0, 0, 255)
ally_x = player_x
ally_y = player_y -50
ally_speed= -1.5



bullet_width=5
bullet_height=10
bullet_color=(255,255,0)
bullet_speed=7
bullets=[]




rocket_width=6
rocket_height=25
rocket_color=(255,140,0)
rocket_speed=7
rockets=[]





score=0

def draw_text(text, x, y):
    img = FONT.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

running = True
while running:
    clock.tick(60)



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event. type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bullets.append([player_x, player_y])
            elif event.key==pygame.K_LALT or event.key == pygame.K_RALT:
                rockets.append([player_x, player_y])
            

       

 


    
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_size:
        player_y += player_speed



    distance_x = ally_x - player_x
    threshold = 5
    if abs(distance_x) > threshold:
        direction = -1 if distance_x > 0 else 1
        speed = min(abs(distance_x) * 0.15, 2.5)
        ally_x += direction * speed


    ally_y += ally_speed  
    if ally_y < 100:  
        ally_y = 100






        


    enemy_y += enemy_speed
    enemy2_y +=enemy2_speed

    
    



   

    

    if enemy_y > height:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, width - enemy_size)
        score += 1
        enemy_speed +=0.01


    
    if enemy2_y > height:
        enemy2_y = -enemy2_size
        enemy2_x = random.randint(0, width - enemy2_size)
        score += 1
        enemy2_speed +=0.01
    
    
    if ally_y > height:
        ally_y =  -ally_size
        ally_x = random.randint(0, width - ally_size)



    for bullet in bullets[:]:
        bullet[1] -=bullet_speed
        if bullet[1] <0:
            bullets.remove(bullet)




    for rocket in rockets[:]:
        rocket[1] -=rocket_speed
        if rocket[1] <0:
            rockets.remove(rocket)



        
            
            
    


        
    

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, enemy2_size, enemy2_size)
    ally_rect=pygame.Rect(ally_x, ally_y, ally_size, ally_size)
    
    
    



    for bullet in bullets[:]: 
        bullet_rect=pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
        if bullet_rect.colliderect(enemy_rect):
            bullets.remove(bullet)
            score +=1
            enemy_y= -enemy_size
           enemy_x= random.randint(0,width - enemy_size)
           enemy_speed += 0.01
       elif bullet_rect.colliderect(enemy2_rect):
           bullets.remove(bullet)
           score +=1
           enemy2_y= -enemy2_size
           enemy2_x= random.randint(0,width - enemy2_size)




        for rocket in rockets[:]:
            rocket_rect=pygame.Rect(rocket[0], rocket[1], rocket_width, rocket_height)
            if rocket_rect.colliderect(enemy_rect):
               rockets.remove(rocket)
               score +=5
               enemy_y= -enemy_size
               enemy_x= random.randint(0, width - enemy_size)
               enemy_speed +=0.01
             elif rocket_rect.colliderect(enemy2_rect):
                rockets.remove(rocket)
            score +=5
            enemy2_y = -enemy2_size
            enemy2_x = random.randint(0, width - enemy2_size)
            enemy2_speed += 0.01



    if ally_rect.colliderect(enemy_rect):
        enemy_y= -enemy_size
        enemy_x= random.randint(0, width - enemy_size)
        score +=5
        print("Your ally destroy an enemy, 5 points added!")
        enemy_y = -enemy_size
        enemy_x = random.randint(0, width - enemy_size)
        enemy_speed += 0.01




    if ally_rect.colliderect(enemy2_rect):
        enemy_y= -enemy2_size
        enemy_x= random.randint(0, width - enemy2_size)
        score +=5
        print("Your ally destroy an enemy, 5 points added!")
        enemy2_y = -enemy2_size
        enemy2_x = random.randint(0, width - enemy2_size)
        enemy2_speed += 0.01



    if player_rect.colliderect(enemy_rect)or player_rect.colliderect(enemy2_rect):
      print("Game over! Final score:", score)
      running = False
  

rocket

        


    screen.fill((30,30,30))
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, enemy_color, enemy_rect)
    pygame.draw.rect(screen, enemy2_color, enemy2_rect)
    pygame.draw.rect(screen, ally_color, ally_rect)


    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))



    for rocket in rockets:
        pygame.draw.rect(screen, rocket_color, (rocket[0], rocket[1], rocket_width, rocket_height))


    
    draw_text(f"Score: {score}", 10, 10)

    


    pygame.display.flip()

pygame.quit()
sys.exit()
