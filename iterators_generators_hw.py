import random

def gen_squares(n):
    for num in range(n):
        yield num ** 2

for x in gen_squares(10):
    print(x)


def rand_num(low,high,n):
    while num in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)


s = 'hello'

s_iter = iter(s)

print(next(s_iter))
