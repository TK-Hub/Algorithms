#==================================================================================================
#                       Python-Implementation of different Sorting Algorithms
#                       Author: T.K.
#                       Created: 06.04.2020
#==================================================================================================
import random
import matplotlib.pyplot as plt

def bubble_sort(Sortlist):
    fin = False
    counter = 0
    while fin==False:
        fin = True
        for i in range(0, len(Sortlist)-1):    
            a = Sortlist[i]
            b = Sortlist[i+1]
            ind = i
            if a < b:
                pass
            elif a > b:
                Sortlist[ind], Sortlist[ind+1] = b, a
                fin = False
            counter += 1
    print("End: ", Sortlist)
    print("Number of steps: ", counter)


if __name__ == "__main__":
    sortlist = [i for i in range(10)]
    random.shuffle(sortlist)
    print("Start: ", sortlist)
    bubble_sort(sortlist)