def ReverseReverse(L):
    # The index for our list
    i = 0
    # Goes through our list and reverses each items order
    for x in L:
        """ [::-1] makes it so the item starts and traverses
            from ending to beginning, this is then assigned to the
            original item. The index then moves to the next item after.
        """
        L[i] = L[i][::-1]
        i += 1

    """ Finally, we do the same procedure with did with the items
        but instead we do this on a list level and return the list
    """
    return L[::-1]

L = ["Monkey", "Elephant", "Dog", "Cat"]

print (L)
print (ReverseReverse(L))
