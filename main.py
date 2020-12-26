from random import randint

import time 
start_time = time.time()

array = []
for _ in range(10000):
  array.append(randint(1,100))


end_time = time.time()
print('tiem:', end_time - start_time)
