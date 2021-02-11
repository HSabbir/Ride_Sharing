#driver_bot
import random
from urllib import request
import time

location = []
id = ''

iter = 1

while(iter<100):
  x1 = random.randrange(2000)
  y1 = random.randrange(2000)
  location += [[x1, y1]]
  id = str(iter)
  webUrl = request.urlopen(f"http://127.0.0.1:8000/confirm_ride/driver/{x1}/{y1}")
  #time.sleep(1)
  iter += 1
