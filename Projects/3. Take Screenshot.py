import pyscreenshot as ps
import time
time.sleep(4)

image = ps.grab()
image.show()
image.save('ss by python.png')
# img = ps.grab(bbox=(10,10,500,1000))  # coordinates (x1,x2,y1,y2)
# img.show()
