import numpy as np
import sys
import time
#why numpy? because of the less size and processing speed
#we are comparing 

SIZE=1000000

a = np.arange(SIZE)
b = np.arange(SIZE)

start = time.time()
t= a + b
total_time = (time.time()-start)*1000

print(total_time)




