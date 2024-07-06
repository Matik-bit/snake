import pygame
import random

pygame.init()
#кольори для фрукту і змійки
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)  
RED = (255, 0, 0)

# Розміри вікна
WIDTH = 800
HEIGHT = 600

# Розміри блоку
BLOCK_SIZE = 20

# Швидкість руху змійки
SPEED = 15

# Ініціалізація вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
back = (0,0,0) 
screen.fill(back)
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

#Класи 
class Area(): 
    def __init__(self, x=0, y=0, width=10, height=10, color=None): 
        self.rect = pygame.Rect(x, y, width, height) #прямокутник 
        self.fill_color = back 
        if color: 
            self.fill_color = color 
 
    def color(self, new_color): 
        self.fill_color = new_color 
 
    def fill(self): 
        pygame.draw.rect(screen, self.fill_color, self.rect)     
 
    def outline(self, frame_color, thickness): #обведення існуючого прямокутника 
        pygame.draw.rect(screen, frame_color, self.rect, thickness)    
    def collidepoint(self, x, y): 
        return self.rect.collidepoint(x, y)       
 
    def colliderect(self,rect): 
        return self.rect.colliderect(rect)
 
class Picture(Area): 
    def __init__(self,filename,x=0,y=0,width=10,height=10): 
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None) 
        self.image = pygame.image.load(filename) 
 
    def draw(self): 
        screen.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Label(Area): 
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)): 
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color) 
  def draw(self, shift_x=0, shift_y=0): 
      self.fill() 
      screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) 


exit = Picture("photo_2024-05-13_19-25-20.jpg",0,0,200,200)
btn_start = Picture('photo_2024-05-13_19-25-17.jpg', 325, 250, 100, 100)
seting = Picture("menu_knopki-removebg-preview.png", 325, 350, 100,100)

score = Label(500, 20, 200, 50, BLACK)
score.set_text('0', 40, GREEN)
score.draw(0, 0)


text = ("Рахунок")
rahynok = 0

score.set_text('Рахунок: ' + str(rahynok), 40,  GREEN )

# Початкові координати змійки
snake = [(WIDTH // 2, HEIGHT // 2)]
dx, dy = 0, 0

# Початкові координати фрукту
fruit = (random.randint(0, WIDTH-BLOCK_SIZE)//BLOCK_SIZE*BLOCK_SIZE, random.randint(0, HEIGHT-BLOCK_SIZE)//BLOCK_SIZE*BLOCK_SIZE)
screen_1 = 'menu'
menu_bg = 'back'
screen_2 = 'seting'

while True:
    if screen_1 =='menu':
        screen.fill((0, 0, 220))
        btn_start.draw()
        seting.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    screen_1 = 'game'
        

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if seting.rect.collidepoint(x, y):
                    screen_1 = 'seting'
                    screen.fill((0, 220, 0))
    if screen_1 =='seting':
        

            for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()





    if screen_1 == 'game':
        screen.fill((0,0,0))

        score.set_text(str(rahynok),40,  RED)
        score.draw(0,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_1 = 'menu'
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if exit.rect.collidepoint(x, y):
                    screen_1 = 'menu'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                if event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                if event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0

        # Рух змійки
        new_head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, new_head)
        if new_head == fruit:
            fruit = (random.randint(0, WIDTH-BLOCK_SIZE)//BLOCK_SIZE*BLOCK_SIZE, random.randint(0, HEIGHT-BLOCK_SIZE)//BLOCK_SIZE*BLOCK_SIZE)
            rahynok += 1
            score.set_text(str(rahynok), 40, RED)  # Оновлення рахунку
            score.draw(0, 0)  # Відображення оновленого рахунку
        else:
            snake.pop()

        # Малюємо змійку
        for block in snake:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        # Малюємо фрукт
        pygame.draw.rect(screen, WHITE, (fruit[0], fruit[1], BLOCK_SIZE, BLOCK_SIZE))

        #Відмалювання виходу
        exit.draw()
        



    pygame.display.update()
    clock.tick(SPEED)