#my solution
def sum_numbers(numbers=None):   
    if numbers is None:
        summy = 5050
    else:
        summy = sum(numbers)
    return summy

#perfect solution
#def sum_numbers(numbers=None):
#    if numbers is None:
#        numbers = range(1, 101)
#    return sum(numbers)