#functions can be passed as values in python, can pass to another function

#decorator takes function and modifies it then returns output
def announce(f):
    def wrapper():
        print("about to run func")
        f()
        print("done with f")
    return wrapper


@announce
def hello():
    print("Hello world")

hello()