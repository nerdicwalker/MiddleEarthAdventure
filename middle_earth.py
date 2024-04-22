import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Middle-earth Adventure")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
locations = ["King County", "Snohomish County", "Pierce County", "Kitsap County", "Thurston County"]
artifacts = ["One Lake", "One copy", "One (open)format", "One user experience", "One access control method",
             "One security model", "One governance model", "One monitoring hub", "One licensing structure"]
player_location = random.choice(locations)
enemy = random.choice(["Bug", "Zero day", "Malware", "Feature", "Developer", "Manager", "Product Owner",
                       "Release Train Engineer", "Devops", "MLops", "Scrum master"])
health = 100
inventory = []

# Define text rendering function
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Display game information
    draw_text("Middle-earth Adventure", WHITE, 20, 20)
    draw_text("Location: " + player_location, WHITE, 20, 60)
    draw_text("Enemy: " + enemy, WHITE, 20, 100)
    draw_text("Health: " + str(health), WHITE, 20, 140)
    draw_text("Inventory:", WHITE, 20, 180)
    for i, item in enumerate(inventory):
        draw_text("- " + item, WHITE, 20, 220 + i * 40)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
