import threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def foo():
    print ("hello")

setInterval(foo, 5)