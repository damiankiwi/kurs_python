import multiprocessing
import os

def f():
    print("function f")
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())
    print("hello D")

if __name__ == '__main__':
    print("Main line")
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

    p = multiprocessing.Process(target=f)
    p.start()
    p.join()