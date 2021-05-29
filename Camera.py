import cv2 

def takepicture():
    try:
        videocaptureobject = cv2.VideoCapture(0)

        result=True
        while(result):
            print("Taking image now....")
            on,frame=videocaptureobject.read()
            cv2.imwrite("stalker.jpg", frame)
            cv2.imwrite("stalker1.jpg", frame)
            result=False 
    except:
        print("Hmm....")
    videocaptureobject.release()
    cv2.destroyAllWindows()
   
takepicture()