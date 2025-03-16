import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_image = pygame.image.load("mickey_clock.png")
right_hand = pygame.image.load("right_hand.png")
left_hand = pygame.image.load("left_hand.png")

clock_center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_image, (0, 0))

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    second_angle = -seconds * 6  # 360 degrees / 60 seconds = 6 degrees per second
    minute_angle = -minutes * 6  # 360 degrees / 60 minutes = 6 degrees per minute

    rotated_left = pygame.transform.rotate(left_hand, second_angle)
    rotated_right = pygame.transform.rotate(right_hand, minute_angle)

    left_rect = rotated_left.get_rect(center=clock_center)
    right_rect = rotated_right.get_rect(center=clock_center)

    screen.blit(rotated_left, left_rect.topleft)
    screen.blit(rotated_right, right_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()