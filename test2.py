# Python program to explain cv2.imshow() method
  
# importing cv2
import cv2
  
# path
path = r'C:\Users\12354\Documents\PyronProg\CamCap\webcam.png'
image = cv2.imread(path)
window_name = 'image'
try:
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
except:
    print("ErrorCap")    
cv2.destroyAllWindows()