from urllib import request
for i in range(10):
    webUrl  = request.urlopen('http://127.0.0.1:8000/confirm_ride/driver/4/10')

    print ("result code: " + str(webUrl.getcode()))
    print("need to commit")
