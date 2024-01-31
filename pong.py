import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 15
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = [random.choice([-2, 2]), random.choice([-2, 2])]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]

        if pygame.sprite.collide_rect(self, paddle_left) or pygame.sprite.collide_rect(self, paddle_right):
            self.speed[0] = -self.speed[0]

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.speed = [random.choice([-2, 2]), random.choice([-2, 2])]

paddle_left = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle_right = Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_left, paddle_right, ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()