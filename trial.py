import sys
import dlib
from skimage import io
import cv2
import numpy as np
cam=cv2.VideoCapture(0);
face_detector = dlib.get_frontal_face_detector();
win = dlib.image_window();
sampleNum=0;
while(True):
    ret,image=cam.read();
    detected_faces = face_detector(image, 1);
    win.set_image(image);
    win.clear_overlay();
    for i, face_rect in enumerate(detected_faces):
        sampleNum=sampleNum+1;
        win.clear_overlay();
        print("- Face #{} found at Top: {} Bottom: {} Left: {} Right: {}".format(i, face_rect.top(),face_rect.bottom(), face_rect.left(),face_rect.right()))
        cv2.imwrite("dataSet/User."+str(sampleNum)+".jpg",image[face_rect.top():face_rect.top()+(640-face_rect.bottom()),face_rect.left():face_rect.left()+(640-face_rect.right())]);
        win.add_overlay(face_rect);
    if(sampleNum>3):
        break;
    if(cv2.waitKey(1)==ord('q')):
        break;	
    dlib.hit_enter_to_continue()
cam.release()
cv2.destroyAllWindows()    
