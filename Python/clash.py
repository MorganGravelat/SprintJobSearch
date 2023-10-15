import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
DOT_RADIUS = 20
DOT_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
SPEED = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dot Clash Simulation")

# Initialize dot positions and velocities
dot1_x, dot1_y = random.randint(DOT_RADIUS, WIDTH - DOT_RADIUS), random.randint(DOT_RADIUS, HEIGHT - DOT_RADIUS)
dot2_x, dot2_y = random.randint(DOT_RADIUS, WIDTH - DOT_RADIUS), random.randint(DOT_RADIUS, HEIGHT - DOT_RADIUS)
dot1_vel_x, dot1_vel_y = random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)
dot2_vel_x, dot2_vel_y = random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the dots
    dot1_x += dot1_vel_x
    dot1_y += dot1_vel_y
    dot2_x += dot2_vel_x
    dot2_y += dot2_vel_y

    # Check for collisions with the screen edges and bounce back
    if dot1_x < DOT_RADIUS or dot1_x > WIDTH - DOT_RADIUS:
        dot1_vel_x = -dot1_vel_x
    if dot1_y < DOT_RADIUS or dot1_y > HEIGHT - DOT_RADIUS:
        dot1_vel_y = -dot1_vel_y

    if dot2_x < DOT_RADIUS or dot2_x > WIDTH - DOT_RADIUS:
        dot2_vel_x = -dot2_vel_x
    if dot2_y < DOT_RADIUS or dot2_y > HEIGHT - DOT_RADIUS:
        dot2_vel_y = -dot2_vel_y

    # Check for collision between the two dots
    distance = ((dot1_x - dot2_x) ** 2 + (dot1_y - dot2_y) ** 2) ** 0.5
    if distance <= 2 * DOT_RADIUS:
        dot1_vel_x, dot2_vel_x = dot2_vel_x, dot1_vel_x
        dot1_vel_y, dot2_vel_y = dot2_vel_y, dot1_vel_y

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the dots
    pygame.draw.circle(screen, DOT_COLOR, (int(dot1_x), int(dot1_y),), DOT_RADIUS)
    pygame.draw.circle(screen, DOT_COLOR, (int(dot2_x), int(dot2_y),), DOT_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
