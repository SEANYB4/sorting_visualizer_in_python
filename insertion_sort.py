import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()

FPS = 100
# VARIABLES

display_width = 800
display_height = 600

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
block_size = 50

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Bubble sort")

game_exit = False


# FONTS
# System Font
font = pygame.font.SysFont('Garamond', 30)
textsurface = font.render('Press UP to run insertion sort again', False, (0, 0, 0))

number_text = font.render('0', False, (0, 0, 0))

current_idx = 0

# IMAGES


# OTACON
img1 = pygame.image.load('OIP-CXK8W05AK.jpg')
scaled_image = pygame.transform.scale(img1, (100, 100)) 


# FUNCTIONS
def insertion_sort(nums):
    for i in range(0, len(nums)):
        j = 0
        draw_list(list_for_sort)
        clock.tick(FPS)
        while j < len(nums):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
            draw_list(list_for_sort)
            
    return nums

def draw_list(list_for_sort):
    gameDisplay.fill(white)
    for i in range(len(list_for_sort)):
      color = red
      if i == current_idx:
          color = green
      height = (list_for_sort[i]*10)
      pygame.draw.rect(gameDisplay, color, [(i*80), display_height-height, block_size, height])
      number_text = font.render(str(list_for_sort[i]), False, (0, 0, 0))
      gameDisplay.blit(number_text, ((i*80)+15, 40))
      gameDisplay.blit(scaled_image, (0, 0))
      pygame.display.update()


def redo_insertion_sort(list_for_sort):
    list_for_sort = [random.randrange(0, 50) for i in range(0, 10)]
    draw_list(list_for_sort)
    clock.tick(FPS)
    list_for_sort = insertion_sort(list_for_sort)
    draw_list(list_for_sort)
    gameDisplay.blit(textsurface,(100, 100))



# INITIAL SETUP

list_for_sort = [random.randrange(0, 50) for i in range(0, 10)]
draw_list(list_for_sort)
clock.tick(FPS)
list_for_sort = insertion_sort(list_for_sort)
draw_list(list_for_sort)


gameDisplay.blit(textsurface,(100, 100))
# GAME LOOP

while not game_exit:

   # EVENT HANDLING
    # event handling
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                redo_insertion_sort(list_for_sort)
   
   pygame.display.update()

pygame.quit()