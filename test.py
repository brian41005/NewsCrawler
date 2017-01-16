import random
import time
t = random.random()
print(t)
ts = time.time()
time.sleep(t)
te = time.time()
print(te - ts)
