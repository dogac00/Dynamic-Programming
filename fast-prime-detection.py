import time

# my function of is_prime

def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True
  
t1 = time.clock()

for n in range(1,150000):
  is_prime(n)
  
t2 = time.clock()

print("{} seconds.".format(t2-t1))

# it calls my is_prime function
# from 1 to 150000
# the output in my computer is
# 0.627116 seconds.
# which is faster than sympy module function
