"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    odds = []   #declare a new list as an accumulator for odds
    for num in numbers: #looping through numbers in the list
        if num % 2 != 0: #if number has a remainder when divided by 2, it will be odd
            odds.append(num) #add odds to new list
    return odds #return list of odds

    


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """
    used = [] #create an empty list for storing the used/duplicate indexes
    for xcar in items: #for car name in items list
        used.append(xcar) #add that car to the used list
        if xcar in used:    #if a car is in the used list
            totalinc = len(used) - 1 #we will reset it's increment based on the length of used indexes
            print str(totalinc) + " " + xcar # we will print a string of the index and car name
        else: #if the car name has not already been used we will  have a similar print statement
             print str(items.index(xcar - 1)) + " " + xcar  

def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']
        
    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    not_in_common = [] #establish two conditions, in common and not in common, where data will be stored as lists
    in_common = []
    for item in foods1: #for every item existing in foods1
        if item in foods2: #if that item also exists in foods2, add it to the 
            in_common.append(item) #in common list 
        elif item not in foods2: #if the item from foods1 is not in foods2, add it to the
            not_in_common.append(item) #not in common list
    if len(not_in_common) == len(foods2): #if the list of things not in common between the two lists is the same length
        return list() #as foods1, i.e., there's nothing in common, return an empty list
    else: 
        return sorted(in_common)    #return the in common items alphabetically 
     
   
def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    every_other = [] #create new accumulator list
    for thing in items[ : : 2]: #accessing every other item in the list using step 2
        every_other.append(thing) #add every other item to the new list
    return every_other #return the new list


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    itemslist = items 
    numberslist = [] #new number list that will be returned 
    count = 0 #we want the counter to start at 0
    while count < n: #while the counter is less than n, the number of large numbers we want
        largest = itemslist[-1] #set the last number in the list as the default large number
        for num in itemslist: #loop through the numbers in the list, 
            if num > largest: #if the number at the index is larger than the largest default number
                largest = num #it is set as the largest number 
                numberslist.append(largest) #and added to numberslist 
                count += 1 #the count is incremeneted after each loop, until n
                            #the largest number is removed from the list before the next loop 
    return numberslist


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
