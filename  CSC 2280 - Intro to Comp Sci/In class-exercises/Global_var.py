verbose = True

def example():
    if verbose:
        print("This is an example function.")

example()
        
been_called = False
def example2():
    global been_called;
    been_called = True

example2()
print(been_called)

count = 0
def example3():
    global count
    count += 1

    print("this ran")

example3()
