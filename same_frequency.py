def freq(collection):
    count = {}

    for x in collection:
        count[x] = count.get(x, 0) + 1

    return count

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return freq(str(num1)) == freq(str(num2))