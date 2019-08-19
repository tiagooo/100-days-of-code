
##the decorator function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

#calling of the decorator function
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print (decorate())

#or the simpler way to call it

@uppercase_decorator
def say_hi():
    return 'hello there'

print (say_hi())