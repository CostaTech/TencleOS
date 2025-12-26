# TencleOS Snake Game - TLang Version
# Simplified Pygame Snake game

use pygame
use random

pygame.init()

# Screen setup
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("TencleOS Snake Game")

# Colors
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLACK = [0, 0, 0]

# Game settings
BLOCK = 20
clock = pygame.time.Clock()

# Snake starting position
snake_x = 300
snake_y = 200
dir_x = BLOCK
dir_y = 0

# Snake body (list of segments)
snake_body = [[300, 200]]
snake_length = 1

# Food position
food_x = 240
food_y = 160

# Score
score = 0

# Game loop
running = on
<<While>>! <on> running {
    
    # Handle events
    events = pygame.event.get()
    for e in events {
        << ! >func> if e.type == pygame.QUIT {
            running = off
        } elif e.type == pygame.KEYDOWN {
            << ! >func> if e.key == 1073741906 {
                << ! >func> if dir_y == 0 {
                    dir_x = 0
                    dir_y = 0 - BLOCK
                }
            } elif e.key == 1073741905 {
                << ! >func> if dir_y == 0 {
                    dir_x = 0
                    dir_y = BLOCK
                }
            } elif e.key == 1073741904 {
                << ! >func> if dir_x == 0 {
                    dir_x = 0 - BLOCK
                    dir_y = 0
                }
            } elif e.key == 1073741903 {
                << ! >func> if dir_x == 0 {
                    dir_x = BLOCK
                    dir_y = 0
                }
            }
        }
    }
    
    # Move snake
    snake_x = snake_x + dir_x
    snake_y = snake_y + dir_y
    
    # Add new head to body
    snake_body.append([snake_x, snake_y])
    
    # Check boundaries
    << ! >func> if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT {
        int << func >> ("================================")
        int << func >> ("         GAME OVER!            ")
        int << func >> ("================================")
        running = off
    }
    
    # Check food collision
    << ! >func> if snake_x == food_x and snake_y == food_y {
        score = score + 1
        snake_length = snake_length + 1
        food_x = random.randint(0, 29) * BLOCK
        food_y = random.randint(0, 19) * BLOCK
    }
    
    # Keep snake at correct length (remove tail if not eating)
    use builtins
    << ! >func> if builtins.len(snake_body) > snake_length {
        snake_body.pop(0)
    }
    
    # Draw everything
    screen.fill(WHITE)
    
    # Draw snake body
    for segment in snake_body {
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK, BLOCK])
    }
    
    # Draw food
    pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK, BLOCK])
    
    # Update display
    pygame.display.flip()
    clock.tick(10)
}

pygame.quit()
int << func >> ("Game Over! Press Enter...")
var wait = input()


