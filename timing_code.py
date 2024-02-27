# Timing Python Code
import time, timeit

# Very simple way but not helpful if functions run very quickly
def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))


start_time = time.time()
result = func_one(100000)
end_time = time.time()
elapsed_time = end_time - start_time

print(elapsed_time)

start_time = time.time()
result2 = func_one(100000)
end_time = time.time()
elapsed_time = end_time - start_time

print(elapsed_time)

# Using timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=1000000))


stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

print(timeit.timeit(stmt2, setup2, number=1000000))

