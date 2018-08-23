import time

def a():

    while True:

        print("-------1------")

        yield None





def b():

    while True:

        print("-------2---------")

        yield None





G1 = a()

G2 = b()

while True:

    G1.__next__()

    G2.__next__()

    time.sleep(1)
