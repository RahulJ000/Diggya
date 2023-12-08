import time 
from picamera import PiCamera  
camera = PiCamera()  
camera.resolution = (1280, 720)
camera.start_preview()  

time.sleep(2)
camera.capture('/home/pi/Desktop/image1.jpg')

camera.start_recording('/home/pi/Desktop/video1.h264')
camera.wait_recording(5)
camera.stop_recording()
print("Finished Recording!")

camera.stop_preview()  
