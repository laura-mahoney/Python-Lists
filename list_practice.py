"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    longwords = []
    for word in words: 
        if len(word) > 4: 
            longwords.append(word)
    return longwords



def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    longerthann = [] #new list goes outside for loop
    for word in words: 
        if len(word) > n: 
            longerthann.append(word)
    return longerthann



def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    # smallest = numbers[0]
    if len(numbers) > 0: #checked for length first, to see if list empty
        smallest = numbers[0] #made the first number my base for checking all other numbers against
        for num in numbers: #looping through the numbers
            if num < smallest: #if number is smaller than initial number, replace initial number
                smallest = num #updating the base number after check 
        return smallest 
    else: 
        return None #make sure none is not a string 



def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    if len(numbers) > 0: 
        largest = numbers[0]
        for num in numbers: 
            if num > largest:
                largest = num
        return largest
    else: 
        return None


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    halved = []
    for num in numbers: 
        if num % 2 == 0:
            halved.append(float(num/2))
        if num % 2 != 0: 
            halved.append(float(num)/2) #I floated the number first then divided
    return halved


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    lengths = [] # making an empty list that we will return 
    for word in words: #for each word in the list,
        lengths.append(len(word)) #add its length to the lengths array
    return lengths #return the new array of lengths


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """
    accumulator = 0 #we will start at zero, and add to accumulator
    if len(numbers) > 0: #if the length of the list is greater than zero(not empty)
        for num in numbers: #for each number in the list
            accumulator += num #add it to the accumulator
    else: 
        return 0 #if list is empty, return 0
    return accumulator #return the accumulator 

def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """
    product = 1 #start product at 1, not 0
    if len(numbers) > 0: #if there's input in list
        for num in numbers: #loop through the numbers
            product = num * product #multiply the number by the accumulated products
    else: 
        return 1
    return product 


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """
    joinedstr = "" #empty string variable to add to
    if len(words) > 0: #checking for content in list of words
        for word in words: #looping over words
            joinedstr = joinedstr + word #adding each word to joinedstr
    else: 
        return ""
    return joinedstr #returning joined string


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """
    
    if len(numbers) > 0: #for lists with content
        total = 0   #total is my accumulator
        for num in numbers: #loop through all numbers in the list
            total += num #add the numbers to each other, and store in total
        return float(float(total) / len(numbers)) #return the decimal values of the total's decimal value/amount of items in list to get avg
    else: 
        return "Undefined" #if list is empty, print undefined 


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    if len(words) == 1: 
        return words[0]
    elif len(words) > 1: 
        withcomma = ""
        for word in words[:-1]: 
            withcomma = withcomma + word + ", " 
        return withcomma + words[- 1]
    else: 
        return "Empty List of Words"


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    reversedlist = [] #creating a new list to add to
    for item in items[::-1]: #looped through the items specifying a step backwards
        reversedlist.append(item) #added the items to the reversed list backwards
    return reversedlist #returned the new list


def reverse_list_in_place(items): #i had a difficult time with this one
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    
    for item in range(0, len(items)/2):
        items[item], items[len(items)-1-item] = items[len(items)-1-item], items[item]
   


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    dupl = []
    temp = []
    for word in items: 
        if word in temp and word not in dupl:
            dupl.append(word)
        else: 
            temp.append(word)

    return sorted(dupl)


def find_letter_indices(words, letter): #difficult for me to compelte
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    indiceslist = []
     
    for word in words:      
        index = -1 
        for char in word:
            index = index + 1  
            if char == letter:
                indiceslist.append(index)
        if letter not in word:
            indiceslist.append(None) 
    return indiceslist

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
