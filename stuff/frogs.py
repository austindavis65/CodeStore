import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FROG_SIZE = 50

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the frog
frog_x, frog_y = WIDTH / 2, HEIGHT - FROG_SIZE * 2
frog_speed = 5

# Set up the cars
cars = []
for i in range(5):
    car_x, car_y = 0, i * 50
    cars.append((car_x, car_y))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the frog
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        frog_y -= frog_speed
    if keys[pygame.K_DOWN]:
        frog_y += frog_speed
    if keys[pygame.K_LEFT]:
        frog_x -= frog_speed
    if keys[pygame.K_RIGHT]:
        frog_x += frog_speed

    # Move the cars
    for i, (car_x, car_y) in enumerate(cars):
        car_x += 2
        if car_x > WIDTH:
            car_x = 0
        cars[i] = (car_x, car_y)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (frog_x, frog_y, FROG_SIZE, FROG_SIZE))
    for car_x, car_y in cars:
        pygame.draw.rect(screen, WHITE, (car_x, car_y, 50, 50))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)