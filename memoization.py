import time

look_up = {0: 1}

def memoize(x):
  if x in look_up:
    return look_up[x]
  else:
    look_up[x] = x * memoize(x-1)
    return look_up[x]

def recursion(x):
  if x == 0:
    return 1
  else:
    return x * recursion(x-1)

def iteration(x):
  result = 1
  for i in range(2,x+1):
    result *= i
  return result

t1 = time.time()
for i in range(500):
  recursion(i)
t2 = time.time()

print("time for recursion... {}".format(t2-t1))

t1 = time.time()
for i in range(500):
  iteration(i)
t2 = time.time()

print("time for iteration... {}".format(t2-t1))

t1 = time.time()
for i in range(500):
  memoize(i)
t2 = time.time()

print("time for memoize... {}".format(t2-t1))

"""

the output in my computer is

time for recursion... 0.09875273704528809
time for iteration... 0.018121719360351562
time for memoize... 0.00048279762268066406

calculation with memoization is much faster than the other two
this is because with memoization you wouldn't have to calculate
same results over and over again, and this decreases
the expensiveness of the function and saves us time

"""
