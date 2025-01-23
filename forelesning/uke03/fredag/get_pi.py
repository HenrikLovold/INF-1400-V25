"""
This application calculates pi using a monte carlo method,
and visualizes the results compared to the constant in the
math library
"""

from random import random
from math import sqrt
from math import pi
from collections import deque
import time
import pygame

SCREEN_SIZE = 800
PRINT_INTERVAL = 100
DRAW_INTERVAL = 2

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE,
                                  SCREEN_SIZE))
point = pygame.Surface((1, 5))
point.fill((0, 255, 0))

# Variables used for visualization
accumulated_error = 0
values = deque(maxlen=SCREEN_SIZE)
time_iteration = time.clock_gettime(time.CLOCK_MONOTONIC)

# Calculated pi for the current number of iterations
current_iterations = 100
current_pi = 0

while True:
    # Calculate an estimate for pi
    points_inside_circle = 0
    for _ in range(current_iterations): 
        # Generate a random point between (-0.5, -0.5) and (0.5, 0.5)
        x_position = random() - 0.5
        y_position = random() - 0.5
        # Check if point is inside the circle
        if sqrt(x_position**2 + y_position**2) <= 0.5:
            points_inside_circle += 1
    current_pi = 4 * points_inside_circle / current_iterations

    # Visualize results
    accumulated_error += abs(current_pi - pi)
    # Add most recent pi calculation to the drawing list
    y_value = int((current_pi - 2.5) * (SCREEN_SIZE * 0.75))
    values.append(y_value)

    # Draw results to screen every 2nd iteration
    if current_iterations % DRAW_INTERVAL == 0:
        screen.fill((0, 0, 0))
        # Draw all estimates on the screen
        for x_coord, y_coord in enumerate(values):
            screen.blit(point, (x_coord, y_coord))

        # Draw the reference pi value on the screen
        real_pi_y = int((pi - 2.5) * (SCREEN_SIZE * 0.75))
        pygame.draw.line(screen,
                         (255, 0, 0),
                         (SCREEN_SIZE - 50, real_pi_y),
                         (SCREEN_SIZE, real_pi_y),
                         5)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final_str = "Final value for pi: {}"
                print(final_str.format(current_pi))
                pygame.quit()
                exit()

    # Print statistics every 100 iterations
    if current_iterations % PRINT_INTERVAL == 0:
        time_passed = time.clock_gettime(time.CLOCK_MONOTONIC) - time_iteration
        output = "At iteration {:>6}, pi is {:>6.5}, average error is {:<8.5}, " \
                 "done in {:<4.2} seconds ({} iterations per second)"
        print(output.format(current_iterations,
                            current_pi,
                            accumulated_error/PRINT_INTERVAL,
                            time_passed,
                            int(PRINT_INTERVAL/time_passed)))
        accumulated_error = 0
        time_iteration = time.clock_gettime(time.CLOCK_MONOTONIC)
    current_iterations += 1
