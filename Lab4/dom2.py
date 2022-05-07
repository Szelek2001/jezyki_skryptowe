import random
import time


def timer(func):
    def func2():
        start = time.time()
        result = func(random.randint(0,50))
        timex = time.time() - start
        print(result)
        print(timex)
        return result

    return func2

@timer
def mnmn(x):
    time.sleep(random.random())
    res = 0
    for i in range(x):
        res += i*x
    return res


mnmn()