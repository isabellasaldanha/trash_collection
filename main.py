import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trash Collection Game")

# Path to the assets folder
assets_folder = os.path.join(os.path.dirname(__file__), 'assets')

# Load images
background_image = pygame.image.load(os.path.join(assets_folder, 'background.png')).convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

player_image = pygame.image.load(os.path.join(assets_folder, 'bin.png')).convert_alpha()
player_image = pygame.transform.scale(player_image, (120, 100))

trash_image = pygame.image.load(os.path.join(assets_folder, 'trash.png')).convert_alpha()
trash_image = pygame.transform.scale(trash_image, (80, 80))

# Load sounds
collect_sound = pygame.mixer.Sound(os.path.join(assets_folder, 'collect.wav'))
game_over_sound = pygame.mixer.Sound(os.path.join(assets_folder, 'game_over.wav'))

# Load font
font_path = os.path.join(assets_folder, 'comic.ttf')
font = pygame.font.Font(font_path, 24) 

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Prevent the player from going off the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

# Trash class
class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = trash_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 5  # Increase the trash speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()
            global lost_trash_count
            lost_trash_count += 1

# Function to reset the game
def reset_game():
    global score, lost_trash_count, game_over
    game_over_sound.stop()
    score = 0
    lost_trash_count = 0
    game_over = False
    all_sprites.empty()
    trash_sprites.empty()
    all_sprites.add(player)

# Sprite groups
all_sprites = pygame.sprite.Group()
trash_sprites = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

# Variable to control trash generation
ADD_TRASH_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_TRASH_EVENT, 1000)

# Score and lost trash count
score = 0
lost_trash_count = 0

# Main loop
running = True
clock = pygame.time.Clock()
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADD_TRASH_EVENT and not game_over:
            trash = Trash()
            all_sprites.add(trash)
            trash_sprites.add(trash)
        elif event.type == pygame.KEYDOWN and game_over:
            reset_game()

    if not game_over:
        # Update sprites
        all_sprites.update()

        # Check for collisions
        hits = pygame.sprite.spritecollide(player, trash_sprites, True)
        if hits:
            score += 10
            if not pygame.mixer.get_busy():  # Play sound only if no other sound is playing
                collect_sound.play()

        # Check if lost trash count reached 3
        if lost_trash_count >= 3:
            game_over = True
            if pygame.mixer.get_busy():
                pygame.mixer.stop()  # Stop any playing sounds
            game_over_sound.play()

        # Draw the background
        screen.blit(background_image, (0, 0))

        # Draw sprites
        all_sprites.draw(screen)

        # Draw the score with shadow
        shadow_offset = 2
        score_text = font.render(f"Score: {score}", True, (255, 182, 193))  
        screen.blit(score_text, (12, 12))
        score_text = font.render(f"Score: {score}", True, (255, 0, 0))  # Red text
        screen.blit(score_text, (10, 10))

        # Draw lost trash count with shadow
        lost_text = font.render(f"Lost Trash: {lost_trash_count}", True, (255, 182, 193))  
        screen.blit(lost_text, (12, 52))
        lost_text = font.render(f"Lost Trash: {lost_trash_count}", True, (255, 0, 0))  # Red text
        screen.blit(lost_text, (10, 50))
    else:
        # Draw game over screen
        screen.fill((255, 182, 193))  
        game_over_text = font.render("Game Over! Press any key to restart", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
