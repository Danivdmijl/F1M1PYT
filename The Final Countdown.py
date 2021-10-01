import webbrowser
import time
tijd = 1000
while tijd > 0:
    print(tijd)
    tijd = tijd -1
    time.sleep(0.01)
else:
    print("Timer is om")
    webbrowser.open("https://www.youtube.com/watch?v=jEexefuB62c")