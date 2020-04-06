#==================================================================================================
#                       Python-Implementation of the A*-Algorithm for Pathfinding
#                       Author: T.K.
#                       Created: 06.04.2020
#==================================================================================================
import pygame
import sys

class Block:
    def __init__(self, init_x, init_y):
        self.f = 0
        self.g = 0
        self.h = 0
        self.x = init_x
        self.y = init_y
        self.color = (255, 255, 255)
        self.status = "N" # N: Not checked; F: Checked; S: Start position; E: End Position


def main(Blocknumber, Size_Blocks):
    # Define the Board
    global screen
    pygame.init()
    screen = pygame.display.set_mode((xSize, ySize))
    screen.fill((255, 255, 255))

    # Initialize the Board
    fields_new, fields_fin = [], []
    for i in range(Blocknumber):
        for j in range(Blocknumber):
            block = Block(i * 20, j * 20)
            fields_new.append(block)
            #print(block.x, block.y)
    #print(fields_new, len(fields_new))

    # Setting Start and End
    fields_new[1].color, fields_new[1].status = (0, 0, 0), "S"
    fields_new[358].color, fields_new[358].status = (0, 0, 0), "E"

    while True:
        DrawGrid(fields_new, fields_fin, Size_Blocks)
        fields_new, fields_fin = Evaluate_Field(fields_new, fields_fin)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


# Visualize the Board
def DrawGrid(Field1, Field2, Blocksize):
    for i in Field1:
        rect = pygame.Rect(i.x, i.y, 
        Blocksize, Blocksize)
        # With line
        pygame.draw.rect(screen, i.color, rect, 1)
        # Without line
        #pygame.draw.rect(screen, i.color, rect, 1)

    for i in Field1:
        rect = pygame.Rect(i.x, i.y, 
        Blocksize, Blocksize)
        # With line
        #pygame.draw.rect(screen, i.color, rect, 1)
        # Without line
        pygame.draw.rect(screen, i.color, rect)


# Calculate the Block Properties
def Evaluate_Field(Fields_New, Fields_Fin):
    neighbours = []
    for i in Fields_New:
        if i.status="S:
            neighbours.append()

    fields_new, fields_fin = Fields_New, Fields_Fin
    return fields_new, fields_fin



if __name__ == "__main__":
    xSize, ySize = 400, 400
    nr_blocks = 20
    size_blocks = 20
    main(nr_blocks, size_blocks)