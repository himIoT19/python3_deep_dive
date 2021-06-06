import sys
import time

# Example1:
a = 10
print(f"Type of a: {type(a)}")

print(f"<-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*->")
# Example2;
print(f"Size of 0: {sys.getsizeof(0)}")
print(f"Size of 1: {sys.getsizeof(1)}")
print(f"Size of 2 ** 1000 : {sys.getsizeof(2 ** 1000)}")

print(f"<-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*-><-*->")


# Example3:
def calc(a):
    for i in range(10000000):
        a * 2


start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(f"Time taken calc(10) = {end - start}")

start = time.perf_counter()
calc(2 ** 100)
end = time.perf_counter()
print(f"Time taken calc(2 ** 100) = {end - start}")

start = time.perf_counter()
calc(2 ** 10000)
end = time.perf_counter()
print(f"Time taken calc(2 ** 10000) = {end - start}")
