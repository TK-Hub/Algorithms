#==================================================================================================
#                       Python-Implementation of different Sorting Algorithms
#                       Author: T.K.
#                       Created: 06.04.2020
#==================================================================================================
import random
import matplotlib.pyplot as plt

def bubble_sort(Sortlist):
    cont = True

    while cont==True:
        for i in range(len(Sortlist)-1):
            a = Sortlist[i]
            b = Sortlist[i+1]
            ind = i
            if a < b:
                cont=False
            elif a > b:
                Sortlist[ind], Sortlist[ind+1] = b, a
                cont=True
            print(Sortlist)
            


if __name__ == "__main__":
    sortlist = [i for i in range(10)]
    random.shuffle(sortlist)
    #print(sortlist)
    bubble_sort(sortlist)