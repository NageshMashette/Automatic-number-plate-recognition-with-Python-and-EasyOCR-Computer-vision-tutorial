import easyocr
import cv2
import time

##########
reader = easyocr.Reader(['en'],gpu=False) #True
vid = cv2.VideoCapture("demo.mov") #0 and 1
#vid = cv2.VideoCapture(0)
skip_frame =True

while(True):
    a = time.time()
    ret, img = vid.read()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    result = reader.readtext(gray)
    text = ""

    for res in result:
        text += res[1] + " "
    cv2.putText(img,text,(50,70),cv2.FONT_HERSHEY_SIMPLEX,3, (255,50,255),5)


    #####FPS
    b = time.time()
    fps = 1/(b-a)
  #  cv2.line(img, (20,25), (127,25),[85,45,255],30)
   # cv2.putText(img,text,(50,70),cv2.FONT_HERSHEY_SIMPLEX,1, (50,50,255),2)
    cv2.imshow("result",img)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    #print(result)
    print(text)
    