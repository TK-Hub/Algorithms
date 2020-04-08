#==================================================================================================
#                       Python-Implementation of different Sorting Algorithms
#                       Author: T.K.
#                       Created: 06.04.2020
#==================================================================================================
import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(Sortlist):
    print("Start: ", Sortlist)
    fin = False
    counter = 0
    
    #fig = plt.figure()  # create a figure object
    #ax = plt.gca()
    #fig = plt.bar(np.asarray(range(0, len(Sortlist))), np.asarray(Sortlist), align='center')
    #plt.show()
    #fig.canvas.draw()

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

            #plt.bar(np.asarray(range(0, len(Sortlist))), np.asarray(Sortlist))
            #fig.canvas.draw()

    print("End Bubble Sort: ", Sortlist)
    print("Number of steps: ", counter)

def selection_sort(Sortlist):
    counter = 0
    random.shuffle(Sortlist)
    positions = len(Sortlist)
    print("Start: ", Sortlist)
    for pos in range(0,positions):
        smallest = min(Sortlist[pos:len(Sortlist)])
        ind_smallest = Sortlist.index(smallest)
        current = Sortlist[pos]
        Sortlist[pos], Sortlist[ind_smallest] = smallest, current
    counter+=1
    print("End Selection Sort: ", Sortlist)
    print("Number of steps: ", counter)    


#==================================================================================================

if __name__ == "__main__":
    sortlist = [i for i in range(10)]
    random.shuffle(sortlist)
    bubble_sort(sortlist)
    selection_sort(sortlist)