import pygame
import random



pygame.init()


# VARIABLES

display_width = 800
display_height = 600

white = (255, 255, 255)
red = (255, 0, 0)
block_size = 50

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Bubble sort")

game_exit = False
list_for_sort = [random.randrange(0, 50) for i in range(0, 10)]


# FUNCTIONS

def bubble_sort(nums):
   
   for i in range(len(nums)-1):
      swapping = True
      j = i
      while swapping:
         swapping = False
         if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swapping = True
            print("swap")
         j += 1
   
   return nums


# Python program for implementation of Bubble Sort
 
 
# def bubble_sort(arr):
#    n = len(arr)
 
#    # Traverse through all array elements
#    for i in range(n):
 
#       # Last i elements are already in place
#       for j in range(0, n-i-1):
 
#          # traverse the array from 0 to n-i-1
#          # Swap if the element found is greater
#          # than the next element
#          if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#    return arr





print(list_for_sort)

print(bubble_sort(list_for_sort))


# GAME LOOP


while not game_exit:





   # EVENT HANDLING

    # event handling
   for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game_exit = True


   gameDisplay.fill(white)


   for i in range(len(list_for_sort)):

      height = (list_for_sort[i]*10)
      pygame.draw.rect(gameDisplay, red, [(i*80), display_height-height, block_size, height])
   
   
   
   pygame.display.update()






pygame.quit()