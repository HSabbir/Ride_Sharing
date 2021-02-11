#rider_bot
import random
from urllib import request
import time
from socket import timeout

start = []
end = []
id = ''

iter = 0

while(iter<10):
  x1 = random.randrange(2000)
  y1 = random.randrange(2000)
  x2 = random.randrange(2000)
  y2 = random.randrange(2000)
  start.append([x1, y1])
  end.append([x2, y2])
  id = str(iter)

  url = f"http://127.0.0.1:8000/confirm_ride/rider/{x1}/{y1}/{x2}/{y2}"

  try:
    response =request.urlopen(url, timeout=10).read().decode('utf-8')


  except timeout:
    print('hoina')

  print("result code: " + str(response.getcode()))
  #time.sleep(5)
  iter+= 1


'''try:
    response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
except (HTTPError, URLError) as error:
    logging.error('Data of %s not retrieved because %s\nURL: %s', name, error, url)
except timeout:
    logging.error('socket timed out - URL %s', url)
else:
    logging.info('Access successful.')'''
